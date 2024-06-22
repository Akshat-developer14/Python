def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


factorial_input = int(input("Enter any positive integer to factorial : "))
print(factorial(factorial_input))


# Sum using recursion
def sumOfN(n):
    if n == 1:
        return 1
    else:
        return n + sumOfN(n - 1)


Sum = int(input("Enter a number: "))
print(sumOfN(Sum))
# 1+2+3+4+5
