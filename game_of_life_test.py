import pytest
from game_of_life import Game, Cell


neighbors_for_upper_left_cell = [
    Cell(0, 1), Cell(1, 0), Cell(1, 1)
]
neighbors_for_upper_center_cell = [
    Cell(0, 0), Cell(1, 0), Cell(1, 1), Cell(1, 2), Cell(0, 2)
]
neighbors_for_middle_cell = [
    Cell(0, 0), Cell(0, 1), Cell(0, 2),
    Cell(1, 0), Cell(1, 2),
    Cell(2, 0), Cell(2, 1), Cell(2, 2)
]


def test_new_instance_creates_empty_grid():
    game = Game()

    assert len(game.grid) == 0


@pytest.mark.parametrize("size", [1, 2, 4, 8, 16, 32, 64])
def test_grid_size(size):
    game = Game(size, size)
    assert len(game.grid) == size
    assert all(len(row) == size for row in game.grid)


def test_a_cell_is_defaulted_to_dead():
    game = Game(1, 1)

    assert len(game.grid) == 1
    assert str(game) == Game.DEAD


def test_can_get_a_single_cell():
    game = Game(3, 3)

    assert game.get_cell(Cell(1, 1)) == Game.DEAD


def test_all_cells_are_defaulted_to_dead():
    game = Game(10, 10)

    assert all(i == Game.DEAD for row in game.grid for i in row)


def test_can_return_a_string_representation_with_all_dead_cells():
    game = Game(2, 3)

    assert game.__str__() == '   \n   '


def test_can_return_a_string_representation_with_some_living_cells():
    game = Game(3, 3)
    alive_cells = [Cell(0, 2), Cell(1, 1), Cell(2, 0)]
    for cell in alive_cells:
        game.mark_cell(cell, Game.ALIVE)

    assert game.__str__() == '  {}\n {} \n{}  '.format(*[Game.ALIVE]*3)


def test_can_mark_a_cell_as_alive():
    game = Game(3, 3)
    cell_1_1 = Cell(1, 1)

    game.mark_alive(cell_1_1)

    assert game.get_cell(cell_1_1) == Game.ALIVE


def test_can_mark_a_cell_as_dead_or_alive():
    game = Game(3, 3)
    cell_1_1 = Cell(1, 1)

    game.mark_cell(cell_1_1, Game.ALIVE)
    assert game.get_cell(cell_1_1) == Game.ALIVE

    game.mark_cell(cell_1_1, Game.DEAD)
    assert game.get_cell(cell_1_1) == Game.DEAD


@pytest.mark.parametrize("initial_state,live_neighbors,new_state", [
    (Game.ALIVE, 0, Game.DEAD),
    (Game.ALIVE, 1, Game.DEAD),
    (Game.ALIVE, 2, Game.ALIVE),
    (Game.ALIVE, 3, Game.ALIVE),
    (Game.ALIVE, 4, Game.DEAD),
    (Game.ALIVE, 5, Game.DEAD),
    (Game.ALIVE, 6, Game.DEAD),
    (Game.ALIVE, 7, Game.DEAD),
    (Game.ALIVE, 8, Game.DEAD),
    (Game.DEAD, 0, Game.DEAD),
    (Game.DEAD, 1, Game.DEAD),
    (Game.DEAD, 2, Game.DEAD),
    (Game.DEAD, 3, Game.ALIVE),
    (Game.DEAD, 4, Game.DEAD),
    (Game.DEAD, 5, Game.DEAD),
    (Game.DEAD, 6, Game.DEAD),
    (Game.DEAD, 7, Game.DEAD),
    (Game.DEAD, 8, Game.DEAD)
])
def test_new_state_for_live_cells(initial_state, live_neighbors, new_state):
    assert Game.new_state(initial_state, live_neighbors) == new_state


