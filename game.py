import numpy as np
from time import sleep
import os

def is_in_bounds(cell, shape):
    if any([cell[0] < 0, cell[0] >= shape[0], cell[1] < 0, cell[1] >= shape[1]]):
        return False
    return True

def get_neighbors(cell, shape):
    neighbors = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            offset = (x, y)
            if offset == (0, 0):
                continue
            n = (cell[0] + offset[0], cell[1] + offset[1])
            if (is_in_bounds(n, shape)):
                neighbors.append(n)
    return neighbors

def get_num_alive_neighbors(cell, grid):
    neighbors = get_neighbors(cell, grid.shape)
    n_alive = 0
    for neighbor in neighbors:
        n_alive = n_alive + grid[neighbor]
    return n_alive

def alive_next_gen(cell, grid):
    cell_alive = grid[cell]
    neighbors_alive = get_num_alive_neighbors(cell, grid)
    next_value = 0
    if cell_alive == 1 and neighbors_alive < 2:
        next_value = 0
    if cell_alive == 1 and neighbors_alive in [2, 3]:
        next_value = 1
    if cell_alive == 1 and neighbors_alive > 3:
        next_value = 0
    if cell_alive == 0 and neighbors_alive == 3:
        next_value = 1
    return next_value

def update_grid(grid):
    for index, value in np.ndenumerate(grid):
        grid[index] = alive_next_gen(index, grid)

if __name__ == "__main__":
    g = np.random.choice([0, 1], size = (15, 15), p = [0.6, 0.4])
    generation = 0

    while sum(sum(g)) > 0:
        os.system("clear")
        print(g)
        print(f"Generation {generation}")
        last_gen = np.copy(g)
        update_grid(g)

        if np.array_equal(g, last_gen):
            print("Nothing changed!")
            break

        generation = generation + 1

        sleep(0.25)
