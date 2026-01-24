"""
Evaluator for JNN
"""

from functools import reduce as _reduce
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
        case "const":
            return evaluate(jnn["val"],vars)
        case "sum":
            return sum([evaluate(o,vars) for o in jnn["val"]])
        case "product":
            return _reduce(_mul, [evaluate(o,vars) for o in jnn["val"]], 1)
        case "reciprocal":
            return 1/evaluate(jnn["val"],vars)
        case "variable":
            return vars[jnn["val"]] # no need to evaluate because nothing returns str
        case e:
            raise ValueError(f"Invalid type {repr(e)}")