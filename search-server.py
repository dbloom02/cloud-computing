import Pyro4

@Pyro4.expose

class Search(object): 
    def LinearSearch(self, alist, key): 
        for i in alist: 
            if i == key: 
               return True 
        return False
    def BinarySearch(self, alist, key):
        # assume list is already sorted
        l, r = 0, len(alist)
        while l <= r:
            mid = l + ((r - l) // 2)
            if alist[mid] == key and alist[mid-1] != key:
                return True
            elif alist[mid] < key: 
                l = mid + 1
            else: 
                r = mid - 1
        return False

daemon = Pyro4.Daemon()
    
# find the name server
            
ns = Pyro4.locateNS()
                  
uri = daemon.register(Search)

# register the object in the name server as search

ns.register("search", uri)
# print("Ready. Object uri =", uri)

print("Ready.")

daemon.requestLoop()