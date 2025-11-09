# python-game-of-life

A Pygame version of Conway's Game of Life simulation, made with the community branch of pygame, pygame-ce

# About

This game or simulation was made following the [Conway's Game of Life tutorial in Python & Pygame - OOP](https://youtu.be/uR0lNADr4dc?list=PL4NKE1UBtl_eUT7rpi8QPKluc0ihDDVNS) made by [Nick Koumaris](https://www.youtube.com/@programmingwithnick).

![Conway's Game of Life Example](assets/cover.png)

# Rules

There are 4 simple rules to the simulation that each cell follows, these are:

- **Underpopulation**: A live cell with fewer than two live neighbors dies.
- **Stasis**: A live cell with two or three live neighbors lives onto the next generation.
- **Overpopulation**: A live cell with more than three live neighbors dies.
- **Reproduction**: A dead cell with exactly three live neighbors becomes a live cell.

# How to play

1. Create a python environment. 
    ###### `python -m venv venv`

2. Activate the environment.
    - **PowerShell** 
        ###### `venv\Scripts\Activate.ps1`
    - **Linux and MacOS** 
        ###### `source myvenv/bin/activate`

3. Install pygame in the python environment.
    ###### `pip install pygame-ce`

4. Run the `main.py` file.
    ###### `python main.py`

# Controls

|  Key  | Function |
| :---: | -------- |
| ENTER | Starts the simulation |
| SPACE | Stops the simulation |
|   F   | Increase speed of simulation |
|   S   | Decrease speed of simulation |
|   R   | Generate random grid of live cells |
|   C   | Clear grid |
| MOUSE | Toggle the state of a cell on the grid |