# tsp-easyjet
Travelling Salesman Problem (TSP) repository for the hackathon easyJet + Datasparq

# Datasets
The folder `data/` contains three files:
- `tsp_51`
- `tsp_1889`
- `tsp_33810`

Each of these files correspond to a different TSP. 

# Input format
The files in `data/` are formatted as follows:
- First line contains an integer N that indicates the number of locations of the TSP
- Following N lines correspond to a position `(x_n, y_n)` in the plane for location `n`

# Hackathon

## Objective
The objective of the hackathon is to write a piece of code that implements a solution to the TSP.
In particular, we would like each team to implement the function `custom_heuristic` in the file `optimise.py`.

## Implementing your solution
To generate a sequence you need to implement a heuristic or set of heuristics 
in the function `custom_heuristic` in `optimise.py`.

Please branch off from `main` and name your branch `teamX`, with X your team number.
You can modify the code and push your implementation and solutions to that branch.

## Submissions
Each team should submit a solution for each of the TSP above. 
Note that trivial solutions for a non-existent Team 0 have already been submitted. 

We will evaluate one submission per problem per team with the following names:
- `tsp_51 -> sequence_tsp_51`
- `tsp_1889 -> sequence_tsp_1889`
- `tsp_33810 -> sequence_tsp_33810`

Any submission with another name will not be evaluated. Note that by running

`python optimise.py submission_teamX data/tsp_51`

you can generate the sequence for `tsp_51` in your corresponding folder. 

## Evaluation

You can test your code and evaluate your submissions using this call:

`python evaluate submission_teamX`

The **total cost** for each sequence is what we will use for the final classification.

---
#### ABOUT THIS CODE
This code has been partially developed for the Travelling Salesman Problem hackathon
between Datasparq and easyJet. 
The original code is part of the Coursera course "Discrete Optimization", which can be found here: https://www.coursera.org/learn/discrete-optimization

Author: Kiko Rul.lan
