import re

pattern = r"[U][\$]([A-Z][a-z]{2,})[U][\$][P][@][\$]([a-zA-Z]{5,}[0-9]+)[P][@][\$]"
n = int(input())
successfulRegistrationsCount = 0
for match in range(n):
    data = input()
    valid_registration = re.findall(pattern, data)
    if len(valid_registration) == 0:
        print("Invalid username or password")
        continue
    print("Registration was successful")
    for i in valid_registration:
        username = i[0]
        password = i[1]
        print(f"Username: {username}, Password: {password}")
        successfulRegistrationsCount += 1

print(f"Successful registrations: {successfulRegistrationsCount}")
