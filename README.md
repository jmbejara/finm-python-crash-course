# FINM August Review: Python
  

## Summary

The FINM August Review is a series of lectures designed for incoming students to prepare for starting with the Financial Mathematics program. The Python Introduction and Review portion is designed to be a refresher or short introduction to the Python programming language. No prior experience is necessary. Even though some incoming students may have extensive prior experience with Python, this review is designed for those with little experience. The aim is to introduce you to what you need to know for the upcoming FINM program. The academic lectures of September Launch and autumn quarter will assume students have mastered the concepts covered throughout August Review, and so it’s critical that all students enter the year with a solid grasp of this material. 

## Course Info

* **Class:** 
 - Discussion 1: Tuesday, July 30: 6-9pm CT on Zoom
 - Discussion 2: Friday, August 2: 6-9pm CT on Zoom
 - Discussion 3: Tuesday, August 6: 6-9pm CT on Zoom
 - Discussion 4: Friday, August 9: 6-9pm CT on Zoom

* **Lecturer:** Jeremy Bejarano, jeremiah.bejarano@gmail.com
* **Website:** 
 - Canvas: https://canvas.uchicago.edu/courses/57668 will be used for grades. 
 - Lecture notes will be hosted here: https://jeremybejarano.com/finm-python-crash-course/
 - Code for the course will be hosted on GitHub: https://github.com/jmbejara/finm-python-crash-course 

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
   I prefer that you install GitHub Desktop. You will need to install both 
   Git (link here: https://git-scm.com/downloads) 
   and GitHub Desktop (link here: https://github.com/apps/desktop).
   - Some classes will use GitHub. GitHub is a website that allows you to store, interact with, and share your Git repositories online. [Please register an account with GitHub](https://github.com/) if you don't already have one.

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


# Quick Start

To quickest way to run code in this repo is to use the following steps. First, you must have the `conda`  
package manager installed (e.g., via Anaconda). However, I recommend using `mamba`, via [miniforge]
(https://github.com/conda-forge/miniforge) as it is faster and more lightweight than `conda`. Second, you 
must have TexLive (or another LaTeX distribution) installed on your computer and available in your path.
You can do this by downloading and 
installing it from here ([windows](https://tug.org/texlive/windows.html#install) 
and [mac](https://tug.org/mactex/mactex-download.html) installers).
Having done these things, open a terminal and navigate to the root directory of the project and create a 
conda environment using the following command:
```
conda create -n finm python=3.12
conda activate finm
```
and then install the dependencies with pip
```
pip install -r requirements.txt
```
Finally, you can then run 
```
doit
```
And that's it!

If you would also like to run the R code included in this project, you can either install
R and the required packages manually, or you can use the included `environment.yml` file.
To do this, run
```
mamba env create -f environment.yml
```
I'm using `mamba` here because `conda` is too slow. Activate the environment. 
Then, make sure to uncomment
out the RMarkdown task from the `dodo.py` file. Then,
run `doit` as before.

## Other commands

### Unit Tests and Doc Tests

You can run the unit test, including doctests, with the following command:
```
pytest --doctest-modules
```
You can build the documentation with:
```
rm ./src/.pytest_cache/README.md 
jupyter-book build -W ./
```
Use `del` instead of rm on Windows

### Setting Environment Variables

This can be done easily in a Linux or Mac terminal with the following command:
```
set -a
source .env
set +a
```
In Windows, this can be done with the included `set_env.bat` file,
```
set_env.bat
```

# General Directory Structure

 - The `assets` folder is used for things like hand-drawn figures or other pictures that were not generated from code. These things cannot be easily recreated if they are deleted.

 - The `output` folder, on the other hand, contains tables and figures that are generated from code. The entire folder should be able to be deleted, because the code can be run again, which would again generate all of the contents.

 - I'm using the `doit` Python module as a task runner. It works like `make` and the associated `Makefile`s. To rerun the code, install `doit` (https://pydoit.org/) and execute the command `doit` from the `src` directory. Note that doit is very flexible and can be used to run code commands from the command prompt, thus making it suitable for projects that use scripts written in multiple different programming languages.

 - I'm using the `.env` file as a container for absolute paths that are private to each collaborator in the project. You can also use it for private credentials, if needed. It should not be tracked in Git.

# Data and Output Storage

I'll often use a separate folder for storing data. I usually write code that will pull the data and save it to a directory in the data folder called "pulled"  to let the reader know that anything in the "pulled" folder could hypothetically be deleted and recreated by rerunning the PyDoit command (the pulls are in the dodo.py file).

I'll usually store manually created data in the "assets" folder if the data is small enough. Because of the risk of manually data getting changed or lost, I prefer to keep it under version control if I can.

Output is stored in the "output" directory. This includes tables, charts, and rendered notebooks. When the output is small enough, I'll keep this under version control. I like this because I can keep track of how tables change as my analysis progresses, for example.

Of course, the data directory and output directory can be kept elsewhere on the machine. To make this easy, I always include the ability to customize these locations by defining the path to these directories in environment variables, which I intend to be defined in the `.env` file, though they can also simply be defined on the command line or elsewhere. The `config.py` is reponsible for loading these environment variables and doing some like preprocessing on them. The `config.py` file is the entry point for all other scripts to these definitions. That is, all code that references these variables and others are loading by importing `config`.


# Dependencies and Virtual Environments

## Working with `pip` requirements

`conda` allows for a lot of flexibility, but can often be slow. `pip`, however, is fast for what it does.  You can install the requirements for this project using the `requirements.txt` file specified here. Do this with the following command:
```
pip install -r requirements.txt
```

The requirements file can be created like this:
```
pip list --format=freeze
```

## Working with `conda` environments

The dependencies used in this environment (along with many other environments commonly used in data science) are stored in the conda environment called `blank` which is saved in the file called `environment.yml`. To create the environment from the file (as a prerequisite to loading the environment), use the following command:

```
conda env create -f environment.yml
```

Now, to load the environment, use

```
conda activate blank
```

Note that an environment file can be created with the following command:

```
conda env export > environment.yml
```

However, it's often preferable to create an environment file manually, as was done with the file in this project.

Also, these dependencies are also saved in `requirements.txt` for those that would rather use pip. Also, GitHub actions work better with pip, so it's nice to also have the dependencies listed here. This file is created with the following command:

```
pip freeze > requirements.txt
```

**Other helpful `conda` commands**

- Create conda environment from file: `conda env create -f environment.yml`
- Activate environment for this project: `conda activate blank`
- Remove conda environment: `conda remove --name blank --all`
- Create blank conda environment: `conda create --name myenv --no-default-packages`
- Create blank conda environment with different version of Python: `conda create --name myenv --no-default-packages python` Note that the addition of "python" will install the most up-to-date version of Python. Without this, it may use the system version of Python, which will likely have some packages installed already.

## `mamba` and `conda` performance issues

Since `conda` has so many performance issues, it's recommended to use `mamba` instead. I recommend installing the `miniforge` distribution. See here: https://github.com/conda-forge/miniforge

