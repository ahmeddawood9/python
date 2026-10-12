"""
Lab 05: Uninformed Search
File: lab05_uninformed_search.py

Codes in this file (in order):
  1. bfs()  - Breadth-First Search (queue, mark visited at enqueue)
  2. dfs()  - Depth-First Search (recursion)
  3. ucs()  - Uniform-Cost Search (heap by cost)
"""

import networkx as nx
from collections import deque
import heapq

G = nx.DiGraph()
G.add_edges_from([('S','A'), ('S','B'), ('A','C'), ('B','K')])

# ---------- BFS: queue, mark visited at ENQUEUE ----------
def bfs(G, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# ---------- DFS: recursion, mark visited on ENTRY ----------
def dfs(G, node, goal, visited=None, path=None):
    if visited is None: visited = set()
    if path is None: path = [node]
    visited.add(node)
    if node == goal:
        return path
    for neighbor in G.neighbors(node):
        if neighbor not in visited:
            result = dfs(G, neighbor, goal, visited, path + [neighbor])
            if result:
                return result
    return None

# ---------- UCS: heap by cost (cost, node, path) ----------
W = nx.DiGraph()
W.add_weighted_edges_from([('S','A',2), ('S','B',5), ('A','B',2),
                           ('A','C',6), ('B','C',3), ('C','G',1)])

def ucs(G, start, goal):
    pq = [(0, start, [start])]
    visited = {}                                  # node -> best cost
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited and visited[node] <= cost:
            continue                              # stale entry
        visited[node] = cost
        if node == goal:
            return path, cost
        for neighbor in G.neighbors(node):
            edge_cost = G[node][neighbor]['weight']
            heapq.heappush(pq, (cost + edge_cost, neighbor, path + [neighbor]))
    return None, float('inf')

print(bfs(G, 'S', 'K'))        # ['S', 'B', 'K']
print(dfs(G, 'S', 'K'))
print(ucs(W, 'S', 'G'))        # (['S','A','B','C','G'], 8)

# ---------- drawing (not exam critical) ----------
import matplotlib.pyplot as plt
result = bfs(G, 'S', 'K')
pos = nx.spring_layout(G, seed=42)
path_edges = list(zip(result, result[1:]))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800)
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='orange', width=3)
plt.show()
