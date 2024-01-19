# Databricks notebook source
import os

# COMMAND ----------

#====================================================
# SET YOUR TEAM NUMBER AND RUN THE OPTIMISATION
#====================================================
TEAM_NUMBER = 0

"""
Script optimise.py requires two arguments:
   - The directory to write the output (should be submission_teamX) with X in {1...9}
   - An input dataset (e.g. ./data/tsp_51)
Correct call format: $> python optimise.py submission_teamX ./data/tsp_51
"""

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

os.system(f"python evaluate.py submission_team{TEAM_NUMBER} > submission_team{TEAM_NUMBER}/log_evaluate 2>&1")

# COMMAND ----------


