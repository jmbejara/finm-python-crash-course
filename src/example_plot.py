import load_fred
import config
from pathlib import Path
DATA_DIR = Path(config.DATA_DIR)
OUTPUT_DIR = Path(config.OUTPUT_DIR)

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

sns.set()

df = load_fred.load_fred(data_dir=DATA_DIR)

(
    100 * 
    df[['CPIAUCNS', 'GDPC1']]
    .rename(columns={'CPIAUCNS':'Inflation', 'GDPC1':'Real GDP'})
    .dropna()
    .pct_change(4)
    ).plot()
plt.title("Inflation and Real GDP, Seasonally Adjusted")
plt.ylabel('Percent change from 12-months prior')
filename = OUTPUT_DIR / 'example_plot.png'
plt.savefig(filename);
