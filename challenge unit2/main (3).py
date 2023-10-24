#define  the base cass player
class player:
    def play(self):
        print("the player is playing cricket.")
#Define the derived class batsman
class batsman (player):
  def play(self):
      print("the batsman is batting.")
#Define the derived class bowler
class bowler(player):
  def play(self):
      print("the bowler is bowling.")
#create object of batsman and bowler
batsman = batsman()
bowler = bowler()
#call the play()method for each object
batsman.play()
bowler.play()