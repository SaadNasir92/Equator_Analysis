import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd

def make_scatter(df, x, y):
    return df.plot.scatter(x,y, edgecolors='black', alpha = .75)

def make_linregress(df, m, b, x, y, y_pred):
    pass