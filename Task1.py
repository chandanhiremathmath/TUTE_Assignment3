n = int(input("Enter the number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    def factorial(n):
        if n < 2:
            return 1
        else:
            return n * factorial(n - 1)

    result = factorial(n)
    print("The factorial is:", result)
