email = input()

command_list = input()

while command_list != "Complete":
    args = command_list.split()
    command = args[0]

    if command == "Make":
        if "Upper" in args:
            email = email.upper()
            print(email)
        elif "Lower" in args:
            email = email.lower()
            print(email)
    elif command == "GetDomain":
        count = int(args[1])
        domain = email[-count:]
        print(domain)
    elif command == "GetUsername":
        if "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
            command_list = input()
            continue
        username, other_part = email.split("@")
        print(username)

    elif command == "Replace":
        char = args[1]
        email = email.replace(char, "-")
        print(email)
    elif command == "Encrypt":
        ascii_val = []
        for i in email:
            i = str(ord(i))
            ascii_val.append(i)
        print(" ".join(ascii_val))

    command_list = input()
