def get_day_number():
    days = {"monday": 1,"tuesday": 2,"wednesday": 3,"thursday": 4,"friday": 5,"saturday": 6,"sunday": 7}

    day_input = input("Please enter a day of the week: ").strip().lower()

    if day_input in days:
        day_number = days[day_input]
        formatted_day = day_input.capitalize()
        print(f"{formatted_day} is day {day_number}")
    else:
        print("Please enter a valid day of the week.")

get_day_number()