The game of life 
================

this is a simple implementation of the Conway's Game of Life using numpy and scipy packages in Python.

The "game" takes place on a 2D grid which consists of "alive" and "dead" cells, and the rules to step from generation to generation are as in sequel:

Cell death: It happens due to overpopulation or underpopulation. The former is when a living cell surrounded by more than 3 living cells while latter occurs when the it is surrounded by less than 2 living cells.
Surviving: A living cell survives until next generation if the number of living surrounded cells are exactly 2 or 3 
Reproduction: A dead cell becomes alive if the number of surrounded alive cells are exactly 3.

In our implementation, we model the 2D grid with a sparse matrix as in general the dimensions of  gris is not important. The important thing is the number of the alive cells and their location. So, an sparse matrix can be a good data structure. Besides, it is suit for our processing.
So obviously, in each iteration the early task is to find the status of surrounding cells in terms of total number of alive cells. This task is done in surrounding_matrix_calculator(M)
The main point is that the current value of the cell is not important at this stage. Here the reducer is the csr_matrix object in python who aggregate the values for mapped indexes.
The next step is to filter the surrounding in two senses: surviving cells and reproduced. This task is done in find_next_generation(surrounding_matrix,M)

In order to demonstrate the functionality, I created some demo of the popular patterns from wikipedia page of “Game of Life”. To select 
	demo(1) represents the “Blinker” pattern
 	demo(2) simulates “Toad” pattern
	demo(3) depicts “Spaceships” pattern

