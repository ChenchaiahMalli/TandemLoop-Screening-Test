chenchu = input("Enter numbers separated by commas: ")
numbers = [int(num.strip()) for num in chenchu.split(',')]

multiples_count = {i: 0 for i in range(1, 10)}

for num in numbers:
    for divisor in multiples_count:
        if num % divisor == 0:
            multiples_count[divisor] += 1

print(multiples_count)