# Lauren Spee
# 261008497

MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'

import treasure_utils as tu
import random

def generate_treasure_map_row(width, is_3D):
    """(int, bool) -> str
    Takes in a width and a bool if the map is 3D or not,
    returns a row of the treasure map with the given width
    >>> random.seed(8)
    >>> generate_treasure_map_row(6,True)
    'v<>.<*'
    >>> random.seed(8)
    >>> generate_treasure_map_row(5,False)
    'v<>.<'
    >>> random.seed(8)
    >>> generate_treasure_map_row(10,False)
    'v<>.<<>^^<'
    """

    i = 0
    row = ''

    for i in range(0,width):
        random_int = random.randint(1,6)
        
        if random_int == 1:
            row += EMPTY_SYMBOL
            
        else:
            char_int = random.randint(0,3)
            row += MOVEMENT_SYMBOLS[char_int]
        
        i += 1
        
    if is_3D == True:
        turn_3D = random.randint(0,1)
        
        if turn_3D == 1:
            random_3D = random.randint(0,width-1)
            char_3D = random.randint(0,1)
            
            row = row[:random_3D] +\
            MOVEMENT_SYMBOLS_3D[char_3D] + row[random_3D+1:]
            
    return row

def generate_treasure_map(width, height, is_3D):
    """(int, int, bool) -> str
    Takes the dimensions of the treasure map (height and
    width) and if the treasure map is 3D. Returns the treasure map
    >>> random.seed(8)
    >>> generate_treasure_map(3, 3, False)
    '><>.<<>^^'
    >>> random.seed(8)
    >>> generate_treasure_map(4, 5, True)
    '><>.<|^^.<.|>v.*><><'
    >>> random.seed(8)
    >>> generate_treasure_map(2, 3, True)
    '><>.<|'
    """
    
    i = 0
    mapstr = ''
    
    while i < height:  
        mapstr += generate_treasure_map_row(width, is_3D)
        
        i += 1
    
    mapstr = MOVEMENT_SYMBOLS[0] + mapstr[1:]
    
    return mapstr

def generate_3D_treasure_map(width, height, depth):
    """(int, int, int) -> str
    Returns a 3D treasure map with the given width,
    height, and depth.
    >>> random.seed(8)
    >>> generate_3D_treasure_map(3, 3, 2)
    '><><|>*<>v^^v.|.><'
    >>> random.seed(8)
    >>> generate_3D_treasure_map(3, 4, 4)
    '><><|>*<>v^^v.|.><<<><^|<>|<<v<*.|vv*><v^|^.*|.>'
    >>> random.seed(8)
    >>> generate_3D_treasure_map(3, 2, 2)
    '><><|>*<>v^^'
    """
   
    j = 0
    mapstr3d = ''
    
    while j < depth:  
        k = 0
        
        while k < height:  
            mapstr3d += generate_treasure_map_row(width, True)
        
            k += 1
        
        j += 1
    
    mapstr3d = MOVEMENT_SYMBOLS[0] + mapstr3d[1:]
    
    return mapstr3d
    
