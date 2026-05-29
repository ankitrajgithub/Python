# Match-case statement (switch) = An alternative of using many "elif" statements.
#                                 Executes some code if a value matches a 'case'.
#                                 Benefits : Cleaner and syntax is more readable.
from unittest import case


def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"

week_day=day_of_week(1)
print(week_day)

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday"| "Thursday"| "Friday":
            return False
        case _:
            return False

print(is_weekend("Sunday"))