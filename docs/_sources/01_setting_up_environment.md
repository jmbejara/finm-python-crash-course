# 1.1 Setting up your computing environment

## Required Software

As noted on the first page, this review session requires the following software:

 - **Python 3.11 or greater, Anaconda Distribution**
   - For this class, please download the [Anaconda distribution of Python](https://www.anaconda.com/products/distribution). Be sure to download current version, with Python version 3.9. or greater. When you install Anaconda, be sure to install the full Anaconda distribution. 
   The MiniConda version is nice, but I only recommend it for advanced users. Nice instructions for installing and using Anaconda can be found (here.)[https://datascience.quantecon.org/introduction/local_install.html]

```{note}
I highly recommend checking the box to add Anaconda to your PATH. This will make it easier to use Anaconda from the command line.
This is an option you can choose when you install Anaconda. (See the image below.) However, you can also add Anaconda to your PATH after installation. See [Common Issues](#common-issues) below.

```

```{image} ./assets/anaconda_add_to_path.png
:alt: Add Anaconda to PATH
:class: bg-primary
:width: 66%
:align: center
```



 - **The Cursor AI Code Editor**
   - A good text editor is important for software development. Some of your classes will use a fully-fledged Integrated Development Environment (IDE) like PyCharm. For this review, I suggest that you use Cursor. You can download it here: https://www.cursor.com/
   - Cursor has many of the same extensions available as VS Code. To learn about extensions, see [here.](https://code.visualstudio.com/docs/editor/extension-marketplace) I recommend installing at least these two extensions: the [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) and [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extensions.
   - **Important for Students**: Cursor offers a **free one-year Pro subscription for verified students**. To claim your free year, visit https://www.cursor.com/students and follow the verification process using your university email (.edu address).

 - **Git**
   - Although there are many different Git clients and Git GUI's that you could use,
   I prefer that you install GitHub Desktop. You will need to install both 
   Git (link here: https://git-scm.com/downloads) 
   and GitHub Desktop (link here: https://github.com/apps/desktop).
   - Some classes will use GitHub. GitHub is a website that allows you to store, interact with, and share your Git repositories online. [Please register an account with GitHub](https://github.com/) if you don't already have one.

   - Some classes will use GitHub. GitHub is a website that allows you to store, interact with, and share your Git repositories online. [Please register an account with GitHub](https://github.com/) if you don't already have one.

 - **GitHub**

```{note}
It's also important that you have a quality laptop. I recommend a laptop with at least 16GB of RAM and at least 500 GB of storage (at a minimum). 
So much of your schooling and of your job will revolve around your laptop. 
It's important to invest in a good one. If you have any questions about your laptop, please ask in the discussion section on Canvas.
```


## What is Anaconda?

Anaconda is a free and open-source distribution of Python and R programming languages for scientific computing, that aims to simplify package management and deployment. Package versions are managed by the package management system `conda`. Anaconda is widely used in the scientific community and data science, as it simplifies the installation of packages and their dependencies.


- What is the different between Python and Anaconda?
  - Python is a general purpose programming language. It's not just used for data science, etc. It is also used in web development, as example. For example, Python is used in the back end of the website Reddit was used to create parts of YouTube back in the day. 
  - Anaconda, on the other hand, is a software *distribution*. It is a collection of Python packages that are targeted towards data science and scientific computing.
  There are other distributions of Python that are also targeted towards scientific computing, but Anaconda is one of the most popular ones.
  - Anaconda is a set of about a hundred packages that are useful for data science and scientific computing, including conda, numpy, scipy, ipython notebook, and so on.
- What's the difference between Anaconda and `conda`?
  - Anaconda is a software distribution, while `conda` is the package manager that comes with the Anaconda distribution. 
  - `conda` is a package manager that installs packages from the Anaconda repository as well as from other repositories. A package manager is useful for installing new packages, 
  keeping track of the packages you have installed, and updating packages. 
  - `conda` also makes it easy to manage software environments. This is useful when you have different projects that require different versions of packages.


```{note} 
Let's pause here and make sure that everyone has Anaconda installed. Let's test the following. Please raise your hand if any of these things is not working:

- Open a terminal and type `conda --version`. You should see the version of `conda` that you have installed. Depending on how you installed Anaconda, you may 
 have to open the Anaconda Prompt on Windows.
- Type `conda activate` to make sure that you can activate the base environment. Later on we'll create our own environment for use in our projects.
- Type `jupyter notebook` to make sure that you can open a Jupyter notebook. This will open a new tab in your web browser with the Jupyter notebook interface.
- Type `jupyter lab` to try out Jupyter Lab. This is a newer interface that is similar to Jupyter notebook but has more features.
```

### Common Issues

- *Running `conda` in the terminal gives an error message*: There are two common problems. The first is that `conda` is not in your `PATH`. The second is that you're using Powershell.
  - If `conda` is not in your `PATH`, you can add it by following the directions [here](https://stackoverflow.com/a/44597801/1411791).
  - If you're using Powershell, you have two options. Switch to Command Prompt or initialize Powershell. I recommend using Command Prompt. You can set it as the default terminal in VS Code with the directions found [here](https://stackoverflow.com/a/61300365/1411791). This also links to some directions on how to initialize Powershell for use with Anaconda.



## What is Visual Studio Code?

Visual Studio Code is a lightweight code editor that is great for Python development. It has a lot of features that make it a great editor for data science work.

- **IntelliSense**: IntelliSense is a feature that helps you write code faster. It provides code completions based on variable types, function definitions, and imported modules.
- **Debugging**: Visual Studio Code has a built-in debugger that makes it easy to debug your Python code.
- **Git integration**: Visual Studio Code has built-in Git integration that makes it easy to work with Git repositories.
- **Extensions**: Visual Studio Code has a rich ecosystem of extensions that add additional functionality to the editor. There are extensions for Jupyter notebooks, Python, and many other languages and tools.


- What's the difference between Visual Studio and Visual Studio Code?
    - Visual Studio is a full-fledged Integrated Development Environment (IDE) that is used primarily for developing in C# and .NET. It is a very powerful IDE that has a lot of features.
    - Visual Studio Code (VS Code), on the other hand, is a lightweight code editor. Visual Studio Code has become a very popular editor for Python development and will be better suited for data science work than Visual Studio (the IDE).

<iframe width="560" height="315" src="https://www.youtube.com/embed/KMxo3T_MTvY?si=DIfqvwpEwJfQk2Dn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## What is Cursor and Why Are We Using It?


<iframe width="560" height="315" src="https://www.youtube.com/embed/LR04bU_yV5k?si=_FkL8X4dvxEHdfnI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

I've explained Visual Studio Code above as a foundation for understanding Cursor. **Cursor is a fork of VS Code**, meaning it's built on the same foundation but with significant AI-powered enhancements. The two editors are extremely similar in their core functionality, with nearly identical:
- User interface and layout
- Extension compatibility (most VS Code extensions work in Cursor)
- Keyboard shortcuts and commands
- Git integration and debugging capabilities

The key difference is that Cursor includes built-in AI capabilities that go far beyond what's available in VS Code with GitHub Copilot. While VS Code users can install GitHub Copilot as an extension for AI assistance, Cursor provides:

- **Multiple AI Models**: Access to GPT-4, Claude 3.5, and other cutting-edge language models
- **Context-Aware Code Generation**: AI that understands your entire codebase, not just the current file
- **Natural Language to Code**: Write descriptions of what you want, and Cursor generates the code
- **AI-Powered Debugging**: Get intelligent help fixing errors and understanding complex code
- **Smart Refactoring**: AI assists in improving code structure and efficiency


[![Cursor Bloomberg Article](./assets/cursor_bloomberg_article.png)](https://www.bloomberg.com/news/articles/2025-04-07/cursor-an-ai-coding-assistant-draws-a-million-users-without-even-trying)



### Why Cursor is Essential for Modern Development

In today's rapidly evolving tech landscape, **learning to work with AI coding assistants is no longer optional, it's essential**. Cursor represents the leading edge of AI-assisted development, and mastering it now will give you a significant advantage in both your studies and future career. Here's why:

1. **Industry Adoption**: Major tech companies and startups are rapidly adopting AI coding tools. Being proficient with these tools is becoming a expected skill.

2. **Productivity Multiplier**: Students report completing assignments 40-60% faster with Cursor, allowing more time for understanding concepts rather than wrestling with syntax.

3. **Learning Accelerator**: Cursor can explain complex code, suggest improvements, and help you learn new programming patterns and best practices in real-time.

4. **Competitive Advantage**: As AI tools become standard in the industry, those who master them early will have a significant edge in internships and job applications.



```{note} 
Let's pause here and make sure that everyone has Cursor installed. We'll run a few test files and configure Cursor with some helpful defaults. Please raise your hand if any of these things is not working:

- Open Cursor and create a new Python file. You can do this by clicking on the New File button in the top left corner of the window and then saving the file with a `.py` extension.
- Make sure the proper extensions are installed: Python and Jupyter. Also, you might consider the following additional extensions: Black Formatter, Data Wrangler, Excel Viewer, Markdown Preview Github styling, Rainbow CSV, Rewrap, Code Spell Checker, and GitLens.
- Set the default terminal in Windows to Command Prompt. Use the "Select Default Profile" option in the Cursor terminal to do this. You may also want to memorize the keyboard shortcuts for Cursor. You can start with the command ``ctrl + ` ``.
- Open the terminal in Cursor and type `python --version` to make sure that Python is installed and that Cursor can find it.
- Try running `conda activate` in the terminal.
- Create a Python file `.py` and try using Cursor's AI features. Press `Ctrl+K` (or `Cmd+K` on Mac) to generate code from a natural language prompt.
- Test the AI chat feature by pressing `Ctrl+L` (or `Cmd+L` on Mac) to ask questions about your code.
- Claim your free student subscription at https://www.cursor.com/students if you haven't already.
```


## What is Git and GitHub?

Git is a distributed version control system that is used to track changes in source code during software development. It is designed to handle everything from small to very large projects with speed and efficiency. GitHub is a website that allows you to store, interact with, and share your Git repositories online. GitHub is a great tool for collaborating with others on software projects and for sharing your code with the world.

Please watch the following video to learn more about version control with Git:

<iframe width="560" height="315" src="https://www.youtube.com/embed/M-O8ZNW9icQ?si=4nDDihfcrD4YwjJH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Now, let's take a look at GitHub.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4lkrx2U9f6I?si=nG5NzBGowiyGhgPN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

You can find another nice video about GitHub [here.](https://www.youtube.com/watch?v=pBy1zgt0XPc)
The code for this course is available on GitHub. You can find the repository [here](https://github.com/jmbejara/finm-python-crash-course).


```{note} 
Let's pause here and make sure that everyone has Git installed and is able to download the code for the course.

- First, let's make sure that everyone has an account on GitHub. If you don't have an account, please create one now.
- Open a new Window in VS Code and choose the option to clone a repository. Clone the repository for this course: https://github.com/jmbejara/finm-python-crash-course . 
- Be sure to choose a good place for your Git repositories. Try not to put them in a folder that is synced with a cloud service like Dropbox or Google Drive. Git is what we'll be using to sync files, not Dropbox or Googe Drive. Putting a Git repo in a Dropbox folder is like putting a Google Drive folder inside of Dropbox. It's redundant.
- Open the Git tab in VS Code and see what happens when you make a change to a file in the repository. Notice how you can see the changes in the Git tab. You can stage the changes and commit them to the repository. For now, we won't worry about pushing the changes to GitHub. We'll do that in a later discussion.
- Discuss: What is the difference between Git and GitHub?
```

## Installing the Required Packages for this Course

Now that we have cloned the repository for this course, let's install the
required packages. For the code that we use today, you should be fine with the
packages that come with the Anaconda distribution. However, we will be using
additional packages in future discussions. 


You'll need to make sure that you navigate to the directory where you cloned the
repository before running the required commands. You can do this by running the
following command in the terminal:

```bash
cd path/to/finm-python-crash-course
```

Now, you can install the required packages by running the following command in the terminal:

```bash
conda create -n finm python=3.12
conda activate finm 
pip install -r requirements.txt
```


Test that the packages are installed by running the following command in a Python interpreter:
  
```python
import numpy as np
import decouple
``` 


## WRDS: How do I sign up?

[![WRDS Logo](./assets/wrds_logo.png)](https://wrds-www.wharton.upenn.edu/)

This course requires that you create a WRDS account. WRDS is a comprehensive data research platform that provides access to a wide range of financial, economic, and marketing data.
Follow the instructions below to create an account.

```{important}
If you have not requested an account already, please do so ASAP. You will need this for the next session.
```



**New to WRDS?**

Use the following link to access the WRDS Registration form at https://wrds-www.wharton.upenn.edu/register/?user_type=class-student

- Follow the directions on the Registration form to enter your identifying information.
  - For the Subscriber, select your school's name from the drop-down list. 
  - Your User type, Class - Students with Code, has been selected by default.
  - You will need to enter the course code. This can be found on Canvas here: TODO

- Click the Register for WRDS button.
  - WRDS accounts require two-factor authentication. We recommend you use a smartphone for the verification process. First, install the Duo Mobile app on your phone. This free app can be downloaded through your device’s app store. Follow the directions at How to Log into WRDS to register your smartphone and use Duo two-factor authentication to set up your WRDS account.

**Already Have a WRDS Account?**

After you have logged into WRDS, use the following steps to enroll in our class account. You will need the Class Code above to enroll.

 - In the top right corner of the screen, select Your Account > Your Account Info.
 - Scroll down until you see the Your Classes table and click the Enroll in a Class button.
 - Enter the Class Code and click Submit. You can find the code here: TODO


```{important}
If you have any difficulty setting up your account please contact WRDS Support at: https://wrds-www.wharton.upenn.edu/contact-support/. When opening your support ticket you must use the email associated with your existing WRDS account, or the email you intend to use to set up your new WRDS account.
```






