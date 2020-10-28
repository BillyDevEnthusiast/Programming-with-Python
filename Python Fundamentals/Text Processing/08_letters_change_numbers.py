def letter_position(letter:str):
    letter_pos = ord(letter) - 64

    if letter.islower():
        letter_pos = ord(letter) - 96

    return letter_pos


data = input(). split()

total_value = 0

for item in data:
    number = int(item[1:-1])
    first_letter = item[0]
    last_letter = item[-1]
    first_letter_position = letter_position(first_letter)
    last_letter_position = letter_position(last_letter)

    if first_letter.isupper():
        total_value += number / first_letter_position
    else:
        total_value += number * first_letter_position

    if last_letter.isupper():
        total_value -= last_letter_position
    else:
        total_value += last_letter_position
total_value = round(total_value, 2)
print(f"{total_value:.2f}")
