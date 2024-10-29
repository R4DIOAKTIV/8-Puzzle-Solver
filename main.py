import heapq
import numpy as np
from utils import *
import time

class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(self.state)
    
    def __str__(self):
        return f"Node({self.state}, {self.f})"
    
    def __repr__(self):
        return str(self)
    
def aStar(start, goal, heuristic):
    t = time.time()
    startNode = Node(start, None, 0, heuristic(start))
    frontier = [startNode]
    explored = set()
    
    while frontier:
        currentNode = heapq.heappop(frontier)
        explored.add(currentNode.state)
        # print(f"Exploring {currentNode}")
        
        if currentNode.state == goal:
            path = [currentNode.state]
            while currentNode.parent:
                path.append(currentNode.parent.state)
                currentNode = currentNode.parent
            t = time.time() - t
            return path[::-1], explored, t
        
        for childState in getChildren(currentNode.state):
            if childState not in explored:
                childNode = Node(childState, currentNode, currentNode.g + 1, heuristic(childState))
                if childNode not in frontier:
                    heapq.heappush(frontier, childNode)
    return None

if __name__ == "__main__":
    start = "702853614"
    goal = "012345678"

    manhattanPath, explored, t = aStar(start, goal, calculateManhattan)
    print(f"Manhattan path: {manhattanPath}")
    print(f"Length of Manhattan path: {len(manhattanPath) - 1}")
    print(f"number of nodes explored: {len(explored)}")
    print(f"time taken: {t}")

