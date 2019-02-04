import random_generators as rg
class smoke_joint:
    def __init__(self):
        self.name = "Smoke a joint"
        self.prompt = "You have been offered a joint from your %s"%(rg.acquaintance_name())
        self.options = ["smoke", "leave"]
        self.option_prompts = ["You smoked the joint", "You said no to drugs :("]

     
    def do(self, option, player):
        if(option == "smoke"):
            player.death_possibilities[1]["chance"] += 20

        return option

class beer_can():
    def __init__(self):
        self.name = "Drink a beer"
        self.prompt = "You have been offered a can of beer from your %s"%(rg.acquaintance_name())
        self.options = ["drink", "leave"]
        self.option_prompts = ["You drank the beer", "U didnt drink the beer"]

    def do(self, option, player):
        if(option == "drink"):
            player.ptrait["happiness"] += 10

        return option