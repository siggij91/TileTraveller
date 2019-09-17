##Project 5 Tile Traveler https://github.com/siggij91/TileTraveller

#Create tile structure and label it
#Append allowable moves to file structure
#N = +1 in second index and S = -1
#E = +1 in first index and W = -1
#Once in new tile, show the allowable moves
#Once player enters 3, 1 show them that they win.



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
            
def select_move(current_square, x, y):
    
    loop_continue = True

    while loop_continue:
        
        move = str(input('Direction: '))
    
        for char in current_square:
            
            if move.upper() == 'N' and move.upper() == char:
                y += 1
                loop_continue = False
                break
            elif move.upper() == 'E' and move.upper() == char:
                x += 1
                loop_continue = False
                break
            elif move.upper() == 'S' and move.upper() == char:
                y -= 1
                loop_continue = False
                break
            elif move.upper() == 'W' and move.upper() == char:
                x -= 1
                loop_continue = False
                break
        else:
            print('Not a valid direction!')
        

    return x, y
        
SQ = [['N','N','N'],
['NES','SW','NS'],
['ES','EW','SW']]

x = 1
y = 1
current_square = SQ[y-1][x-1]

while True:
    can_move(current_square)
    x, y = select_move(current_square, x, y)
    current_square = SQ[y-1][x-1]

    if x == 3 and y == 1:
        print('Victory!')
        break


    
    