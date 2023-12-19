# CV-analysis
### Overview

This Python script analyzes a collection of CVs (resumes) in PDF format to assess their similarity to a set of target skills. The tool uses natural language processing techniques to extract text from PDFs and compute cosine similarity scores between the CVs and predefined skills.

### Features

Extracts text from PDFs using the PyMuPDF library.
Utilizes scikit-learn for text vectorization (CountVectorizer).
Computes cosine similarity scores for each CV with respect to target skills.
Generates an Excel report with the analysis results.



### Usage

Install the required libraries. Select the desired features. There are explanations in the code. CVs will be scored according to the selected features and an excel table will be created. An example result table created according to the features I specified is shown in the cv_analysis_result file. The data generally consists of engineer CVs.
