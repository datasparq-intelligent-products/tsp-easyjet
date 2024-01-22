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
from scipy.spatial import distance_matrix
import pandas as pd


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

    # Calculate distance matrix
    distance_matrix_df = pd.DataFrame(columns=['x', 'y'])
    for i, point in enumerate(points):
        distance_matrix_df.loc[i] = point.x, point.y

    distances = pd.DataFrame(distance_matrix(distance_matrix_df.values, distance_matrix_df.values), index=distance_matrix_df.index, columns=distance_matrix_df.index)

    # Initial greedy solution
    solution = []
    start_point = random.randint(0, nodeCount)
    solution.append(start_point)
    for i in range(nodeCount - 1):
        min_distance_index = distances[[x for x in list(distances) if x not in solution]].loc[solution[-1]].idxmin()
        solution.append(min_distance_index)

    best_solution = solution
    best_solution_cost = tour_cost(solution, points)

    # Large swaps
    for i in range(50):
        
        num_points = random.randint(1, int(nodeCount/5))
        b = random.randint(num_points, int(nodeCount/2))
        a = b-num_points
        c = random.randint(int(nodeCount/2), nodeCount-num_points)
        d = c + num_points
    
        solution[a:b], solution[c:d] = solution[c:d], solution[a:b]

        solution_cost = tour_cost(solution, points)

        if solution_cost < best_solution_cost:
            best_solution = solution
            best_solution_cost = solution_cost
    

    # solution = list(solution)
    # random.shuffle(solution)
    # solution[1], solution[0] = solution[0], solution[1]
    # solution[21], solution[50] = solution[50], solution[21]

    # Return
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
