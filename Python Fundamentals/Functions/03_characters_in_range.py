def num_characters_range(a, b):
    for character in range(a + 1, b):
        print(chr(character), end=" ")


first_character = ord(input())
second_character = ord(input())

num_characters_range(first_character, second_character)
