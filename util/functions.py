import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd
import numpy as np
import pandas as pd


def plot_scatter(x:list|pd.Series, y:list|pd.Series, x_label:str, y_label:str, title:str, regress=False, **kwargs):
    """
    Plot a scatter plot and optionally add a regression line.

    Parameters
    ----------
    x : list | Series
        The x data points.
    y : list | Series
        The y data points.
    x_label : str
        The label for the x-axis.
    y_label : str
        The label for the y-axis.
    title : str
        The title of the plot.
    regress : bool, default False
        If True, add a regression line to the plot.
    **kwargs : dict
        Additional keyword arguments to pass to the scatter function.

    Returns
    -------
    tuple
        A tuple containing the figure and axis objects, and optionally the regression formula.
    """
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.scatter(x, y, **kwargs)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    if not regress:
        return fig, ax
    else:
        y_pred, formula = perform_regress(x, y)
        ax.plot(x, y_pred, color='red')
        ax.grid(False)
        return fig, ax, formula


def perform_regress(x:list|pd.Series, y:list|pd.Series):
    """
    Perform linear regression on x and y data points.

    Parameters:
        x (list|pd.Series): The x data points.
        y (list|pd.Series): The y data points.
    
    Returns:
        tuple: The predicted y values and the regression formula as a string.
    """
    x_values = np.array(x)
    y_values = np.array(y)
    
    stat_results = linregress(x_values, y_values)
    m = stat_results.slope
    b = stat_results.intercept
    r = stat_results.rvalue
    print(f'The r value is: {r}')
    
    dy = m * np.array(x) + b
    formula_text = f'y={round(m,2)}x + {round(b,2)}'
    
    return dy, formula_text
