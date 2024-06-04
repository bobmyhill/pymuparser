import muparser
import numpy as np


class ScalarExpression(object):
    def __init__(self, expr, vars):
        self.vars = vars
        self.values = np.array([None for i in range(len(vars))])
        self.expr = expr + " "

    def _parse_var(self, name):
        idx = self.vars.index(name)
        return self.values[idx]

    def evaluate(self, values):
        muparser.init_parser(self._parse_var)
        if len(values.shape) == 1:
            self.values = values
            muparser.clear_vars()
            return muparser.parse_expr(self.expr)
        else:
            y = np.empty(values.shape[0])
            values_list = values

            for i, vals in enumerate(values_list):
                self.values = vals
                muparser.clear_vars()
                y[i] = muparser.parse_expr(self.expr)
            return y


vars = ["x", "var", "mp_timelimit"]
expr = 'if (x < 3., mp_timelimit^var, 1.1)'
parser1 = ScalarExpression(expr, vars)


values = np.array([2., 2., 2.])
print(parser1.evaluate(values))
values = np.array([[4., 3., 1.], [2., 2., 2.]])
print(parser1.evaluate(values))

vars = ["z"]
expr = 'z * 2.'
parser2 = ScalarExpression(expr, vars)
values = np.array([[4.], [2.]])
print(parser2.evaluate(values))


values = np.array([[4., 3., 1.], [2., 2., 2.]])
print(parser1.evaluate(values))
