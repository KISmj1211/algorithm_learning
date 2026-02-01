graph_sample = {
    1:[2,3],
    2:[1,7],
    3:[1,5,7],
    5:[3,7],
    7:[2,3]
}


graph = {
    'A':['B','D'],
    'B':['A','C'],
    'C':['B','F'],
    'D':['A','E'],
    'E':['D','F'],
    'F':['C','E']
}

print(len(graph))

print(graph.values())

total_connections = 0
for edge in graph.values():
    total_connections += len(edge)
num_edges = total_connections // 2

print("실제 다리(연결)의 수는:", num_edges)



