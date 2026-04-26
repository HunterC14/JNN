"""
Evaluator for JNN
"""

from functools import reduce as _reduce
from math import floor, ceil
import random
_mul = lambda x, y: x*y
random.seed()

def evaluate(jnn: dict | int | float, vars: dict[str, int | float] = {}) -> int | float:
    """
    Evaluate a JNN object.
    May cause an IndexError if not formatted properly. This function does not catch exceptions.
    Documentation is in a separate file.
    Raises ValueError upon invalid type.
    """
    if isinstance(jnn, (int, float)):
        return jnn
    def ev():
        return evaluate(jnn["val"],vars)
    def ev2(n: int):
        return evaluate(jnn["val"][n],vars)
    match jnn["type"]:
        case "const" | "constant":
            return ev()
        case "sum":
            return sum([evaluate(o,vars) for o in jnn["val"]])
        case "prod" | "product":
            return _reduce(_mul, [evaluate(o,vars) for o in jnn["val"]], 1)
        case "recip" | "reciprocal" | "inv":
            return 1/ev()
        case "floor":
            return floor(ev())
        case "ceil" | "ceiling":
            return ceil(ev())
        case "match" | "switch":
            val = ev2(0)
            if val != int(val) or val >= len(jnn["val"]) - 1:
                return ev2(1)
            return ev2(int(val) + 1)
        case "comp" | "compare":
            val1 = ev2(0)
            val2 = ev2(1)
            if val1 > val2:
                return ev2(2)
            if val1 < val2:
                return ev2(3)
            return ev2(4)
        case "var" | "variable":
            return vars[jnn["val"]] # no need to evaluate because nothing returns str
        case "uniform" | "rng":
            return random.random()
        case "normal" | "gauss":
            return random.normalvariate(ev2(0), ev2(1))
        case e:
            raise ValueError(f"Invalid type {repr(e)}")