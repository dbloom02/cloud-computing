import Pyro4

@Pyro4.expose

class LoadBalancer(object):

    c = 0 # a counter is set to zero, counter will be 0 for LB1 and 1 for LB2

    def callServer(self,name,alist,key): # method to call servers 
        res = Pyro4.Proxy(name) # pass the name of the server 
        result = res.myCount(alist,key) # pass the list and the key 
        return result # return the results from server 

    def roundRobin(self,alist,key): # implement the round robin 
        if LoadBalancer.c == 0:
            result = LoadBalancer.callServer(self,"PYRONAME:Server1",alist,key) 
            LoadBalancer.c = 1 
            return result 
        elif LoadBalancer.c == 1:
            result = LoadBalancer.callServer(self,"PYRONAME:Server2",alist,key)  
            LoadBalancer.c = 2
            return result
        else: 
            result = LoadBalancer.callServer(self,"PYRONAME:Server3",alist,key)  
            LoadBalancer.c = 0
            return result
        print("Load balancer used: ", LoadBalancer.c)

daemon = Pyro4.Daemon()     

ns = Pyro4.locateNS()                   

uri = daemon.register(LoadBalancer)    

ns.register("LoadBalancer", uri)   

print("Load balancer is live!") 

daemon.requestLoop() 