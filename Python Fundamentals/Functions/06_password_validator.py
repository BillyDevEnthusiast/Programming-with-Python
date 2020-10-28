def check_length(word: str):
    if 6 > len(word) or len(word) > 10:
        return "Password must be between 6 and 10 characters"
    else:
        return


def check_digit_letters(word):
    for sign in word:
        if not sign.isalpha() and not sign.isdigit():
            return "Password must consist only of letters and digits"


def check_2_digits(word):
    counter_digit = 0
    for digit in word:
        if digit.isdigit():
            counter_digit += 1
    if not counter_digit >= 2:
        return "Password must have at least 2 digits"


def password_validator(word):
    res = []
    validators = [check_length(word), check_digit_letters(word), check_2_digits(word)]
    for validator in validators:
        result = validator
        if result is not None:
            res.append(result)
    if len(res) == 0:
        return "Password is valid"
    else:
        return "\n".join(res)


password = input()

final_res = password_validator(password)
print(final_res)
