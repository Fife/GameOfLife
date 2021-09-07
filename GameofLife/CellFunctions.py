import math, random
from recordclass import recordclass

#Definition of a cell using recordclass
Cell = recordclass("Cell", "status num_neighbors")


#Returns world full of dead cells of passed length
def gen_world(length):
    world = []
    for x in range(length):
        world.append(list())
        for y in range(length):
            world[x].append(Cell(bool(random.getrandbits(1)), 0))
    find_neighbors(world)
    return world

def gen_blank_world(length):
    world = []
    for x in range(length):
        world.append(list())
        for y in range(length):
            world[x].append(Cell(False, 0))
    find_neighbors(world)
    return world

#Returns Next Board State
def next_board(world):
    new_board = []
    r_count = 0
    #Naive first attemtpt
    for row in world:
        new_board.append(list())
        for cell in row:
            neighborhood = get_neighborhood(world, world.index(row), row.index(cell))
            cell.num_neighbors = count_neighbors(neighborhood)
            if (cell.status):
                if ((count_neighbors(neighborhood) < 2) or (count_neighbors(neighborhood) > 3)):
                    cell.status = False
            else:
                if (count_neighbors(neighborhood) == 3):
                    cell.status = True
            new_board[r_count].append(cell)
        r_count += 1
    return new_board

def find_neighbors(world):
    for row in world:
        for cell in row:
            neighborhood = get_neighborhood(world, world.index(row), row.index(cell))
            cell.num_neighbors = count_neighbors(neighborhood)

#Gets the neighborhood of a surrounding cell, note that cells can wrap around.
def get_neighborhood(world, row, col):
    neighborhood = []
    for rows in range(3):
        neighborhood.append(list())
        for cols in range(3):
            n_row = rows+row
            n_col = cols+col
            while(n_row>len(world)):
                n_row -=len(world)
            while(n_col>len(world[cols])):
                n_col -=len(world[cols])
            neighborhood[rows].append(world[(n_row)-1][(n_col)-1])
    print(neighborhood)
    return neighborhood

#Count number of neighbors surrounding a cell, not including itself
def count_neighbors(neighborhood):
    count =0
    for row in neighborhood:
        for cell in row:
            if (cell.status):
                count +=1
    if (neighborhood[1][1].status):
        count -=1
    return count

def clamp(val, minval, maxval):
    if val < minval: return minval
    if val > maxval: return maxval
    return val