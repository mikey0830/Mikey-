def password_check():
    password = input("Please enter a password: ").strip()
    if len(password) < 8:
        print("Your password must contain at least 8 characters")
    elif password.isalpha() or password.isdigit():
        print("Your password must contain a mix of letters and numbers")
    else:
        print("Your password is valid")
