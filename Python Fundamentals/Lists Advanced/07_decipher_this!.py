def parse_to_char(word):
    temp = ""

    for ch in word:
        if not str(ch).isdigit():
            break
        temp += ch
    ascii_value = int(temp)
    char_value = chr(ascii_value)
    new_word = word.replace(temp, char_value)
    return new_word


def replace_word(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return "".join(temp)


def decrypt(word):
    res = parse_to_char(word)
    res = replace_word(res)
    return res


words = input().split()
new_word = [decrypt(word) for word in words]
print(" ".join(new_word))
