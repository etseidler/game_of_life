import os
import random
from collections import namedtuple
from time import sleep


Cell = namedtuple('Cell', 'x y')


class Game(object):
    ALIVE = '\u2588'
    DEAD = ' '

    def __init__(self, rows=0, cols=0):
        self.grid = [list(Game.DEAD * cols) for r in range(rows)]

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)

    @staticmethod
    def new_state(state, num_live_neighbors):
        alive_with_two_live_neighbors = state == Game.ALIVE and \
            num_live_neighbors == 2
        return Game.ALIVE if alive_with_two_live_neighbors or \
            num_live_neighbors == 3 else Game.DEAD

    def mark_alive(self, cell):
        self.grid[cell.x][cell.y] = Game.ALIVE

    def mark_cell(self, cell, state):
        self.grid[cell.x][cell.y] = state

    def get_cell(self, cell):
        return self.grid[cell.x][cell.y]

    def tick(self):
        updated = [row[:] for row in self.grid]
        for i, row in enumerate(self.grid):
            for j, _ in enumerate(row):
                num_live_neighbors = self._count_live_neighbors(i, j)
                updated[i][j] = self.new_state(
                    self.get_cell(Cell(i, j)), num_live_neighbors)
        self.grid = updated

    def random_seed(self):
        for i, row in enumerate(self.grid):
            for j, _ in enumerate(row):
                self.grid[i][j] = random.choice([Game.ALIVE, Game.DEAD])

    def _count_live_neighbors(self, i, j):
        x_last = len(self.grid) - 1
        y_last = len(self.grid[0]) - 1
        count = 0
        for x in [i-1, i, i+1]:
            for y in [j-1, j, j+1]:
                out_of_bounds = x < 0 or y < 0 or x > x_last or y > y_last
                is_self = (x == i and y == j)
                if out_of_bounds or is_self:
                    continue
                if self.grid[x][y] == Game.ALIVE:
                    count += 1
        return count


if __name__ == '__main__':
    game = Game(35, 300)
    game.random_seed()
    for _ in range(10000):
        os.system('clear')
        print(str(game))
        game.tick()
        sleep(0.2)
