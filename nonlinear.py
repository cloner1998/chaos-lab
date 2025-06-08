# non-linear test
from lab.iterate import fixed_point_non_linear_dynamic1, general_iteration, draw_diagram, non_linear_dynamic1


mu: float = 0.7
initial = fixed_point_non_linear_dynamic1(mu)
print(initial)
non_linear = general_iteration(100, mu, initial, non_linear_dynamic1)
draw_diagram(non_linear)

mu: float = 0.7
initial = fixed_point_non_linear_dynamic1(mu)
print(initial)
non_linear = general_iteration(100, mu, 0.5, non_linear_dynamic1)
draw_diagram(non_linear)

mu: float = 0.76
initial = fixed_point_non_linear_dynamic1(mu)
print(initial)
non_linear = general_iteration(100, mu, 0.5, non_linear_dynamic1)
draw_diagram(non_linear)
