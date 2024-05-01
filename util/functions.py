import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd

def make_scatter(df, x, y, x_label, y_label, title, **kwargs):
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.scatter(df[x],df[y], **kwargs)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    
    return fig, ax

def make_linregress(df, m, b, x, y, y_pred):
    pass