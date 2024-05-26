def InAndPre_Post(inorder, preorder):
    if len(inorder) == 0:
        return []
    if len(inorder) == 1:
        return inorder[0]
    postorder = []
    root = preorder[0]
    rootindex = inorder.index(root)
    lefti = inorder[:rootindex]
    righti = inorder[rootindex + 1:]
    leftp = preorder[1:rootindex + 1]
    rightp = preorder[rootindex + 1:]

    postorder.extend(InAndPre_Post(lefti, leftp))
    postorder.extend(InAndPre_Post(righti, rightp))
    postorder.append(root)
    return postorder


while True:
    try:

        preorder,inorder=input().split()
        post = InAndPre_Post(inorder, preorder)
        print(''.join(post))
    except EOFError:
        break
