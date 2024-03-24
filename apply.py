from sympy import symbols, log, sin, limit, oo
x, y = symbols('x y')
equation = log(sin(x) * sin(y))
result = limit(equation, x, oo)
print("Limit as x approaches infinity:", result)

