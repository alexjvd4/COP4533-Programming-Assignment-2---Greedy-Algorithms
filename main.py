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
    :return: cache capacity, requests list, number of requests
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

    return cache_capacity, requests, num_requests


def main():
    filename = input("Type the name of the txt file to use as input\n")
    cache_capacity, requests, num_requests = read_input_file(filename)


if __name__ == '__main__':
    main()
