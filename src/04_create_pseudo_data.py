"""Create pseudo data and save to disk.

Let's also crate a plot and save to disk.
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = np.random.randn(100).reshape((10,10))
df = pd.DataFrame(data)
df.to_csv('pseudo_data.csv', index=False)

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.savefig('sine.png')




