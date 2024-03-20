class file_tree_node:

    def __init__(self, name=''):
        self.files = []
        self.dirs = []
        self.name = name


def output_structure(node, indent=0):
    formati = '|     '
    print(formati * indent + node.name)
    for dir in node.dirs:
        output_structure(dir, indent + 1)
    node.files.sort()
    for file in node.files:
        print(formati * indent + file)


datax = 1
temp = []
root = file_tree_node('ROOT')
stack = [root]
while True:
    line = input()
    if line == '*':
        print(f'DATA SET {datax}:')
        output_structure(root)
        print()
        root = file_tree_node('ROOT')
        stack = [root]
        temp = []
        datax += 1
    elif line == '#':
        break
    else:
        if line[0] == 'f':
            stack[-1].files.append(line)
        elif line[0] == 'd':
            node = file_tree_node(line)
            stack[-1].dirs.append(node)
            stack.append(node)
        elif line == ']':
            stack.pop()
