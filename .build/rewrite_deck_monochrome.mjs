import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {execFileSync} from 'node:child_process';
import {PresentationFile,FileBlob} from '@oai/artifact-tool';
const ROOT=path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const SKILL='/Users/efehankeles/.codex/plugins/cache/openai-primary-runtime/presentations/26.1119.11507/skills/presentations';
const PY='/Users/efehankeles/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3';
const {finalizePresentation}=await import(pathToFileURL(path.join(SKILL,'container_tools/artifact_tool_utils.mjs')).href);
const pres=await PresentationFile.importPptx(await FileBlob.load(path.join(ROOT,'02_presentation/GroupXXXXX_milestone_presentation_DRAFT.pptx')));
const priorNotes=pres.slides.items.map(s=>s.speakerNotes.text);
const snapshot=await pres.inspect({kind:'textbox,shape,table,chart',maxChars:100000});
for(const r of snapshot.records){
  if(r.slideIndex===6)continue;
  if(r.slideIndex===2&&r.kind==='chart')continue;
  if(r.slideIndex===7&&r.kind==='table')continue;
  if(['textbox','shape','table','chart'].includes(r.kind))pres.delete(r.id);
}
function txt(s,text,x,y,w,h,size=28,bold=false){
  const z=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
  z.text=text;z.text.style={fontFamily:'Arial',fontSize:size,color:'#000000',bold};return z;
}
function base(index,title){
  const s=pres.slides.items[index];s.background.fill='#FFFFFF';
  txt(s,title,70,45,1130,70,38,true);
  txt(s,`GroupXXXXX   ${index+1}`,70,674,1120,26,16);
  return s;
}
function notes(i,spoken,seconds){
  pres.slides.items[i].speakerNotes.text=`Suggested spoken outline (${seconds} seconds)\n${spoken}\n\nReference and preparation notes (not part of the spoken outline)\n${priorNotes[i]}`;
}
let s=base(0,'Word sense change over time');
txt(s,'SemEval 2027 Task 3, Subtask 1',70,137,1110,45,28);
txt(s,'We group uses of a word by meaning, then compare the groups across time periods.',70,207,1090,95,30);
txt(s,'For example',70,326,1100,40,24,true);
txt(s,'“The mouse ate the grain.”',95,391,850,46,29);
txt(s,'Group 0',1000,391,200,46,29);
txt(s,'“The mouse has a wireless receiver.”',95,465,880,46,29);
txt(s,'Group 1',1000,465,200,46,29);
txt(s,'Illustrative English examples. The project data is Swedish.',70,565,1110,42,22);
notes(0,'Our project studies how word meanings change over time. We first group similar uses of each word. We then compare how common these groups are in different periods. These two sentences show why context matters: mouse has a different meaning in each. The examples are illustrative; our actual data is Swedish.',35);

s=base(1,'Dataset');
txt(s,'We use the official Swedish development set.',70,142,1110,50,30);
txt(s,'1,983 usages of 10 target words\n10 period labels between 1880 and 2023\nNo observations between 1915 and 2006',70,221,1110,150,29);
txt(s,'Input',70,414,160,45,27,true);
txt(s,'Sentence, target-word span, word ID and period label',260,414,900,70,27);
txt(s,'Output',70,508,160,45,27,true);
txt(s,'One or more sense-group labels for each usage',260,508,900,70,27);
txt(s,'Public labels are available for development. No additional corpus is selected.',70,610,1110,40,22);
notes(1,'The development set contains 1,983 usages for ten Swedish words. We selected it because it includes both the task inputs and the reference labels. Each input gives us the context, target span and period. The output is a list of sense-group labels. We currently use no additional corpus or independent test set.',40);

s=base(2,'Data analysis');
const chart=s.charts.items[0];
chart.series.getItemAt(0).apply({name:chart.series.getItemAt(0).name,fill:'#333333'});
chart.dataLabels={showValue:true,position:'outEnd',textStyle:{fontSize:18,typeface:'Arial',color:'#000000',bold:false}};
chart.xAxis={textStyle:{fontSize:17,typeface:'Arial',color:'#000000'}};
chart.yAxis={textStyle:{fontSize:16,typeface:'Arial',color:'#000000'},majorGridlines:{fill:'#DDDDDD',width:1}};
txt(s,'98 to 291 usages per word',867,185,330,90,27,true);
txt(s,'Five words appear in all ten periods; the other five appear in five.',867,300,330,145,27);
txt(s,'262 usages (13.2%) have more than one reference label.',867,460,330,120,27);
txt(s,'Five exact-text pairs have different official IDs; we retained them.',70,610,1110,42,22);
notes(2,'The data is uneven. The chart shows that some words have almost three times as many examples as others. Half of the words cover all ten periods, while the rest cover five. Also, 262 usages have multiple labels. This matters because our first model will assign only one label. The data checks found five repeated-text pairs, which we kept because their official IDs differ.',50);

s=base(3,'Related work');
txt(s,'Giulianelli et al. (2020), ACL',70,155,1120,45,29,true);
txt(s,'Cluster contextual word representations and compare the groups over time.',70,213,1110,80,28);
txt(s,'Cassotti et al. (2023), ACL',70,322,1120,45,29,true);
txt(s,'Use XL-LEXEME as our first candidate for representing word usages.',70,380,1110,80,28);
txt(s,'Periti and Tahmasebi (2024), NAACL',70,489,1120,45,29,true);
txt(s,'Guide our comparison of representations and evaluation choices.',70,547,1110,80,28);
notes(3,'Three papers guide our plan. Giulianelli and colleagues provide the starting point for clustering word usages across time. Cassotti and colleagues introduce XL-LEXEME, our first representation candidate. Periti and Tahmasebi help us plan controlled comparisons. We will test these choices on our data before deciding on the final method.',35);

