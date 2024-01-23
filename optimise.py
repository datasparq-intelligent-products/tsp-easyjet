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
from copy import deepcopy as dc
from sklearn.cluster import DBSCAN

# def get_radius(points):
#     min_x_coord = min(points, key=itemgetter(0))[0]
#     min_y_coord = min(points, key=itemgetter(1))[1]
#     max_x_coord = max(points, key=itemgetter(0))[0]
#     max_y_coord = max(points, key=itemgetter(1))[1]
#     radius = length(
#         Point(min_x_coord,min_y_coord),
#         Point(max_x_coord,max_y_coord)
#     )/2
#     return radius

def greedy_solution(points:List, nodeCount:int) -> List:
    # select closes 10 points
    init_point = 42

    tree = KDTree(points)
    current_loc = init_point
    solution = [init_point]
    points_remaining = set(range(nodeCount))
    points_remaining.remove(init_point)

    for z in range(nodeCount - 1):
        _, i_next = tree.query(points[current_loc], k=50)
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

def calc_dists(solution, points):
    nodeCount = len(solution)
    dist_list = [length(points[solution[-1]], points[solution[0]])]
    for index in range(0, nodeCount):
        dist_list.append(length(points[solution[index]], points[solution[index+1]]))

    return dist_list

# def cluster_points(points):
#     cluster_thresh = get_radius*0.1
#     min_points = len(points)*0.1
#     clustering = DBSCAN(eps = cluster_thresh, min_samples = min_points)
#     clustering.fit(X)
#     return clustering.labels_

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
    list_index = list(np.arange(0, nodeCount+1))

    # initial solution
    init_soln = greedy_solution(points, nodeCount)

    #Best solution
    best_solution = dc(init_soln)
    best_tour_cost = tour_cost(init_soln, points)

    # Cluster into subproblems
    cluster_dict = {c: list_index[c*20:(c*20)+20] for c in range(int(nodeCount/20)+1)}
    # print(cluster_dict)

    for iter in range(10):
        # len current solution
        travel_dists = calc_dists(best_solution, points)

        # Remove insert heuristics
        # select random cluster
        clust = random.sample(cluster_dict.keys(), 1)[0]

        # Distances to arrive at nodes in our cluster
        dist_for_nodes_in_clust = {i: travel_dists[i] for i in cluster_dict[clust]}
        node_in_clust_max_dist_to = max(dist_for_nodes_in_clust, key=dist_for_nodes_in_clust.get)

        for clust_node in cluster_dict[clust]:
            solution_tmp = dc(best_solution)
            solution_tmp = [n for n in solution_tmp if n != clust_node]
            solution_tmp = solution_tmp[:node_in_clust_max_dist_to] + [clust_node] + solution_tmp[node_in_clust_max_dist_to:]
            len_solution_tmp = tour_cost(solution_tmp, points)
            if len_solution_tmp < best_tour_cost:
                best_solution = solution_tmp


    return best_solution



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
