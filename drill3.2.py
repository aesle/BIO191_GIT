rows = 3
columns = 5

for i in range(rows):
    for j in range(columns):
        if j % 2 == 0:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()  
