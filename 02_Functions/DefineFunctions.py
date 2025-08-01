#Function in one line  
#Method1
def fun(x): return True if x % 2 == 0 else False   
print(fun(2)) # False  
#Method2
fun = lambda x : x % 2 == 0   
print(fun(2)) # True   
print(fun(3)) # False


# Filtering arrays in a single line  
mylist = [2, 3, 5, 8, 9, 12, 13, 15]  

# One-line method  
result = [x for x in mylist if x % 2 == 0]   
print(result) # [2, 8, 12]