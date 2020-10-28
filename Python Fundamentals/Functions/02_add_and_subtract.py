def sum_numbers(a, b):
    sum_num = a + b
    return sum_num


def substract_numbers(a, b):
    return a - b


a = int(input())
b = int(input())
c = int(input())

sum = sum_numbers(a, b)
final = substract_numbers(sum, c)

print(final)
