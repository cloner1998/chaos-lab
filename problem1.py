from lab.iterate import simple_dynamic, iterate, draw_diagram, general_iteration, fixed_point_non_linear_dynamic1
import numpy as np

# you should see that y goes to infinity
iteration_diverge = iterate(100, 1.1, 1)
draw_diagram(iteration_diverge)

# you should see that y goes to zero
iteration_converge = iterate(100, 0.1, 1)
draw_diagram(iteration_converge)

# non-linear test
mu: float = 1.3
initial = fixed_point_non_linear_dynamic1(mu)
non_linear = general_iteration(100, mu, initial, lambda imu,x : 4 * imu * x * ( 1 - x))
draw_diagram(non_linear)