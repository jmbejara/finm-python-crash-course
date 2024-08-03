# FINM August Review: Python
  

## Summary

The FINM August Review is a series of lectures designed for incoming students to prepare for starting with the Financial Mathematics program. The Python Introduction and Review portion is designed to be a refresher or short introduction to the Python programming language. No prior experience is necessary. Even though some incoming students may have extensive prior experience with Python, this review is designed for those with little experience. The aim is to introduce you to what you need to know for the upcoming FINM program. The academic lectures of September Launch and autumn quarter will assume students have mastered the concepts covered throughout August Review, and so it’s critical that all students enter the year with a solid grasp of this material. 


```{note}
This class will be most useful to you if it is interactive. Please ask questions and participate in the discussion. 
Furthermore, we will plan pauses in the middle of lectures to give time to help students one-on-one with their setup. Please plan to follow along with all of the steps as we go along, so we can troubleshoot the issues as they arise.
```


## Course Info

- **Class:** 
 - Discussion 1: Tuesday, July 31: 6-9pm CT on Zoom
 - Discussion 2: Friday, August 1: 6-9pm CT on Zoom
 - Discussion 3: Tuesday, August 14: 6-9pm CT on Zoom
 - Discussion 4: Friday, August 15: 6-9pm CT on Zoom
- **Lecturer:** Jeremy Bejarano, jeremiah.bejarano@gmail.com
- **Notes:** https://jeremybejarano.com/finm-python-crash-course/
- **Canvas:** https://canvas.uchicago.edu/courses/57668 will be used for grades. 
- **Code Repository:** Code for the course will be hosted on GitHub: https://github.com/jmbejara/finm-python-crash-course 

**Required Software**
Each lecture after this will use the following software. Please make sure to install these before then. If you need help installing this software, please  ask for help in the discussion section on Canvas.

 - Python 3.11 or greater, Anaconda Distribution
   - For this class, please download the [Anaconda distribution of Python](https://www.anaconda.com/products/distribution). Be sure to download current version, with Python version 3.9. or greater. When you install Anaconda, be sure to install the full Anaconda distribution. 
   The MiniConda version is nice, but I only recommend it for advanced users. Nice instructions for installing and using Anaconda can be found (here.)[https://datascience.quantecon.org/introduction/local_install.html]
 - The Visual Studio Code (VS Code) text editor
   - A good text editor is important for software development. Some of your classes will use a fully-fledged Integrated Development Environment (IDE) like PyCharm. For this review, I suggest Visual Studio Code. You can download it here: https://code.visualstudio.com/
   - There are several VS Code extensions that I recommend installing. To learn about extensions, see [here.](https://code.visualstudio.com/docs/editor/extension-marketplace) I recommend installing at least these two extensions: the [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) and [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) VS Code extensions.
 - Git
   - Although there are many different Git clients and Git GUI's that you could use,
   I prefer that you install GitKraken. You will need to install both 
   Git (link here: https://git-scm.com/downloads) and GitKraken (link here: https://www.gitkraken.com/).
   You can also try GitHub Desktop if you like (link here: https://github.com/apps/desktop), but please at least install GitKraken.
   - GitKraken is free for students. You can get a free license by signing up with your student email address. More information about this here: https://www.gitkraken.com/github-student-developer-pack
   - Some classes will use GitHub. GitHub is a website that allows you to store, interact with, and share your Git repositories online. [Please register an account with GitHub](https://github.com/) if you don't already have one.

*NOTE:* It's also important that you have a quality laptop. I recommend a laptop with at least 16GB of RAM and at least 500 GB of storage (at a minimum). 
So much of your schooling and of your job will revolve around your laptop. 
It's important to invest in a good one. If you have any questions about your laptop, please ask in the discussion section on Canvas.

**WRDS Account**

This course requires that you create a WRDS account. WRDS is a comprehensive data research platform that provides access to a wide range of financial, economic, and marketing data.
Follow the instructions [here](./01_setting_up_environment.md#wrds-how-do-i-sign-up) to sign up.



## Helpful References

A lot of my lecture material will use content from the following helpful books:

* [Introduction to Economic Modeling and Data Science](https://datascience.quantecon.org/), by Thomas J. Sargent and John Stachurski (QuantEcon)
* Note, the whole lectures series on QuantEcon's website is very good: [Quantitative Economics](https://lectures.quantecon.org/), by Thomas J. Sargent and John Stachurski (QuantEcon)
* [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/), by Jake VanderPlas (PDSH)
* [Python for Data Analysis, 2nd Edition](https://github.com/wesm/pydata-book), by Wes McKinney (PDA)

## Table of Contents / Schedule


```{toctree}
:maxdepth: 1
:caption: Discussion 1
discussion_01.md
01_setting_up_environment.md
01_methods_for_using_python.md
01_vscode_cursor.md
01_environment_faq.md
HW1.md
```

```{toctree}
:maxdepth: 1
:caption: Discussion 2
discussion_02.md
syncing_files_with_git_and_github.md
WRDS_intro_and_web_queries.md
_notebook_build/_02_01-Introducing-Pandas-Objects.ipynb
_notebook_build/_02_02-Data-Indexing-and-Selection.ipynb
_notebook_build/_02_03-Operations-in-Pandas.ipynb
_notebook_build/_02_04-Missing-Values.ipynb
_notebook_build/_02_CRSP_market_index.ipynb
```

```{toctree}
:maxdepth: 1
:caption: Discussion 3
discussion_03.md
_notebook_build/_03_overview_of_pydata_stack.ipynb
_notebook_build/_03_comparing_plotting_libraries.ipynb
_notebook_build/_03_Using_Interact.ipynb
_notebook_build/_03_python_by_example.ipynb
_notebook_build/_HW2-numpy-scipy.ipynb
_notebook_build/_03_factor_analysis_demo.ipynb
HW3.md
```

```{toctree}
:maxdepth: 1
:caption: Discussion 4️
discussion_04.md
using_CRSP_data.md
_notebook_build/_04_wrds_python_package.ipynb
```


```{toctree}
:maxdepth: 1
:caption: Appendix
myst_markdown_demos.md
apidocs/index
```


## Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`

