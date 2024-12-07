# Given function
def f(x):
    return -x**2 + 4*x + 1

# Derivative of given function
def f_prime(x):
    return -2*x + 4


def gradient_ascent(x0, rate, N):
    x = x0
    # Iterate N times
    for i in range(N):
        gradient = f_prime(x)
        x = x + rate * gradient
    return x, f(x)

# Input
x0 = float(input("Initial guess (x0): "))
rate = float(input("Learning rate (a): "))
N = int(input("Number of iterations (N): "))

# Find x_max and f_max with Gradient Ascent Method
x_max, f_max = gradient_ascent(x0, rate, N)

# Output
print(f"Approximate maximum point xmax = {x_max}")
print(f"Maximum value of f(x): f(xmax) = {f_max}")
