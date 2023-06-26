from space import Space
from game_output import game_output

class Board:    
    def __init__( self ):
       self.go =  Space("Millennium Square",   0,  0)
       ## Woodhouse
       wh1 = Space("Woodhouse Street",  60, 20)
       wh2 = Space("Melville Place",  50, 12)
       wh3 = Space("Quarry Mount",  30, 8)
       ## Hyde Park
       hp1 = Space("Hyde Park Road", 200, 60)
       hp2 = Space("Brudenell Road", 120, 40)
       hp3 = Space("Victoria Road", 250, 80)
       ## Headingley
       h1  = Space("Bearpit Gardens", 300,  2)
       h2  = Space("North Lane",    100,   50)
       ## Education
       e1 = Space("Leeds University", 700, 150)
       e2 = Space("Notre Dame", 200, 60)
       
       self.spaces = [ 
               self.go,
               wh1, wh2, wh3,
               e1,
               hp1, hp2, hp3,
               e2,
               h1, h2
             ]
       
       set1 = [wh1, wh2, wh3]
       set2 = [hp1, hp2, hp3]
       set3 = [h1,  h2]
       set4 = [e1,e2]
       self.sets = [set1, set2, set3, set4]
       self.num_spaces = len(self.spaces)
       for propset in self.sets:
           for prop in propset:
               #game_output(prop.name)
               prop.neighbours = propset.copy()
               prop.neighbours.remove(prop)
    
def test_neighbours():
     board = Board()
     for space in board.spaces:
         game_output("{}: {}".format(space.name, ", ".join([s.name for s in space.neighbours])))   