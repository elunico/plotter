import math

from plotter.graph import Graph
from plotter.mathfunction import MathFunction, MathFunctionBase
from plotter.axes import Axes

# from plotter.everything import *
# import plotter.everything as plotter

import numpy as np

from plotter.xrange import XRange


class TrigMathFunction(MathFunctionBase):
    def __init__(self):
        super().__init__(series_name="trigonometric", color="blue", line_style=":-")

    def __call__(self, xs) -> XRange:
        return np.array([math.sin(x) ** 2 + math.cos(x) for x in xs])


class PositionOverTimeFunction(MathFunctionBase):
    def __init__(self, x0, v, a):
        super().__init__(series_name="accelerating", color="blue")
        self.x0 = x0
        self.v = v
        self.a = a

    def __call__(self, xs):
        return self.x0 + self.v * xs + 0.5 * self.a * xs * xs


class VelocityOverTimeFunction(MathFunctionBase):
    def __init__(self, v0, a):
        super().__init__(series_name="velocity", color="red")
        self.v0 = v0
        self.a = a

    def __call__(self, xs):
        return self.v0 + self.a * xs


# Example usage:
if __name__ == "__main__":
    Graph(
        VelocityOverTimeFunction(1 / 5, 1 / 9),
        PositionOverTimeFunction(1, 1 / 5, 1 / 9),
        xs=np.arange(0, 10, 1e-5),
        title="My Graph",
        axes=Axes(x_label="θ", y_label="θ`"),
    ).show()
