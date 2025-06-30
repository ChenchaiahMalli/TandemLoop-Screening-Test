a = int(input("Enter value: "))

current_number = 1
count = 0
while count < a:
    print(current_number, end="")
    current_number += 2
    count += 1
    if count < a:
        print(", ", end="")