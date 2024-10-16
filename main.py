import math

from plotter.graph import Graph
from plotter.mathfunction import MathFunction
from plotter.axes import Axes

# from plotter.everything import *
# import plotter.everything as plotter

import numpy as np

# Example usage:
if __name__ == "__main__":
    Graph(
        MathFunction(
            lambda xs: np.array([math.sin(x) ** 2 + math.cos(x) for x in xs]),
            series_name="trigonometric",
        ),
        MathFunction(lambda xs: 0.2 * xs * xs - 3 * xs + 2, series_name="parabolic"),
        xs=np.arange(0, 10, 1e-5),
        title="My Graph",
        axes=Axes(x_label="θ", y_label="θ`"),
    ).show()
