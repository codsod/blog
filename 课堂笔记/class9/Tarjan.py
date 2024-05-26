def tarjan(graph):
    index=0
    stack=[]
    indices=[0]*len(graph)
    low_link=[0]*len(graph)
    on_stack=[False]*len(graph)
    sccs=[]
    def dfs(node):
        nonlocal index,stack,indices,low_link,on_stack,sccs
        index+=1
        indices[node]=index
        low_link[node]=index
        stack.append(node)
        on_stack[node]=True
        
        for neighbor in graph[node]:
            if indices[neighbor]==0 :
                dfs(neighbor)
                low_link[node]=min(low_link[node],low_link[neighbor])
            elif on_stack[neighbor]:
                low_link[node]=min(low_link[node],indices[neighbor])
        