password = input()

cypher = ""

for sign in str(password):
    cypher += chr(ord(sign) + 3)

    if sign == "":
        cypher += "#"

print(cypher)
