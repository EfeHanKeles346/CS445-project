from pathlib import Path
import json
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(__file__).resolve().parents[1]
S=json.loads((ROOT/'04_data/processed/eda_summary.json').read_text())
A=json.loads((ROOT/'04_data/processed/quality_audit.json').read_text())
D=json.loads((ROOT/'04_data/processed/scorer_diagnostic.json').read_text())
doc=Document()
sec=doc.sections[0]
sec.page_width=Inches(8.27);sec.page_height=Inches(11.69)
sec.top_margin=Inches(.65);sec.bottom_margin=Inches(.65)
sec.left_margin=Inches(.72);sec.right_margin=Inches(.72)
sec.header_distance=Inches(.25);sec.footer_distance=Inches(.25)
for name in ['Normal','Title','Subtitle','Heading 1','Heading 2','Caption']:
 st=doc.styles[name];st.font.name='Arial';st.font.color.rgb=RGBColor(0,0,0)
 st.font.size=Pt(10.5)
 st.paragraph_format.space_after=Pt(6)
 st.paragraph_format.line_spacing=1.08
doc.styles['Title'].font.size=Pt(21)
doc.styles['Title'].font.bold=True
doc.styles['Heading 1'].font.size=Pt(15)
doc.styles['Heading 1'].paragraph_format.space_before=Pt(9)
doc.styles['Heading 2'].font.size=Pt(11.5)
doc.styles['Heading 2'].paragraph_format.space_before=Pt(7)
doc.styles['Caption'].font.size=Pt(9)
doc.styles['Caption'].font.italic=True
doc.styles['Caption'].font.bold=False
for style in doc.styles:
 for node in list(style.element.iter(qn('w:pBdr'))):
  node.getparent().remove(node)
for node in list(doc.element.iter(qn('w:pBdr'))):
 node.getparent().remove(node)
doc.styles['Subtitle'].font.size=Pt(10)
header=sec.header.paragraphs[0];header.text='CS 445   Fall 2026   GroupXXXXX'
header.style='Caption';header.runs[0].italic=False
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.RIGHT
footer.add_run('Team review draft  |  ')
field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)
for r in footer.runs:r.font.size=Pt(8)

def p(text,style=None):return doc.add_paragraph(text,style)
def h(text):doc.add_heading(text,level=1)
def h2(text):doc.add_heading(text,level=2)
def table(headers,rows,widths):
 t=doc.add_table(rows=1,cols=len(headers));t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
 for i,w in enumerate(widths):t.columns[i].width=Inches(w)
 for i,x in enumerate(headers):t.rows[0].cells[i].text=x
 for row in rows:
  cells=t.add_row().cells
  for i,x in enumerate(row):cells[i].text=str(x)
 for ri,row in enumerate(t.rows):
  for ci,c in enumerate(row.cells):
   c.width=Inches(widths[ci]);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
   pr=c._tc.get_or_add_tcPr()
   borders=OxmlElement('w:tcBorders')
   for edge in ['top','left','bottom','right']:
    el=OxmlElement('w:'+edge);el.set(qn('w:val'),'single');el.set(qn('w:sz'),'4');el.set(qn('w:color'),'D9D9D9');borders.append(el)
   pr.append(borders)
   shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'233F50' if ri==0 else ('F2F5F7' if ri%2==0 else 'FFFFFF'));pr.append(shade)
   margins=OxmlElement('w:tcMar')
   for side in ['top','bottom','left','right']:
    el=OxmlElement('w:'+side);el.set(qn('w:w'),'70');el.set(qn('w:type'),'dxa');margins.append(el)
   pr.append(margins)
   for para in c.paragraphs:
    para.paragraph_format.space_after=Pt(2);para.paragraph_format.line_spacing=1.0
    for r in para.runs:
     r.font.size=Pt(9);r.font.name='Arial'
     if ri==0:r.font.bold=True;r.font.color.rgb=RGBColor(255,255,255)
  if ri==0:
   repeat=OxmlElement('w:tblHeader');row._tr.get_or_add_trPr().append(repeat)
 p('')
 return t
def page():doc.add_page_break()

