from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '01_report/GroupXXXXX_milestone_report_STYLE_REVISED.docx'
doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.27), Inches(11.69)
sec.top_margin = sec.bottom_margin = Inches(.7)
sec.left_margin = sec.right_margin = Inches(.78)
sec.footer_distance = Inches(.3)
for name in ['Normal', 'Title', 'Heading 1', 'Heading 2', 'Caption']:
    s = doc.styles[name]
    s.font.name = 'Calibri'
    s.font.size = Pt(11)
    s.font.color.rgb = RGBColor(0, 0, 0)
    s.paragraph_format.space_after = Pt(7)
    s.paragraph_format.line_spacing = 1.08
    for node in list(s.element.iter(qn('w:pBdr'))):
        node.getparent().remove(node)
doc.styles['Heading 1'].font.size = Pt(14)
doc.styles['Heading 1'].font.bold = True
doc.styles['Heading 1'].paragraph_format.space_before = Pt(9)
doc.styles['Heading 2'].font.size = Pt(11)
doc.styles['Heading 2'].font.bold = True
doc.styles['Heading 2'].paragraph_format.space_before = Pt(7)
doc.styles['Caption'].font.size = Pt(9)
doc.styles['Caption'].font.italic = True
footer = sec.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
field = OxmlElement('w:fldSimple')
field.set(qn('w:instr'), 'PAGE')
footer._p.append(field)

def p(text, style=None):
    return doc.add_paragraph(text, style)

def h(text):
    doc.add_heading(text, 1)

def h2(text):
    doc.add_heading(text, 2)

def page():
    doc.add_page_break()

def picture(name, caption):
    para = doc.add_paragraph()
    para.paragraph_format.space_after = Pt(3)
    para.paragraph_format.keep_with_next = True
    para.add_run().add_picture(str(ROOT / '08_figures' / name), width=Inches(6.65))
    p(caption, 'Caption')

def table(headers, rows, widths):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for i, width in enumerate(widths):
        t.columns[i].width = Inches(width)
        t.rows[0].cells[i].text = headers[i]
    for row in rows:
        cells = t.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = str(value)
    for ri, row in enumerate(t.rows):
        pr = row._tr.get_or_add_trPr()
        pr.append(OxmlElement('w:cantSplit'))
        if ri == 0:
            pr.append(OxmlElement('w:tblHeader'))
        for ci, cell in enumerate(row.cells):
            cell.width = Inches(widths[ci])
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            tcpr = cell._tc.get_or_add_tcPr()
            borders = OxmlElement('w:tcBorders')
            for edge in ['top', 'left', 'bottom', 'right']:
                el = OxmlElement('w:' + edge)
                for key, val in [('val', 'single'), ('sz', '4'), ('color', 'D9D9D9')]:
                    el.set(qn('w:' + key), val)
                borders.append(el)
            tcpr.append(borders)
            if ri == 0:
                shd = OxmlElement('w:shd'); shd.set(qn('w:fill'), 'E7E6E6'); tcpr.append(shd)
            margins = OxmlElement('w:tcMar')
            for edge in ['top', 'bottom', 'left', 'right']:
                el = OxmlElement('w:' + edge)
                el.set(qn('w:w'), '85'); el.set(qn('w:type'), 'dxa'); margins.append(el)
            tcpr.append(margins)
            for para in cell.paragraphs:
                para.paragraph_format.space_after = Pt(0)
                para.paragraph_format.line_spacing = 1.05
                for run in para.runs:
                    run.font.size = Pt(10)
                    run.bold = ri == 0
    p('').paragraph_format.space_after = Pt(0)

h('1 Introduction')
p('A word may be used in different ways in older and more recent texts. Some meanings may become more common, while others may appear less often. The goal of our project is to group similar uses of a word and examine how these groups change across time. We will work on SemEval 2027 Task 3, Subtask 1, which focuses on diachronic word sense induction. This is the subtask required for our course project (CS 445, 2026).')
p('For each target word, the system receives sentences from different time periods. It assigns each occurrence to one or more sense groups, represented by integer labels. These labels must remain consistent across the periods of the same word so that we can follow changes in its usage. The task evaluates both the quality of these assignments and the changes in sense distributions between periods (SemEval 2027 Task 3 organizers, 2026).')
p('At this stage, the Swedish development data has been downloaded and checked. The preparation includes an exploratory data analysis notebook, figures showing the main data characteristics, and a test of the official evaluation code. We have also selected three papers to guide the method. The representation and clustering experiments are planned for the next stage; no neural model has been evaluated yet.')

