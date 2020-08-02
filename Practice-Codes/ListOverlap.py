a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
overlap = []

#For loop for variable a
for a_item in a:
    #For loop for variable b
    for b_item in b:
        if a_item == b_item:
            #Adding common number to the list
            overlap.append(a_item)
unique_overlap = set(overlap)
print(unique_overlap)
