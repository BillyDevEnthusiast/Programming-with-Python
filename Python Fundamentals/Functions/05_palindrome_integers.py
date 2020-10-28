def check_palindrome_integers(a: str):
    list_numbers = a.split(", ")
    list_palindromes = []
    for number in list_numbers:
        res = number == number[::-1]
        list_palindromes.append(str(res))
    return print(*list_palindromes,sep='\n')


numbers = input()
res = check_palindrome_integers(numbers)
