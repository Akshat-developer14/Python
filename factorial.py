def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


factorial_input = int(input("Enter any positive integer to factorial : "))
print(factorial(factorial_input))
