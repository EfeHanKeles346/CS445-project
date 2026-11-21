# CS445 Project

CS 445 Fall 2026 term project: **SemEval 2027 Task 3, Subtask 1 — Diachronic Word Sense Induction**.

This repository contains the milestone working package. The data preparation, exploratory analysis and official scorer integration check are complete. Neural representation and clustering experiments remain planned. Group membership and work allocation still need to be confirmed.

## Current report and presentation

- [Milestone report — Word](01_report/GroupXXXXX_milestone_report_SIMPLE.docx)
- [Milestone report — PDF](01_report/GroupXXXXX_milestone_report_SIMPLE.pdf)
- [Milestone presentation — PowerPoint](02_presentation/GroupXXXXX_milestone_presentation_SIMPLE.pptx)
- [Executed EDA notebook](03_analysis/GroupXXXXX_milestone_EDA.ipynb)
- [Start here — Turkish](00_ONCE_BUNU_OKU_TR.md)
- [Presentation rehearsal and questions — Turkish](02_presentation/SUNUM_PROVA_VE_SORULAR_TR.md)

The report contains four main pages plus references. The presentation has six main slides and two hidden backup slides. Earlier report and presentation versions are retained for comparison.

## Repository contents

| Directory | Contents |
|---|---|
| `01_report` | Current and previous milestone reports |
| `02_presentation` | Presentation files and rehearsal notes |
| `03_analysis` | Executed notebook, analysis code and setup instructions |
| `04_data` | Official Swedish development release and derived analysis files |
| `05_literature` | Three selected ACL/NAACL papers, references and reading notes |
| `06_planning` | Workflow, checklist and preparation/contribution record |
| `07_sources` | Course description, organizer documentation and official scorer |
| `08_figures` | Analysis figures and design variants |
| `.build` | Document/deck generation code, validation records and rendered previews |

Additional working files are preserved. Local dependencies, Python caches and macOS metadata are excluded.

## Data and analysis

The selected public Swedish development release contains **1,983 usages, 10 target words and 10 period labels**. No competition evaluation-phase data is included. Download provenance and hashes are recorded in [the data manifest](04_data/raw/download_manifest.json).

See [the analysis setup instructions](03_analysis/CALISTIRMA_TR.md) for the environment and execution steps. The stored notebook outputs describe the development data. The single-cluster diagnostic is a format/scorer check, not the result of a trained semantic model.

## Sources and authorship

Methodology references are Giulianelli et al. (ACL 2020), Cassotti et al. (ACL 2023) and Periti and Tahmasebi (NAACL 2024). Full citations are in [references.bib](05_literature/references.bib).

The official task is hosted on [Codabench](https://www.codabench.org/competitions/17510/). The evaluator comes from [ChangeIsKey/semeval2027-task3](https://github.com/ChangeIsKey/semeval2027-task3); its pinned revision is documented in [scorer provenance](07_sources/scorer/provenance.json).

This is an AI-assisted working draft for team review. Preparation history and pending individual contributions are recorded in [AI_VE_KATKI_KAYDI.md](06_planning/AI_VE_KATKI_KAYDI.md). The course's authorship requirements apply to the final submission.

Third-party papers, course materials, data and evaluator code retain their original rights and conditions. Their inclusion does not grant a new license; consult the original sources and [organizer terms](07_sources/official/terms.md).
