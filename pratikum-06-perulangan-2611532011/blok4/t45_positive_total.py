total = 0
number = 1

while number >= 0:
    number = int(input("Enter a number: "))

    if number < 0:
        break
    elif number == 0:
        continue
    else:
        print("Positive number:", number)
        total += number

print("Total:", total)