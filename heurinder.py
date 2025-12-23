import numpy as np
from numpy.typing import NDArray

class HeurinderProblem:
    """Main class of the Heurinder Optimization Problem."""

    def __init__(
        self,
        matrix_filename: str = "data/preferences.dat"
    ):
        # deserialize similarity matrix
        self.mat = np.loadtxt(matrix_filename, delimiter=",", skiprows=1)
        self.size = self.mat.shape[0]

    def check_solution(self, p: NDArray):
        """Returns `True` if the input numpy array is a valid solution and `False` otherwise."""
        return  p.size == self.size and np.unique(p).size == self.size and (np.unique(p) == np.arange(p.size)).all()

    def evaluate(self, p: NDArray):
        """Computes the objective function value (fitness) of the input solution."""
        perm_above_mat = np.triu(self.mat[p][:,p],k=1)
        return np.sum(perm_above_mat)