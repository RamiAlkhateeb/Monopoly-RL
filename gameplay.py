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
                    
                    game_output( result, " lost all money and now declared BANKRUPT!" )
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
             game_output( "* The winner is {} with M {}.".format(winner.name, winning_amount))

          else:
             winners_str = ", ".join([winner.name for winner in winners])
             game_output( "* The winners are {}, who have M {}.".format(winners_str,winning_amount))
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
tight_strategy =  Strategy( 0,  0.7,  2,   10,   5,  500,  1000,   10000) #TIGHT BOUNDARY 
greedy_strategy =  Strategy( 3, 0,  2,   50,  50,    0,  1200,   20000) #GREEDY BOUNDARY
irrational_strategy =  Strategy( 0,   0,   0,    0,   0,   0,     0 ,   0    ) #IRRATIONAL BOUNDARY  
random_strategy1 =  Strategy( 3,  0,  3,     10,  10,  100,   500,   10000) #RANDOM TESTER 1
random_strategy2 =  Strategy( 2,  0.1,  3,   10,  10,  300,   500,   10000) #RANDOM TESTER 2
random_strategy3 =  Strategy( 9,  0,    1,   10,  10,   0 ,   900,   20000) #RANDOM TESTER 3
optimal_strategy =  Strategy( 3,  0,    1,   10,  10,   0 ,   900,   20000) #OPTIMAL STRATEGY

brandon = Player("Brandon",  tight_strategy )
marya   = Player("Marya",   irrational_strategy )
lucia   = Player("Lucia",   greedy_strategy )
AI = Player("AI",   optimal_strategy)
players = [ brandon, marya, lucia, AI] 

 

def test_series(players, num_games, start_money, game_length, game_output_flag=False):
      global GAME_OUTPUT
      GAME_OUTPUT = game_output_flag
      if GAME_OUTPUT == False:
          game_output("Running wihout game output ...\n")
      games_played = 0
      winning_strategies = []
      while games_played < num_games:
            random.shuffle(players)
            game = Game( players, start_money, game_length )
            winners = game.play("no display")
            if len(winners) == 1: ## if there is a unique winner
                winners[0].games_won += 1
                games_played += 1
                winning_strategies.append(winners[0].strategy)

    #   game_output("************************************")
    #   game_output("************************************")
    #   game_output("************************************")
    #   game_output("************************************")
    #   game_output("************************************")
      
    #   rent_mult_sum =0
    #   opponent_money_mult_sum = 0 
    #   opponent_rent_mult_sum = 0
    #   buy_margin_sum = 0
    #   sell_margin_sum = 0
    #   reserve_sum= 0
    #   reserve_penalty_sum = 0
    #   jeopardy_aversion_sum = 0

    #   lettt = len(winning_strategies)
    #   for i in winning_strategies:
    #       rent_mult_sum += i.rent_mult 
    #       opponent_money_mult_sum += i.opponent_money_mult
    #       opponent_rent_mult_sum += i.opponent_rent_mult
    #       buy_margin_sum += i.buy_margin 
    #       sell_margin_sum += i.sell_margin 
    #       reserve_sum += i.reserve 
    #       reserve_penalty_sum += i.reserve_penalty 
    #       jeopardy_aversion_sum += i.jeopardy_aversion 

    #   rent_mult_avg=  rent_mult_sum/ lettt
    #   opponent_money_mult_avg = opponent_money_mult_sum / lettt
    #   opponent_rent_mult_avg= opponent_rent_mult_sum/ lettt
    #   buy_margin_avg= buy_margin_sum/ lettt
    #   sell_margin_avg= sell_margin_sum/ lettt
    #   reserve_avg= reserve_sum/ lettt
    #   reserve_penalty_avg= reserve_penalty_sum/ lettt
    #   jeopardy_aversion_avg= jeopardy_aversion_sum/ lettt

    #   optimal_strategy_new =  Strategy( 
    #       rent_mult_avg,  
    #       opponent_money_mult_avg,
    #       opponent_rent_mult_avg,       
    #       buy_margin_avg,  
    #       sell_margin_avg,   
    #       reserve_avg ,   
    #       reserve_penalty_avg,   
    #       20000) #OPTIMAL STRATEGY
      
    #   NewAI = Player("NewAI",   optimal_strategy_new)
    #   players = [ brandon, marya, lucia, NewAI]

    #   brandon.games_won = 0 
    #   lucia.games_won = 0 
    #   marya.games_won = 0 
    #   NewAI.games_won = 0 

    #   games_played = 0
    #   while games_played < num_games:
    #         random.shuffle(players)
    #         game = Game( players, start_money, game_length )
    #         winners = game.play("no display")
    #         if len(winners) == 1: ## if there is a unique winner
    #             winners[0].games_won += 1
    #             games_played += 1
    #             winning_strategies.append(winners[0].strategy)


      GAME_OUTPUT = True
      game_output("PLAYER     WINS  PERCENT  |   RM  OPM  OPR   BM  SM   RES  RPEN   JEPAV")
      for player in players:
          won = player.games_won
          percent = ((won*100)/num_games)
          s = player.strategy
          game_output("{:<9} {:>4}    {:>5.2f}%  |  {:>3.1f}  {:>3.1f} {:4.1f}  {:>3} {:>3}  {:>4}  {:>4}  {:>6}"
                 .format(player.name, won, percent,
                         s.rent_mult, 
                         s.opponent_money_mult,s.opponent_rent_mult,
                         s.buy_margin, s.sell_margin,
                         s.reserve, s.reserve_penalty,
                         s.jeopardy_aversion ) )  
             
test_series( players, 100, 500, 14, game_output_flag=True)