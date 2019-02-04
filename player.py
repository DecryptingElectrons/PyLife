import random_generators as rg
from event_handler import event_handler
class player:
    def __init__(self):
        #gender assigned from generator
        self.gender = rg.gender()
        #name assigned from generator with respect to gender
        self.name = rg.name(self.gender)

        #placeholders for later in life
        self.job = None
        self.qualifications = [None]
        self.finance = {
            "income":None,
            "bank_balance":None
        }
        self.ptraits = {
            "happiness":100,
            "intelligence":rg.randint(0, 30)
        }
        self.death_possibilities = [
            {"name":"heart attack", "chance":0},
            {"name":"lung disease", "chance":0}
        ]
        self.sexuality = None
        self.alive = True
        self.education = None
        self.age = 0

        #create and add to the events the user sees
        self.eventhandler = event_handler()
        self.eventhandler.new_event_log("Age: 0")
        self.eventhandler.new_event_log("You are %s and your name is %s"%(self.gender, self.name))
    
    def ageforward(self):
        if(not self.alive):
            self.eventhandler.new_event_log("dead")
            return None
        #really technically the -main- code
        self.age += 1
        self.eventhandler.new_event_log("Age: %i"%(self.age))

        #try to kill the player by thier own actions
        for dp in self.death_possibilities:
            #chance of death is randomized for thousandths
            deathchance = rg.rand(0, 1000)

            #higher the number(per death possibility), greater the chance of death
            if(deathchance < dp["chance"]):
                self.alive = False
                self.eventhandler.new_event_log("dead - %s"%(dp["name"]))
        
        eventchance = rg.rand(0, 18)

        if(eventchance == 4):
            event = self.eventhandler.randevent()
            self.eventhandler.new_event_log(event.prompt, requiresinteract=True, eventin=event)