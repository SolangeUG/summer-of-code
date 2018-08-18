#!/usr/bin/env python3

import time
from board import Board
from solver import Solver
from dictionary import Dictionary


def benchmarking(board_size: int, dice_distribution: dict, dictionary: Dictionary):
    """
    Find average time taken to find all valid (given by dictionary) in a standard Boggle board game
    :param board_size: size of the board
    :param dice_distribution: dice distribution
    :param dictionary: Boggle dictionary
    :return: average time taken by the Boggle solver to compute all valid words and the total game score
    """
    total_time = 0
    computations_count = 100
    for i in range(computations_count):
        # initialize a board and its solver
        boggle_board = Board(board_size, dice_distribution)
        boggle_solver = Solver(boggle_board, dictionary)
        
        start_time = time.time()
        algorithm_run_count = 10
        for j in range(algorithm_run_count):
            boggle_solver.get_words()
        end_time = time.time()
        duration = end_time - start_time
        # average time taken by the algorithm
        total_time = total_time + (duration / algorithm_run_count)
        
    avg = total_time / computations_count
    return avg
   
   
def main():
    """
    Program entry point to get the boggle solver started
    :return: Boogle game score
    """
    # create and initialize our dictionary
    filename = 'dictionary.txt'
    boggle_dictionary = Dictionary(filename)

    # create and initialize our board
    board_size = 4
    distribution = {
        0: 'AAEEGN',
        1: 'ELRTTY',
        2: 'AOOTTW',
        3: 'ABBJOO',
        4: 'EHRTVW',
        5: 'CIMOTU',
        6: 'DISTTY',
        7: 'EIOSST',
        8: 'DELRVY',
        9: 'ACHOPS',
        10: 'HIMNQU',
        11: 'EEINSU',
        12: 'EEGHNW',
        13: 'AFFKPS',
        14: 'HLNNRZ',
        15: 'DEILRX'
    }
    boggle_board = Board(board_size, distribution)

    # create and initialize our solver
    boggle_solver = Solver(boggle_board, boggle_dictionary)

    print('Boggle board after shuffle:')
    for row in boggle_board.get_board():
        print(row)
    
    print('\nAll valid words found on the board:')
    word_list = boggle_solver.get_words()
    for word in word_list:
        print(word)
    
    # create result object
    result = dict()
    result['score'] = boggle_solver.get_score()
    result['words'] = sorted(word_list)
    print('\nResult object:')
    print(result)

    # benchmarking
    print('\nAverage time taken to find words on a standard Boggle board is:')
    print(benchmarking(board_size, distribution, boggle_dictionary), 'seconds')

    return result


if __name__ == '__main__':
    main()
