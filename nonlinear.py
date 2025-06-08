# non-linear test
from lab.iterate import fixed_point_non_linear_dynamic1, general_iteration, draw_diagram, non_linear_dynamic1

'''
by finding fix point of this particular dynamic (non-linear-dynamic1) you can see that
if you set initial value same as fix point, you will see there is no change in x_j values
but your value of mu should be in 0.25 < mu <= 0.75
if your mu value is greater than 0.76, you will see your fix point which was stable, now it is not stable    
'''

'''stable fix point'''
mu: float = 0.7
initial = fixed_point_non_linear_dynamic1(mu)
print(initial)
non_linear = general_iteration(100, mu, initial, non_linear_dynamic1)
draw_diagram(non_linear)

'''stable fix point'''
mu: float = 0.7
initial = fixed_point_non_linear_dynamic1(mu)
print(initial)
non_linear = general_iteration(100, mu, 0.5, non_linear_dynamic1)
draw_diagram(non_linear)

'''non-stable fix point'''
mu: float = 0.76
initial = fixed_point_non_linear_dynamic1(mu)
print(initial)
non_linear = general_iteration(100, mu, 0.5, non_linear_dynamic1)
draw_diagram(non_linear)

'''the value mu = 0.75 is called critical value'''


'''depending on initial conditions for different values of mu'''
# you can see that by setting mu = 0.89 and just a tiny different in initial value there is no significant change
mu: float = 0.89
initial = fixed_point_non_linear_dynamic1(mu)
print(initial)
non_linear = general_iteration(100, mu, 0.5, non_linear_dynamic1)
draw_diagram(non_linear)

mu: float = 0.89
initial = fixed_point_non_linear_dynamic1(mu)
print(initial)
non_linear = general_iteration(100, mu, 0.50001, non_linear_dynamic1)
draw_diagram(non_linear)

# but here now you can see by setting mu = 0.91 and tiny different in initial value there is significant change
# in long term behavior
mu: float = 0.91
initial = fixed_point_non_linear_dynamic1(mu)
print(initial)
non_linear = general_iteration(100, mu, 0.5, non_linear_dynamic1)
draw_diagram(non_linear)

mu: float = 0.91
initial = fixed_point_non_linear_dynamic1(mu)
print(initial)
non_linear = general_iteration(100, mu, 0.50001, non_linear_dynamic1)
draw_diagram(non_linear)