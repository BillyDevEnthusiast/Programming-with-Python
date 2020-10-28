def substract(a, b):
    res = a - b
    return res


def divide(a, b):
    res = a / b
    return res


def multiply(a, b):
    res = a * b
    return res

def add(a, b):
    res = a + b
    return res


action = input()
number1 = int(input())
number2 = int(input())

if action == "add":
    res = add(number1, number2)
elif action == "subtract":
    res = substract(number1, number2)
elif action == "multiply":
    res = multiply(number1, number2)
elif action == "divide":
    res = divide(number1, number2)

print(round(res))
