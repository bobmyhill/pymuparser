from pymuparser.expression import ScalarExpression
import numpy as np
import matplotlib.pyplot as plt

# In this example, we evaluate the following scalar expression
# at a user-defined set of positions.
# The expression is taken from the test vof_linear_2f.prm
# in ASPECT.
expr = "cos(init*pi)*(x-x0_0-xv*t)+sin(init*pi)*(y-y0_0-yv*t)"

# Here, the variables are defined as x and y (spatial coordinates)
# and time.
variables = ["x", "y", "t"]

# The constants are defined as a dictionary.
constants = {
    "init": 1.25,
    "x0_0": 1.0,
    "y0_0": 0.0,
    "x0_1": 0.75,
    "y0_1": 0.0,
    "xv": -0.25,
    "yv": -0.25,
    "pi": np.pi,
}

# We now define the positions over which we would like
# to evaluate the scalar expression. In this case
# we want to create a 2D grid of spatial positions
# at two distinct times.
xs = np.linspace(0, 1, 11)
ys = np.linspace(0, 1, 11)
ts = np.linspace(0, 0.5, 2)

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

# Here's where we define our parser
parser = ScalarExpression(expr, variables, constants)

# And here we evaluate the vector expression
# at the given values.
compositions = parser.evaluate(values)

# Finally, let's plot the values.
fig = plt.figure(figsize=(12, 4))
ax = [fig.add_subplot(1, 2, i) for i in range(1, 3)]

i = 0
for idx_t in range(2):

    ax[i].set_title(f"Time {ts[idx_t]}")
    cset = ax[i].contourf(xs, ys, compositions[:, :, idx_t])
    ax[i].set_xlabel("x")
    ax[i].set_ylabel("y")
    fig.colorbar(cset, ax=ax[i])
    i += 1

fig.set_tight_layout(True)
plt.show()
