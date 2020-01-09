"""
##### DATA VISUALIZATIONS #####

This module contains the functions for all the visualizations for our project.

"""

import seaborn as sns
import matplotlib.pyplot as plt


# Controls appearance of seaborn plots. Options: paper, notebook, talk, or poster
SEABORN_CONTEXT = 'poster' 


 
def barplots_side_by_side(dcmi, x, y, plot1_title, plot2_title):
    """
    This function graphs 2 barplots side by side using a DCMetroInfo object

    """
    
    f, ax = plt.subplots(1, 2, figsize=(30,10), sharey=True)
    sns.set_context(SEABORN_CONTEXT)
    sns.despine(f)
    sns.barplot(dcmi.low_price_counties[x], dcmi.low_price_counties[y], ax=ax[0], color='red')
    plt.setp(ax[0].xaxis.get_majorticklabels(),rotation=90)
    ax[0].title.set_text(plot1_title)
    sns.barplot(dcmi.high_price_counties[x], dcmi.high_price_counties[y], ax=ax[1], color='green')
    plt.setp(ax[1].xaxis.get_majorticklabels(),rotation=90);
    ax[1].title.set_text(plot2_title)
    
    return f, ax

def barplots_side_by_side_proportion(dcmi, x, y_num, y_denom, plot1_title, plot2_title):
    """
    This function graphs 2 barplots side by side using a DCMetroInfo object

    """
    
    f, ax = plt.subplots(1, 2, figsize=(30,10), sharey=True)
    sns.set_context(SEABORN_CONTEXT)
    sns.despine(f)
    sns.barplot(dcmi.low_price_counties[x], 
                dcmi.low_price_counties[y_num] / dcmi.low_price_counties[y_denom], ax=ax[0], color='red')
    plt.setp(ax[0].xaxis.get_majorticklabels(),rotation=90)
    ax[0].title.set_text(plot1_title)
    sns.barplot(dcmi.high_price_counties[x], 
                dcmi.high_price_counties[y_num] / dcmi.high_price_counties[y_denom], ax=ax[1], color='green')
    plt.setp(ax[1].xaxis.get_majorticklabels(),rotation=90);
    ax[1].title.set_text(plot2_title)

    return f, ax
