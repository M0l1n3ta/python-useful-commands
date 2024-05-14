#One line map function 
elements = [5, 6, 7, 8, 9, 10]
print("add 2 to all elements:",list(map(lambda a: a + 2, elements)))  
# print
# [7, 8, 9, 10, 11, 12]


print("even elements:",list(map(lambda a: a % 2 == 0,elements)))


print("even elements:",list(filter(lambda a: a % 2 == 0,elements)))