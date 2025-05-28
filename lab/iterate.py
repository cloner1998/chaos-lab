import numpy as np
import matplotlib.pyplot as plt

def simple_dynamic(mu: float, initial: float) -> float:
    x_next: float = mu * initial
    return x_next

## function below uses native python function and it is not fast enough
def iterate(iteration: int, mu: float, initial: float) -> list[float]:
    coordinates_list = []
    x = initial
    for i in range(iteration):
        x = simple_dynamic(mu, x)
        coordinates_list.append(x)

    return coordinates_list

##below i try to rewrite function iteration by numpy for better performance
def iteration_np(iteration: int, mu: float, initial: float) -> np.ndarray:
    mu_array = np.full(iteration, mu)
    cumulative_mu = np.cumprod(mu_array)
    return initial * cumulative_mu

def draw_diagram(coordinates_list: list[float]) -> None:
    y = coordinates_list
    x = np.arange(len(coordinates_list))
    plt.plot(x, y)
    plt.show()
    plt.close()