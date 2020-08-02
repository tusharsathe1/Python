#Ask user to input a number
number = input("Enter an integer: ")

#Calculate the remainder
remainder = int(number) % 2

#Print the result
if remainder == 0:
    print(number + " is an even number")
else:
    print(number + " is an odd number")
