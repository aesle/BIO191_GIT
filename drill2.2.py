age = int(input("Please enter your age: "))
is_natural_born_citizen = input("Are you a natural born citizen of the U.S. (yes/no)? ").lower() == "yes"
years_resided = int(input("How many years have you resided in the U.S.? "))

eligible_to_run = True

if not is_natural_born_citizen:
    eligible_to_run = False

if age < 35:
    eligible_to_run = False

if years_resided < 14:
    eligible_to_run = False

if eligible_to_run:
    print("You can run for president of USA")
else:
    print("You are not eligible to run for president of USA")
