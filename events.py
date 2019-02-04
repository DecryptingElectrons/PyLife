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