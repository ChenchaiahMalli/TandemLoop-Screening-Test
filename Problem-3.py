a = int(input("Enter value: "))

terms = a if a % 2 == 1 else a - 1

current_num = 1
count = 0

while count < terms:
    print(current_num, end="")
    current_num += 2
    count += 1
    if count < terms:
        print(", ", end="")