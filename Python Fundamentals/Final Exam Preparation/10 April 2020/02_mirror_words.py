import re

pattern = r"#[a-zA-Z]{3,}##[a-zA-Z]{3,}#|@[a-zA-Z]{3,}@@[a-zA-Z]{3,}@"

text = input()

matches = re.findall(pattern, text)
matches_length = len(matches)

mirror_words = []

if matches_length > 0:
    print(f"{matches_length} word pairs found!")
else:
    print("No word pairs found!")

for match in matches:
    if match[0] == "#":
        match_new = match.replace("#", "")
    else:
        match_new = match.replace("@", "")

    middle = int(len(match_new) / 2)
    first_word = match_new[:middle]
    second_word = match_new[middle:]

    if first_word[::-1] == second_word:
        mirror_words.append(f"{first_word} <=> {second_word}")
if len(mirror_words) > 0:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")
