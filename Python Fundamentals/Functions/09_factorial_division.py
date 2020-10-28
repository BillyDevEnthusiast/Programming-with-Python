def calc_factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    return fact


def calc_factorial_both(a,b):
    res1 = calc_factorial(a)
    res2 = calc_factorial(b)
    res3 = res1 / res2
    return f"{res3:.2f}"


num1 = int(input())
num2 = int(input())
result = calc_factorial_both(num1, num2)
print(result)
