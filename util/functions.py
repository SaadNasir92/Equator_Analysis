import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd
import numpy as np

def make_scatter(df:object, x:str, y:str, x_label:str, y_label:str, title:str, regress:bool=False, **kwargs):
    """Function designed to plot scatter and perform and plot a simple linear regression if desired.

    Args:
        df (obj): Pandas Dataframe
        x (str): Independent Variable Column Name
        y (str): Dependant Variable Column Name
        x_label (str): x_axis name
        y_label (str): y_axis name
        title (str): graph title
        regress (bool, optional): Perform linear regression. Defaults to False.

    Returns:
        Scatter plot only, set = to fig, ax to capture returned tuple. For Eg. "fig, ax = make_scatter(parameters)"
        Both scatter and linear regression, set = fig, ax, text to capture returned tuple. For Eg. "fig, ax, formula = make_scatter(parameters...regress=True)"
    """
    fig, ax = plt.subplots()
    
    ax.grid(True)
    
    ax.scatter(df[x],df[y], **kwargs)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    
    if regress:
        stat_results = linregress(df[x], df[y])
        m = stat_results.slope
        b = stat_results.intercept
        r = stat_results.rvalue
        dy = m * np.array(df[x]) + b
        reg_text = f'y={round(m,2)}x + {round(b,2)}'
        print(f'The r value is: {r}')
        ax.plot(df[x], dy, color='red')
        ax.grid(False)

        return fig, ax, reg_text

    else:
        return fig, ax
    
    

    