doc.add_paragraph('Semantic Change Across Multiple Time Periods',style='Title')
p('Milestone report for Subtask 1',style='Subtitle')
p('GroupXXXXX   Prepared 14 November 2026   Presentation 23 November 2026',style='Subtitle')
p('Working draft for group discussion. Member names and responsibilities remain unconfirmed. This AI-assisted draft is a study resource; the team must prepare its own submission in accordance with the course AI policy.',style='Caption')
h('1 Introduction')
p('The project studies how a target word is used in different senses across historical periods. Our selected scope is SemEval 2027 Task 3, Subtask 1. The course requires Subtask 1 and leaves other subtasks optional [C]. We plan to induce sense groups from dated usages and evaluate both assignment quality and sense dynamics. No Subtask 2 model is included.')
p('The technical unit is a target-word occurrence in context. A system assigns each occurrence one or more integer cluster identifiers. Identifiers have meaning only within a target word. This allows the same sense to be tracked across the periods in which that word appears. The current Codabench specification, rather than the older overview example, defines the input and output contract [T].')
p('Completed preparation includes downloading the current Swedish development release, checking its schema and reference alignment, computing descriptive statistics, saving an executed EDA notebook, and running an integration diagnostic against the official scorer. The proposed neural method has not been trained or evaluated. All numerical observations in this report come from the released development data.')
h('2 Dataset Selection')
h2('Selected data and rationale')
p('We select the official Swedish development package downloaded on 14 November 2026 [T]. It provides task-matched inputs and public reference labels. We use no additional corpus at this milestone. This keeps the analysis traceable and avoids adding a second annotation scheme before the primary pipeline is understood. The multilingual evaluation release is not used.')
table(['Property','Verified development release'],[
 ['Language and target words','Swedish SV; 10 target words'],
 ['Usage records','1,983 inputs and 1,983 Subtask 1 reference records'],
 ['Time coverage','10 period labels spanning 1880–2023, with a gap between 1915 and 2006'],
 ['Per-word coverage','5 words cover 10 periods; 5 words cover 5 periods'],
 ['Available labels','1,721 single-label and 262 multiple-label usages'],
 ['Data split','One released development collection; proposed word-level folds, no independent test set']
],[1.75,5.05])
p('Input fields are word, sentence_id, text, pos, period_label, start, end and year. The offsets identify a target surface form such as kvinnor for lemma kvinna. For Subtask 1 we exclude definitions.jsonl, which supports Subtask 2. We preserve the original text and offsets.',style=None)

page()
h('2 Dataset Selection continued')
h2('Exploratory data analysis')
p('The number of usages ranges from 98 for skär to 291 for motiv. The coverage matrix contains 75 populated word-period cells and 25 empty cells. Empty cells indicate absent observations and cannot establish that a sense was absent from the language. Periods have unequal widths and a long historical gap, so the figure uses discrete categories rather than implying continuous temporal coverage.')
doc.add_picture(str(ROOT/'08_figures/01_word_period_coverage.png'),width=Inches(6.75))
p('Figure 1. Counts recomputed from usages.jsonl. All 1,983 official usage records are retained.',style='Caption')
p(f'Multiple reference labels occur in 262 usages ({S["multi_label_percentage"]:.2f}%). A single-assignment baseline therefore cannot express every reference membership. We split a usage’s mass equally across its labels when plotting reference sense proportions, matching the official scorer’s aggregation. Whitespace token counts describe context length only; they are not transformer token counts.')
doc.add_picture(str(ROOT/'08_figures/03_labels_and_lengths.png'),width=Inches(6.75))
p('Figure 2. Reference label cardinality and context lengths. These are descriptive data statistics, not model results.',style='Caption')
h2('Quality checks and implications')
p(f'All input keys match the references. Required fields are populated, and all character spans are in bounds and nonempty. There are {A["year_period_mismatches"]} year-to-period inconsistencies. Five exact-text pairs have distinct official IDs; we retain them for scorer compatibility and record them for review. A future split must keep duplicate text together. Word-level folds satisfy this for the observed repeats.')
p('The supplied usages_count.tsv agrees with the JSONL counts. In contrast, 69 cells of senses_count.tsv differ from unique reference-label counts. Its counting convention is not documented here. We therefore calculate sense statistics from subtask1.jsonl and preserve the auxiliary file unchanged for investigation.')

