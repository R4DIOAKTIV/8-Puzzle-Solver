# 8-Puzzle Solver
This repo contains our work for 8-Puzzle Solver using different searching algorithms:
- BFS
- DFS
- A* with Manhattan Distance and Euclidean Distance
- IDS

Table of Contents
=================

   * [8-Puzzle Solver](#8-puzzle-solver)
   * [Table of Contents](#table-of-contents)
   * [How to run](#how-to-run)
   * [state representation](#state-representation)
     * [Node Class](#node-class)
     * [util functions](#helper-functions)
   * [Algorithms](#algorithm)
      * [BFS](#bfs)
      * [DFS](#dfs)
      * [A*](#a)
            * [Manhattan Distance](#manhattan-distance)
            * [Euclidean Distance](#euclidean-distance)
      * [IDS](#ids)
    * [Results](#results)
    * [GUI](#gui)
    * [Members](#members)

# How to run
- Clone the repo: 
```bash
git clone https://github.com/R4DIOAKTIV/Artificial-Intelligence-.git
```
- Run the following command:
```bash
python gui.py
```
- Choose the algorithm you want to use and enter the initial state of the puzzle.
- Click on the solve button to get the solution.

# state representation
The state of the puzzle is represented as string of 9 characters, where each character represents a tile in the puzzle. The empty tile is represented by '0'
The state is then further represented in a custom class called Node.

## Node Class
The Node class contains the following attributes:
- state: the state of the puzzle
- parent: the parent node
- g: the cost to reach this node
- h: the heuristic value of the node
- f: the total cost of the node (f = g + h)

and has the method:
- \_\_lt\_\_: dunder method to be used with priority queue in aStar algorithm
## util functions
- getChildren: returns the children of a node
- calculateManhattan: calculates the manhattan distance of a node
- calculateEuclidean: calculates the euclidean distance of a node
- isSolvable: checks if the puzzle is solvable
- randomState: generates a random state for the puzzle

# Algorithms
## BFS Implementation

The Breadth-First Search (BFS) algorithm uses a queue to explore nodes level by level starting from the `startNode`. It explores all neighbor nodes before moving to the next depth level. The algorithm tracks explored states and maintains the maximum depth reached during the search.

## DFS Implementation

The Depth-First Search (DFS) algorithm uses a stack to explore as far as possible along each branch before backtracking. Starting from the `startNode`, it dives deep into each path. It keeps track of explored states and updates the maximum depth reached.

## A\* Search Implementation

The A\* Search algorithm uses a priority queue (min-heap) to select the node with the lowest total cost `f = g + h`, where:
- `g` is the cost from the start node to the current node.
- `h` is the heuristic estimate from the current node to the goal.
The heuristic functions used can be Manhattan or Euclidean distance. This algorithm efficiently finds the shortest path to the goal by considering both the cost to reach a node and the estimated cost to reach the goal from that node.

## DLS Implementation

Depth-Limited Search (DLS) is a variation of DFS with a predetermined depth limit. It explores nodes up to a certain depth and prunes paths that exceed this limit. This approach prevents infinite loops in graphs with cycles by restricting how deep the search can go.

## IDS Implementation

Iterative Deepening Search (IDS) combines the benefits of DFS and BFS by repeatedly applying DLS with increasing depth limits. Starting from a depth limit of zero, it incrementally increases the limit until the goal is found. IDS achieves completeness like BFS while maintaining the memory efficiency of DFS.

# Results
For our results, we used this initial state: '702853614' to test the algorithms. The following table shows the results for each algorithm:
| Algorithm          | Path Length | Nodes Explored | Time Taken (s)       |
|--------------------|-------------|----------------|----------------------|
| A* w/ Manhattan    | 27          | 5827           | 0.11850690841674805  |
| A* w/ Euclidean    | 27          | 11700          | 0.2696387767791748   |
| BFS                | 27          | 176308         | 2.3264243602752686   |
| DFS                | 12083       | 12441          | 0.12152719497680664  |
| IDS                | 37          | 10788          | 0.09427118301391602  |

# GUI
The GUI is implemented using PyQT5. It allows the user to select the algorithm they want to use and enter the initial state of the puzzle. The user can then click the solve button to get the solution. The GUI displays the path length, nodes explored, and time taken for the selected algorithm.
