def patternReverse(n):
    if n == 0:
        return
    print("*" * n)
    patternReverse(n - 1)


patternInReverse = int(input("Enter a number you want to print * in reverse order : "))
patternReverse(patternInReverse)
