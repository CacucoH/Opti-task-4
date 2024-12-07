# Given function
def f(x):
    return x ** 3 - 6 * x ** 2 + 11 * x - 6

def bisection(a, b, e):
    # Bisection method require for signs of f(a) and f(b) to have different signs, exit if it's not true
    if f(a) * f(b) > 0:
        return None

    # Iterate until interval is less than tolerance
    iteration = 0
    while (b - a) / 2 > e:
        c = (a + b) / 2
        iteration += 1

        # If value of f(c) is less than tolerance (solution found) - exit w/o considering current interval length
        if abs(f(c)) < e:
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    c = (a + b) / 2
    return c

# Input
a = float(input("Starting point of the interval (a): "))
b = float(input("End point of the interval (b): "))
e = float(input("Tolerance (e): "))

# Find root using Bisection Method
root = bisection(a, b, e)

# Output
if root:
    #Answer found
    print(f"Approximate root of the function ~ {root}")
else:
    # Bisection method is not applicable for given interval
    print(f"f(a) and f(b) must have opposite signs. (For provided values: f(a) = {f(a)}, f(b) = {f(b)}")