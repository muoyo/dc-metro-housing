"""
##### DATA VISUALIZATIONS #####

This module contains the functions for all the visualizations for our project.

"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Controls appearance of seaborn plots. Options: paper, notebook, talk, or poster
SEABORN_CONTEXT = 'talk' 


def barplots_2x2_matrix(dcmi, x, y, figsize=(20, 20), context=SEABORN_CONTEXT,
                        plot_titles=[['Higher Price, Lower % Private Schools', 'Higher Price, Higher % Private Schools'],
                                                 ['Lower Price, Lower % Private Schools', 'Lower Price, Higher % Private Schools']]):    

    f, ax = plt.subplots(2, 2, figsize=figsize, sharey=True)

#     plot_titles = [['Higher Price, Lower % Private Schools','Higher Price, Higher % Private Schools'],
#                    ['Lower Price, Lower % Private Schools','Lower Price, Higher % Private Schools']]

    sns.set_context(context)
    sns.despine(f)
    
    sns.barplot(dcmi.high_price_low_pct_private_schools[x], 
                dcmi.high_price_low_pct_private_schools[y], ax=ax[0][0], color='blue')
    sns.barplot(dcmi.high_price_high_pct_private_schools[x], 
                dcmi.high_price_high_pct_private_schools[y], ax=ax[0][1], color='magenta')
    sns.barplot(dcmi.low_price_low_pct_private_schools[x], 
                dcmi.low_price_low_pct_private_schools[y], ax=ax[1][0], color='red')
    sns.barplot(dcmi.low_price_high_pct_private_schools[x], 
                dcmi.low_price_high_pct_private_schools[y], ax=ax[1][1], color='green')

    for i in np.arange(0,2):
        for j in np.arange(0,2):
            plt.setp(ax[i][j].xaxis.get_majorticklabels(),rotation=90)
            ax[i][j].title.set_text(plot_titles[i][j])
            ax[i][j].set_xlim(-0.5,8-0.5)


    plt.tight_layout()
    
    return f, ax


 
def barplots_side_by_side(dcmi, x, y, plot1_title, plot2_title, figsize=(25,10), context=SEABORN_CONTEXT):
    """
    This function graphs 2 barplots side by side using a DCMetroInfo object

    """
    
    f, ax = plt.subplots(1, 2, figsize=figsize, sharey=True)
    sns.set_context(context)
    sns.despine(f)
    sns.barplot(dcmi.low_price_counties[x], dcmi.low_price_counties[y], ax=ax[0], color='red')
    plt.setp(ax[0].xaxis.get_majorticklabels(),rotation=90)
    ax[0].title.set_text(plot1_title)
    sns.barplot(dcmi.high_price_counties[x], dcmi.high_price_counties[y], ax=ax[1], color='green')
    plt.setp(ax[1].xaxis.get_majorticklabels(),rotation=90);
    ax[1].title.set_text(plot2_title)
    
    return f, ax

def barplots_side_by_side_proportion(dcmi, x, y_num, y_denom, plot1_title, plot2_title, figsize=(25,10), context=SEABORN_CONTEXT):
    """
    This function graphs 2 barplots side by side using a DCMetroInfo object

    """
    
    f, ax = plt.subplots(1, 2, figsize=figsize, sharey=True)
    sns.set_context(context)
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
