"""
Evaluator for JNN
"""

from functools import reduce as _reduce
from math import floor, ceil
_mul = lambda x, y: x*y

def evaluate(jnn: dict | int | float, vars: dict[str, int | float] = {}) -> int | float:
    """
    Evaluate a JNN object.
    May cause an IndexError if not formatted properly. This function does not catch exceptions.
    Documentation is in a seperate file.
    Raises ValueError upon invalid type.
    """
    if isinstance(jnn, (int, float)):
        return jnn
    match jnn["type"]:
        case "const" | "constant":
            return evaluate(jnn["val"],vars)
        case "sum":
            return sum([evaluate(o,vars) for o in jnn["val"]])
        case "prod" | "product":
            return _reduce(_mul, [evaluate(o,vars) for o in jnn["val"]], 1)
        case "recip" | "reciprocal":
            return 1/evaluate(jnn["val"],vars)
        case "floor":
            return floor(evaluate(jnn["val"],vars))
        case "ceil" | "ceiling":
            return ceil(evaluate(jnn["val"],vars))
        case "match" | "switch":
            val = evaluate(jnn["val"][0], vars)
            if val != int(val) or val >= len(jnn["val"]) - 1:
                return evaluate(jnn["val"][1], vars)
            return evaluate(jnn["val"][val+1], vars)
        case "comp" | "compare":
            val1 = evaluate(jnn["val"][0], vars)
            val2 = evaluate(jnn["val"][1], vars)
            if val1 < val2:
                return evaluate(jnn["val"][2], vars)
            if val1 > val2:
                return evaluate(jnn["val"][3], vars)
            return evaluate(jnn["val"][4], vars)
        case "var" | "variable":
            return vars[jnn["val"]] # no need to evaluate because nothing returns str
        case e:
            raise ValueError(f"Invalid type {repr(e)}")