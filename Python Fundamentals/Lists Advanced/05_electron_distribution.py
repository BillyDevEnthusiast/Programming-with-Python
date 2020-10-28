electrons = int(input())
electrons_list = []
electron = 0
n = 1

while electrons > 0:
    shell_capacity = 2 * n ** 2
    if shell_capacity <= electrons:
        electron = shell_capacity
        electrons -= electron
        electrons_list.append(electron)
    else:
        electrons_list.append(electrons)
        break
    n += 1

print(electrons_list)
