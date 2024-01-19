# Databricks notebook source
from collections import namedtuple
import math
import random
import sys
from optimise import run_optimiser
from tsp_utils import tour_cost, read_data

# COMMAND ----------

TEAM_NAME = 'submission_teamX'

# COMMAND ----------

run_optimiser('TEAM_NAME',
              'tsp_50')

# COMMAND ----------

team_directory = 'submission_team1'

#===============================================
# READ AND EVALUATE SUBMISSIONS
#===============================================
problems = ["tsp_51", "tsp_1889", "tsp_33810"]

for problem in problems:
    # Read submission
    solution = []
    try:
        with open(f"{TEAM_NAME}/sequence_{problem}") as f:
            lines = f.readlines()
            for line in lines:
                solution.append(int(line.strip()))
            
                # Evaluate submission
        points = read_data("data/" + problem)
        total_cost = tour_cost(solution, points)
        print(f"Total cost for {problem}: %.4e" % total_cost)
                
    except:
        print(f"No data for {team_directory}/sequence_{problem}")
