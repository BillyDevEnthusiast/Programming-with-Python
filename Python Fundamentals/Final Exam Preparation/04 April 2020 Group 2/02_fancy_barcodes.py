import re

pattern = r"@[#]+[A-Z][a-zA-Z0-9]{4,}[A-Z]@[#]+"
pattern_digit = r"[0-9]+"

n = int(input())

for i in range(n):
    barcode = input()

    valid_barcode = re.findall(pattern, barcode)

    if len(valid_barcode) == 0:
        print("Invalid barcode")
        continue

    for i in valid_barcode:
        valid_barcode_digits = "".join(re.findall(pattern_digit, i))

    if len(valid_barcode_digits) == 0:
        print("Product group: 00")
    else:
        print(f"Product group: {valid_barcode_digits}")
