from appJar import gui
from player import player
from event_handler import event

class myapp:
    def __init__(self):
        self.app = gui()
        self.p = player()

        self.app.size  = (600, 300)
        self.app.resizable = False

        self.app.addListBox("event-log")
        self.app.addButton("age", self.age)
        self.app.addButton("new life", self.newlife)
        self.app.addButton("ram usage", self.printramstuff)
        self.app.addButton("stats", self.showstats)

        self.add_unshown_events()
    def showstats(self):
        self.app.addListItem("event-log", str(vars(self.p)))


    def check_option_input(self, event):
        answer = self.app.stringBox(event.event.name, event.event.prompt + " " + str(event.event.options) + "?")
        print(answer)
        while(answer not in event.event.options):
            answer = event.event.do(self.app.stringBox(event.event.name, event.event.prompt + " " + str(event.event.options) + "?"), self.p)
        
        return answer
                
   
    def add_unshown_events(self):
        newmessage = False
        
        for event in self.p.eventhandler.get_unshown():
            self.app.addListItem("event-log", event.message)
            if(event.interact):
                answer = self.check_option_input(event)
                event.event.do(answer, self.p)
                self.p.eventhandler.new_event_log(event.get_option_prompt(answer))
                newmessage = True

        if(newmessage): self.add_unshown_events()
                
        

    def age(self):
        self.p.ageforward()

        self.add_unshown_events()

    def newlife(self):
        self.p = player()

        self.app.clearListBox("event-log")

        self.add_unshown_events()

    def printramstuff(self):
        for obj in globals():
            print(str(obj) + "  " + str(obj.__sizeof__()))

a = myapp()
a.app.go()