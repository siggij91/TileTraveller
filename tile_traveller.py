##Project 5 Tile Traveler

#Create tile structure and label it
#Append allowable moves to file structure
#N = +1 in second index and S = -1
#E = +1 in first index and W = -1
#Once in new tile, show the allowable moves
#Once player enters 3, 1 show them that they win.

SQ11 = 'N'
SQ12 = 'NES'
SQ13 = 'ES'
SQ21 = 'N'
SQ22 = 'WS'
SQ23 = 'WE'
SQ31 = 'N'
SQ32 = 'NS'
SQ33 = 'WS'

current_square = SQ11

while current_square != SQ31:
    can_move()
    select_move()
else:
    print("Victory!")