page()
h('3 Approach Plan')
h2('Literature basis')
p('All three methodology papers come from venues allowed by the course. Giulianelli et al. [1] represent word occurrences with BERT, cluster usages with K-means and study temporal distributions. Cassotti et al. [2] introduce XL-LEXEME, a multilingual model trained on word-in-context similarity. Periti and Tahmasebi [3] compare contextual representations and distinguish sense induction from aggregate change estimation. These motivate a contextual clustering pipeline, while leaving its performance on this release to be measured.')
h2('Proposed pipeline')
for text in [
 '1. Validate each target span and preserve the original text. If truncation is required, keep a window containing the marked target and record the truncation policy.',
 '2. Encode each occurrence with the released XL-LEXEME model using its documented target-marking convention. Cache representations by data hash, model revision and preprocessing settings. This model is a candidate, not a completed experiment.',
 '3. For each target word, pool usages across all its observed periods and cluster jointly. Start with K-means and silhouette selection over K = 2 through 10, inspired by [1]. Use fixed seeds and repeated initializations. Joint clustering keeps cluster identities consistent across time.',
 '4. Compare a single-cluster control and an affinity-propagation candidate. Silhouette selection excludes K = 1 and can over-split a genuinely single-sense word. Evaluate this limitation explicitly rather than interpreting every cluster as a distinct dictionary sense.',
 '5. Export one JSONL record per official usage with word, sentence_id and label, where label is a nonempty list of integers. A first version assigns one cluster; overlapping membership is a later extension.',
 '6. Use the pinned official scorer to calculate assignment and temporal-change metrics. Inspect representative contexts from predicted clusters to explain errors.'
]:p(text)
h2('Validation and reproducibility')
p('We propose five development folds with two complete target words per validation fold, using seed 445. The remaining eight words support any supervised hyperparameter selection. The validation words keep all of their observed periods and their gold labels do not enter encoding or clustering. Joint clustering on their unlabeled usages reflects the intended transductive induction setting. All words have already appeared in descriptive EDA, so these are development comparisons, not untouched test estimates.')
p('Report word-macro BCubed precision, recall and F1 for 1a. For 1b, follow the reference implementation: fractional sense counts, chronologically adjacent observed periods, at least 10 usages in both periods, and a global Spearman correlation over eligible word-period transitions [E]. The implementation uses base-2 Jensen–Shannon distance, the square root of divergence. We will preserve that implementation rather than silently substitute another formula.')
p('The proposed contribution is a controlled comparison of representation and clustering choices, with analysis of multiple-label usages and uneven temporal coverage. This is a plan, not a claim of novelty or improved performance. The pretrained model, source methods and evaluator will remain explicitly attributed.')

page()
h('4 Next Steps')
h2('Technical status')
p(f'The one-cluster-per-word diagnostic produces BCubed F1 {D["subtask1a"]["fcubed"]:.4f} on the development release. This checks the prediction format and scorer integration only. Its change scores are constant, so Spearman correlation is undefined; the official scorer returns 0 for this case. The scorer considers {D["candidate_period_pairs"]} candidate transitions and retains {D["scored_period_pairs"]} after its minimum-count filter. No neural-system performance is claimed.')
h2('Proposed allocation for group review')
p('The current preparation supports a later group discussion. The table assigns work packages, not completed individual contributions. Names must be filled by the group, and the packages can be combined or divided to match the actual team size.')
table(['Work package','Owner','Planned output'],[
 ['A Data and EDA','Unassigned','Verify inputs, review repeated texts and explain the EDA figures'],
 ['B Literature and representation','Unassigned','Read the three papers and verify model input and resource requirements'],
 ['C Clustering and evaluation','Unassigned','Implement the agreed experiment, preserve folds and report scorer outputs'],
 ['D Report and presentation','Unassigned','Write the student-authored report, consolidate citations and lead rehearsal']
],[1.8,1.0,4.0])
h2('Milestone preparation schedule')
table(['Target date','Action and completion condition'],[
 ['14–16 November','Group reviews this package, confirms Subtask 1 scope and assigns owners'],
 ['17–18 November','Members verify data findings and literature; agree on the proposed method'],
 ['19–20 November','Members prepare their report text and update the method and next steps'],
 ['21–22 November','Replace placeholders, check the four-page limit and rehearse five minutes'],
 ['23 November','Milestone presentation; all members attend and answer questions']
],[1.45,5.35])
p('Dates above are a proposed internal schedule. The course document gives 23 November for the presentation; the group must verify the separate submission cutoff and select its assigned TA slot [C].')
h2('Decisions before submission')
p('Confirm the group number and member names, agree the allocation, and verify whether the course expects both 1a and 1b reporting and which languages it expects later. The course final date is 4 January, while the official evaluation release is scheduled later in January; the group should confirm the intended course evaluation arrangement. Current experiments can use the public development labels.')
p('The method must address historical spelling and OCR noise, rare senses, small per-period samples and possible over-clustering. We will not infer historical sense absence from missing samples. We will also distinguish descriptive gold analysis, scorer diagnostics and learned-model results in every subsequent report.')

