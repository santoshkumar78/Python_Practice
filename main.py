calculation_to_units = 24
name_of_units = "Hours"


def days_to_hours(number_of_days):
    convert_to_hours = calculation_to_units * number_of_days
    return f"There are {convert_to_hours} {name_of_units} in {number_of_days} days"


def validate_and_execute():
    try:

        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculate_value = days_to_hours(user_input_number)
            print(calculate_value)
        elif user_input_number == 0:
            print("You have entered zero day, please enter positive number")
        else:
            print("You have  entered negative number, please enter only positive number")

    except ValueError:
        print("Your input is not a valid value, don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey, user, enter number of days in comma seperated and I will convent into Hours\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(type(list_of_days))
    print(set(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):
        validate_and_execute()
