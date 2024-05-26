def bfs(A,B,target):
    start=(0,0)
    visited=set()
    visited.add(start)
    queue=[(start,[])]
    
    while queue:
        (a,b),actions =queue.pop(0)
        if a==target or b==target:
            return actions
        
        next_states=[(A,b),(a,B),(0,b),(a,0),(min(a+b,A),max(0,a+b-A)),(max(0,a+b-B),min(B,a+b))]
        
        for i in next_states:
            if i not in visited:
                visited.add(i)
                new_actions=actions+[get_action(a,b,i)]
                queue.append((i,new_actions))
    return ['impossible']

def get_action(a,b,next_state):
    if next_state==(A,b):
        return "FILL(1)"
    elif next_state==(a,B):
        return "FILL(2)"
    elif next_state==(0,b):
        return "DROP(1)"
    elif next_state==(a,0):
        return "DROP(2)"
    elif next_state==(min(a+b,A),max(0,a+b-A)):
        return "POUR(2,1)"
    else:
        return "POUR(1,2)"
    
A,B,target=map(int,input().split())
solution=bfs(A,B,target)

if solution==['impossible']:
    print("impossible")
else:
    print(len(solution))
    for i in solution:
        print(i)