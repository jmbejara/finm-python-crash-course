# 4. Agenda

- Today we move away from Jupyter notebooks entirely and focus on writing `.py` files directly. We'll focus on writing our own modules, discuss automating tasks by using the command line, we'll discuss task management software (Python's `doit` package and Makefiles), and discuss the importance of conda environments (and hint at Docker containers).
- Give an overview of GitKraken and GitHub.
  - Create a new repository on GitHub and clone it in GitKraken.
  - Create a commit and push to GitHub
  - Make edits to code and view the diffs.
  - Discuss pull requests and the open source model (delegating oversight)
- Now, let's briefly move away from notebooks and write `.py` files directly. We'll discuss the pros and cons of working with Notebooks vs `.py` files.
  - To do this, complete again the `Occupations` exercises the following in-class Pandas exercises within a `.py` file. Complete using the %% cells.
  - Once the assignment is complete, remove the %% cells for comparison.
  - Show how to use the debugger.
  - Show how to run the script from the command line. 
    - Use the script to print to the command line.
    - Use the script to save a figure.
    - Write a shell script to run several Python scripts.
- Discussion of writing our own modules
  - Start with a review of functions in Python: review the ["Functions"](https://datascience.quantecon.org/python_fundamentals/functions.html) chapter found here: [./src/02_functions.ipynb](./_notebook_build/_02_functions.ipynb.ipynb)
  - Demonstrate my own, very simple module that I use, called `config`
- Write an end-to-end automatically-run program using a conda environment, the command line, and Python's `doit`. This should download data on it's own, store it somewhere as a cached data set, run the analysis, generate the charts, and insert the charts into a PDF document (do this using a Jupyter notebook).
  - Do this by looking at the structure of my `blank-project` repository.
     