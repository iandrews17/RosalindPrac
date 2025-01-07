
def rabbit_fib(n, k):
    if n <= 0:
        return 0
    if n == 2:
        return 1 + k
    if n == 1:
        return 1
    return (rabbit_fib(n - 1, k) + rabbit_fib(n - 2, k)) * k


def fib(n):
    old = 1
    new = 1
    for i in range(n - 1):
        tempVal = new
        new = old
        old = old + tempVal
    return new

def fib_py(months, offspring):
    parent, child = 1, 1
    for i in range(months - 1):
        child, parent = parent, parent + (child*offspring)
    return child

print(fib_py(33, 5))