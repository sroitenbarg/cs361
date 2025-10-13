def tailFib(n, a, b):
    while n != 0:
        n -= 1
        a, b = b, a + b
    return a

def fib(n):
    return tailFib(n, 0, 1)