"""
Lab 06: Informed Search
File: lab06_informed_search.py

Codes in this file (in order):
  1. greedy_bfs()      - Greedy Best-First Search (heap by h)
  2. astar()           - A* Search (heap by f = g + h)
  3. manhattan() / euclidean() / misplaced_tiles() - heuristics
"""

import networkx as nx
import heapq

G = nx.DiGraph()
G.add_weighted_edges_from([('S','A',9), ('S','B',2), ('A','G',9),
                           ('B','C',2), ('C','G',2)])
h = {'S': 6, 'A': 3, 'B': 4, 'C': 2, 'G': 0}

# ---------- GREEDY: heap (h, node, path), visited = SET ----------
def greedy_bfs(G, start, goal, h):
    pq = [(h[start], start, [start])]
    visited = set()
    while pq:
        h_val, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor, path + [neighbor]))
    return None

# ---------- A*: heap (f, g, node, path), visited = DICT ----------
def astar(G, start, goal, h):
    pq = [(h[start], 0, start, [start])]
    visited = {}
    while pq:
        f_val, g_cost, node, path = heapq.heappop(pq)
        if node in visited and visited[node] <= g_cost:
            continue
        visited[node] = g_cost
        if node == goal:
            return path, g_cost
        for neighbor in G.neighbors(node):
            edge_cost = G[node][neighbor]['weight']
            new_g = g_cost + edge_cost
            new_f = new_g + h[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float('inf')

print(greedy_bfs(G, 'S', 'G', h))   # ['S', 'A', 'G']  (cost 18, not optimal)
print(astar(G, 'S', 'G', h))        # (['S','B','C','G'], 6)

# ---------- HEURISTICS ----------
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

import math
def euclidean(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

goal = (3, 3)
nodes = [(0, 0), (1, 2), (3, 1), (3, 3)]
heuristic = {n: manhattan(n, goal) for n in nodes}
# {(0,0): 6, (1,2): 3, (3,1): 2, (3,3): 0}

def misplaced_tiles(state, goal_state):
    return sum(1 for s, g in zip(state, goal_state) if s != g and s != 0)
