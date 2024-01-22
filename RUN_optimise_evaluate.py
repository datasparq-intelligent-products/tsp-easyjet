# Databricks notebook source
import os

# COMMAND ----------

#====================================================
# SET YOUR TEAM NUMBER AND RUN THE OPTIMISATION
#====================================================
TEAM_NUMBER = 1

"""
Script optimise.py requires two arguments:
   - The directory to write the output (should be submission_teamX) with X in {1...9}
   - An input dataset (e.g. ./data/tsp_51)
Correct call format: $> python optimise.py submission_teamX ./data/tsp_51
"""

# COMMAND ----------

# from sklearn.cluster import DBSCAN

# clustering = DBSCAN(eps = cluster_thresh, min_samples = len(coord_list*0.1))
# clustering.fit(X)
# clustering.labels_

# COMMAND ----------

# MAGIC %md
# MAGIC # Optimise

# COMMAND ----------

# Run optimiser - TSP 51
os.system(f"python optimise.py submission_team{TEAM_NUMBER} data/tsp_51 > submission_team{TEAM_NUMBER}/log_tsp_51 2>&1")

# COMMAND ----------

# Run optimiser - TSP 1889
os.system(f"python optimise.py submission_team{TEAM_NUMBER} data/tsp_1889 > submission_team{TEAM_NUMBER}/log_tsp_1889 2>&1")

# COMMAND ----------

# Run optimiser - TSP 33810
os.system(f"python optimise.py submission_team{TEAM_NUMBER} data/tsp_33810 > submission_team{TEAM_NUMBER}/log_tsp_33810 2>&1")

# COMMAND ----------

# MAGIC %md
# MAGIC # Evaluate

# COMMAND ----------

# from tsp_utils import length, tour_cost, read_data, Point, write_solution

# points = read_data('/Workspace/Repos/Matthew.Carr@easyjet.com/tsp-easyjet/data/tsp_1889')

# points

# COMMAND ----------

# # works for 1889
# clustering = cluster_points(points, 0.05, 0.01)
# set(clustering.labels_)

# # clustering = cluster_points(points, 0.05, 0.01)
# # set(clustering.labels_)

# COMMAND ----------

# clustering.labels_

# COMMAND ----------

# set(clustering.labels_)

# COMMAND ----------

# round(len(points)*0.01)

# COMMAND ----------

# from operator import itemgetter

# print(max(points, key=itemgetter(0))) 
# print(max(points, key=itemgetter(1)) )

# COMMAND ----------

# from collections import namedtuple

# mid_x = (max(points, key=itemgetter(0))[0] - min(points, key=itemgetter(0))[0])/2 + min(points, key=itemgetter(0))[0]

# mid_y = (max(points, key=itemgetter(1))[1] - min(points, key=itemgetter(1))[1])/2 + min(points, key=itemgetter(1))[1]

# Point = namedtuple("Point", ['x', 'y'])

# Point(mid_x, mid_y)

# COMMAND ----------

# from collections import namedtuple

# mid_x = (max(points, key=itemgetter(0))[0] - min(points, key=itemgetter(0))[0])/2 + min(points, key=itemgetter(0))[0]

# mid_y = (max(points, key=itemgetter(1))[1] - min(points, key=itemgetter(1))[1])/2 + min(points, key=itemgetter(1))[1]

# Point = namedtuple("Point", ['x', 'y'])

# Point(mid_x, mid_y)

# COMMAND ----------

# import math
# def length(point1: Point, point2: Point) -> float:
#     """
#     [PLEASE DO NOT MODIFY THE CODE IN THIS FUNCTION]
#     This function calculates the distance between points point1 and point2

#     param: point1: point 1
#     param: point2: point 2
    
#     return: Euclidean distance between point1 and point2
#     """

#     return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    
# length(Point(min(points, key=itemgetter(0))[0],min(points, key=itemgetter(1))[1]),
#     Point(max(points, key=itemgetter(0))[0],max(points, key=itemgetter(1))[1]))/2

# COMMAND ----------

# from operator import itemgetter

# print(min(points, key=itemgetter(0))) 
# print(min(points, key=itemgetter(1)) )

# COMMAND ----------

os.system(f"python evaluate.py submission_team{TEAM_NUMBER} > submission_team{TEAM_NUMBER}/log_evaluate 2>&1")

# COMMAND ----------


