
# def add(x, y):
#     return(x + y)
# We don't need this anymore. We just had it to test the unittest TestCase.

from string import ascii_uppercase
from random import choice

def make_grid(columns, rows):
    return {(c, r) : choice(ascii_uppercase) 
                        for r in range(rows) 
                            for c in range(columns)} # This is a nested loop.

def potential_neighbours(position):
    c, r = position
    return [(c-1, r-1), (c, r-1),  (c+1, r-1), 
            (c-1, r),              (c+1, r), 
            (c-1, r+1), (c, r+1),  (c+1, r+1)] # This list data structure is just for visual purposes to see the potential neighbours of a tupple, which is why there is a space in the middle.  # "set" as a data structure will also work here.
            
def path_to_word(path, grid):
    word = ""
    for position in path: # Loop through path, data type list.
        word += grid[position] # Match position in path list to position in grid dictionary and create string. 
    return word # Return string of letters.
    
    
def load_word_list(filename):
    with open(filename) as f: # We use variable filename instead of "words.txt" so that we can use this function again to call any filname, see below.
        text = f.read().upper().split("\n") # .upper() pulls in the file name in upper case - see above ascii is uppercase means the letters in the grid are uppercase.
    return text    
    
# words = load_word_list("words.txt")

# Real neighbours that are on the grid.
def get_real_neighbours(grid): 
    real_neighbours = {}
    
    for position in grid:
        pn = potential_neighbours(position)
        
        # on_the_grid = []
        # for p in pn:
        #     if p in grid:
        #         on_the_grid.append(p)
            
        # With list comprehension, it is also written as;
        on_the_grid = [ p for p in pn if p in grid]
        
        real_neighbours[position] = on_the_grid
        
    return real_neighbours    

grid = make_grid(2, 2)

rn = get_real_neighbours(grid)
print(rn)

    