import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def plot_sine_function(N=1000):
    x = np.linspace(-10, 10, N)
    y = np.sin(x)
    plt.plot(x, y)
