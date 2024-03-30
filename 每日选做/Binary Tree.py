def searchfreq(left, right):
    out = [0, 0]
    if left != 1 and right != 1:

        while not (left == right == 1):
            if left > right:
                leftadd = left // right
                left %= right
                if left == 0:
                    leftadd -= 1
                    left = 1
                out[0] += leftadd
            else:
                rightadd = right // left
                right %= left
                if right == 0:
                    rightadd -= 1
                    right = 1
                out[1] += rightadd
    else:
        out[0] = left - 1
        out[1] = right - 1
    return out


cases = int(input())
caseptr = 0
for _ in range(cases):
    caseptr += 1
    left, right = map(int, input().split())
    a = searchfreq(left, right)
    b = [str(x) for x in a]
    print(f"Scenario #{caseptr}:")
    print(" ".join(b))
    print()
