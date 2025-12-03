def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

# Sample call
number = 5
result = factorial(number)

print("Factorial of", number, "is:", result)
