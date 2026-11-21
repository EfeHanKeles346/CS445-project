import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {Presentation,PresentationFile} from '@oai/artifact-tool';
const ROOT=path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const SKILL='/Users/efehankeles/.codex/plugins/cache/openai-primary-runtime/presentations/26.1112.11217/skills/presentations';
const PY='/Users/efehankeles/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3';
const {finalizePresentation,applyPresentationChartFont}=await import(pathToFileURL(path.join(SKILL,'container_tools/artifact_tool_utils.mjs')).href);
const summary=JSON.parse(await fs.readFile(path.join(ROOT,'04_data/processed/eda_summary.json'),'utf8'));
const presentation=Presentation.create({slideSize:{width:1280,height:720}});
const F='Arial',C={ink:'#16394A',muted:'#4D5C65',blue:'#1F607A',pale:'#EEF3F5',white:'#FFFFFF',orange:'#B86B32'};
const task='https://www.codabench.org/competitions/17510/';
const paper=['https://aclanthology.org/2020.acl-main.365/','https://aclanthology.org/2023.acl-short.135/','https://aclanthology.org/2024.naacl-long.240/'];
function txt(s,text,x,y,w,h,size=28,bold=false,color=C.ink){
 const z=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 z.text=text;z.text.style={fontFamily:F,fontSize:size,bold,color};return z;
}
function slide(title,n,backup=false){
 const s=presentation.slides.add();s.background.fill=C.white;
 txt(s,title,64,44,1150,90,44,true);
 txt(s,`GroupXXXXX   ${backup?'Backup':'Milestone'}   ${n}`,64,675,1150,24,16,false,C.muted);
 return s;
}
function table(s,values,x,y,w,h,widths,fsz=23){
 const t=s.tables.add({rows:values.length,columns:values[0].length,left:x,top:y,width:w,height:h,columnWidths:widths,values});
 t.borders.assign({fill:'#D9E1E5',width:1,style:'solid'});
 t.cells.block({row:0,column:0,rowCount:values.length,columnCount:values[0].length}).assign({textStyle:{fontFamily:F,fontSize:fsz,color:C.ink},margins:{left:12,right:12,top:9,bottom:9},anchor:'center'});
 for(let r=0;r<values.length;r++)for(let c=0;c<values[0].length;c++){
  const cell=t.getCell(r,c);cell.fill=r===0?C.ink:(r%2===0?C.pale:C.white);
  cell.text.style={fontFamily:F,fontSize:fsz,color:r===0?C.white:C.ink,bold:r===0};
 }
 return t;
}
let s=slide('Semantic change across multiple time periods',1);
txt(s,'Task 3   Subtask 1',64,145,1100,44,30,true,C.blue);
txt(s,'Discover sense groups from dated word usages, then track their distribution across periods.',64,206,1100,88,32);
table(s,[['Illustrative usage','Predicted group'],['The mouse ate the grain.','[0]'],['The mouse has a wireless receiver.','[1]']],64,326,1150,210,[860,290],25);
txt(s,'Cluster IDs are arbitrary. These English examples are illustrative.',64,558,1120,40,22,false,C.muted);
txt(s,'Team review draft   23 November 2026',64,612,1120,34,23,false,C.muted);
s.speakerNotes.text=`35 seconds. The project studies word senses over time. Our scope is Subtask 1. A system groups usages by meaning and uses those groups across time. The example is illustrative and not from the Swedish data. We have prepared the data and method plan; no neural model result is claimed. Source: ${task}. Course scope: supplied course project description, page 1. This deck is a team-review draft; member names and final ownership remain pending.`;

s=slide('Selected development data',2);
table(s,[['Verified item','Current release'],['Language / target words','Swedish / 10'],['Usages / reference records','1,983 / 1,983'],['Observed periods','10 labels across 1880–2023'],['Additional datasets','None selected']],64,152,640,355,[310,330],24);
txt(s,'Input',770,157,400,42,30,true,C.blue);
txt(s,'Context text and target offsets\nWord and usage ID\nOfficial period label',770,214,430,144,27);
txt(s,'Output',770,387,400,42,30,true,C.blue);
txt(s,'One or more integer cluster IDs\nfor every usage',770,442,430,100,27);
txt(s,'Public development labels support EDA and planned validation. No test data used.',64,563,1150,70,25,false,C.muted);
s.speakerNotes.text=`40 seconds. We downloaded the official development archive. It contains only Swedish at this stage. We have 1,983 usages for ten words. The package includes references. The text field is named text, and start/end mark the target. We use period_label for evaluation; definitions.jsonl belongs to Subtask 2. Data source: ${task}. Download URL and SHA-256: 04_data/raw/download_manifest.json. Counts: 04_data/processed/eda_summary.json. All periods are not present for every word, which is shown next.`;

