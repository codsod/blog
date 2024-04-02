class BinHeap:

    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def percdown(self, i):
        while i * 2 <= self.currentsize:
            mi = self.minchild(i)
            if self.heaplist[i] > self.heaplist[mi]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mi]
                self.heaplist[mi] = tmp
            i = mi

    def percup(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                tmp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def minchild(self, i):
        if i * 2 + 1 > self.currentsize:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildheap(self, alist):
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.percdown(i)
            i = i - 1

    def insert(self, item):
        self.heaplist.append(item)
        self.currentsize += 1
        self.percup(self.currentsize)

    def delmin(self):
        minn = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.heaplist.pop()
        self.currentsize = self.currentsize - 1
        self.percdown(1)
        return minn


bh = BinHeap()
n = int(input())
for _ in range(n):
    line = input().strip()
    if line[0] == '1':
        bh.insert(int(line[2:]))
    else:
        print(bh.delmin())
