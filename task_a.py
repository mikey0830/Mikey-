day = input("Please enter a day of week: ").strip().capitalize()
days = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
if days in days:
    print(f"{day} is day {days[day]}")
else:
    print("Please enter a valid day")