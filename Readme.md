# Graph Traversal Algorithms: BFS & DFS

This repository contains Python implementations of two fundamental graph traversal algorithms for undirected graphs represented as an adjacency list:
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**

Both algorithms start at vertex `0` and traverse the graph in the order given by the adjacency list.

## Table of Contents

- [Overview](#overview)
- [Algorithm Explanations](#algorithm-explanations)
  - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
  - [Depth-First Search (DFS)](#depth-first-search-dfs)
- [Dynamic Diagrams](#dynamic-diagrams)
  - [BFS Diagram](#bfs-diagram)
  - [DFS Diagram](#dfs-diagram)
- [Code](#code)
- [How to Run](#how-to-run)
- [Examples](#examples)
- [License](#license)

## Overview

Graph traversal is a key operation in many algorithms.  
- **BFS** explores the graph level by level using a queue, making it ideal for finding the shortest path in unweighted graphs.  
- **DFS** explores as deep as possible along a branch before backtracking using recursion (or an explicit stack), which is useful for tasks such as connectivity testing and topological sorting.

## Algorithm Explanations

### Breadth-First Search (BFS)

1. **Initialization:**  
   - Create a `visited` list to keep track of visited vertices.
   - Initialize a queue (using `deque`) with the starting vertex (`0`) and mark it as visited.
   - Prepare a `result` list to record the order of traversal.

2. **Traversal:**  
   - While the queue is not empty, dequeue the front vertex.
   - Append this vertex to the `result` list.
   - For each neighbor of this vertex (in the order given by the adjacency list):
     - If the neighbor is not visited, mark it as visited and enqueue it.

3. **Termination:**  
   - When the queue is empty, the `result` list contains the BFS order.

### Depth-First Search (DFS)

1. **Initialization:**  
   - Create a `visited` list to track visited vertices.
   - Prepare a `result` list to store the order of traversal.

2. **Traversal (Recursion):**  
   - Start at vertex `0`, mark it as visited, and add it to the result.
   - For each neighbor of the current vertex (following the order in the adjacency list):
     - If the neighbor is unvisited, recursively perform DFS from that neighbor.
   - Backtracking occurs automatically when all neighbors have been processed.

3. **Termination:**  
   - The recursion unwinds once all vertices reachable from the starting point have been visited, and the `result` list contains the DFS order.

## Dynamic Diagrams

### BFS Diagram

```mermaid
flowchart TD
    A[Start at vertex 0<br>Mark as visited and enqueue]
    B{Is the queue empty?}
    C[Dequeue vertex from queue]
    D[Append vertex to result list]
    E[For each neighbor of current vertex<br>in order from the adjacency list]
    F{Is neighbor visited?}
    G[Mark neighbor as visited<br>Enqueue neighbor]
    H[Proceed to next neighbor]
    I[Return result list]

    A --> B
    B -- No --> C
    C --> D
    D --> E
    E --> F
    F -- No --> G
    F -- Yes --> H
    G --> H
    H --> E
    E -- All neighbors processed --> B
    B -- Yes --> I

flowchart TD
    A[Start at vertex 0<br>Mark as visited and add to result]
    B[For each neighbor of current vertex<br>in order from the adjacency list]
    C{Is neighbor visited?}
    D[Call DFS recursively on neighbor]
    E[Backtrack to previous vertex]
    F[Return result list when complete]

    A --> B
    B --> C
    C -- No --> D
    C -- Yes --> B
    D --> E
    E --> B
    B -- All neighbors processed --> F

