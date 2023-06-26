from gamestate import GameState
from strategy import Strategy
from player import Player
from game_output import game_output
import random     


class Game:
      def __init__(self, players, start_money, max_rounds):
          self.players = players
          self.start_money = start_money
          self.max_rounds = max_rounds
          self.num_players = len(players)
          
          self.state = GameState.startState(self)
          self.board = self.state.board
          for i in range(len(players)):
              players[i].game = self
              players[i].index = i
              players[i].opponents = players[i+1:].copy() + players[:i].copy()

          game_output("** ==== Leodopoly: the Leeds landlords game ==== **")

      def play(self, display="verbose"):
          self.state.display_state()
          
          while self.max_rounds == 0 or self.state.round <= self.max_rounds:
                result = self.state.progress(display)
                if self.state.phase == "bankrupcy":
                    if result.gender == "male":
                        pronoun = "his"
                    else:
                        pronoun = "her"
                    game_output( result, "has lost all", pronoun, "money and is declared BANKRUPT!" )
                    break
                
          game_output("\nThe final state of play:")      
          self.state.display_state()
                
          if  self.state.phase == "bankrupcy":
              game_output("\n* The game ended in round {} due to bankrupcy).".format(self.state.round))
          else:
              game_output("\n* End of game (the full {} rounds have been played).".format(self.max_rounds))
          
          winning_amount = max([player.money(self.state) for player in players])
          winners = [player for player in players if player.money(self.state) == winning_amount]
          if len(winners) == 1:
             winner = winners[0]
             game_output( "* The winner is {} with £{}.".format(winner.name, winning_amount))
          else:
             winners_str = ", ".join([winner.name for winner in winners])
             game_output( "* The winners are {}, who have £{}.".format(winners_str,winning_amount))
          return winners
        
      def check_for_quit(self):
          key = input( "Press <return> to continue, or enter 'q' to quit: ")  
          if key == "q" or key == "Q":
              return True
          return False
  



############# Players, number of games, start money, number of rounds, game output    
# 
# # Strategies
#               rm opmm  oprm  bm   sm   res   respen  jep av
s1 =  Strategy( 0,  0.7,  2,   10,   5,  500,  1000,   10000) #TIGHT BOUNDARY 
s2 =  Strategy( 3, 0,  2,   50,  50,    0,  1200,   20000) #GREEDY BOUNDARY
s3 =  Strategy( 0,   0,   0,    0,   0,   0,     0 ,   0    ) #IRRATIONAL BOUNDARY  
s4 =  Strategy( 3,  0,  3,     10,  10,  100,   500,   10000) #RANDOM TESTER 1
s5 =  Strategy( 2,  0.1,  3,   10,  10,  300,   500,   10000) #RANDOM TESTER 2
s6 =  Strategy( 9,  0,    1,   10,  10,   0 ,   900,   20000) #RANDOM TESTER 3
s7 =  Strategy( 3,  0,    1,   10,  10,   0 ,   900,   20000) #OPTIMAL STRATEGY

brandon = Player("Brandon", "male",   s1 )
marya   = Player("Marya",   "female", s1 )
lucia   = Player("Lucia",   "female", s2 )
AI = Player("AI",   "female", s2 )
players = [ brandon, marya, lucia, AI] 

 

def test_series(players, num_games, start_money, game_length, game_output=False):
      global GAME_OUTPUT
      GAME_OUTPUT = game_output
      if GAME_OUTPUT == False:
          print("Running wihout game output ...\n")
      games_played = 0
      while games_played < num_games:
            random.shuffle(players)
            game = Game( players, start_money, game_length )
            winners = game.play("no display")
            if len(winners) == 1: ## if there is a unique winner
                winners[0].games_won += 1
                games_played += 1
      GAME_OUTPUT = True
      print("PLAYER     WINS  PERCENT  |   RM  OPM  OPR   BM  SM   RES  RPEN   JEPAV")
      for player in players:
          won = player.games_won
          percent = ((won*100)/num_games)
          s = player.strategy
          print("{:<9} {:>4}    {:>5.2f}%  |  {:>3.1f}  {:>3.1f} {:4.1f}  {:>3} {:>3}  {:>4}  {:>4}  {:>6}"
                 .format(player.name, won, percent,
                         s.rent_mult, 
                         s.opponent_money_mult,s.opponent_rent_mult,
                         s.buy_margin, s.sell_margin,
                         s.reserve, s.reserve_penalty,
                         s.jeopardy_aversion ) )  
             
test_series( players, 1, 500, 40, game_output=False)