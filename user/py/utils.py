import random
import warnings

"""
Función que lee la instancia en el fichero indicado.
Input:
    - path: Ruta al fichero con la instancia del problema.
Output:
    - size: Tamaño del problema.
    - mat: Matriz de preferencias del problema.
"""
def readInstance(path="preferences.dat"):
    try:
        mat = []
        with open(path,"r",encoding="utf-8") as txt:
            # Guarda el tamaño del problema
            size = int(next(txt))
            # Lee la instancia, fila por fila
            for line in txt:
                # Guarda los valores correspondientes a la fila actual
                vals = [int(x) for x in line.split(",")]
                mat.append(vals)
    except Exception as e:
        raise RuntimeError("Error al leer el fichero.") from e
    return(size,mat)

"""
Función que genera una solución aleatoria al problema.
Input: 
    - size: Tamaño del problema.
Output:
    Ordenación aleatoria de size números del 0 a size-1, sin duplicados.
"""
def randomSolution(size):
    # Crea una lista con los números del 0 a size-1
    solution = list(range(size))
    # Reordena aleatoriamente la lista
    random.shuffle(solution)
    return(solution)

"""
Función que comprueba si la solución indicada es una solución válida para el problema.
Input:
    - solution: Solución a validar.
    - size: Tamaño del problema.
Output:
    True si se trata de una solución válida, y False en caso contrario.
"""
def checkSolution(solution,size):
    if not isinstance(solution, list):
        warnings.warn("La solución debe de ser una lista de Python.")
        return(False)
    if len(solution) != size:
        warnings.warn(f"La solución debe de tener el mismo tamaño que el problema ({len(solution)}!={size}).")
        return(False)
    if set(solution) != set(range(size)):
        warnings.warn(f"La solución debe contener los números del 0 al {size-1}, sin duplicados.")
        return(False)
    return(True)