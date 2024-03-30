def versionSort(arr):
    for i in range(len(arr)):
        arr[i]=list(map(int,arr[i].split('.')))
    arr.sort()
    for i in range(len(arr)):
        arr[i]='.'.join(map(str,arr[i]))
    return arr


n=int(input())
arr=[]
for _ in range(n):
    arr.append(input())
traver=versionSort(arr)
for i in traver:
    print(i)

    