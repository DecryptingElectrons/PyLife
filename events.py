class smoke_rollup:
    def __init__(self):
        self.name = "Smoke a rollup"
        self.prompt = "You have been offered a rollup from your mate"
        self.options = ["smoke", "leave"]
     
    def do(self, option, player):
        if(option == "smoke"):
            player.death_possibilities[1]["chance"] += 300