s=slide('Coverage and multiple meaning labels',3);
const chart=s.charts.add('bar',{position:{left:64,top:152,width:760,height:420},categories:summary.word_summary.map(r=>r.word),series:[{name:'Usages',values:summary.word_summary.map(r=>r.usages),fill:C.blue}],barOptions:{direction:'bar',grouping:'clustered',gapWidth:60},hasLegend:false,dataLabels:{showValue:true,position:'outEnd',textStyle:{fontSize:18,typeface:F}},yAxis:{minimumScale:0,maximumScale:350,majorGridlines:{fill:'#DDE5E8',width:1}},chartFill:C.white,plotAreaFill:C.white});
applyPresentationChartFont(chart,{fontFamily:F});
chart.xAxis={textStyle:{fontSize:14,typeface:F}};
chart.yAxis={textStyle:{fontSize:16,typeface:F}};
txt(s,'13.2%',867,168,320,72,55,true,C.blue);
txt(s,'262 usages have\nmultiple gold labels',867,248,340,92,27);
txt(s,'5 words cover 10 periods\n5 words cover 5 periods',867,373,345,100,27);
txt(s,'Counts vary from 98 to 291. Five exact-text pairs have distinct official IDs.',64,595,1150,55,24,false,C.muted);
s.speakerNotes.text='50 seconds. These are measured counts from the data, not model results. Coverage differs across words. Half the words have only five periods. There is a long gap between the historical and modern periods; no observations fill it. 262 usages, or 13.21 percent, have multiple reference labels. A first single-label method cannot express all memberships. All keys align and the spans are nonempty and in bounds. We preserve five repeated-text pairs because official IDs differ. Sources: 04_data/processed/eda_summary.json; quality_audit.json. Reproduce with 03_analysis/milestone_analysis.py.';

s=slide('Literature supporting the method plan',4);
table(s,[['Allowed publication','Use in our plan'],['Giulianelli et al. 2020\nACL','Contextual usage clustering'],['Cassotti et al. 2023\nACL','XL-LEXEME as an encoder candidate'],['Periti and Tahmasebi 2024\nNAACL','Controlled comparison of representations']],64,160,1150,342,[500,650],26);
txt(s,'All three papers are from the course’s permitted venues.',64,543,1130,50,27,true,C.blue);
txt(s,'Model choice remains provisional until resource and validation checks.',64,604,1150,40,24,false,C.muted);
s.speakerNotes.text=`35 seconds. We selected three publications from explicitly allowed venues. The first motivates clustering contextual usages. The second provides a multilingual target-aware representation candidate. The third supports controlled comparison and separate evaluation of sense induction. We are adapting a method plan; no claim of reproducing their results is made. Citations: ${paper.join('\n')}. Full bibliographic details appear on backup slide 7 and in 05_literature/references.bib.`;

s=slide('Proposed method and evaluation',5);
txt(s,'1   Preserve target spans and encode usages with XL-LEXEME',64,155,1150,55,29);
txt(s,'2   Cluster all periods jointly for each target word',64,222,1150,55,29);
txt(s,'3   Compare clustering choices and export integer label lists',64,289,1150,55,29);
table(s,[['Evaluation','Planned measurement'],['1a   Sense assignment','Word-macro BCubed precision, recall and F1'],['1b   Sense dynamics','Official change calculation and Spearman correlation']],64,376,1150,178,[340,810],24);
txt(s,'Five development folds hold out two complete words each. Seed 445.',64,579,1150,40,25,true,C.blue);
txt(s,'Neural experiments remain planned. The scorer integration check is complete.',64,625,1150,35,22,false,C.muted);
s.speakerNotes.text=`65 seconds. The first candidate encodes marked target usages using the pretrained XL-LEXEME model. We cluster jointly across periods so label identity is stable. Start with K-means, selecting K from 2 to 10 by silhouette, then compare the single-cluster control and affinity propagation. K>=2 can force splits, so we must examine that limitation. We propose five word-level development folds with seed 445. Gold labels are for tuning on other words and evaluation, not inputs to clustering. EDA used all released words, so this is development validation. Official scorer commit 0e69238bf8b69b4ea0933627ed14e6ca2769d670 computes base-2 Jensen-Shannon distance and filters pairs below ten usages. It retains 60 of 65 candidate transitions. Single-cluster diagnostic BCubed F1 is 0.7563; it is not neural performance. Constant change scores have undefined correlation; the scorer returns zero. Sources: ${paper[0]}; ${paper[1]}; https://github.com/ChangeIsKey/semeval2027-task3. Full diagnostic: 04_data/processed/scorer_diagnostic.json.`;

