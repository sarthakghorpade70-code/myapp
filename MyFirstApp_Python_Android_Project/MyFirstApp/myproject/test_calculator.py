from main import safe_calculate

cases = {
    "2+3*4": 14,
    "(10-2)/4": 2,
    "50%": 0.5,
    "200*10%": 20,
    "-5+8": 3,
    "2**3": 8,
}
for expression, expected in cases.items():
    actual = safe_calculate(expression)
    assert abs(actual - expected) < 1e-9, (expression, actual, expected)
print(f"Passed {len(cases)} calculator tests.")
