data = input().split()

args1 = data[0]
args2 = data[1]

total_value = 0

args1_ord = [ord(num) for num in args1]
args2_ord = [ord(num) for num in args2]

min_value = min(len(args1), len(args2))

for i in range(min_value):
    value = args1_ord[i] * args2_ord[i]
    total_value += value

if len(args1_ord) > len(args2_ord):
    sliced_value = args1_ord[len(args2_ord):]
else:
    sliced_value = args2_ord[len(args1_ord):]

total_value += sum(sliced_value)


print(total_value)
