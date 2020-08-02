#Ask user to enter a string
input_string = input("Enter a word: ")

#Define an empty list
string_char = []

#Split every character of the string into an element of the list
for i in input_string:
    string_char.append(i)

#Reverse the list
reverse_string = string_char[::-1]

#Print the result
if string_char == reverse_string:
    print(input_string + " is a Palindrome word")
else:
    print(input_string + " is not a Palindrome word")
