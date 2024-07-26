r"""
You can test out the latex code in the following minimal working
example document:

\documentclass{article}
\usepackage{booktabs}
\begin{document}
First document. This is a simple example, with no 
extra parameters or packages included.

\begin{table}
\centering
YOUR LATEX TABLE CODE HERE
%\input{example_table.tex}
\end{table}
\end{document}

"""
import pandas as pd
import numpy as np
np.random.seed(100)

import config
from pathlib import Path
DATA_DIR = Path(config.DATA_DIR)
OUTPUT_DIR = Path(config.OUTPUT_DIR)


## Suppress scientific notation and limit to 3 decimal places
# Sets display, but doesn't affect formatting to LaTeX
pd.set_option('display.float_format', lambda x: '%.2f' % x)
# Sets format for printing to LaTeX
float_format_func = lambda x: '{:.2f}'.format(x)


df = pd.DataFrame(np.random.random((5, 5)))
latex_table_string = df.to_latex(float_format=float_format_func)
print(latex_table_string)

path = OUTPUT_DIR / f'pandas_to_latex_simple_table1.tex'
with open(path, "w") as text_file:
    text_file.write(latex_table_string)

