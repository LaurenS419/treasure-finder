# Lauren Spee
# 261008497

MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'

def get_nth_row_from_map(mapstr, n, width, height):
    """ (str, int, int, int) -> str
    Takes a treasure map string, a number, and width and height of
    the string, and returns the string of what the row n is
    >>> get_nth_row_from_map('^..>>>..v', 1, 3, 3)
    '>>>'
    >>> get_nth_row_from_map('>.^..<<.', 0, 2, 4)
    '>.'
    >>> get_nth_row_from_map('><^..<', 1, 3, 2)
    '..<'
    """
    
    n_start = (width*n)
    n_end = n_start + width
    
    return mapstr[n_start:n_end]
    
    
def print_treasure_map(mapstr, width, height):
    """(str, int, int) -> NoneType
    Takes a map string mapstr, and ints of the width and height of the
    map. Returns the map with the correct dimensions
    >>> print_treasure_map('<..vvv..', 2, 4)
    <.
    .v
    vv
    ..
    >>> print_treasure_map('>..^>v..^..>', 3, 4)
    >..
    ^>v
    ..^
    ..>
    >>> print_treasure_map('>.v..^<.', 4, 2)
    >.v.
    .^<.
    """
    
    i = 0
    
    while i < height:  
        print(get_nth_row_from_map(mapstr, i, width, height))
        
        i += 1
        
def change_char_in_map(mapstr, row, column, c, width, height):
    """ (str, int, int, str, int int) -> str
    Takes the map string, the row and column the char is
    located, the new char c, and the width and height of the map.
    Returns the map string with that character changed into c.
    >>> change_char_in_map('.........', 1, 1, 'X', 3, 3)
    '....X....'
    >>> change_char_in_map('<..^>.', 0, 1, 'a', 2, 3)
    '<a.^>.'
    >>> change_char_in_map('..>>.<>.v...', 2, 2, 'X', 3, 4)
    '..>>.<>.X...'
    """
    
    location = (width*row)+column
    
    return mapstr[:location] + c + mapstr[location+1:]

def get_proportion_travelled(mapstr):
    """ (str) -> float
    Takes a treasure map string and returns a percentage
    in decimal form the amount Xs in the map (the Xs show
    where has been travelled)
    >>> get_proportion_travelled('.X..X.XX.')
    0.44
    >>> get_proportion_travelled('XX..>.')
    0.33
    >>> get_proportion_travelled('..XXXXXXX')
    0.78
    """
    
    travelled = mapstr.count(BREADCRUMB_SYMBOL)
    
    return round(travelled / len(mapstr),2)
    
def get_nth_map_from_3D_map(mapstr3d, n, width, height, depth):
    """ (str, int, int, int, int) -> str
    Returns the map at the nth depth in the 3d treasure map based
    on width and height.
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 1, 3, 3, 2)
    '.v.vXv.v.'
    >>> get_nth_map_from_3D_map('...X.>vX...<..XX<.', 2, 2, 3, 2)
    '..XX<.'
    >>> get_nth_map_from_3D_map('X..>Xv..>>.v^..X.>', 0, 3, 3, 1)
    'X..>Xv..>'
    """
    
    n_start = (width*height*n)
    n_end = n_start + (width*height)
    
    return mapstr3d[n_start:n_end]
    
def print_3D_treasure_map(mapstr3d, width, height, depth):
    """(str, int, int, int) -> NoneType
    Prints the whole 3d treasure map in its correct form
    using the width, height, and depth.
    >>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.', 3, 3, 2)
    .X.
    XXX
    .X.
    
    
    .v.
    vXv
    .v.
    >>> print_3D_treasure_map('.X..v>>.Xv^>>..X..', 2, 3, 3)
    .X
    ..
    v>


    >.
    Xv
    ^>


    >.
    .X
    ..
    >>> print_3D_treasure_map('XXX.>>.>v.vv....>>>v.X>^', 4, 3, 2)
    XXX.
    >>.>
    v.vv


    ....
    >>>v
    .X>^
    """
    
    j = 0
    k = 0
    
    while j < depth:  
        layer = get_nth_map_from_3D_map(mapstr3d, j, width, height, depth)
        
        while k < height:
            print(get_nth_row_from_map(layer, k, width, height))
            k += 1
        
        if j < depth - 1:
            print("")
            # adds a space between the maps of each layer
            
        j += 1
        k = 0
        
def change_char_in_3D_map(mapstr3d, row, column, level, c, width, height, depth):
    """ (str, int, int, int, str, int, int, int, int) -> str
    Returns the string of the 3d treasure map with the character
    at the given row, coloum, and level changed into character c
    >>> change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 0, '#', 3, 3, 2)
    '#X.XXX.X..v.vXv.v.'
    >>> change_char_in_3D_map('..>.v.v^.>>.<.v.^>', 1, 1, 1, 'X', 3, 3, 2)
    '..>.v.v^.>>.<Xv.^>'
    >>> change_char_in_3D_map('..>.<^..>.X.', 1, 2, 0, 'X', 2, 3, 2)
    '..>.X^..>.X.'
    """
    
    location = (width*height*level) + (width*row) + column
    
    return mapstr3d[:location] + c + mapstr3d[location+1:]