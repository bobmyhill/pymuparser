# pyMuParser
This is a Python binding for MuParser (https://github.com/beltoforion/muparser).
It is based on the project by Ayuto (https://github.com/Ayuto/Py-MuParser), adapted for the modern MuParser project, and with additional helper classes.

### Installation
The easiest way to install this project on your machine, is to use pip:

`python -m pip install pymuparser`

### Getting started

Examples for scalar and vector expressions (using the `ScalarExpression` and `VectorExpression` classes in `pymuparser.expression`) are given in the examples directory (https://github.com/bobmyhill/pymuparser/tree/main/examples). A vector example with added functions (those provided by deal.II) is reproduced below:

```
from pymuparser.expression import VectorExpression
import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt

# In this example, we evaluate the following vector expression
# at a user-defined set of positions.
# The expressions are taken from the tests convection_box_phase_function.prm
# and vof_linear_2f.prm in ASPECT.
expr = "500 + 500*(erfc(z/(h*delta)) - erfc((1-z/h)/delta)) + A*cos(pi*x/h)*sin(pi*z/h) + A*cos(2*pi*x/h)*sin(pi*z/h) + A*cos(pi*x/h)*sin(2*pi*z/h) + A*cos(2*pi*x/h)*sin(2*pi*z/h);cos(init*pi)*(x-x0_1-xv*t)+sin(init*pi)*(z-z0_1-zv*t)"

# These are the deal.II functions we want to add to muparser processing.
# They must all take only one variable as argument.
extra_functions = [["int", lambda x: np.round(x, 0)],
                   ["ceil", np.ceil],
                   ["floor", np.floor],
                   ["cot", lambda x: 1./np.tan(x)],
                   ["csc", lambda x: 1./np.sin(x)],
                   ["sec", lambda x: 1./np.cos(x)],
                   ["erfc", erfc],
                   ["rand", np.random.rand],
                   ["rand_seed", np.random.seed]]


# Here, the variables are defined as x and y (spatial coordinates)
# and time.
variables = ["x", "z", "t"]

# The constants are defined as a dictionary.
constants = {
    "delta": 0.1,
    "A": 10,
    "h": 1350000,
    "init": 1.25,
    "x0_1": 0.75,
    "z0_1": 0.0,
    "xv": -0.25,
    "zv": -0.25,
    "pi": np.pi,
}

# We now define the positions over which we would like
# to evaluate the scalar expression. In this case
# we want to create a 2D grid of spatial positions
# at two distinct times.
xs = np.linspace(0, 1350000, 11)
ys = np.linspace(0, 1350000, 11)
ts = np.linspace(0, 2.e8, 2)

# To evaluate the function in the minimal number of lines,
# we use the meshgrid function of numpy to create equally
# spaced grids over x, y and t.
grid = np.array(np.meshgrid(xs, ys, ts))

# In the pymuparser functions, the loop over variables
# must be the innermost loop, but numpy meshgrid returns
# an array where the outermost loop is over the variables.
# We can deal with this by moving the first axis to the last
# position.
values = np.moveaxis(grid, 0, -1)

# Here's where we define our parser.
parser = VectorExpression(expr, variables, constants, extra_functions)

# And here we evaluate the vector expression
# at the given values.
compositions = parser.evaluate(values)

# Finally, let's plot the values.
fig = plt.figure(figsize=(12, 8))
ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]

i = 0
for idx_c in range(2):
    for idx_t in range(2):

        ax[i].set_title(f"Composition {idx_c}, time {ts[idx_t]}")
        cset = ax[i].contourf(xs, ys, compositions[idx_c, :, :, idx_t])
        ax[i].set_xlabel("x")
        ax[i].set_ylabel("y")
        fig.colorbar(cset, ax=ax[i])
        i += 1

fig.set_tight_layout(True)
plt.show()
```
