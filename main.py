"""
COP4533 Algorithm Abstraction & Design Programming Assignment 2
Greedy Algorithms: Cache Eviction Policies

Main program main.py

Alejandro Velez & Marco Fernandez
"""
import sys


def read_input_file(filename):
    """
    Reads the input file and obtains the cache capacity and the requests
    :param filename: An input filename string
    :return: cache capacity, requests list
    """
    with open(filename, "r") as f:
        line = f.readline().strip()
        if line != '':
            cache_capacity, num_requests = map(int, line.split())
        else:
            print("ERROR: Empty input file.")
            sys.exit(0)
        line = f.readline().strip()
        if line != '' and num_requests > 0:
            requests = list(map(int, line.split()))
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
    Will evict a number that never occurs again before a request that exists far in the future
    :param requests: List of requests, earliest at index 0
    :param cache: Input cache list
    :return: Cache after Belady's Farthest-in-Future, optimal offline is applied
    """
    if len(cache) > 0:
        farthest = -1
        num_to_remove = cache[0]

        for num in cache:
            if num not in requests:
                num_to_remove = num
                break

            next_use = requests.index(num)

            if next_use > farthest:
                farthest = next_use
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
        for index, request in enumerate(requests):
            if request in cache:
                if i == 1:
                    cache.remove(request)
                    cache.append(request)
            elif len(cache) < cache_capacity:
                if i == 0:
                    fifo_misses += 1
                elif i == 1:
                    lru_misses += 1
                elif i == 2:
                    optff_misses += 1
                cache.append(request)
            else:
                cache = eviction_selector(i, cache, requests[index + 1:])
                if i == 0:
                    fifo_misses += 1
                elif i == 1:
                    lru_misses += 1
                elif i == 2:
                    optff_misses += 1
                cache.append(request)

    # Output handling
    result_text = (
        "\nFIFO  : " + str(fifo_misses) + "\n" +
        "LRU   : " + str(lru_misses) + "\n" +
        "OPTFF : " + str(optff_misses) + "\n"
    )

    print(result_text)

    with open("output.txt", "w") as out_file:
        out_file.write(result_text)

    print("Results have been written to output.txt")


if __name__ == '__main__':
    main()
