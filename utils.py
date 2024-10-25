import math
import numpy as np

def calculateManhattan(state):
    goal = "012345678"
    manhattan = 0
    state_2d = [list(state[i:i+3]) for i in range(0, len(state), 3)]
    print(state_2d)
    for i in range(3):
        for j in range(3):
            if state_2d[i][j] != "0":  # Skip the blank tile
                goalIndex = goal.index(state_2d[i][j])
                goalRow = goalIndex // 3
                goalCol = goalIndex % 3
                manhattan += abs(i - goalRow) + abs(j - goalCol)
    return manhattan

def calculateEuclidean(state):
    goal = "012345678"
    euclidean = 0
    state_2d = [list(state[i:i+3]) for i in range(0, len(state), 3)]
    for i in range(3):
        for j in range(3):
            if state_2d[i][j] != "0":  # Skip the blank tile
                goalIndex = goal.index(state_2d[i][j])
                goalRow = goalIndex // 3
                goalCol = goalIndex % 3
                euclidean += math.sqrt((i - goalRow)**2 + (j - goalCol)**2)
    return euclidean