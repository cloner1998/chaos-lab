from lab.iterate import simple_dynamic, iterate, draw_diagram
import numpy as np

# you should see that y goes to infinity
iteration_diverge = iterate(100, 1.1, 1)
draw_diagram(iteration_diverge)

# you should see that y goes to zero
iteration_converge = iterate(100, 0.1, 1)
draw_diagram(iteration_converge)
