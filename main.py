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
    if len(cache) > 0:
        cache.pop(0)
    return cache


def lru(cache):
    """
    Least recently used cache eviction
    :param cache: Input cache list
    :return: Cache with least recently used item removed
    """
    if len(cache) > 0:
        cache.pop(0)
    return cache


def optff(cache, requests):
    """
    Belady’s Farthest-in-Future, optimal offline
    :param requests: List of requests, earliest at index 0
    :param cache: Input cache list
    :return: Cache after Belady's Farthest-in-Future, optimal offline is applied
    """
    index = 0
    num_to_remove = 0
    for num in cache:
        if num not in requests:
            cache.remove(num)
            return cache
        elif index < requests.index(num):
            index = requests.index(num)
            num_to_remove = num
    cache.remove(num_to_remove)
    return cache


def eviction_selector(num, cache, requests):
    """
    Selects the cache eviction policy based on the parameter
    :param requests: Incoming requests list
    :param cache: Input cache list
    :param num: Selects which eviction policy to use
    :return: Output of specified eviction policy
    """
    if num == 0:
        return fifo(cache)
    elif num == 1:
        return lru(cache)
    elif num == 2:
        return optff(cache, requests)
    return cache


def main():
    # Input handling
    filename = input("Type the name of the txt file to use as input\n")
    cache_capacity, requests = read_input_file(filename)

    # Begin cache insertion and eviction process
    fifo_misses = 0
    lru_misses = 0
    optff_misses = 0
    for i in range(3):
        cache = []
        for request in requests:
            if request in cache:
                print("Cache hit!\n")
            elif len(cache) < cache_capacity:
                cache.append(request)
                print("Cache miss!\n")
            else:
                cache = eviction_selector(i, cache, requests)
                if i == 0:
                    fifo_misses += 1
                elif i == 1:
                    lru_misses += 1
                elif i == 2:
                    optff_misses += 1
                cache.append(request)
                print("Cache miss! Eviction taking place!\n")

    # Output handling
    print("FIFO : "+ str(fifo_misses))
    print("LRU : "+ str(lru_misses))
    print("OPTFF : " + str(optff_misses))


if __name__ == '__main__':
    main()
