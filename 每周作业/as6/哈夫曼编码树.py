import heapq
class Treenode:
    def __init__(self,freq,char=None):
        self.freq=freq
        self.char=char
        self.left=None
        self.right=None
    def __lt__(self,other):
        if self.freq!=other.freq:
            return self.freq<other.freq
        else:
            return self.char<other.char
    def is_leaf(self):
        return self.left==None and self.right==None

def build_huffman_tree(dict):
    heap=[]
    for char,freq in dict.items():
        heapq.heappush(heap,Treenode(freq,char))
    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)
        merge=Treenode(left.freq+right.freq)
        merge.left=left
        merge.right=right
        merge.char=min(left.char,right.char)
        heapq.heappush(heap,merge)
    return heap[0]
def encode(root):
    codes={}
    def traverse(node,code):
        if node.is_leaf():
            codes[node.char]=code
        else:
            traverse(node.left,code+'0')
            traverse(node.right,code+'1')
            
    code=''
    traverse(root,code)
    return codes
def encoding(codes,string):
    ret=''
    for char in string:
        ret+=codes[char]
    return ret
def decoding(root,strings):
    ret=''
    node=root
    for i in strings:
        if i=='0':
            node=node.left
        elif i=='1':
            node=node.right
        if node.is_leaf():
            ret+=node.char
            node=root
    return ret

n=int(input())
dict={}
for _ in range(n):
    char,freq=input().split()
    freq=int(freq)
    dict[char]=freq
root=build_huffman_tree(dict)
codes=encode(root)
strings=[]
while True:
    try:
        tmp=input()
        strings.append(tmp)
    except EOFError:
        break
for string in strings:
    if string[0]=='1' or string[0]=='0':
        print(decoding(root,string))
    else:
        print(encoding(codes,string))
