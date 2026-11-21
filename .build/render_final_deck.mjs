import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {PresentationFile,FileBlob} from '@oai/artifact-tool';
const root=path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const pres=await PresentationFile.importPptx(await FileBlob.load(path.join(root,'02_presentation/GroupXXXXX_milestone_presentation_DRAFT.pptx')));
const out=path.join(root,'.build/final_deck_render');await fs.mkdir(out,{recursive:true});
for(const [i,s] of pres.slides.items.entries()){
 const b=await pres.export({slide:s,format:'png',scale:1});
 await fs.writeFile(path.join(out,`slide-${i+1}.png`),new Uint8Array(await b.arrayBuffer()));
}
console.log(`Rendered ${pres.slides.items.length} slides from final PPTX.`);
