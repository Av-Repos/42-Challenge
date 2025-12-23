import numpy as np
from problem import ForUTwo

def evaluate_solution(solution):
    solution = np.array(solution).astype(int)

    problem = ForUTwo()

    assert problem.check_solution(solution), f"La solución debe de ser una lista de {problem.size} números del 0 al {problem.size-1}, sin duplicados."

    return problem.evaluate(solution)
