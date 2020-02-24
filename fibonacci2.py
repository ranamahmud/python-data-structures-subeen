def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
def test_fibonacci():
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for n , f in enumerate(fib):
        assert fibonacci(n + 1) == f