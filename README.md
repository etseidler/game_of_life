# Implement Conway's Game of Life in Python

## Initial Setup
0. Make sure Python3 is installed
    * `brew update && brew install pyenv`
    * `pyenv install 3.7.4 && pyenv global 3.7.4`
    * `python --version` or `python`
1. Create a new virtual environment: `python -m venv env` and `source env/bin/activate`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the tests: `ptw` will run the tests and watch for changes
4. Write code and make the tests pass


## The Rules of the Game (directly from Wikipedia)

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbours dies.
2. Any live cell with more than three live neighbours dies.
3. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbours will come to life.

The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths happen simultaneously, and the discrete moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of the one before.) The rules continue to be applied repeatedly to create further generations. 