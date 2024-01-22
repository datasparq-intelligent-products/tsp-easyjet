# Databricks notebook source


# COMMAND ----------

from itertools import permutations


def total_distance(perm, distance_matrix):
    distance = 0
    for i in range(len(perm)):
        distance += distance_matrix[perm[i]][perm[(i + 1) % len(perm)]]
    return distance

def tsp_brute_force(cities, distance_matrix):
    shortest_distance = float('inf')
    shortest_path = None
    for perm in permutations(cities):
        current_distance = total_distance(perm, distance_matrix)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = perm
    return shortest_path, shortest_distance

# Example usage
cities = [0, 1, 2, 3]
distance_matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(tsp_brute_force(cities, distance_matrix))

# COMMAND ----------

### Import data

from tsp_utils import read_data

