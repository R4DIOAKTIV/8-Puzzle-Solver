import heapq
import time
from utils import *
from queue import Queue
import matplotlib.pyplot as plt

class Node:
    __slots__ = ('state', 'parent', 'g', 'h', 'f')  # Limits instance attributes, saves memory
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f
    
    def __hash__(self):
        return hash(self.state)
    
def aStar(start, goal, heuristic):
    t = time.time()
    startNode = Node(start, None, 0, heuristic(start))
    frontier = []
    heapq.heappush(frontier, startNode)
    explored = set()
    cost_so_far = {start: 0}  # Tracks the lowest g cost to each state
    max_depth = 0

    while frontier:
        currentNode = heapq.heappop(frontier)
        
        if currentNode.g > max_depth:
            max_depth = currentNode.g

        if currentNode.state == goal:
            path = []
            while currentNode:
                path.append(currentNode.state)
                currentNode = currentNode.parent
            t = time.time() - t
            return path[::-1], explored, t, max_depth

        explored.add(currentNode.state)
        
        for childState in getChildren(currentNode.state):
            new_cost = currentNode.g + 1  # Assuming uniform cost for simplicity
            if childState not in explored and childState not in cost_so_far:
                cost_so_far[childState] = new_cost
                childNode = Node(childState, currentNode, new_cost, heuristic(childState))
                heapq.heappush(frontier, childNode)
            
            elif childState in cost_so_far and new_cost < cost_so_far[childState]:
                cost_so_far[childState] = new_cost
                childNode = Node(childState, currentNode, new_cost, heuristic(childState))
                heapq.heappush(frontier, childNode)
    return None, explored, time.time() - t, max_depth
                
def BFS(start, goal):
    t = time.time()  # Start time

    startNode = Node(start, None, 0)
    frontier = Queue()
    frontier.put(startNode)
    explored = set()
    frontier_set = {start}
    max_depth = 0

    while not frontier.empty():
        currentNode = frontier.get()
        frontier_set.remove(currentNode.state)
        explored.add(currentNode.state)

        if currentNode.g > max_depth:
            max_depth = currentNode.g

        if currentNode.state == goal:
            path = []
            while currentNode:
                path.append(currentNode.state)
                currentNode = currentNode.parent
            t = time.time() - t
            return path[::-1], explored, t, max_depth

        for childState in getChildren(currentNode.state):
            if childState not in explored and childState not in frontier_set:
                childNode = Node(childState, currentNode, currentNode.g + 1)    
                frontier.put(childNode)
                frontier_set.add(childState)
    
    return None, explored, time.time() - t, max_depth

def DFS(start, goal):
    t = time.time()  # Start time

    startNode = Node(start, None)
    frontier = [startNode]
    explored = set()
    frontier_set = {start}  # Track nodes currently in frontier
    max_depth = 0

    while frontier:
        currentNode = frontier.pop()
        frontier_set.remove(currentNode.state)
        explored.add(currentNode.state)

        if currentNode.g > max_depth:
            max_depth = currentNode.g

        if currentNode.state == goal:
            path = []
            while currentNode:
                path.append(currentNode.state)
                currentNode = currentNode.parent
            t = time.time() - t
            return path[::-1], explored, t, max_depth

        for childState in getChildren(currentNode.state):
            if childState not in explored and childState not in frontier_set:
                childNode = Node(childState, currentNode, currentNode.g + 1) 
                frontier.append(childNode)
                frontier_set.add(childState)
    return None, explored, time.time() - t, max_depth

