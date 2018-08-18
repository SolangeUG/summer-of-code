#!/usr/bin/env python3

from board import Board
from dictionary import Dictionary


class Solver(object):
    """
    This class represents the Boggle game solver
    """

    def __init__(self, board: Board, dictionary: Dictionary):
        """
        Constructor: initializes
        :param board: Boggle board to solve
        :param dictionary: word dictionary to use
        """
        self.__words = []
        self.__board = board
        self.__dictionary = dictionary

    def get_words(self):
        """
        Return a list of valid words on the board
        :return: all valid words
        """
        self.__words = self.__find_words()
        return self.__words

    def get_score(self):
        """
        Calculate the score of the current Boggle game
        :return: the total score of the game
        """
        score = 0
        for word in self.__words:
            word_size = len(word.strip())
            if word_size > 2:
                score = score + (word_size - 2)
        return score

    def __find_words(self):
        """
        Compute list of all legal words that can be formed from the distribution on the board
        :return: valid words on the board
        """
        tiles_in_prefix = {'stack': [], 'set': set()}
        size = self.__board.get_board_size()
        words = []

        for i in range(self.__board.get_board_size()):
            row = i // size  # integer division
            col = i % size

            # add letter to prefix
            prefix = self.__board.get_board()[row][col]

            # add tile to tiles_in_word
            position = (row, col)
            tiles_in_prefix['set'] = {position}
            tiles_in_prefix['stack'] = [position]

            if self.__dictionary.is_path(prefix):
                words += self.__find_next_words(position, prefix, tiles_in_prefix)
        return words

    def __find_next_words(self, position: tuple, prefix: str, tiles_in_prefix: dict):
        """
        Find a list of all valid words on the board which correspond to the given prefix
        :param position: position of last character in the given prefix
        :param prefix: prefix made up of letters from board tiles traversed so far
        :param tiles_in_prefix: stores positions of board tiles that make up the given prefix
        :return: the list of valid words corresponding to the given prefix
        """
        words = []
        for pos in self.__board.get_neighbours(position):
            if pos not in tiles_in_prefix['set']:
                current_letter = self.__board.get_board()[pos[0]][pos[1]]
                word = prefix + current_letter

                if self.__dictionary.is_word(word):
                    # newly formed string is a valid word
                    words.append(word)

                if self.__dictionary.is_path(word):
                    # newly formed string is a valid prefix
                    tiles_in_prefix['stack'].append(pos)
                    tiles_in_prefix['set'].add(pos)
                    words += self.__find_next_words(pos, word, tiles_in_prefix)

                    visited_position = tiles_in_prefix['stack'].pop()
                    tiles_in_prefix['set'].remove(visited_position)
        return words
