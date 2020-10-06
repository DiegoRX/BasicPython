def factorial(n):
    """Calculates the factorial of n

    n int > 0
    returns n!
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input('Type an Int: '))
print(factorial(n))

help(factorial)