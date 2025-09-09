import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    result = linregress(x, y)
    x_pred = pd.Series(range(1880, 2051))
    y_pred = result.slope * x_pred + result.intercept
    plt.plot(x_pred, y_pred, color='green')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    result_recent = linregress(x_recent, y_recent)
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = result_recent.slope * x_pred_recent + result_recent.intercept
    plt.plot(x_pred_recent, y_pred_recent, color='blue')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()