import Pyro4 

@Pyro4.expose 

class Server1(object): 
    def myCount(self, alist, key):
        print("Someone accessed Server1.count")
        count = 0
        for i in alist: 
         if i == key:count+=1 
        return(count,"1")   #1 for load balancer 1 

daemon = Pyro4.Daemon()
   
ns = Pyro4.locateNS()
    
uri = daemon.register(Server1)
             
ns.register("Server1", uri)   # Register as Server1

print("Server1 is live!")

daemon.requestLoop()