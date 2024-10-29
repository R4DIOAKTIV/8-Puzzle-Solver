import heapq
import time
from utils import *

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
    cost_so_far = {start: 0}  # Tracks the lowest g cost to each state

    while frontier:
        currentNode = heapq.heappop(frontier)
        
        if currentNode.state == goal:
            path = []
            while currentNode:
                path.append(currentNode.state)
                currentNode = currentNode.parent
            t = time.time() - t
            return path[::-1], explored, t

        explored.add(currentNode.state)
        
        for childState in getChildren(currentNode.state):
            new_cost = currentNode.g + 1
            if childState not in explored or new_cost < cost_so_far.get(childState, float('inf')):
                cost_so_far[childState] = new_cost
                childNode = Node(childState, currentNode, new_cost, heuristic(childState))
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
