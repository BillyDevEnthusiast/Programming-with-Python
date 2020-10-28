current_version = input().split(".")
res = "".join(current_version)
number = (int(res) + 1)
res = list(map(int, str(number)))
res_str = ".".join(map(str, res))

print(res_str)
