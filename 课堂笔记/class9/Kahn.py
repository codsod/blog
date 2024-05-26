from collections import defaultdict,deque

def topo(graph):
    indegree=defaultdict(int)
    result=[]
    queue=deque()

    for u in graph:
        for v in graph[u]:
            indegree[v]+=1

    for u in graph:
        if indegree[u]==0:
            queue.append(u)

    while queue:
        u=queue.popleft()
        result.append(u)

        for v in graph[u]:
            indegree[v]-=1
            if indegree[v]==0:
                queue.append(v)

    if len(result)==len(graph):
        return result
    else:
        return None


graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

sorted_vertices = topo(graph)
if sorted_vertices:
    print("Topological sort order:", sorted_vertices)
else:
    print("The graph contains a cycle.")
