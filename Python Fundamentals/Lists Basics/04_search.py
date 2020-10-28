n = int(input())
search_word = input()
strings = []

for _ in range(n):
    string = input()
    strings.append(string)

filtered_strings = []
for string in strings:
    if search_word in string:
        filtered_strings.append(string)

print(strings)
print(filtered_strings)
