from collections import defaultdict,deque

def bfs(start,l):
    queue=deque([(1,start)])
    visited=set(start)
    while queue:
        len,cur=queue.popleft()
        if cur==ed:
            return len
        for i in range(l):
            for nword in buckets[cur[:i]+'_'+cur[i+1:]]:
                if nword not in visited:
                    visited.add(nword)
                    queue.append((len+1,nword))
    
    return 0

st,ed=input().split()
word=list(input().split())
words=set(word)
words.add(st)
words.add(ed)

buckets=defaultdict(list)
l=len(st)
for word in words:
    for i in range(l):
        buckets[word[:i]+'_'+word[i+1:]].append(word)

print(bfs(st,l))