h('2 Dataset Selection')
p('We selected the official Swedish development dataset because it provides the inputs and reference labels needed for Subtask 1. This allows us to understand the data and check our evaluation process before considering further resources. The version used in this report was downloaded on 14 November 2026. We will initially work with this collection without adding another corpus or using the multilingual evaluation release.')
p('Table 1 summarises the selected data. Each record contains a target word, a sentence identifier, the text, part of speech, a period label, character offsets and a year. The offsets locate the actual word form in the sentence. For example, a record for the lemma kvinna may mark the form kvinnor. We will preserve these spans when preparing model inputs. The definition file belongs to Subtask 2 and is outside our current scope.')
p('Table 1. Main characteristics of the Swedish development dataset.', 'Caption')
table(['Characteristic', 'Observation'], [
    ['Target words and usages', '10 words; 1,983 usages with matching reference records'],
    ['Time coverage', '10 periods from 1880 to 2023; a gap between 1915 and 2006'],
    ['Coverage for each word', '5 words appear in 10 periods; 5 words appear in 5 periods'],
    ['Reference labels', '1,721 single-label usages; 262 usages with multiple labels'],
    ['Available split', 'Development data only; no independent test set used'],
], [1.9, 4.75])

page()
h2('Exploratory data analysis')
p('The amount of data differs between words and periods. The number of usages ranges from 98 for skär to 291 for motiv. Figure 1 shows 75 observed word-period combinations and 25 combinations with no records. A missing combination only means that we have no observations in this dataset. It does not show that the word or a particular sense was absent from the language.')
picture('01_word_period_coverage.png', 'Figure 1. Number of usages for each word and period, calculated from the released input records.')
p('As shown in Figure 2, 262 usages have more than one reference label, which corresponds to 13.21% of the data. Our first version will assign one group to each usage, so it will not capture every reference membership. The contexts contain between 16 and 100 whitespace-separated tokens, with a median of 27. We will check model token lengths separately when deciding how to handle long inputs.')
picture('03_labels_and_lengths.png', 'Figure 2. Number of reference labels per usage and distribution of context lengths.')
p('The checks found no missing required values, invalid target spans or disagreements between years and period labels. Each input record matches a reference record. Five pairs have identical text but different official identifiers. We retained these records and recorded the duplicates so that they can be considered during validation.')
p('The supplied usage-count table agrees with the input records. However, 69 cells in the supplied sense-count table differ from the unique label counts calculated from the references. The reason for this difference is not yet clear. We therefore use counts calculated directly from the JSONL records for our analysis and keep the auxiliary table for further review.')

page()
h('3 Approach Plan')
p('We propose a system that represents each target occurrence using its context and then groups similar occurrences. Giulianelli et al. (2020) provide the starting point for this approach. They use contextual word representations, cluster usages with K-means and compare the distributions of these groups over time. Their work guides our clustering plan, but it does not establish how well the same choices will work on the Swedish data.')
p('Cassotti et al. (2023) introduce XL-LEXEME, a multilingual model trained to compare word meanings in context. We plan to use it as the first candidate for representing the target occurrences. Periti and Tahmasebi (2024) compare contextual representations for lexical semantic change. Their study will guide how we compare model choices and distinguish sense grouping from overall change estimation. These three papers were published in ACL or NAACL, which are among the venues allowed by the course.')
h2('Proposed method')
p('First, we will mark the target span in each context according to the model’s input format and calculate its representation. If a context is too long, we will keep a window containing the target word. We will save the representations together with the model version and preprocessing settings so that later comparisons use the same inputs.')
p('Next, we will collect all occurrences of each word across its observed periods and cluster them together. This allows the same group label to be followed over time. We will start with K-means and use silhouette scores to choose between 2 and 10 clusters, following the approach of Giulianelli et al. (2020). We will use repeated initialisations and fixed random seeds. This range may split a word that needs only one group or miss distinctions when more groups are needed. We will therefore include a single-cluster control and consider affinity propagation before finalising the method.')
p('The first version will return one cluster label per usage in the required list format. Each output record will contain the word, sentence identifier and label list. We will later consider whether allowing more than one label improves the handling of ambiguous usages. We will also inspect example sentences from each predicted group to understand where the method makes mistakes.')
h2('Validation and evaluation')
p('We plan to use five development folds, with two complete words held out in each fold and seed 445 used to generate the split. The remaining eight words will support parameter selection. The held-out words will keep all their periods, and their unlabelled usages will be clustered jointly without using reference labels. Since all words have already been examined during data analysis, these comparisons will be development results rather than independent test results.')
p('For sense assignment, we will use the official BCubed precision, recall and F1 scores averaged across words. For sense dynamics, we will use the official Spearman correlation over eligible period transitions. The scorer divides a multi-label usage equally between its labels, compares adjacent observed periods with at least 10 usages each, and calculates base-2 Jensen–Shannon distance (ChangeIsKey, 2026). We will keep these settings unchanged. The final method will depend on the development comparisons, the quality of the predicted groups and the resources needed to run the model.')