def DLS(start, goal, limit):
    t = time.time()
    startNode = Node(start, None, 0, 0)
    frontier = [(startNode, 0)]
    explored = set()
    max_depth = 0
    frontier_set = {start}  # Track nodes currently in frontier

    while frontier:
        currentNode, depth = frontier.pop()
        frontier_set.remove(currentNode.state)
        explored.add(currentNode.state)
        if depth > limit:
            continue
        if currentNode.g > max_depth:
            max_depth = currentNode.g
        if currentNode.state == goal:
            path = []
            while currentNode:
                path.append(currentNode.state)
                currentNode = currentNode.parent
            t = time.time() - t
            return path[::-1], explored, t, max_depth
        explored.add(currentNode.state)

        for childState in getChildren(currentNode.state):
            if childState not in explored and childState not in frontier_set:
                childNode = Node(childState, currentNode, currentNode.g + 1) 
                frontier.append((childNode, depth + 1))
                frontier_set.add(childState)

    return None, explored, time.time() - t, max_depth

def IDS(start, goal):
    t = time.time()
    limit = 0
    while True:
        path, explored, t, max_depth = DLS(start, goal, limit)
        if path:
            return path, explored, t, max_depth
        limit += 1

if __name__ == "__main__":
    start = "702853614"
    goal = "012345678"
    
    ts=[]
    manhattanPath, manhattanexplored, t, max_depth = aStar(start, goal, calculateManhattan)
    # print(f"Manhattan path: {manhattanPath}")
    print(f"Length of Manhattan path: {len(manhattanPath) - 1}")
    print(f"number of nodes explored: {len(manhattanexplored)}")
    print(f"time taken: {t}")
    print(f"max depth: {max_depth}\n\n\n")
    ts.append(t)
    
    euclideanPath, euclideanexplored, t, max_depth = aStar(start, goal, calculateEuclidean)
    # print(f"Euclidean path: {euclideanPath}")
    print(f"Length of Euclidean path: {len(euclideanPath) - 1}")
    print(f"number of nodes explored: {len(euclideanexplored)}") 
    print(f"time taken: {t}")
    print(f"max depth: {max_depth}\n\n\n")
    ts.append(t)
    
    bfsPath, bfsexplored, t, max_depth = BFS(start, goal)
    # print(f"BFS path: {bfsPath}")
    print(f"Length of BFS path: {len(bfsPath) - 1}")
    print(f"number of nodes explored: {len(bfsexplored)}")
    print(f"time taken: {t}")
    print(f"max depth: {max_depth}\n\n\n")
    ts.append(t)
    
    dfsPath, dfsexplored, t, max_depth = DFS(start, goal)
    # print(f"DFS path: {dfsPath}")
    print(f"Length of DFS path: {len(dfsPath) - 1}")
    print(f"number of nodes explored: {len(dfsexplored)}")
    print(f"time taken: {t}")
    print(f"max depth: {max_depth}\n\n\n")
    ts.append(t)    
    
    idsPath, idsexplored, t, max_depth = IDS(start, goal)
    # print(f"IDS path: {idsPath}")
    print(f"Length of IDS path: {len(idsPath) - 1}")
    print(f"number of nodes explored: {len(idsexplored)}")
    print(f"time taken: {t}")
    print(f"max depth: {max_depth}")
    ts.append(t)
    
    algorithms = ['A* Manhattan', 'A* Euclidean', 'BFS', 'DFS', 'IDS']
    nodes_explored = [len(manhattanexplored), len(euclideanexplored), len(bfsexplored), len(dfsexplored), len(idsexplored)]
    path_lengths = [len(manhattanPath) - 1, len(euclideanPath) - 1, len(bfsPath) - 1, len(dfsPath) - 1, len(idsPath) - 1]
    times = ts  

    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    axs[0].bar(algorithms, nodes_explored, color='blue')
    axs[0].set_title('Number of Nodes Explored')
    axs[0].set_ylabel('Nodes')
    axs[0].set_yscale('log')

    axs[1].bar(algorithms, path_lengths, color='green')
    axs[1].set_title('Path Length')
    axs[1].set_ylabel('Length')
    axs[1].set_yscale('log')

    axs[2].bar(algorithms, times, color='red')
    axs[2].set_title('Time Taken')
    axs[2].set_ylabel('Time (s)')
    axs[2].set_yscale('log')

    plt.tight_layout()
    plt.show()
    