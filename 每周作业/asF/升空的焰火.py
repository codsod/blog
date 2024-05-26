class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def otherview(root):
    queue = []
    out = []
    queue.append(root)
    sons = []
    while queue:
        a = queue.pop(0)
        if a.left:
            sons.append(a.left)
        if a.right:
            sons.append(a.right)
        if not queue and sons:
            queue = sons
            sons = []
            out.append(a.data)
        if not queue and not sons:
            out.append(a.data)
    print(*out)


N = int(input())
Nodelist = []
for i in range(N):
    Nodelist.append(Node(i + 1))
for i in range(N):
    left, right = map(int, input().split())
    if left != -1:
        Nodelist[i].left = Nodelist[left - 1]
    if right != -1:
        Nodelist[i].right = Nodelist[right - 1]
otherview(Nodelist[0])