page()
h('4 Next Steps')
p('Our next step is to review the prepared data analysis and agree on the first experiment as a group. The current evaluation check assigns every usage of a word to a single cluster. It produces a BCubed F1 score of 0.7563. This result only checks that the prediction file and evaluation code work together; it does not measure a learned sense induction model. Its change predictions are constant, so Spearman correlation is undefined and the official scorer returns 0. Of 65 candidate period transitions, 60 pass the scorer’s minimum-count condition.')
p('After reviewing this check, we will confirm the XL-LEXEME input format and resource requirements, calculate the representations and implement the initial clustering method. We will then compare clustering settings using the planned folds. If the model requires more memory than available, we will first reduce the batch size and reuse saved representations. If the clustering produces unclear groups, we will inspect their contexts and compare the alternative settings before adding more complex methods.')
p('Table 2 shows a proposed division of the remaining work. Member names and responsibilities have not yet been agreed, so the roles remain unassigned. We will complete this allocation during the group review and adjust the work packages to match the actual team size. The table describes planned responsibilities and does not claim that individual members have already completed them.')
p('Table 2. Proposed responsibilities for the next stage.', 'Caption')
table(['Work package', 'Responsible member', 'Planned work'], [
    ['Data and analysis', 'To be assigned', 'Review the data checks, repeated texts and figures.'],
    ['Literature and representation', 'To be assigned', 'Review the three papers and prepare the model inputs and representations.'],
    ['Clustering and evaluation', 'To be assigned', 'Run the agreed experiments and compare the official evaluation scores.'],
    ['Report and presentation', 'To be assigned', 'Consolidate the report, check references and organise the presentation rehearsal.'],
], [1.55, 1.4, 3.7])
p('For the milestone presentation on 23 November, we plan to review the findings and method on 17–18 November, complete the report revisions on 19–20 November, and rehearse on 21–22 November. All members will need to understand the task, the data and the proposed approach. We will also confirm the assigned presentation slot and the submission time with the teaching assistant. These dates are our proposed preparation schedule.')
p('Some decisions remain open. We need to agree on the final clustering settings, decide how to handle multiple-label usages and confirm the language scope expected after the milestone. We will also ask how the course’s 4 January final deadline relates to the competition’s later evaluation release. Throughout the experiments, we will consider historical spelling, possible OCR errors, rare senses and small samples. Missing observations will not be interpreted as evidence that a sense disappeared.')

page()
h('References')
refs = [
    'Cassotti, P., Siciliani, L., DeGemmis, M., Semeraro, G., & Basile, P. (2023). XL-LEXEME: WiC Pretrained Model for Cross-Lingual LEXical sEMantic changE. Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), 1577–1585. https://doi.org/10.18653/v1/2023.acl-short.135',
    'ChangeIsKey. (2026). SemEval 2027 Task 3 official evaluation implementation. GitHub. https://github.com/ChangeIsKey/semeval2027-task3 (Commit 0e69238bf8b69b4ea0933627ed14e6ca2769d670; accessed 14 November 2026).',
    'CS 445. (2026). Fall 2026 project description [Course document]. Milestone requirements and report format, pp. 4–5 and 7.',
    'Giulianelli, M., Del Tredici, M., & Fernández, R. (2020). Analysing Lexical Semantic Change with Contextualised Word Representations. Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 3960–3973. https://doi.org/10.18653/v1/2020.acl-main.365',
    'Periti, F., & Tahmasebi, N. (2024). A Systematic Comparison of Contextualized Word Embeddings for Lexical Semantic Change. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), 4262–4282. https://doi.org/10.18653/v1/2024.naacl-long.240',
    'SemEval 2027 Task 3 organizers. (2026). Task and evaluation, phases, and data and submission format. Codabench competition 17510. https://www.codabench.org/competitions/17510/ (Accessed 14 November 2026).',
]
for ref in refs:
    para = p(ref)
    para.paragraph_format.left_indent = Inches(.22)
    para.paragraph_format.first_line_indent = Inches(-.22)
    para.paragraph_format.space_after = Pt(12)
doc.core_properties.title = 'Semantic Change Across Multiple Time Periods Milestone Report'
doc.core_properties.subject = 'CS 445 Task 3 Subtask 1 milestone draft revised in the supplied writing style'
doc.core_properties.author = 'GroupXXXXX'
doc.core_properties.comments = 'AI-assisted revision for group review. ENS491 document used for writing style only. Group allocation remains pending.'
doc.save(OUT)
text = []
for element in doc.element.body:
    if element.tag == qn('w:p'):
        text.append(''.join(element.itertext()) if False else ''.join(t.text or '' for t in element.iter(qn('w:t'))))
    elif element.tag == qn('w:tbl'):
        for row in element.findall(qn('w:tr')):
            text.append(' | '.join(''.join(t.text or '' for t in cell.iter(qn('w:t'))) for cell in row.findall(qn('w:tc'))))
(ROOT / '01_report/report_text_STYLE_REVISED.txt').write_text('\n\n'.join(x for x in text if x), encoding='utf-8')
print(OUT)
