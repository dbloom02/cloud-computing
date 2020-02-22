import Pyro4 

#x, y = [1,2,3], [3,5,7]
x, y = [1,2,3,4,5], [5,7,9,11,13] 

res = Pyro4.Proxy("PYRONAME:models")    
 
print(res.estimate_coef(x,y))