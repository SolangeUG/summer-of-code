#!/usr/bin/env python3

import random
import time

# Global variables
tiles_queue = []


def generate_random_world(n):
    """
    Randomly generate a world of size n
    :param n: desired size for the world to be generated
    :return: a randomly generated world
    """
    random_world = [[0] * n for x in range(n)]
    for i in range(n):
        for j in range(n):
            value = random.randint(0, 1)
            random_world[i][j] = value
    return random_world


def get_two_largest_continents(grid):
    """
    Given a world, determine its two largest continents
    :param grid: input world
    :return: a dictionary associating the two largest continents with their sizes
    """
    continents = compute_all_continents_sizes(grid)
    largest = sorted(continents.items(), key=lambda kv: kv[1], reverse=True)
    if len(largest) > 2:
        largest = largest[0:2]
    return dict(largest)


def compute_all_continents_sizes(grid):
    """
    Given a world, compute all its continents sizes
    :param grid: given world
    :return: a dictionary that associates each continent with its size
    """
    counter = 0
    result = {}
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                counter += 1
                size = get_continent_size(grid, list((i, j)))
                result['continent ' + str(counter)] = size
    return result


def get_continent_size(grid, start):
    """
    Return the size of the continent which the start tile is part of
    :param grid: given world that contains the start position
    :param start: given starting position/tile is an array of indexes
    :return: the continent size around the input tile
    """
    size = 0
    n = len(grid)
    # make sure the starting position is within the grid/world bounds
    if (start[0] >= 0) and (start[0] < n) \
            and (start[1] >= 0) and (start[1] < n):
        tiles_queue.append(start)
        while len(tiles_queue) > 0:
            tile = tiles_queue.pop(0)
            i = tile[0]
            j = tile[1]
            if grid[i][j] == 1:
                size += 1
                # mark this element as "already treated"
                grid[i][j] = 0
                check_neighbours(grid, tile)
    return size


def check_neighbours(grid, tile):
    """
    Check if the neighbouring tiles have a desired value (1 in this case)
    and add them to our global variable tiles_queue
    :param grid: input world that contains the tile in question
    :param tile: input tile as an array of indexes
    :return: None
    """
    x = tile[0]
    y = tile[1]
    n = len(grid)
    for i in range(x - 1, x + 2):
        if (i >= 0) and (i < n):
            for j in range(y - 1, y + 2):
                if (j >= 0) and (j < n):
                    if grid[i][j] == 1:
                        tiles_queue.append(list((i, j)))


def print_grid(grid):
    """
    Print the given grid in a readable form
    :param grid: input grid/world to be printed
    """
    print('[')
    for row in grid:
        print('\t', row, ',')
    print(']')


def program_benchmark(n):
    """
    Benchmark computing all the continents sizes of a randomly generated world
    :param n: size of world to be generated
    :return: average running time of our program run 1000 times
    """
    total_time = 0
    iterations = 1000
    for i in range(iterations):
        start = time.process_time()
        grid = generate_random_world(n)
        compute_all_continents_sizes(grid)
        total_time += time.process_time() - start
    return total_time/iterations


if __name__ == '__main__':
    """
    Main
    """
    print()
    world_size = input('Enter valid number for size of world to generate: ')
    while not world_size.isdigit():
        world_size = input('Enter valid number for size of world to generate: ')
    world_size = int(world_size)

    world = generate_random_world(world_size)
    # uncomment the following line to display randomly generated world
    # print_grid(world)
    largest_continents = get_two_largest_continents(world)
    print('Largest continents sizes:', largest_continents)

    # benchmark: measure average time taken by program to run over a thousand iterations
    average_running_time = program_benchmark(world_size)
    print('Average program running time (in seconds):', "{:10.20f}".format(average_running_time))
