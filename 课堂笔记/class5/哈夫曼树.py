import heapq


class TreeNode:

    def __init__(self, freq, char=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.char < other.char
        return self.freq < other.freq


def build_huffman_tree(character):
    heap = []
    for char, freq in character.items():
        heapq.heappush(heap, TreeNode(freq, char))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merge = TreeNode(left.freq + right.freq)
        merge.left = left
        merge.right = right
        heapq.heappush(heap, merge)

    return heap[0]


def encode(root):
    codes = {}

    def traverse(node, code):
        if node.char:
            codes[node.char] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    code = ''
    traverse(root, code)
    return codes


def encoding(codes, string):
    encode = ''
    for char in string:
        encode += codes[char]
    return encode


def decoding(root, string):
    decode = ''
    node = root
    for value in string:
        if value == '0':
            node = node.left
        elif value == '1':
            node = node.right
        if node.left == None and node.char:
            decode += node.char
            node = root
    return decode


n = int(input())
character = {}
for _ in range(n):
    char, freq = input().split()
    freq = int(freq)
    character[char] = freq

huffman_tree = build_huffman_tree(character)
codes = encode(huffman_tree)
strings = []
while True:
    try:
        line = input()
        strings.append(line)
    except EOFError: 
        break
results = []
for string in strings:
    if string[0] in ('0', '1'):
        results.append(decoding(huffman_tree, string))
    else:
        results.append(encoding(codes, string))

for result in results:
    print(result)
