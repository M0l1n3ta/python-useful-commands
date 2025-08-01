d1 = { 'A': 1, 'B': 2 }   
d2 = { 'C': 3, 'D': 4 }  
#Method1   
d1.update(d2)   
print(d1) # {'A': 1, 'B': 2, 'C': 3, 'D': 4}  
#Method2   
d3 = {**d1, **d2}   
print(d3) # {'A': 1, 'B': 2, 'C': 3, 'D': 4}