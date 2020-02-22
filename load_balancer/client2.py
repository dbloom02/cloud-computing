import Pyro4 

alist,key = [1,3,3,4,3,5,7,7,7,7,7,7,9],7 # Example list and key 

'''res = Pyro4.Proxy("PYRONAME:Server2")
res = res.myCount(alist,key) 
print(f'{key} present {res[0]} times')'''

res = Pyro4.Proxy("PYRONAME:LoadBalancer")  
res = res.roundRobin(alist,key)
print(f'{key} present {res[0]} times (server: {res[1]})')