s=base(4,'Planned approach');
txt(s,'1. Encode each target occurrence with XL-LEXEME.',70,153,1120,65,29);
txt(s,'2. Cluster all periods together for each word, starting with K-means.',70,246,1120,88,29);
txt(s,'3. Evaluate the sense groups and their changes over time.',70,357,1120,65,29);
txt(s,'Development comparison',70,455,1110,42,26,true);
txt(s,'Five folds: two whole words held out in each fold; tune on the other eight.',70,506,1110,65,26);
txt(s,'Sense assignment: BCubed F1.  Sense dynamics: Spearman correlation.',70,581,1110,55,25);
notes(4,'We will encode each target occurrence with XL-LEXEME and cluster all periods of the same word together. That keeps the group labels comparable over time. We will start with K-means and examine alternative clustering settings. For development, each fold holds out two whole words while the other eight support parameter selection. We will use the official scorer for sense assignment and sense dynamics. The scorer check is complete; the neural experiments are still planned.',65);

s=base(5,'Next steps');
txt(s,'Data checks, EDA and the scorer check are complete.',70,137,1120,50,28);
const values=[['Work','Owner'],['Review data and examples','To be assigned'],['Prepare XL-LEXEME representations','To be assigned'],['Compare clustering methods and scores','To be assigned'],['Revise the report and rehearse','To be assigned']];
const t=s.tables.add({rows:5,columns:2,left:70,top:220,width:1120,height:290,columnWidths:[800,320],values});
t.borders.assign({fill:'#999999',width:1,style:'solid'});
for(let r=0;r<5;r++)for(let c=0;c<2;c++){
  const cell=t.getCell(r,c);cell.fill='#FFFFFF';cell.text.style={fontFamily:'Arial',fontSize:26,color:'#000000',bold:r===0};
}
t.cells.block({row:0,column:0,rowCount:5,columnCount:2}).assign({margins:{left:14,right:14,top:10,bottom:10},anchor:'center'});
txt(s,'We will agree on names during the group review.',70,548,1120,45,26);
txt(s,'Before 23 November: finish the review and rehearse the five-minute talk.',70,607,1120,45,24);
notes(5,'The data, exploratory analysis and scorer check are ready. Next we need to review these together, assign the remaining work and run the representation and clustering experiments. The four work areas are listed here; owners are still to be agreed. Before the milestone, we will finish the review and rehearse. Every member should be ready to explain the task and answer questions.',55);

s=pres.slides.items[6];
for(const sh of s.shapes.items){
  sh.text.style={fontFamily:'Arial',color:'#000000'};
  if(sh.position.top===44){sh.text.style={fontSize:38,bold:true};}
  if(sh.text.toString().includes('GroupXXXXX'))sh.text='GroupXXXXX   7';
}
s.hidden=true;
s=base(7,'Usages by word and period');s.hidden=true;
const cov=s.tables.items[0];
cov.borders.assign({fill:'#BBBBBB',width:1,style:'solid'});
for(let r=0;r<11;r++)for(let c=0;c<11;c++){
 const cell=cov.getCell(r,c);cell.fill='#FFFFFF';cell.text.style={fontFamily:'Arial',fontSize:18,color:'#000000',bold:r===0};
}
txt(s,'A zero means no observation in this dataset. Periods have gaps and unequal widths.',70,620,1130,48,23);

const build=path.join(ROOT,'.build/monochrome_deck');await fs.mkdir(build,{recursive:true});
const candidate=path.join(build,'candidate.pptx');
await(await PresentationFile.exportPptx(pres)).save(candidate);
execFileSync(PY,[path.join(ROOT,'.build/restore_chart_workbook.py'),path.join(ROOT,'02_presentation/GroupXXXXX_milestone_presentation_DRAFT.pptx'),candidate]);
await fs.writeFile(path.join(build,'inspection.json'),JSON.stringify(await pres.inspect({kind:'slide,table,chart,textbox',maxChars:100000}),null,2));
const result=await finalizePresentation({workspaceDir:ROOT,candidatePath:candidate,finalPath:path.join(ROOT,'02_presentation/GroupXXXXX_milestone_presentation_MONOCHROME.pptx'),pythonExecutable:PY,integrityValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide','6','--require-native-table-slide','8'],explicitTotalSlideCount:8,requiredNativeTableOwnerSlides:[6,8],requiredNativeChartOwnerSlides:[3],fontPolicy:{basis:'design',families:['Arial']},verifyArtifactToolImport:true,receiptPath:path.join(build,'validation.json')});
const final=await PresentationFile.importPptx(await FileBlob.load(result.finalPath));
for(const [i,slide]of final.slides.items.entries()){
 const b=await final.export({slide,format:'png',scale:1});await fs.writeFile(path.join(build,`slide-${i+1}.png`),new Uint8Array(await b.arrayBuffer()));
}
console.log(JSON.stringify({finalPath:result.finalPath,sha256:result.finalSha256}));
