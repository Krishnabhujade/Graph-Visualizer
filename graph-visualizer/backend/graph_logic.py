from collections import deque

def bfs(nodes, edges, start):
    return ["A", "B", "C"]  # Dummy output for now


def buid_adj_list(nodes,edges):
    adj = {node : [] for node in nodes}
    for edge in edge:
        src = edge["source"]
        tgt = edge["target"]
        adj[src].append(tgt)
        adj[tgt].append(src)
    return adj

def bfs(nodes, edges, start):
    visited = []
    queue = deque()
    adj = buid_adj_list(nodes, edges)
    
    queue.append(start)
    visited_set = set()
    
    while queue:
        node = queue.popleft()
        if node not in visited_set:
            visited.append(node)
            visited_set.add(node)
            for neighbor in adj(node):
                if neighbor in visited_set:
                    queue.append(neighbor)
    return visited