import numpy as np
from problem import ForUTwo
import itertools as it
import matplotlib.pyplot as plt
import seaborn as sns

def generate_heatmap(solution):    

    solution = np.array(solution).astype(int)

    problem = ForUTwo()
    
    mat = np.zeros((problem.size, problem.size))
    
    indexes = it.combinations(solution,2)
    
    for (i,j) in indexes:
    	mat[i][j] = problem.mat[i][j]
    
    fig, ax = plt.subplots()
    sns.heatmap(mat, annot=False, vmin=0, vmax=100, cmap="viridis", ax = ax)
    
    return fig
