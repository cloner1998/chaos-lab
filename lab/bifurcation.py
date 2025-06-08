# finding bifurcation point of non-linear-dynamic1
from iterate import *

def dynamic_func_transient(mu:float, initial:float, iteration: int, transient:int
                           , dynamic_func: Callable[[float, float], float]):
    x = initial
    for i in range(transient):
        x = dynamic_func(mu, x)

    values = []
    for i in range(iteration):
        x = dynamic_func(mu, x)
        values.append(x)

    return np.array(values)

def find_period(values, tolerance = 1e-6):
    n = len(values)
    for period in range(1, n//4):
        periodic = True
        for i in range(period, min(n, 4 * period)):
            if abs(values[i] - values[i - period]) > tolerance:
                periodic = False
                break
        if periodic:
            return period
    return -1