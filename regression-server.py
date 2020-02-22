import Pyro4 

import numpy as np 

@Pyro4.expose 

class Models(object):
    def estimate_coef(self, x, y):  
        x,y,n = np.array(x), np.array(y),np.size(x) 
        m_x, m_y = np.mean(x), np.mean(y)  
        SS_xy = np.sum(y*x) - n*m_y*m_x  
        SS_xx = np.sum(x*x) - n*m_x*m_x  
        b_1 = SS_xy / SS_xx  
        b_0 = m_y - b_1*m_x  
        return(b_0, b_1)

daemon = Pyro4.Daemon()  
               
ns = Pyro4.locateNS()  
                
uri = daemon.register(Models)    

ns.register("models", uri)   

print("Ready.") 

daemon.requestLoop()