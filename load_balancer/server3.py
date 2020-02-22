import Pyro4 

@Pyro4.expose 

class Server3(object): 
    def myCount(self, alist, key):
        print("Someone accessed Server3.count")
        count = 0
        for i in alist: 
         if i == key:count+=1 
        return(count,"3")   #3 for load balancer 3 

daemon = Pyro4.Daemon()
   
ns = Pyro4.locateNS()
    
uri = daemon.register(Server3)
             
ns.register("Server3", uri)   # Register as Server3

print("Server3 is live!")

daemon.requestLoop()