from openvisualizer.eventBus import eventBusClient

class Ga(eventBusClient.eventBusClient):
   
    def __init__(self):
                # initialize parent class
        eventBusClient.eventBusClient.__init__(
            self,
            name                  = 'Ga',
            registrations         =  [
               {
                    'sender'      : self.WILDCARD,
                    'signal'      : ((187, 187, 0, 0, 0, 0, 0, 0, 20, 21, 146, 204, 0, 0, 0, 1), 'udp', 15001),
                    'callback'    : self._ga_notif,
                },
            ]
        )
        print 'ABCDEFG'
    
    #======================== public ==========================================
    #Triggered by parser data as a hack 
    def _ga_notif(self,sender,signal,data):
        print "In GA!!",data
