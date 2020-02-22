import Pyro4

@Pyro4.expose

class HelloWorldMaker(object):

    def get_message(self, name):
    
        print("Someone just used the get_message method") 
        
        return "Hello world {0}\n" \
               "This message is coming from the server".format(name)

    def sum_of_2(self, a,b): 

        print("CALL: sum_of_2 method")
        
        return int(a)+int(b)

# make a Pyro daemon to start the server 
daemon = Pyro4.Daemon()

# register the hello world maker class as a Pyro object
uri = daemon.register(HelloWorldMaker)

# print the uri (URL) so we can use it in the client later
print("Ready. Object uri =", uri)
 
# start the event loop of the server to wait for calls
daemon.requestLoop()