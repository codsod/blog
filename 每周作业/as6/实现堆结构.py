class heap:

    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def buildheap(self, list):
        self.heaplist.extend(list)
        self.currentsize = len(list)
        ind = len(list) // 2
        while ind > 0:
            self.percdown(ind)
            ind = ind - 1
        return self.heaplist

    def percdown(self, i):
        while i * 2 <= self.currentsize:
            mic = self.minchild(i)
            if self.heaplist[i] > self.heaplist[mic]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mic]
                self.heaplist[mic] = tmp
            i = mic

    def minchild(self, i):
        if i * 2 + 1 > self.currentsize:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, item):
        self.heaplist.append(item)
        self.currentsize += 1
        self.percup(self.currentsize)

    def percup(self, i):
        while i // 2 > 0:
            if self.heaplist[i // 2] > self.heaplist[i]:
                tmp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def delmin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.heaplist.pop()
        self.currentsize = self.currentsize - 1
        self.percdown(1)
        return retval


bh = heap()
n = int(input())
for _ in range(n):
    line = input().strip()
    if line[0] == '1':
        bh.insert(int(line[2:]))
    else:
        print(bh.delmin())
