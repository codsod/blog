def dfs1(graph,node,visited,stack):
    visited[node]=True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs1(graph,neighbor,visited,stack)
    stack.append(node)
def dfs2(graph,node,visited,component):
    visited[node]=True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs2(graph,neighbor,visited,component)

def kosaraju(graph):

    stack=[]
    visited=[False]*len(graph)
    for node in range(len(graph)):
        if not visited[node]:
            dfs1(graph,node,visited,stack)

    transposed_graph=[[]for _ in range(len(graph))]
    for node in range(len(graph)):
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)

    visited=[False]*len(graph)
    sccs=[]
    while stack:
        node=stack.pop()
        if not visited[node]:
            scc=[]
            dfs2(transposed_graph,node,visited,scc)
            sccs.append(scc)
    return sccs


graph = [[1], [2, 4], [3, 5], [0, 6], [5], [4], [7], [5, 6]]
sccs = kosaraju(graph)
print("Strongly Connected Components:")
for scc in sccs:
    print(scc)
