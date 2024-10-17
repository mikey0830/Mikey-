def grade_converter():
    try:
        grade = float(input("Please enter a numerical grade between 0 and 100: ").strip())

        if 80 <= grade <= 100:
            letter_grade = 'A'
        elif 60 <= grade < 80:
            letter_grade = 'B'
        elif 50 <= grade < 60:
            letter_grade = 'C'
        elif 40 <= grade < 50:
            letter_grade = 'D'
        elif 0 <= grade < 40:
            letter_grade = 'F'
        else:
            print("Please enter a grade between 0 and 100.")
            return

        print(f"Your grade is: {letter_grade}")

    except ValueError:
        print("Please enter a valid numerical grade.")

grade_converter()

