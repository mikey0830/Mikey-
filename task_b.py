def grade_to_letter():
    try:
        grade = float(input("Please enter a numerical grade between 0–100: "))
        if grade < 0 or grade > 100:
            print("Error: Grades must be between 0 and 100")
            return
        if grade >= 80:
            print("Your grade is: A")
        elif grade >= 60:
            print("Your grade is: B")
        elif grade >= 50:
            print("Your grade is: C")
        elif grade >= 40:
            print("Your grade is: D")
        else:
            print("Your grade is: F")
    except ValueError:
        print("Error: Please enter a number")

