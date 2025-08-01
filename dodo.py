"""Run or update the project. This file uses the `doit` Python package. It works
like a Makefile, but is Python-based
"""

#######################################
## Configuration and Helpers for PyDoit
#######################################

## Make sure the src folder is in the path
import sys

sys.path.insert(1, "./src/")

from os import getcwd
import shutil

## Custom reporter: Print PyDoit Text in Green
# This is helpful because some tasks write to sterr and pollute the output in
# the console. I don't want to mute this output, because this can sometimes
# cause issues when, for example, LaTeX hangs on an error and requires
# presses on the keyboard before continuing. However, I want to be able
# to easily see the task lines printed by PyDoit. I want them to stand out
# from among all the other lines printed to the console.
from doit.reporter import ConsoleReporter
from colorama import Fore, Style, init


class GreenReporter(ConsoleReporter):
    def write(self, stuff, **kwargs):
        self.outstream.write(Fore.GREEN + stuff + Style.RESET_ALL)


DOIT_CONFIG = {
    "reporter": GreenReporter,
    # other config here...
    # "cleanforget": True, # Doit will forget about tasks that have been cleaned.
}
init(autoreset=True)

##################################
## Begin rest of PyDoit tasks here
##################################
import config
from pathlib import Path
from doit.tools import run_once

OUTPUT_DIR = Path(config.OUTPUT_DIR)
DATA_DIR = Path(config.DATA_DIR)
DOCS_PUBLISH_DIR = Path(config.DOCS_PUBLISH_DIR)
OS_TYPE = config.OS_TYPE

## Helpers for handling Jupyter Notebook tasks
# fmt: off
## Helper functions for automatic execution of Jupyter notebooks
def jupyter_execute_notebook(notebook):
    return f"jupyter nbconvert --execute --to notebook --ClearMetadataPreprocessor.enabled=True --inplace ./src/{notebook}.ipynb"
def jupyter_to_html(notebook, output_dir=OUTPUT_DIR):
    return f"jupyter nbconvert --to html --output-dir={output_dir} ./src/{notebook}.ipynb"
def jupyter_to_md(notebook, output_dir=OUTPUT_DIR):
    """Requires jupytext"""
    return f"jupytext --to markdown --output-dir={output_dir} ./src/{notebook}.ipynb"
def jupyter_to_python(notebook, build_dir):
    """Convert a notebook to a python script"""
    return f"jupyter nbconvert --to python ./src/{notebook}.ipynb --output _{notebook}.py --output-dir {build_dir}"
def jupyter_clear_output(notebook):
    return f"jupyter nbconvert --ClearOutputPreprocessor.enabled=True --ClearMetadataPreprocessor.enabled=True --inplace ./src/{notebook}.ipynb"
# fmt: on


def copy_notebook_to_folder(notebook_stem, origin_folder, destination_folder):
    origin_path = Path(origin_folder) / f"{notebook_stem}.ipynb"
    destination_folder = Path(destination_folder)
    destination_folder.mkdir(parents=True, exist_ok=True)
    destination_path = destination_folder / f"_{notebook_stem}.ipynb"
    if OS_TYPE == "nix":
        command = f"cp {origin_path} {destination_path}"
    else:
        command = f"copy  {origin_path} {destination_path}"
    return command


def task_pull_fred():
    """ """
    file_dep = ["./src/load_fred.py"]
    file_output = ["fred.parquet"]
    targets = [DATA_DIR / "pulled" / file for file in file_output]

    return {
        "actions": [
            "ipython ./src/load_fred.py",
        ],
        "targets": targets,
        "file_dep": file_dep,
        "clean": [],  # Don't clean these files by default. The ideas
        # is that a data pull might be expensive, so we don't want to
        # redo it unless we really mean it. So, when you run
        # doit clean, all other tasks will have their targets
        # cleaned and will thus be rerun the next time you call doit.
        # But this one wont.
        # Use doit forget --all to redo all tasks. Use doit clean
        # to clean and forget the cheaper tasks.
    }


def task_pull_CRSP():
    """ """
    file_dep = ["./src/load_CRSP_stock.py"]
    targets = [
        DATA_DIR / "pulled" / "CRSP_MSF_INDEX_INPUTS.parquet",
        DATA_DIR / "pulled" / "CRSP_MSIX.parquet",
        ]

    return {
        "actions": [
            "ipython ./src/load_CRSP_stock.py",
        ],
        "targets": targets,
        "file_dep": file_dep,
        "clean": [],  # Don't clean these files by default.
    }


