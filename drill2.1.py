age = int(input("What is your age? "))
has_license = input("Do you have a fishing license in MN (yes/no)? ").lower() == "yes"

parent_has_license = input("Does your parent have a fishing license (yes/no)? ").lower() == "yes"

legal_to_fish = (age <= 15 and parent_has_license) or (age >= 16 and has_license)

if legal_to_fish:
    print("You are legal to fish in MN.")
else:
    print("You are not legal to fish in MN.")
