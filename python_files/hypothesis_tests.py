"""
##### DATA VISUALIZATIONS #####

This module contains the functions for all the visualizations for our project.

"""

import numpy as np
from scipy import stats


def chi2_contingency(contingency_matrix):
    """This function runs a chi square test for a given contingency matrix."""
    
    return stats.chi2_contingency(np.array(contingency_matrix), False)


def cohen_d(x, y):
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    
    return (np.mean(x) - np.mean(y)) / np.sqrt(((nx-1)*np.std(x, ddof=1) ** 2 + (ny-1)*np.std(y, ddof=1) ** 2) / dof)
