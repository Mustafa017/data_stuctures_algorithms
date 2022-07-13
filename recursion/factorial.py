def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n - 1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value


factorial(4)
