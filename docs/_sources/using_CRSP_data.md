# 4.1 Using CRSP Data

In this discussion, we will learn how to use the CRSP dataset. The CRSP dataset is a comprehensive dataset that contains information on stock prices, returns, and other financial information. This dataset is widely used in academic research and is a valuable resource for anyone interested in studying financial markets.

There are several pitfalls that one might encounter when working with the CRSP dataset. In this discussion, we will discuss some of these pitfalls and how to avoid them.

## Key Concepts

- Always be sure to read the manual first! Before working with a dataset, it is important to read the manual to understand the structure of the data and how it is organized. There are often some pitfalls that you could miss if you don't first read the manual. Here, we'll demonstrate some of these that show up in the CRSP data.
  - You can find manuals for data sets in WRDS in the documentation section.
  - You can also find video tutorials associated with many of the key datasets in WRDS. See here: https://wrds-www.wharton.upenn.edu/pages/video-support/

- Go over the "Useful Variables" in CRSP described here: [CRSP Useful Variables](./assets/CRSP_useful_variables.pptx)
  - What do the negative prices in CRSP mean?
  - How does CRSP handle stock splits?

- Merging CRSP and Computstat: As a note, there is a matrix of linking suggestions provided by WRDS that gives recommendations about how to merge various datasets. See here: https://wrds-www.wharton.upenn.edu/pages/wrds-research/database-linking-matrix/ For CRSP and Compustat, there is a separate table that provides the links between the two: https://wrds-www.wharton.upenn.edu/pages/wrds-research/database-linking-matrix/linking-crsp-with-compustat/ 

## Try it out yourself!

- Download a sample of the CRSP dataset using the WRDS query form. Then, open a `.py` file and interactively explore it. Call the file, `./src/CRSP_exploration.py`. I have provided an example in this repo.
- When using the web query form, make sure you learn the following:
  - Save a query so you can reuse it later. 
  - How can I explore some backend information about the query?
  - Learn how to use SAS Studio to explore the data interactively.
  - Make sure you know where you can access the documentation for the dataset.