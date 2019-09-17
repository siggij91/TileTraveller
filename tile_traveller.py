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
SQ22 = 'SW'
SQ23 = 'EW'
SQ31 = 'N'
SQ32 = 'NS'
SQ33 = 'SW'

current_square = SQ11

def can_move(current_square):
    
    prt_str = 'You can travel: '
    length = len(current_square)
    
    for char in current_square:
        if char == 'N' and length == 1:
            prt_str += '(N)orth.'
        elif char == 'N': 
            length -= 1
            prt_str += '(N)orth or '
        
        if char == 'E' and length == 1:
            prt_str += '(E)ast.'
        elif char == 'E': 
            length -= 1
            prt_str += '(E)ast or '
        
        if char == 'S' and length == 1:
            prt_str += '(S)outh.'
        elif char == 'S': 
            length -= 1
            prt_str += '(S)outh or '
        
        if char == 'W' and length == 1:
            prt_str += '(W)est.'
        elif char == 'W': 
            length -= 1
            prt_str += '(W)est or '
        
    return print(prt_str)         
            
can_move(current_square)

# while current_square != SQ31:
#     can_move()
#     select_move()
# else:
#     print("Victory!")