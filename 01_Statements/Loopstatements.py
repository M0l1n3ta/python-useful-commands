#For loop in one line
mylist = [200, 300, 400, 500]
#Single line For loop
result = [] 
for x in mylist: 
    if x > 250: 
        result.append(x) 
print(result) # [300, 400, 500]
#One-line code way
result = [x for x in mylist if x > 250] 
print(result) # [300, 400, 500]



#Method 1 Single Statement   

x = 0   
while x < 5: print(x); x= x + 1 # 0 1 2 3 4 5