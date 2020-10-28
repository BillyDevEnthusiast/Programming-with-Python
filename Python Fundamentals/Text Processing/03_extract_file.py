data = input().split("\\")

last_item = data[-1].split(".")
file_name = last_item[0]
extension = last_item[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")
