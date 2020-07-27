from pysat.solvers import Glucose3

from famapy.core.operations.Valid import Valid
from famapy.metamodels.pysat_metamodel.models.PySATModel import PySATModel


class Glucose3Valid(Valid):

    def __init__(self):
        self.res = False

    def execute(self, model):
        g = Glucose3()
        for clause in model.cnf:  # AC es conjunto de conjuntos
            g.add_clause(clause)  # añadimos la constraint
        self.res = g.solve()

    def isValid(self):
        return self.res