page()
h('References')
p('References are excluded from the four-page main report limit. Only the following three ACL and NAACL publications support the methodology. The course specification and organizer resources document requirements, data and evaluation.',style=None)
refs=[
 '[1] Mario Giulianelli, Marco Del Tredici, and Raquel Fernández. 2020. Analysing Lexical Semantic Change with Contextualised Word Representations. Proceedings of ACL, pp. 3960–3973. https://aclanthology.org/2020.acl-main.365/ DOI 10.18653/v1/2020.acl-main.365',
 '[2] Pierluigi Cassotti, Lucia Siciliani, Marco DeGemmis, Giovanni Semeraro, and Pierpaolo Basile. 2023. XL-LEXEME: WiC Pretrained Model for Cross-Lingual LEXical sEMantic changE. Proceedings of ACL, Volume 2, pp. 1577–1585. https://aclanthology.org/2023.acl-short.135/ DOI 10.18653/v1/2023.acl-short.135',
 '[3] Francesco Periti and Nina Tahmasebi. 2024. A Systematic Comparison of Contextualized Word Embeddings for Lexical Semantic Change. Proceedings of NAACL, Volume 1, pp. 4262–4282. https://aclanthology.org/2024.naacl-long.240/ DOI 10.18653/v1/2024.naacl-long.240',
 '[C] CS 445. Fall 2026 Project Description. Supplied course document. Milestone requirements and report format, pp. 4–5 and 7; AI policy, p. 9.',
 '[T] SemEval 2027 Task 3 organizers. Codabench competition 17510, Task and Evaluation, Phases, and Data and Submission Format. Accessed 14 November 2026. https://www.codabench.org/competitions/17510/ The selected data download and SHA-256 are recorded in 04_data/raw/download_manifest.json.',
 '[E] ChangeIsKey. SemEval 2027 Task 3 official evaluation implementation. https://github.com/ChangeIsKey/semeval2027-task3 Commit 0e69238bf8b69b4ea0933627ed14e6ca2769d670. Accessed 14 November 2026. Unmodified scorer files and hashes are retained in 07_sources/scorer.'
]
for r in refs:p(r)
h2('Supporting files')
p('The milestone folder includes the executed notebook with outputs, immutable source data, derived tables, EDA figures, literature notes, a proposed fold manifest, scorer provenance and a Turkish team review guide. No submission to SUCourse or Codabench has been made.')
doc.core_properties.title='Semantic Change Across Multiple Time Periods Milestone Report'
doc.core_properties.subject='CS 445 Task 3 Subtask 1 team review draft'
doc.core_properties.author='GroupXXXXX'
doc.save(ROOT/'01_report/GroupXXXXX_milestone_report_DRAFT.docx')
lines=[]
for para in doc.paragraphs:
 if para.text:lines.append(para.text)
(ROOT/'01_report/report_text_reference.txt').write_text('\n\n'.join(lines),encoding='utf-8')
print('Report DOCX created')
