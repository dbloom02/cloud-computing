import Pyro4 

import random 

alist = [] 

prev = 0 

# code to generate a list of random numbers in ascending order 
for i in range(100): 
    current = random.randint(1,10) + prev 
    alist.append(current) 
    prev = current 
print(alist)

key = int(input("Give a key to search: "))

# use the name server object to lookup uri shortcut called search 
res = Pyro4.Proxy("PYRONAME:search")

# call Search by passing the list and the key
method = input('Enter search method (linear, binary): ')
if method == 'linear':
    print(f'Is {key} within list using LinearSearch?')
    print(res.LinearSearch(alist,key))
else:
    print(f'Is {key} within list using BinarySearch?')
    print(res.BinarySearch(alist,key))