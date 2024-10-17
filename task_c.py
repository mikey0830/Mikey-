def password_validator():
    password = input("Please enter a password: ").strip()

    if len(password) < 8:
        print("Your password must contain at least 8 characters, and a mix of letters and numbers")
        return

    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)

    if has_letter and has_number:
        print("Your password is valid")
    else:
        print("Your password must contain at least 8 characters, and a mix of letters and numbers")

password_validator()