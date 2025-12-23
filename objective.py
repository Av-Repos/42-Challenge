import numpy as np
from heurinder import HeurinderProblem

def evaluate_solution(solution):
    solution = np.array(solution).astype(int)

    problem = HeurinderProblem()

    assert problem.check_solution(solution), f"La solución debe de ser una lista de {problem.size} números del 0 al {problem.size-1}, sin duplicados."

    return problem.evaluate(solution)
