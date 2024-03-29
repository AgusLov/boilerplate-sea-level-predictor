import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    
    fig, ax = plt.subplots()
    
    ax.scatter(x,y)

    # Create first line of best fit
    result = linregress(x,y)
    x_pred = pd.Series(range(1880, 2051))
    y_pred = result.slope * x_pred + result.intercept
    
    ax.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    
    x_new = new_df['Year']
    y_new = new_df['CSIRO Adjusted Sea Level']
    
    
    result_2 = linregress(x_new, y_new)
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = result_2.slope * x_pred2 + result_2.intercept
    
    ax.plot(x_pred2, y_pred2, 'green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    ax.set_title('Rise in Sea Level')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return ax