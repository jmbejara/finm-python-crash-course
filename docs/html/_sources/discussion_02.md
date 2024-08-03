# 2. Agenda

## Agenda

- [**Sync Changes from GitHub and a Brief Overview of Git Concepts**](./syncing_files_with_git_and_github.md): We'll go over how to sync changes from GitHub and a brief overview of Git concepts.
- **Install Necessary Python Packages**. 
    - Create a new conda environment: `conda create -n finm python=3.13`. If you need to, you can delete the environment with `conda remove -n finm --all`.
    - Activate the environment: `conda activate finm`.
    - Install the necessary packages: `pip install -r requirements.txt`
- [**Introduction to WRDS**](./WRDS_intro_and_web_queries.md): We will discuss the Center for Research in Security Prices (CRSP) database, which is a renowned financial research database, primarily recognized for its comprehensive historical data on securities traded in the United States. We will also discuss how to use the Wharton Research Data Services (WRDS) web query system.
- While going through the following notebooks, be sure to demo the features of using the Python and Jupyter 
extensions within VS Code.
    - Overview: https://code.visualstudio.com/docs/datascience/overview
    - Variable explorer and data viewer: https://code.visualstudio.com/docs/datascience/
    jupyter-notebooks#_variable-explorer-and-data-viewer
    - Custom notebook diffing: https://code.visualstudio.com/docs/datascience/
    jupyter-notebooks#_custom-notebook-diffing
- **Overview of Pandas** As aspiring quantitative finance professionals, Pandas is likely the most important Python package you will use. It is a powerful data manipulation library that is built on top of NumPy. It is especially useful for working with time series data. We will go over the basics of Pandas and then work through a series of exercises to practice using Pandas. I'll skim through some introductory material from [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas.
  - [Introducing Pandas Objects](./_notebook_build/_02_01-Introducing-Pandas-Objects.ipynb)
  - [Data Indexing and Selection](./_notebook_build/_02_02-Data-Indexing-and-Selection.ipynb)
  - [Operations in Pandas](./_notebook_build/_02_03-Operations-in-Pandas.ipynb)
  - [Missing Values](./_notebook_build/_02_04-Missing-Values.ipynb)
- **Hands-On Example with Data in Pandas** Demonstrate Pandas in the context of factor analysis/principal components analysis of a panel of economic and financial time series. [./src/factor_analysis_demo.ipynb](./_notebook_build/_02_factor_analysis_demo.ipynb)
- **Individual Help with Setup.** Save 30-45 minutes at the end to help students individually with their setup.

## Homework

Please complete the following:
- Review the pandas notebooks from today's discussion
- Practice using WRDS web queries as shown in class

Please read the following:
- [Python Data Science Handbook - Chapter 3: Data Manipulation with Pandas](https://jakevdp.github.io/PythonDataScienceHandbook/03.00-introduction-to-pandas.html)
- [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
- Review the [WRDS Research Applications](https://wrds-www.wharton.upenn.edu/pages/support/research-wrds/research-applications/)


## Additional Reading

After class, consider reading some of the following on your own:
- [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Python for Data Analysis, 2nd Edition](https://github.com/wesm/pydata-book) by Wes McKinney
- [Working with Time Series Data in Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
