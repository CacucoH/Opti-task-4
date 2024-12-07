import math

# Given function
def f(x):
    return (x - 2)**2 + 3

def golden_section(a, b, e):
    # Golden Ration constant
    golden_ratio = (math.sqrt(5) - 1) / 2

    c = b - golden_ratio * (b - a)
    d = a + golden_ratio * (b - a)

    iteration = 0
    # Iterate until interval is less than tolerance
    while (b - a) > e:
        iteration += 1
        if f(c) < f(d):
            b = d
            d = c
            c = b - golden_ratio * (b - a)
        else:
            a = c
            c = d
            d = a + golden_ratio * (b - a)

    xmin = (a + b) / 2
    return xmin, f(xmin), iteration

# Input
a = float(input("Starting point of the interval (a): "))
b = float(input("End point of the interval (b): "))
e = float(input("Tolerance (e): "))

# Run Golden Section method
xmin, f_min, iterations = golden_section(a, b, e)

# Output
print(f"Approximate minimum point xmin ~ {xmin}")
print(f"Value of f(xmin) = {f_min}")
