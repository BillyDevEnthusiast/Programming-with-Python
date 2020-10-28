def smallest_number(a, b, c):
    smallest = c
    if a < b and a < c:
        smallest = a
    elif b < a and b < c:
        smallest = b
    return smallest


a = int(input())
b = int(input())
c = int(input())

res = smallest_number(a, b, c)
print(res)
