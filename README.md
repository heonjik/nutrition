# SimplifyText Web Application
## Project Plan
### Objective
* Create a web application that translate words to easier synonyms.
### Scope
| Constraints  | Notes |
| ------------ | ----- |
| Must have:  | Users input the text and highlight the words.<br>Translate the highlighted words to easier synonyms. |
| Nice to have: | Collect the highlighted words and level them.<br>Analyze their level. Give a review session. |
| Not in scope: | - |
## Sources
* WordNet API
* BERT (NLP)
* NLTK
## Steps
1. Search for synonyms from NLTK.
2. Compare the word difficulty level from the trained BERT model.
3. Compare the text similarity using cosine similarity score.
4. (Optional) Compare the readability formulas such as Flesch-Kincaid Grade Level and Gunning Fog Index.
6. Create a visualization of the synonyms.
## Key Metrics
* Word difficulty level
* Cosine similarity score
* Readability formulas
  * Flesch-Kincaid Grade Level
  * Gunning Fog Index
* Word frequency
