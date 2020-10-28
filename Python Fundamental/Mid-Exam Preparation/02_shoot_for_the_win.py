number = list(map(int, input().split()))
numbers = number

command = input()
counter = 0
while command != "End":
    index = int(command)
    try:
        shot_num = numbers[index]
        numbers[index] = -1

        counter += 1

        for num in range(len(numbers)):
            if numbers[num] == -1:
                continue

            else:
                if shot_num >= numbers[num]:
                    numbers[num] += shot_num
                else:
                    numbers[num] -= shot_num
    except IndexError:
        pass
    command = input()

res = f"Shot targets: {counter} -> {' '.join(map(str, numbers))}"

print(res)
