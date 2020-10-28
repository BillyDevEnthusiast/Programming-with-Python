import sys
divisor = int(input())
bound = int(input())
n = -sys.maxsize
new_num = 0

for num in range(0, bound + 1):
    if bound >= num > 0 and num % divisor == 0:
        number = num
        if number > n:
            largest_num = number
            new_num = largest_num
print(new_num)