##############################$
## Demo: Other misc. data pulls
##############################$
# def task_pull_fred():
#     """ """
#     file_dep = [
#         "./src/load_bloomberg.py",
#         "./src/load_CRSP_Compustat.py",
#         "./src/load_CRSP_stock.py",
#         "./src/load_fed_yield_curve.py",
#         ]
#     file_output = [
#         "bloomberg.parquet",
#         "CRSP_Compustat.parquet",
#         "CRSP_stock.parquet",
#         "fed_yield_curve.parquet",
#         ]
#     targets = [DATA_DIR / "pulled" / file for file in file_output]

#     return {
#         "actions": [
#             "ipython ./src/load_bloomberg.py",
#             "ipython ./src/load_CRSP_Compustat.py",
#             "ipython ./src/load_CRSP_stock.py",
#             "ipython ./src/load_fed_yield_curve.py",
#         ],
#         "targets": targets,
#         "file_dep": file_dep,
#         "clean": [],  # Don't clean these files by default.
#     }


##################################################
# Demo for automated SQL pulls from another server
##################################################
# def task_pull_data_via_presto():
#     """
#     Run several data pulls

#     This will run commands like this:
#     presto-cli --output-format=CSV_HEADER --file=presto_something.sql > ../data/pulled/presto_something.csv

#     May need to do this first:

#     sed -ri "/^presto/d" ~/.ssh/known_hosts
#     ssh -t presto.YOURURL.edu "kinit jdoe@YOURURL.edu"


#     """
#     sql_pulls = [
#         'sql_something.sql',
#         'sql_something2.sql',
#     ]

#     def sql_action_to_csv_command(sql_file, csv_output):
#         s = f"""
#             ssh presto.YOURURL.edu <<-'ENDSSH'
#             echo Starting Presto Pull Command for {sql_file}
#             cd {getcwd()}
#             presto-cli --output-format=CSV_HEADER --file=./src/{sql_file} > {csv_output}
#             """
#         return s

#     stems = [file.split(".")[0] for file in sql_pulls]
#     for file in stems:
#         target = DATA_DIR / "pulled" / f"{file}.csv"
#         yield {
#             "name": f"{file}.sql",
#             "actions": [sql_action_to_csv_command(f"{file}.sql", target)],
#             "file_dep": [Path("./src") / f"{file}.sql"],
#             "targets": [target],
#             "clean": [],
#             # "verbosity": 0,
#         }



notebook_tasks = {
    "02_overview_of_pydata_stack.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "02_python_by_example.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "02_Using_Interact.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "HW2-numpy-scipy.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "02_comparing_plotting_libraries.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "HW2--with-solutions.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "03_01-Introducing-Pandas-Objects.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "03_02-Data-Indexing-and-Selection.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "03_03-Operations-in-Pandas.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "03_04-Missing-Values.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "03_factor_analysis_demo.ipynb": {
        "file_dep": [],
        "targets": [],
    },
    "04_CRSP_market_index.ipynb": {
        "file_dep": [
            "src/calc_CRSP_indices.py",
            "src/load_CRSP_stock.py",
            "src/test_calc_CRSP_indices.py",
            "src/misc_tools.py",
            "src/test_misc_tools.py",
            ],
        "targets": [],
    },
    "04_wrds_python_package.ipynb": {
        "file_dep": [],
        "targets": [],
    },
}



def task_convert_notebooks_to_scripts():
    """Convert notebooks to script form to detect changes to source code rather
    than to the notebook's metadata.
    """
    build_dir = Path(OUTPUT_DIR)
    build_dir.mkdir(parents=True, exist_ok=True)

    for notebook in notebook_tasks.keys():
        notebook_name = notebook.split(".")[0]
        yield {
            "name": notebook,
            "actions": [
                # jupyter_execute_notebook(notebook_name),
                # jupyter_to_html(notebook_name),
                # copy_notebook_to_folder(notebook_name, Path("./src"), "./docs_src/_notebook_build/"),
                jupyter_clear_output(notebook_name),
                jupyter_to_python(notebook_name, build_dir),
            ],
            "file_dep": [Path("./src") / notebook],
            "targets": [OUTPUT_DIR / f"_{notebook_name}.py"],
            "clean": True,
            "verbosity": 0,
        }

