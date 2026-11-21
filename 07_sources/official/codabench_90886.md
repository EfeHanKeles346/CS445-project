# Task and Evaluation
## Overview
Computational modeling of semantic change aims to study how the meanings of words evolve over time. While previous shared tasks have focused on comparisons between two (pairwise) time periods, this task extends this setting to **multiple time periods**, allowing participants to model the evolution of individual word senses over time.

The benchmark includes data from **six languages** (Swedish, English, Italian, Spanish, Dutch, and Russian), each spanning **ten historical time periods**. For every target word, participants are provided with dated sentence occurrences ("usages") extracted from diachronic corpora.

The shared task consists of **two main subtasks**, with the first divided into two evaluation tracks.
<img src="https://raw.githubusercontent.com/ChangeIsKey/semeval2027-task3/refs/heads/main/assets/tasks_at_glance.png"
     alt="Tasks at a glance"
     style="max-width: 700px; width: 100%; height: auto;">
---

# Subtask 1: Diachronic Word Sense Induction
The objective of Subtask 1 is to discover how the meanings of a word evolve over time. We do not provide access to predefined sense inventories, however, you are free to use any sense repositories.
Participants receive dated usages of a target word and must automatically identify the underlying senses. The predictions are used for two complementary tracks through which Subtask 1 is evaluated.
### Goal
Assign each usage of a target word to the senses it expresses.
Participants are free to induce any number of senses. The sense identifiers themselves are arbitrary; only the grouping of usages is evaluated.
### Input
For every usage, participants receive:
- the sentence,
- the target word,
- the publication year,

### Example Output
A system could produce:
<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border: 1px solid black; padding: 8px;">Usage</th>
      <th style="border: 1px solid black; padding: 8px;">Senses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">("The mouse ran across the floor.", <i>mouse</i>, 1885)</td>
      <td style="border: 1px solid black; padding: 8px;">[1]</td>
    </tr>
    <tr>
			<td style="border: 1px solid black; padding: 8px;">("The laboratory mouse...", <i>mouse</i>, 1965)</td>
      <td style="border: 1px solid black; padding: 8px;">[1]</td>
    </tr>
	    <tr>
      <td style="border: 1px solid black; padding: 8px;">("The mouse was on the kitchen table.", <i>mouse</i>, 2001)</td>
      <td style="border: 1px solid black; padding: 8px;">[1,2]</td>
    </tr>
    <tr>
			<td style="border: 1px solid black; padding: 8px;">("Click the mouse button.", <i>mouse</i>, 2015)</td>
      <td style="border: 1px solid black; padding: 8px;">[2]</td>
    </tr>
  </tbody>
</table>

Here, **cluster 1** represents the animal sense, while **cluster 2** represents the computer device. 
Multiple senses can be assigned to the same sentence. Read how to format your submission in the Data and Submission Format section.

## Subtask 1a: Diachronic Sense Assignment
### Goal
To measure accuracy of sense assignments across all usages of a word. 

### Evaluation
Performance is measured using [**BCubed F1**](https://aclanthology.org/P98-1012/), a clustering metric that evaluates how well predicted sense assignments match the gold standard.
Scores are computed independently for each target word and then macro-averaged across all target words for each language.


## Subtask 1b: Sense Dynamics
### Goal
Estimate how the distribution of senses changes over time.
Instead of evaluating individual usages, this track focuses on the **temporal evolution** of each induced sense.
### Evaluation
Semantic change is quantified using **Jensen–Shannon Divergence (JSD)** between the sense distributions of each pair of consecutive time periods. Thus, for ∣W∣ target words and ∣T∣ time periods, systems produce ∣W∣×(∣T∣−1) change scores, corresponding to all word–time-period pairs except the first time period of each word.

These scores are used to produce a global ranking of word–time-period pairs by degree of semantic change. The predicted ranking is compared with the gold ranking using **Spearman’s rank correlation coefficient**. Higher correlation indicates better modeling of when and for which words semantic change occurs.

---
# Subtask 2: Hypothesis-Driven Change Detection
Unlike Subtask 1, participants are given a **target sense definition**.
The objective is to identify which usages correspond to that specific meaning.
This setting reflects many real-world humanities applications, where researchers are interested in tracing the evolution of one particular concept rather than discovering all possible senses.
### Input
For every usage, participants receive:
- the sentence,
- the target word,
- the publication year,
- a textual definition of the target sense.

### Output
For each usage, systems must predict whether the usage expresses the provided target sense.
<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border: 1px solid black; padding: 8px;">Usage</th>
      <th style="border: 1px solid black; padding: 8px;">Prediction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">expresses target sense</td>
      <td style="border: 1px solid black; padding: 8px;">1</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">does not express target sense</td>
      <td style="border: 1px solid black; padding: 8px;">0</td>
    </tr>
  </tbody>
</table>

### Evaluation
Performance is measured using **F1-score**, computed independently for each target word and then averaged across all words in a language.

---

# Evaluation Summary
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


## Evaluation scripts

The evaluation scripts are available here:

https://github.com/ChangeIsKey/semeval2027-task3

This repository is provided only for the evaluation scripts. The development data is distributed through Codabench as `dev.zip` in the competition files/public data section.