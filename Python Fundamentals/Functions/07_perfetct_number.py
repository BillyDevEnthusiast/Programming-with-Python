def find_perfect_num(number: int):
    res = []
    for i in range(1, number + 1):
        if number % i == 0 and i != number:
            res.append(i)
    if sum(res) == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(find_perfect_num(num))
