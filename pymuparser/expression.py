import numpy as np
import muparser


class Expression(object):
    def __init__(self, expr, vars):
        self.vars = vars
        self.values = np.array([None for i in range(len(vars))])
        muparser.init_parser(self._parse_var)
        self.expr = expr + " "

    def _parse_var(self, name):
        idx = self.vars.index(name)
        return self.values[idx]

    def evaluate(self, values):
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
