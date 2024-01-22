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
import time
import numpy as np
from typing import List
from tsp_utils import length, tour_cost, read_data, Point, write_solution, trivial_solution


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

    #########################################
    # Initial solution
    #########################################

    # Get the initial solution
    initial_tour = list(trivial_solution(points))

    #########################################
    # Local search
    #########################################

    # algorithm for swapping two edges
    def swap(i, j, tour):
        """
        swap two edges in a tour
        """
        updated_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
        return updated_tour

    def quasi_two_opt(initial_tour,
                max_time,
                alpha = 0.9975,
                T = 100,
                SA = False):
        # Setup
        n = len(initial_tour)
        best_tour = initial_tour
        start_time = time.perf_counter()

        # current best tour (i.e. initial tour)
        i = 0
        best_edge_1 = length(points[best_tour[(i - 1) % n]], points[best_tour[i]])
        best_edge_2 = length(points[best_tour[(i+2)]], points[best_tour[((i+2)+1) % n]])
        best_local_dist = best_edge_1 + best_edge_2

        # run the 2-opt algorithm with the swap fn
        count = 0
        for i in range(0, n - 2):
            for j in range(i + 2, n):
                # proposed new tour with swap
                updated_tour = swap(i, j, best_tour)
                updated_tour_edge_1 = length(points[updated_tour[(i - 1) % n]], points[updated_tour[i]])
                updated_tour_edge_2 = length(points[updated_tour[j]], points[updated_tour[(j + 1) % n]])
                update_tour_local_dist = updated_tour_edge_1 + updated_tour_edge_2

                # keep the best tour
                diff = update_tour_local_dist - best_local_dist
                if diff < 0:
                    best_tour = updated_tour
                    best_local_dist = update_tour_local_dist
                # if it's just as good flip a coin as to which one you take
                elif diff == 0:
                    coin_toss = np.random.binomial(n=1, p=0.5)
                    if coin_toss < 1:
                        best_tour = updated_tour
                        best_local_dist = update_tour_local_dist
                # if it's a worse tour (pos diff), we may still accept it if conducting simulating annealing
                elif SA and diff > 0:
                    T = alpha * T
                    random_point = np.random.uniform()
                    prob = np.exp(-diff / T)
                    if prob >= random_point:
                        best_tour = updated_tour
                        best_local_dist = update_tour_local_dist

                # Stop the algorithm if it's taking too long (note time is in seconds)
                elapsed_time = time.perf_counter() - start_time
                if elapsed_time > max_time and (i+1)/(n-2) < 0.8:
                    print("Stopping...")
                    print("Exceed maximum time allowed to run")
                    print(f"got through roughly:{(i+1)/(n-2):.2%}")
                    return best_tour

        return best_tour


    solution = quasi_two_opt(initial_tour = initial_tour,
                             max_time = 1*120,
                             alpha = 0.9975,
                             T = 100,
                             SA = False)

    # Return
    return solution


# ========================================================================================
# =============                                                 ==========================
# =============     PLEASE DO NOT MODIFY CODE BELOW THIS LINE   ==========================
# =============                                                 ==========================
# =========================================================z===============================

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
