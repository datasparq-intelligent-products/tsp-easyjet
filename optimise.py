# ========================================================================================
# ========================================================================================
# ========================================================================================
# ========================================================================================
# ========================================================================================
# ============                                                       =====================
# ============                                                       =====================
# ============                                                       =====================
# ============       WARNING FOR SUBMISSIONS                         =====================
# ============       Please modify only the code for the             =====================
# ============       function "custom_heuristic"                     =====================
# ============                                                       =====================
# ============                                                       =====================
# ============                                                       =====================
# ========================================================================================
# ========================================================================================
# ========================================================================================
# ========================================================================================
# ========================================================================================

from collections import namedtuple
import math
import random
import sys
from typing import List
from tsp_utils import length, tour_cost, read_data, Point, write_solution
from scipy.spatial import KDTree
import numpy as np

def greedy_solution(points:List, nodeCount:int) -> List:
    # select closes 10 points
    init_point = 0

    tree = KDTree(points)
    current_loc = init_point
    solution = [init_point]
    points_remaining = set(range(nodeCount))
    points_remaining.remove(init_point)

    for z in range(nodeCount - 1):
        _, i_next = tree.query(points[current_loc], k=11)
        # Remove already taken points
        i_next = [i for i in i_next if i in points_remaining]
        if i_next:
            # calc dist. to 10 nearest points
            distances = [length(points[current_loc], points[i]) for i in i_next]

            distances[0] = 1000000000
            # min distance index
            min_idx = i_next[np.argmin(distances)]
        else:
            min_idx = random.sample(points_remaining, 1)[0]

        solution.append(min_idx)
        points_remaining.remove(min_idx)
        current_loc = min_idx

    return solution

def custom_heuristic(points: List) -> List:
    """
    This function is the core function to implement

    param: points: points to visit

    return: solution: sequence of point visits
    """

    # ===============================================
    # ===============================================
    # ====                           ================
    # ====    YOUR CODE GOES HERE    ================
    # ====                           ================
    # ===============================================
    # ===============================================

    # REPLACE THE TRIVIAL SOLUTION WITH YOUR HEURISTIC
    nodeCount = len(points)
    # solution = range(0, nodeCount)

    # initial solution
    init_soln = greedy_solution(points, nodeCount)

    # Return
    solution = init_soln
    return solution


# ========================================================================================
# =============                                                 ==========================
# =============     PLEASE DO NOT MODIFY CODE BELOW THIS LINE   ==========================
# =============                                                 ==========================
# ========================================================================================

def solve_tsp(input_file: str) -> List:
    """
    [PLEASE DO NOT MODIFY THE CODE IN THIS FUNCTION]

    This function runs the following steps
    - Read data (using read_data function from tsp_utils)
    - Runs custom heuristic as implemented by team 
    - Evaluates and prints out the cost of the solution

    """
    # Read data
    points = read_data(input_file)

    # Build solution using your custom heuristic
    solution = custom_heuristic(points)
    
    # Calculate cost of solution
    total_cost = tour_cost(solution, points)

    # prepare the solution in the specified output format
    print("Total cost: %.2f" % total_cost + "\n")
    print("Sequence \n" + " ".join(map(str, solution)))

    return solution


# ================================
# PLEASE DO NOT MODIFY THIS CODE
# ================================
if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Output directory
        output_directory = sys.argv[1].strip()

        # Read input file
        input_file = sys.argv[2].strip()

        # Run optimisation
        solution = solve_tsp(input_file)

        # Write output
        write_solution(output_directory, input_file, solution)

    else:
        print("")
        print("[INPUT ERROR] This script requires two arguments:")
        print("   - The directory to write the output (should be submission_teamX) with X in {1...9}")
        print("   - An input dataset (e.g. ./data/tsp_51)")
        print("Correct call format: $> python optimise.py submission_teamX ./data/tsp_51")
        print("")
