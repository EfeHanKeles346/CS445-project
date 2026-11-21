## About the Task

Semantic change occurs when the meanings associated with a word evolve over time, either through the addition or loss of senses or through shifts in the frequency or distribution of existing senses.

Most existing computational evaluations compare only two time periods. SemEval-2027 Task 3 moves beyond this setting by asking participants to model individual word senses and their development across ten time periods.

Participants wishing to be included in the official shared task proceedings must submit at least one valid submission to Evaluation Phase 1, Phase 2 or both within the time frame specified on the task page; and a system description paper according to the SemEval guidelines no later than the deadline announced on the shared task page detailing all steps taken.

The best-performing system based on open-weight models will be awarded one free full ACL conference registration.

The Github repository with code to run the baselines and the evaluation scripts is available [HERE](https://github.com/ChangeIsKey/semeval2027-task3).

<a href="https://groups.google.com/u/1/g/semeval2027-task3-SCxMTP" target="_blank" rel="noopener noreferrer">
  <img src="https://raw.githubusercontent.com/ChangeIsKey/semeval2027-task3/refs/heads/main/assets/banner.png"
       alt="Tasks at a glance"
       style="max-width: 200px; width: 100%; height: auto;">
</a>

---

## News

### November 12th, 2026:

We updated the GitHub repository last week. The version of the scorer currently available on GitHub is the final one and will be used during the evaluation phase.

For Subtask 2, the evaluation metric is the average of the macro-F1 scores calculated individually for each word. Therefore, the Subtask 2 results currently displayed on the train/dev phase leaderboard may differ from those obtained using the updated scorer available on GitHub.

Please note that the scorer on GitHub is the definitive version and will be used during the evaluation phase.

### November 5th, 2026:

**New Prize Announcement:** The best-performing system based on open-weight models will be awarded one free full ACL conference registration.

### October 7th, 2026:
We have made changes to the Terms, please review those. This in particular relates to the use of proprietary models which are now allowed. 

### October 5th, 2026: 
### IMPORTANT UPDATES
- We fixed several issues in our evaluation pipeline:
  1. B-Cubed and F1 scores were being computed over all words instead of using macro-averaging. This affected the results for Subtask 1a and Subtask 2.
  2. We added formatting checks and checks for missing instances. The updated evaluation scripts are available on GitHub.
- The Train/Development Evaluation Phase was previously scoring submissions only on the two words released as sample data in August. For this reason, and because we have updated the evaluation scripts, the leaderboard has been cleared.
- We fixed an issue with incorrect offsets for target words within sentences. As a result, we have also updated the train/dev data. You can download the latest version from the Data section.

### October 1st, 2026: There is [synthetic change data for English](https://zenodo.org/records/21703081) that can be used for development and [here](https://clic2026.unipa.it/wp-content/uploads/2026/09/88_main_long.pdf) is the paper for describing the data. 

### October 1st, 2026: Don't forget to join our mailing list: https://groups.google.com/u/1/g/semeval2027-task3-SCxMTP

### September 8th, 2026: [Dev Data](https://www.codabench.org/datasets/download/568b0ea8-3490-4b1b-ac87-5b3cf03570c0/) and [example](https://www.codabench.org/datasets/download/6695d1d5-c196-448a-9f02-9af819e44d94/) of valid submission are released. The evaluation script on Codabench is now working.

---

## **Task at a glance** (More details in the "Task and Evaluation" tab on the left)

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border: 1px solid black; padding: 8px;">Track</th>
      <th style="border: 1px solid black; padding: 8px;">Evaluation</th>
      <th style="border: 1px solid black; padding: 8px;">Goal</th>
      <th style="border: 1px solid black; padding: 8px;">Output</th>
      <th style="border: 1px solid black; padding: 8px;">Metric</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid black; padding: 8px; vertical-align: top;" rowspan="2">
        <strong>Subtask 1</strong><br>
        Group usages by semantic sense (i.e., diachronic WSI)
      </td>
      <td style="border: 1px solid black; padding: 8px;"><strong>1a: Accuracy of sense assignments</strong></td>
      <td style="border: 1px solid black; padding: 8px;">Group usages by sense</td>
      <td style="border: 1px solid black; padding: 8px;">Cluster assignment</td>
      <td style="border: 1px solid black; padding: 8px;">BCubed F1</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;"><strong>1b: Semantic change score across time</strong></td>
      <td style="border: 1px solid black; padding: 8px;">Model sense dynamics</td>
      <td style="border: 1px solid black; padding: 8px;">Change ranking</td>
      <td style="border: 1px solid black; padding: 8px;">Spearman Correlation</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px; vertical-align: top;">
        <strong>Subtask 2</strong><br>
        Detect all usages of a given sense
      </td>
      <td style="border: 1px solid black; padding: 8px;"><strong>Accuracy of usage classification</strong></td>
      <td style="border: 1px solid black; padding: 8px;">Detect usages matching a target sense</td>
      <td style="border: 1px solid black; padding: 8px;">Binary classification</td>
      <td style="border: 1px solid black; padding: 8px;">Average F1</td>
    </tr>
  </tbody>
</table>


## Languages

* Swedish 🇸🇪
* English 🇬🇧
* Italian 🇮🇹
* Spanish 🇪🇸
* Dutch 🇳🇱
* Russian 🇷🇺