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
    solution = range(0, nodeCount)

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

def run_optimiser(output_directory: str,
                  input_file: str) -> None:
    
    """
    Function 'run_optimiser' runs through all steps requires through all required steps needed in optimise.py
    :param output_directory: team output directory
    :input_file: problem to optimise
    """
    input_file = "data/" + input_file
    if len(output_directory) != 16 or output_directory[:15]!='submission_team' or int(output_directory[15:]) not in range(1, 10):
        print("   - The directory of the submissions to evaluate (should be submission_teamX) with X in {1...9}")
        return None
    
    if input_file not in ["data/tsp_51", "data/tsp_1889", "data/tsp_33810"]:
        print(" - Input dataset (e.g. tsp_51) doesn't exist. Please check file name")
        return None

    solution = solve_tsp(input_file)

    write_solution(output_directory, input_file, solution)


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
