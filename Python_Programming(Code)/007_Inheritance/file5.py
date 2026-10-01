class Player:
    def play(self):
        print("Player")
class CricketPlayer(Player):
    def bat(self):
        print("CricketPlayer")
class FootballPlayer(Player):
    def goal_keeping(self):
        print("Footbal player")
class KabadiPlayer(Player):
    def raid(self):
        print("KabadiPlayer")


pl1=FootballPlayer()
pl2=CricketPlayer()
pl3=KabadiPlayer()
pl1.goal_keeping()
pl2.play()
pl2.bat()
pl3.raid()
print(KabadiPlayer.__mro__)