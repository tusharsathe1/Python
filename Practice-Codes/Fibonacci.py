#Ask user for the number
n = range((int(input("Enter the count of Fibonacci numbers to generate: ")) - 1))

#Define an empty list for the sequence
sequence = [0, 1]

#Generate the sequence
for i in n:
    next = sequence[i] + sequence[i+1]
    sequence.append(next)

#Print the result
print(sequence[1::])
