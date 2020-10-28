def even_odd_sum(a):
    even_sum = 0
    odd_sum = 0
    a = str(a)
    for i in a:
        i = int(i)
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input())
print(even_odd_sum(number))
