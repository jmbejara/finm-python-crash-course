# 1.2 Ways to Interact with Python

Throughout the course, we'll discuss the various ways of interacting with Python: 
using the standard Python interpreter in the terminal, 
using IPython in the terminal,
running Python scripts directly from the command line (`.py` files), 
using Google Collab, 
Jupyter Notebooks through the standard Jupyter server (Jupyter Lab and Jupyter Notebook), 
Jupyter Notebooks in VS Code, 
and using the Python Interactive window in VS Code.

The point here is that there are many ways to interact with Python and you should be aware of the different options available to you and have an idea of when to use each one.

## Running Python in the Terminal

The **standard Python interpreter** can be run from the terminal by typing `python` and pressing enter. This will open the Python interpreter and you can start typing Python code directly into the terminal. You may have to use
the Anaconda Prompt, depending on how you installed Python (e.g., whether Python and/or `conda` is in your PATH).

![Python in the terminal](assets/python_interpreter_hello_world.png)

**IPython** is an enhanced interactive Python shell that has many features that make it easier to work with Python. To start IPython, type `ipython` in the terminal and press enter.

![IPython in the terminal](assets/ipython_interpreter_hello_world.png)

**Running `.py` files** is the main way that one might interact with Python. You can write Python code in a text file and save it with a `.py` extension. You can then run the file from the terminal by typing `python filename.py` and pressing enter. Using the Python interpreter interactively is useful for developing code, but once the code is written, it will exist in a `.py` file.

![Running a `.py` file script](assets/python_hello_world.png)


```{note} 
Let's pause here and make sure everyone is able to run each. Let's make sure that you can save a `.py` file and navigate the terminal to the proper path to run the file. 
```


## Jupyter Notebooks

**Jupyter Notebooks** are a great way to interact with Python. They allow you to write and run Python code in a web browser. Jupyter Notebooks are great for developing code, writing reports, and sharing code with others.


![Jupyter Notebook](assets/jupyterpreview.png)


```{note}
Discussion: Why have the creators of Jupyter designed it to be a web-based application? What are the advantages and disadvantages of this design choice?
```

JupyterLab is the next-generation web-based interface for Project Jupyter. It allows you to use Jupyter Notebooks, text editors, terminals, and custom components all in one place.

![Jupyter Lab](assets/jupyterlab_advantages.png)


```{note}
Discussion: What are some pros and cons of Jupyter Notebook vs Jupyter Lab?
```


## Python and Jupyter in VS Code

Here I just want to make sure that students can understand the basics of using Python in VS code. We will revisit the topic of using VS Code and all of it's features later. Here, I want to just introduce the highlights and just make sure that students understand basic use of Python in VS Code.

![Python Interactive Window in VS Code](assets/python_interactive_vscode.png)


```{note}
- Discuss the features of Python Interactive in VS Code listed here: https://code.visualstudio.com/docs/python/jupyter-support-py
```


![Jupyter Notebook in VS Code](assets/jupyter_notebook_vscode.png)


```{note}
Discuss the features of Jupyter Notebooks in VS Code listed here: https://code.visualstudio.com/docs/datascience/jupyter-notebooks
```


**GitHub Copilot in VS Code**
GitHub Copilot is an AI pair programmer that helps you write code faster. GitHub Copilot draws context from comments and code, suggesting whole lines or entire functions instantly. See here: https://code.visualstudio.com/docs/copilot/overview

<iframe width="560" height="315" src="https://www.youtube.com/embed/jXp5D5ZnxGM?si=nnyEh0WEdUa8QzZa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>






