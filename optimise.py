from collections import namedtuple
import math
import random
import sys
from typing import List

Point = namedtuple("Point", ['x', 'y'])

def length(point1: Point, point2: Point) -> float:
    """
    This function calculates the distance between points point1 and point2

    param: point1: point 1
    param: point2: point 2
    
    return: Euclidean distance between point1 and point2
    """

    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def tour_cost(solution: List, points: List) -> float:
    """
    This function calculates the cost of a tour, this is the cost of visiting a set of
    points in the given order

    param: points: list of Point objects

    return: cost of tour as sum of distances between consecutive points
    """

    # calculate the length of the tour
    nodeCount = len(solution)
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])
    
    return obj

def read_data(file_location: str) -> List:
    """
    This function reads the input data using the specified location

    param: file_location: relative path where the input is stored
    return: list of points
    """
    
    input_data_file = open(file_location, 'r')
    input_data = input_data_file.read()

    # parse the input
    lines = input_data.split('\n')
    
    # Read number of points
    nodeCount = int(lines[0])
    
    # Ingest points
    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))

    # Return
    return points

def trivial_solution(points: List) -> List:
    """
    This function builds a trivial solution for the points to visit

    param: points: list of points to visit

    return: trivial solution, initial sequence
    """

    # build a trivial solution
    # visit the nodes in the order they appear in the file
    nodeCount = len(points)
    solution = range(0, nodeCount)

    # Return
    return solution

def custom_heuristic(points: List) -> List:
    """
    This function is the core function to implement

    param: points: points to visit

    return: solution: sequence of point visits
    """

    #===============================================
    #===============================================
    #====                           ================
    #====    YOUR CODE GOES HERE    ================
    #====                           ================
    #===============================================
    #===============================================

    # REPLACE THE TRIVIAL SOLUTION WITH YOUR HEURISTIC
    nodeCount = len(points)
    solution = range(0, nodeCount)

    # Return
    return solution
    
    
def solve_tsp(file_location):
    """

    """
    # Read data
    points = read_data(file_location)

    # Build solution using trivial solution
    # Replace this function with a call to custom_heuristic once you have implemented your improved algorithm
    solution = trivial_solution(points)
    
    # Calculate cost of solution
    total_cost = tour_cost(solution, points)

    # prepare the solution in the specified output format
    print("Total cost: %.2f" % total_cost + "\n")
    print("Sequence \n" + " ".join(map(str, solution)))

    return solution



if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        solve_tsp(file_location)
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51)')

