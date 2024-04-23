largest_odd = None
found_odd = False

for i in range(3):
    num = int(input(f"Please enter integer {i+1}: "))
    if num % 2 != 0:  # Check if the number is odd
        if largest_odd is None or num > largest_odd:
            largest_odd = num
        found_odd = True

if found_odd:
    print(f"{largest_odd} is the greatest odd integer.")
else:
    print("None of the given integers are odd.")
