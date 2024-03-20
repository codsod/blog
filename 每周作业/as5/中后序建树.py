def InAndPost_Pre(inorder, postorder):
    if len(inorder) == 0:
        return []
    if len(inorder) == 1:
        return inorder[0]
    preorder = []
    root = postorder[-1]
    rootindex = inorder.index(root)
    lefti = inorder[:rootindex]
    righti = inorder[rootindex + 1:]
    leftp = postorder[:rootindex]
    rightp = postorder[rootindex:-1]

    preorder.append(root)
    preorder.extend(InAndPost_Pre(lefti, leftp))
    preorder.extend(InAndPost_Pre(righti, rightp))
    return preorder


inorder = input()
postorder = input()
pre = InAndPost_Pre(inorder, postorder)
print(''.join(pre))
