# find height of N-ary tree in O(n)
from collections import deque

MAX = 1001
adj = [[] for i in range(MAX)] # Adjacency list to store N-ary tree

def build_tree(arr, n): # Build tree in tree in O(n)
    root_index = 0

    for i in range(n):
        if (arr[i] == -1): # if root node, store index
            root_index = i
        else:
            adj[arr[i]].append(i)

    return root_index


def BFS(start):

    q = deque()
    max_level_reached = 0

    q.append([start, 0]) # height of root node is zero

    # p[0] denotes node in adjacency list
    # p[1] denotes level of p[0]
    p = []

    while (len(q) > 0):
        p = q.popleft()

        max_level_reached = max(max_level_reached, p[1])

        for i in range(len(adj[p[0]])):
            q.append([adj[p[0]][i], p[1] + 1]) # adding 1 to pre_level

    return max_level_reached


# Driver code
if __name__ == '__main__':
    parent = [-1, 0, 1, 2, 3] # node 0 to node n-1
    n = len(parent) # Number of nodes in tree

    root_index = build_tree(parent, n)
    ma = BFS(root_index)
    print("Height of N-ary Tree =", ma)

# output: Height of N-ary Tree = 4
