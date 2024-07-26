import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path

import config




import my_plotting_module

config.read('output_dir')

my_plotting_module.plot_sine_function(N=5)
my_plotting_module.plot_sine_function(N=15)

plt.clf()
my_plotting_module.plot_sine_function(N=1000)
plt.savefig(config.output_dir / 'mysine.png')