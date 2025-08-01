from collections import *

a = {'one':1, 'two2':2}
print(a, type(a))

a.update({'three':3})
print(a)

a['two'] = 2.1
print(a)


#from collections import defaultdict

b = defaultdict(int)
print(b['one'])

b['one'] +=1
print(b['one'])


#from collections import OrderedDict

c = OrderedDict({'two':2,'one':1})
print(c)
c['tree']= 3
print(c)

#from collections import OrderedDict
d = OrderedDict({'one':1,'two':2,'three':3,'four':4})
print(d)
d.move_to_end('one', last= True)
print(d)


#from collections import ChainMap

a = {'one':1, 'two':2}
b = {'three':3, 'four':4}
c = {'five':5, 'seix':6, 'three':3.1}

merged = ChainMap(a,b,c)
print(merged)

print(merged['three'])
## Returns only the first ocurrence of the key


#from collections import Counter

sentence = "we can't control our thoughts, but we can control our words"
s = Counter(sentence.split(' '))
print(s)


#from collections import UserDict

class Mydict(UserDict):
    def __setitem__(self, key, value):
        return super().__setitem__(key, value * 5)
    
d = Mydict({'one':1,'two':2})
print(d)