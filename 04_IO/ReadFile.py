import os
from pathlib import Path

print(os.getcwd())
p = Path(__file__).with_name('test.md')
#Reading a file in one line  
#Single-line method 
with open(p, "r",encoding='utf-8', errors='ignore') as file:   
    data = file.readline()   
    print(data) # Hello world  
#Single line way  
data = [line.strip() for line in open(p,"r",encoding='utf-8', errors='ignore')]   
print(data) # ['hello world', 'Hello Python']