@pytest.mark.parametrize("initial_state,live_neighbors,new_state", [
    (Game.ALIVE, neighbors_for_middle_cell[0:1], Game.DEAD),
    (Game.ALIVE, neighbors_for_middle_cell[0:2], Game.ALIVE),
    (Game.ALIVE, neighbors_for_middle_cell[0:3], Game.ALIVE),
    (Game.ALIVE, neighbors_for_middle_cell[0:4], Game.DEAD),
    (Game.ALIVE, neighbors_for_middle_cell[0:5], Game.DEAD),
    (Game.ALIVE, neighbors_for_middle_cell[0:6], Game.DEAD),
    (Game.ALIVE, neighbors_for_middle_cell[0:7], Game.DEAD),
    (Game.ALIVE, neighbors_for_middle_cell, Game.DEAD),
    (Game.DEAD, neighbors_for_middle_cell[0:1], Game.DEAD),
    (Game.DEAD, neighbors_for_middle_cell[0:2], Game.DEAD),
    (Game.DEAD, neighbors_for_middle_cell[0:3], Game.ALIVE),
    (Game.DEAD, neighbors_for_middle_cell[0:4], Game.DEAD),
    (Game.DEAD, neighbors_for_middle_cell[0:5], Game.DEAD),
    (Game.DEAD, neighbors_for_middle_cell[0:6], Game.DEAD),
    (Game.DEAD, neighbors_for_middle_cell[0:7], Game.DEAD),
    (Game.DEAD, neighbors_for_middle_cell, Game.DEAD)
])
def test_middle_cell_with_neighbors(initial_state, live_neighbors, new_state):
    game = Game(3, 3)
    middle_cell = Cell(1, 1)
    game.mark_cell(middle_cell, initial_state)
    for cell in live_neighbors:
        game.mark_alive(cell)

    game.tick()

    assert game.get_cell(middle_cell) == new_state


@pytest.mark.parametrize("initial_state,live_neighbors,new_state", [
    (Game.ALIVE, [], Game.DEAD),
    (Game.ALIVE, neighbors_for_upper_left_cell[0:1], Game.DEAD),
    (Game.ALIVE, neighbors_for_upper_left_cell[0:2], Game.ALIVE),
    (Game.ALIVE, neighbors_for_upper_left_cell, Game.ALIVE),
    (Game.DEAD, [], Game.DEAD),
    (Game.DEAD, neighbors_for_upper_left_cell[0:1], Game.DEAD),
    (Game.DEAD, neighbors_for_upper_left_cell[0:2], Game.DEAD),
    (Game.DEAD, neighbors_for_upper_left_cell, Game.ALIVE),
])
def test_UL_cell_with_neighbors(initial_state, live_neighbors, new_state):
    game = Game(3, 3)
    upper_left_cell = Cell(0, 0)
    game.mark_cell(upper_left_cell, initial_state)
    for cell in live_neighbors:
        game.mark_alive(cell)

    game.tick()

    assert game.get_cell(upper_left_cell) == new_state


@pytest.mark.parametrize("initial_state,live_neighbors,new_state", [
    (Game.ALIVE, [], Game.DEAD),
    (Game.ALIVE, neighbors_for_upper_center_cell[0:1], Game.DEAD),
    (Game.ALIVE, neighbors_for_upper_center_cell[0:2], Game.ALIVE),
    (Game.ALIVE, neighbors_for_upper_center_cell[0:3], Game.ALIVE),
    (Game.ALIVE, neighbors_for_upper_center_cell[0:4], Game.DEAD),
    (Game.ALIVE, neighbors_for_upper_center_cell, Game.DEAD)
])
def test_UC_cell_with_neighbors(initial_state, live_neighbors, new_state):
    game = Game(3, 3)
    upper_center_cell = Cell(0, 1)
    game.mark_cell(upper_center_cell, initial_state)
    for cell in live_neighbors:
        game.mark_alive(cell)

    game.tick()

    assert game.get_cell(upper_center_cell) == new_state
