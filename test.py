"""
Tester
"""

from evaluator import evaluate as _evj
from json import load

with open("tests.json", "r") as f:
    tests = load(f)

for test in tests:
    res = _evj(test[0],test[2])
    assert res == test[1] and isinstance(res, type(test[1])), test