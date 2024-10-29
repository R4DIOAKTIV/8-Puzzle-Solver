import math
import numpy as np

def calculateManhattan(state):
    # Could be removed if we choose to represent the state as a 2D array
    state_2d = [list(state[i:i+3]) for i in range(0, len(state), 3)]
    
    goal = "012345678"
    manhattan = 0
    for i in range(3):
        for j in range(3):
            if state_2d[i][j] != "0":  # Skip the blank tile
                goalIndex = goal.index(state_2d[i][j])
                goalRow = goalIndex // 3
                goalCol = goalIndex % 3
                manhattan += abs(i - goalRow) + abs(j - goalCol)
    return manhattan

def calculateEuclidean(state):
    # Could be removed if we choose to represent the state as a 2D array
    state_2d = [list(state[i:i+3]) for i in range(0, len(state), 3)]
    
    goal = "012345678"
    euclidean = 0
    for i in range(3):
        for j in range(3):
            if state_2d[i][j] != "0":  # Skip the blank tile
                goalIndex = goal.index(state_2d[i][j])
                goalRow = goalIndex // 3
                goalCol = goalIndex % 3
                euclidean += math.sqrt((i - goalRow)**2 + (j - goalCol)**2)
    return euclidean

def getChildren(state):
    # Could be removed if we choose to represent the state as a 2D array
    state_2d = [list(state[i:i+3]) for i in range(0, len(state), 3)]

    blankRow, blankCol = next((i, j) for i in range(3) for j in range(3) if state_2d[i][j] == "0")
    
    children = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dr, dc in moves:
        newRow, newCol = blankRow + dr, blankCol + dc
        if 0 <= newRow < 3 and 0 <= newCol < 3:
            # Copy the current state and swap the blank with the target
            child = [row[:] for row in state_2d]
            child[blankRow][blankCol], child[newRow][newCol] = child[newRow][newCol], child[blankRow][blankCol]
            # Append the flattened state as a string
            children.append("".join("".join(row) for row in child))
    
    return children