s=slide('Next steps and proposed work allocation',6);
table(s,[['Work package','Owner','Deliverable'],['Data and EDA','To assign','Review counts, examples and data issues'],['Literature and encoding','To assign','Confirm papers and model setup'],['Clustering and evaluation','To assign','Run the agreed development comparison'],['Report and presentation','To assign','Student-authored report and rehearsal']],64,150,1150,320,[370,170,610],24);
txt(s,'Before 23 November',64,506,1100,43,30,true,C.blue);
txt(s,'Confirm names and scope, review the draft, and rehearse five minutes.\nEvery member attends and prepares for questions.',64,558,1150,85,27);
s.speakerNotes.text='55 seconds. These are proposed work packages, not claims about who has completed the work. The group must assign real names and balance the workload. This package includes the data, EDA notebook, method plan, references and draft materials. The main report has four pages plus references. We must confirm the presentation slot and separate submission cutoff. Ask the TA about both evaluation tracks and language scope, and the mismatch between the course final date and the later competition test release. The course requires all members to attend and answer questions. The report and analysis scaffolding are AI-assisted; the group must comply with the course authorship rules. Source: supplied CS445 project description, milestone sections and report format.';

s=slide('References',7,true);
txt(s,'Giulianelli, Del Tredici and Fernández 2020',64,155,1150,45,28,true);
txt(s,'Analysing Lexical Semantic Change with Contextualised Word Representations\nACL, pages 3960–3973   aclanthology.org/2020.acl-main.365',64,204,1150,72,23);
txt(s,'Cassotti, Siciliani, DeGemmis, Semeraro and Basile 2023',64,302,1150,45,28,true);
txt(s,'XL-LEXEME: WiC Pretrained Model for Cross-Lingual LEXical sEMantic changE\nACL, pages 1577–1585   aclanthology.org/2023.acl-short.135',64,351,1150,72,23);
txt(s,'Periti and Tahmasebi 2024',64,449,1150,45,28,true);
txt(s,'A Systematic Comparison of Contextualized Word Embeddings for Lexical Semantic Change\nNAACL, pages 4262–4282   aclanthology.org/2024.naacl-long.240',64,498,1150,78,23);
txt(s,'Task and data: codabench.org/competitions/17510\nScorer: github.com/ChangeIsKey/semeval2027-task3',64,600,1150,60,20,false,C.muted);
s.speakerNotes.text='Backup reference slide. Methodology references: '+paper.join('\n')+'\nOfficial task/data: '+task+'\nOfficial scorer: https://github.com/ChangeIsKey/semeval2027-task3. Prepared 14 November 2026.';

s=slide('Observed word and period coverage',8,true);
const raw=await fs.readFile(path.join(ROOT,'04_data/processed/word_period_counts.csv'),'utf8');
const rows=raw.trim().split('\n').map(x=>x.split(','));
rows[0][0]='Word';for(let j=1;j<rows[0].length;j++)rows[0][j]=rows[0][j].replace('-','\n');
const t=table(s,rows,64,160,1150,420,[180,...Array(10).fill(97)],18);
t.cells.block({row:0,column:0,rowCount:rows.length,columnCount:rows[0].length}).assign({margins:{left:8,right:8,top:3,bottom:3}});
t.rows[0].height=52;
for(let r=1;r<rows.length;r++)t.rows[r].height=36;
for(let r=1;r<rows.length;r++)for(let c=1;c<rows[r].length;c++){
 const v=Number(rows[r][c]);t.getCell(r,c).fill=v===0?'#F2F3F4':v>=25?'#C2D9E3':'#E3EDF1';
}
txt(s,'Zeros indicate missing observations. Periods have unequal widths and gaps.',64,633,1150,32,23,false,C.muted);
s.speakerNotes.text='Backup for data questions. Native editable table from word_period_counts.csv. 75 populated cells and 25 empty cells. Do not interpret absent observations as historical absence of a sense. Data provenance: 04_data/raw/download_manifest.json. Auxiliary senses_count.tsv differs in 69 cells from unique reference labels; all sense counts in our materials are recomputed from subtask1.jsonl.';

const build=path.join(ROOT,'.build/deck');await fs.mkdir(build,{recursive:true});
const candidatePath=path.join(build,'candidate.pptx');await(await PresentationFile.exportPptx(presentation)).save(candidatePath);
for(const [i,s] of presentation.slides.items.entries()){
 const blob=await presentation.export({slide:s,format:'png',scale:1});await fs.writeFile(path.join(build,`slide-${i+1}.png`),new Uint8Array(await blob.arrayBuffer()));
}
await fs.mkdir(path.join(ROOT,'.build/final'),{recursive:true});
const result=await finalizePresentation({workspaceDir:ROOT,candidatePath,finalPath:path.join(ROOT,'.build/final/validated_v4.pptx'),pythonExecutable:PY,integrityValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...[1,2,4,5,6,8].flatMap(n=>['--require-native-table-slide',String(n)])],requiredNativeTableOwnerSlides:[1,2,4,5,6,8],requiredNativeChartOwnerSlides:[3],materializeLiteralChartWorkbooks:true,fontPolicy:{basis:'design',families:[F]},verifyArtifactToolImport:true,receiptPath:path.join(build,'validation_v4.json')});
console.log(JSON.stringify({finalPath:result.finalPath,sha256:result.finalSha256,layout:result.presentationLayout}));
