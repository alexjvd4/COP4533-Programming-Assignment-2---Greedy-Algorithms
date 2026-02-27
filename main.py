"""
COP4533 Algorithm Abstraction & Design Programming Assignment 2
Greedy Algorithms: Cache Eviction Policies

Main program main.py

Alejandro Velez
"""
import sys


def read_input_file(filename):
    """
    Reads the input file and obtains the cache capacity and the requests
    :param filename: An input filename string
    :return: cache capacity, requests list
    """
    with open(filename, "r") as f:
        line = f.readline()
        if line != '':
            cache_capacity = int(line[0])
            num_requests = int(line[2])
        else:
            print("ERROR: Empty input file.")
            sys.exit(0)
        line = f.readline()
        if line != '' and num_requests > 0:
            requests = []
            i = 0
            while i < len(line):
                requests.append(line[i])
                i += 2
            if num_requests != len(requests):
                print("ERROR: Incorrect number of requests provided.")
                sys.exit(0)
        else:
            print("ERROR: No requests provided.")
            sys.exit(0)

    return cache_capacity, requests


def fifo(cache):
    """
    First in first out cache eviction
    :param cache: Input cache list
    :return: Cache with first place item removed (element 0)
    """
    pass


def lru(cache):
    """
    Least recently used cache eviction
    :param cache: Input cache list
    :return: Cache with least recently used item removed
    """
    pass


def optff(cache):
    """
    Belady’s Farthest-in-Future, optimal offline
    :param cache: Input cache list
    :return: Cache after Belady's Farthest-in-Future, optimal offline is applied
    """
    pass


def eviction_selector(num, cache):
    """
    Selects the cache eviction policy based on the parameter
    :param cache: Input cache list
    :param num: Selects which eviction policy to use
    :return: Output of specified eviction policy
    """
    if num == 0:
        return fifo(cache)
    elif num == 1:
        return lru(cache)
    elif num == 2:
        return optff(cache)
    return None


def main():
    filename = input("Type the name of the txt file to use as input\n")
    cache_capacity, requests = read_input_file(filename)
    for i in range(3):
        cache = []
        for request in requests:
            if request in cache:
                print("Cache hit!\n")
            elif len(cache) < cache_capacity:
                cache.append(request)
                print("Cache miss!\n")
            else:
                eviction_selector(i, cache)
                print("Cache miss!\n")


if __name__ == '__main__':
    main()
