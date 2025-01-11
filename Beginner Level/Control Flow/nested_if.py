#Example: Checking if a number is positive and even
number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive and even number")
    else:
        print("Positive but odd number")
elif number < 0:
    print("Negative number")