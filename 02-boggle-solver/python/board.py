#!/usr/bin/env python3

import random


class Board(object):
    """
    This class represents a Boggle board and its functionalities
    """

    def __init__(self, size: int, distribution: dict):
        """
        Constructor: initialize a board with given size and letter distribution
        :param size: the board size
        :param distribution: the dictionary of characters to be sampled from
        """
        self.__size = size
        self.__distribution = distribution
        self.__board = None
        self.__init_board()

    def get_board(self):
        """
        Return generated board
        :return:
        """
        return self.__board

    def get_board_size(self):
        """
        Return the size of this board
        :return: board size
        """
        return len(self.__board)

    def get_neighbours(self, position: tuple):
        """
        Return neighbouring positions of the given position.
        Navigating on the board is done horizontally, vertically and diagonally.
        :param position: current position
        :return: a list of neighbouring tiles on the board
        """
        neighbours = []
        row = position[0]
        col = position[1]

        adj_rows = [row]
        adj_cols = [col]

        size_range = set(range(self.__size))

        if (row - 1) in size_range:
            adj_rows.append(row - 1)
        if (row + 1) in size_range:
            adj_rows.append(row + 1)
        if (col - 1) in size_range:
            adj_cols.append(col - 1)
        if (col + 1) in size_range:
            adj_cols.append(col + 1)

        for i in adj_rows:
            for j in adj_cols:
                neighbours.append((i, j))

        neighbours.remove(position)
        return neighbours

    def __init_board(self):
        """
        Generate the board based on dice distribution from the new Boggle version
        :return: a 2 dimensional array/list containing randomly generated characters
        """
        self.__board = [["" for j in range(self.__size)] for i in range(self.__size)]
        distribution_size = len(self.__distribution[0])
        for i in range(self.__size * self.__size):
            row = i // self.__size  # integer division
            col = i % self.__size
            dice_throw = random.randint(0, distribution_size - 1)
            self.__board[row][col] = self.__distribution[i][dice_throw]