def follow_trail(mapstr, row, column, level, width,
                height, depth, distance):
    """ (str, int, int, int, int, int, int, int) -> str
    Takes a 3d treasure map string with the parameters of
    given width, height, and depth. The path starting place based
    on row, column, and level, and it'll travel the amount set by
    distance.
    >>> follow_trail('>+>v.<+>.*><<.^<+*<.>|v+^*^', 0,0,0,3,3,3,20)
    Treasures collected: 1
    Symbols visited: 3
    'X+Xv.<+>.*><<.^<+*<.>|v+^*^'
    >>> follow_trail('>*.|>|.**^v^|.*^<^.*>...', 1, 1, 1, 2, 4, 3, 14)
    Treasures collected: 0
    Symbols visited: 4
    '>*.|>|.**XvX|.*X<^.*>...'
    >>> follow_trail('>^*<.<<<vvv.>>>.^.>>^>.v^|.', 0,0,0,3,3,3,-1)
    Treasures collected: 0
    Symbols visited: 11
    'XXX<.<XXXvv.>>>.^.>>X>.X^|.'
    """
    
    i = 0
    j = 0
    empty = False
    
    treasures_collected = 0
    
    width_loc = column
    height_loc = row
    depth_loc = level
    new_map = mapstr
    most_recent = EMPTY_SYMBOL
    
    if int(distance) == -1:
        distance = 10**10
        # if distance is set to -1 it'll go for a very
        # long time
        
    while i < distance:
        
        location = (width_loc + (height_loc*width)
                    + (depth_loc*(height*width)))        
        
        if new_map[location] == BREADCRUMB_SYMBOL:
            break
        
        ## Movements ##
        
        if mapstr[location] == MOVEMENT_SYMBOLS[0]: #right
            new_map = tu.change_char_in_3D_map(new_map, height_loc,
                            width_loc, depth_loc, BREADCRUMB_SYMBOL,
                            width, height, depth)
                        
            width_loc += 1
            
            if width_loc > width-1:
                width_loc = 0
            #stops it from going off the map
                
        elif mapstr[location] == MOVEMENT_SYMBOLS[1]: #left
            new_map = tu.change_char_in_3D_map(new_map, height_loc,
                            width_loc, depth_loc, BREADCRUMB_SYMBOL,
                            width, height, depth)
            
            width_loc -= 1
         
            if width_loc < 0:
                width_loc = width-1
                        
        elif mapstr[location] == MOVEMENT_SYMBOLS[2]: #down
            new_map = tu.change_char_in_3D_map(new_map, height_loc,
                                width_loc, depth_loc, BREADCRUMB_SYMBOL,
                                width, height, depth)
            
            height_loc += 1
            
            if height_loc > height-1:
                height_loc = 0
                                        
        elif mapstr[location] == MOVEMENT_SYMBOLS[3]: #up
            new_map = tu.change_char_in_3D_map(new_map, height_loc,
                                width_loc, depth_loc, BREADCRUMB_SYMBOL,
                                width, height, depth)
            
            height_loc -= 1
            
            if height_loc < 0:
                height_loc = height - 1
                                
        elif mapstr[location] == MOVEMENT_SYMBOLS_3D[0]: #hole
            new_map = tu.change_char_in_3D_map(new_map, height_loc,
                                width_loc, depth_loc, BREADCRUMB_SYMBOL,
                                width, height, depth)
            
            depth_loc += 1
            
            if depth_loc > depth-1:
                depth_loc = 0

        elif mapstr[location] == MOVEMENT_SYMBOLS_3D[1]: #ladder
            new_map = tu.change_char_in_3D_map(new_map, height_loc,
                                width_loc, depth_loc, BREADCRUMB_SYMBOL,
                                width, height, depth)
            
            depth_loc -= 1
            
            if depth_loc < 0:
                depth_loc = depth - 1
                
            
        ## Non-movement symbols ##
        
        elif mapstr[location] == EMPTY_SYMBOL\
            or mapstr[location] == TREASURE_SYMBOL:
            
            if most_recent == EMPTY_SYMBOL:
                break
            
            while mapstr[location] == EMPTY_SYMBOL\
                or mapstr[location] == TREASURE_SYMBOL:               

                if i >= distance:
                    break
                
                if mapstr[location] == TREASURE_SYMBOL:
                    treasures_collected += 1
                    
                if new_map[location] == BREADCRUMB_SYMBOL:
                    break
                    
                if most_recent == MOVEMENT_SYMBOLS[0]: #right                     
                    width_loc += 1
                    if width_loc > width-1:
                        width_loc = 0
        
                elif most_recent == MOVEMENT_SYMBOLS[1]: #left            
                    width_loc -= 1
                    if width_loc < 0:
                        width_loc = width-1
                        
                elif most_recent == MOVEMENT_SYMBOLS[2]: #down            
                    height_loc += 1         
                    if height_loc > height-1:
                        height_loc = 0
                                      
                elif most_recent == MOVEMENT_SYMBOLS[3]: #up            
                    height_loc -= 1
            
                    if height_loc < 0:
                        height_loc = height - 1
                        
                elif most_recent == MOVEMENT_SYMBOLS_3D[0]: #hole
                    depth_loc += 1         
                    if depth_loc > depth-1:
                        depth_loc = 0
                            
                elif most_recent == MOVEMENT_SYMBOLS_3D[1]: #ladder
                    depth_loc -= 1        
                    if depth_loc < 0:
                        depth_loc = depth - 1
                
                i += 1
                
                location = (width_loc + (height_loc*width) +
                            (depth_loc*(height*width)))
            empty = True
            
        
        if empty == False:
            i += 1
            # only increases by 1 if the program wasn't going
            # through the 'empty symbol' while loop
            
        empty = False
        most_recent = mapstr[location]
                    
    print("Treasures collected:", treasures_collected)
    print("Symbols visited:", i)
        
    return new_map

