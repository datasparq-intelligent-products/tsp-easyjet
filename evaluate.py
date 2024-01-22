#========================================================================================
#========================================================================================
#========================================================================================
#========================================================================================
#========================================================================================
#============                                                       =====================
#============                                                       =====================
#============                                                       =====================
#============       PLEASE DO NOT MODIFY THIS FILE                  =====================
#============       YOU CAN USE IT TO EVALUATE YOUR SUBMISSIONS     =====================
#============                                                       =====================
#============                                                       =====================
#============                                                       =====================
#========================================================================================
#========================================================================================
#========================================================================================
#========================================================================================
#========================================================================================
import sys
from typing import List
from tsp_utils import length, tour_cost, read_data, Point, write_solution


if __name__ == "__main__":
    if len(sys.argv) == 2:
        # team directory
        team_directory = sys.argv[1].strip()

        #===============================================
        # READ AND EVALUATE SUBMISSIONS
        #===============================================
        problems = ["tsp_51", "tsp_1889", "tsp_33810"]

        for problem in problems:

            # Read submission
            solution = []
            try:
                with open(f"{team_directory}/sequence_{problem}") as f:
                    lines = f.readlines()
                    for line in lines:
                        solution.append(int(line.strip()))
            
                # Evaluate submission
                points = read_data("data/" + problem)
                total_cost = tour_cost(solution, points)
                assert(len(set(solution)) == len(solution))
                print(f"Total cost for {problem}: %.4e" % total_cost)
                
            except FileNotFoundError:
                print(f"No data for {team_directory}/sequence_{problem}")
            except AssertionError:
                print(f"Invalid solution: check that each location appears once and only once")
        
    else:
        print("")
        print("[INPUT ERROR] This script requires a single argument:")
        print("   - The directory of the submissions to evaluate (should be submission_teamX) with X in {1...9}")
        print("Correct call format: $> python evaluate.py submission_teamX")
        print("")
