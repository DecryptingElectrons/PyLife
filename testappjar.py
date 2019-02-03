from appJar import gui
from player import player

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
    def add_unshown_events(self):
        for event in self.p.eventhandler.get_unshown():
            self.app.addListItem("event-log", event["message"])
        
        if(event["interact"]):
            event["event"].do(self.app.stringBox(event["event"].name, event["event"].prompt + " " + str(event["event"].options) + "?"), self.p)

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