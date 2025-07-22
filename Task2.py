import math
num = float(input("Enter a number: "))
if num <= 0:
    print("Logarithm and square root are only defined for positive numbers.")
else:
    sqrt_val = math.sqrt(num)
    log_val = math.log(num)
    sin_val = math.sin(num)
    print(f"Square root of {num} is: {sqrt_val}")
    print(f"Natural logarithm (ln) of {num} is: {log_val}")
    print(f"Sine of {num} radians is: {sin_val}")