# fmt: off
def task_run_notebooks():
    """Preps the notebooks for presentation format.
    Execute notebooks if the script version of it has been changed.
    """

    for notebook in notebook_tasks.keys():
        notebook_name = notebook.split(".")[0]
        yield {
            "name": notebook,
            "actions": [
                """python -c "import sys; from datetime import datetime; print(f'Start """ + notebook + """: {datetime.now()}', file=sys.stderr)" """,
                jupyter_execute_notebook(notebook_name),
                jupyter_to_html(notebook_name),
                copy_notebook_to_folder(
                    notebook_name, Path("./src"), "./docs_src/_notebook_build/"
                ),
                jupyter_clear_output(notebook_name),
                # jupyter_to_python(notebook_name, build_dir),
                """python -c "import sys; from datetime import datetime; print(f'End """ + notebook + """: {datetime.now()}', file=sys.stderr)" """,
            ],
            "file_dep": [
                OUTPUT_DIR / f"_{notebook_name}.py",
                *notebook_tasks[notebook]["file_dep"],
            ],
            "targets": [
                OUTPUT_DIR / f"{notebook_name}.html",
                *notebook_tasks[notebook]["targets"],
            ],
            "clean": True,
            # "verbosity": 1,
        }
# fmt: on

sphinx_targets = [
    "./docs/html/index.html",
    "./docs/html/myst_markdown_demos.html",
    "./docs/html/apidocs/index.html",
    "./docs/html/WRDS_intro_and_web_queries.html"
]

sphinx_file_dep = [
    "./docs_src/conf.py",
    "./docs_src/index.md",
    "./docs_src/myst_markdown_demos.md",
    "./docs_src/WRDS_intro_and_web_queries.md",
    "./docs_src/discussion_01.md",
    "./docs_src/01_setting_up_environment.md",
    "./docs_src/01_methods_for_using_python.md",
    "./docs_src/HW1.md",
    "./docs_src/discussion_02.md",
    "./docs_src/syncing_files_with_git_and_github.md",
    "./docs_src/discussion_03.md",
    "./docs_src/HW3.md",
    "./docs_src/discussion_04.md",
    "./docs_src/01_vscode_cursor.md",
    "./docs_src/01_environment_faq.md",
    *[f"./src/{notebook}" for notebook in notebook_tasks.keys()],
]

def task_compile_sphinx_docs():
    """Compile Sphinx Docs"""


    return {
        "actions": ["sphinx-build -M html ./docs_src/ ./docs"], # Use docs as build destination
        # "actions": ["sphinx-build -M html ./docs/ ./docs/_build"], # Previous standard organization
        "targets": sphinx_targets,
        "file_dep": sphinx_file_dep,
        "task_dep": ["run_notebooks"],
        "clean": True,
    }

def copy_build_files_to_docs_publishing_dir():
    """
    Copy build files to the docs build directory.

    This function copies files and directories from the build directory to the
    docs publishing directory. It iterates over the files and directories in the
    'docs/html' directory and copies them to the corresponding location in the
    'DOCS_PUBLISH_DIR'. If a file or directory already exists in the target
    location, it is removed before copying.

    Additionally, this function creates a '.nojekyll' file in the
    'DOCS_PUBLISH_DIR' if it doesn't already exist.

    Note that I'm using by default the "docs" directory as the build
    directory. It is also the publishing directory. I just need
    to copy the files out of the HTML sub-directory into the
    root of the publishing directory.
    """
    # shutil.rmtree(DOCS_PUBLISH_DIR, ignore_errors=True)
    # shutil.copytree(BUILD_DIR, DOCS_PUBLISH_DIR)

    for item in (DOCS_PUBLISH_DIR / "html").iterdir():
        if item.is_file():
            target_file = DOCS_PUBLISH_DIR / item.name
            if target_file.exists():
                target_file.unlink()
            shutil.copy2(item, DOCS_PUBLISH_DIR)
        elif item.is_dir():
            target_dir = DOCS_PUBLISH_DIR / item.name
            if target_dir.exists():
                shutil.rmtree(target_dir)
            shutil.copytree(item, target_dir)

    nojekyll_file = DOCS_PUBLISH_DIR / ".nojekyll"
    if not nojekyll_file.exists():
        nojekyll_file.touch()


def task_copy_built_docs_to_publishing_dir():
    """copy_built_docs_to_publishing_dir

    # For example, convert this:
    # Copy files from this:
    ['./docs/html/index.html',
    './docs/html/myst_markdown_demos.html',
    './docs/html/apidocs/index.html']
    
    # to this:
    [WindowsPath('docs/index.html'),
    WindowsPath('docs/myst_markdown_demos.html'),
    WindowsPath('docs/apidocs/index.html')]
    """
    file_dep = sphinx_targets
    targets = [Path(DOCS_PUBLISH_DIR) / Path(*Path(file).parts[2:]) for file in sphinx_targets]

    return {
        "actions": [
            copy_build_files_to_docs_publishing_dir,
        ],
        "targets": targets,
        "file_dep": sphinx_file_dep,
        "clean": True,
    }
