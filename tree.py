#binary search tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


i= -1
def buildTree(arr) -> TreeNode:
    global i
    i += 1
    if arr[i] == -1:
        return None
    
    node = TreeNode(arr[i])
    node.left = buildTree(arr)
    node.right = buildTree(arr)

    return node


#dfs search in tree
def preOrder(root: TreeNode):
    if root is None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root: TreeNode):
    if root is None:
        return
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)

def postOrder(root: TreeNode):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")

#level order traversal
def levelOrder(root: TreeNode):
    q = list()
    q.append(root)
    if root is None:
        return
    while q != []:
        node = q.pop(0)
        if node is None:
            break
        else:
            print(node.data,end =" ")
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

#calculate height of tree

def heightOfTree(root: TreeNode) -> int:
    if root is None:
        return 0

    return 1 + max(heightOfTree(root.left), heightOfTree(root.right))

#diameter
class Height:
    def __init__(self):
        self.h = 0

def diameterOfTree(root, height=Height()):
    lh = Height()
    rh = Height()
    if root is None:
        height.h = 0
        return 0
    ldiameter = diameterOfTree(root.left, lh)
    rdiameter = diameterOfTree(root.right, rh)
    height.h = max(lh.h, rh.h) + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))

'''    
def diameterOfTree(root, hei=Height()):
    lh = Height()
    rh = Height()
    if root is None:
        hei.h = 0 
        return 
    left_d = diameterOfTree(root.left, lh)

    right_d = diameterOfTree(root.right, rh)

    hei.h = max(lh.h, rh.h) + 1

    return max( lh.h + rh.h + 1, max(left_d, right_d))
'''


if __name__ == "__main__":
    arr = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    root = buildTree(arr)
    print(root.data,'is the root of the tree.')

    print("___________________\n")
    print("Your preOrder tree traversal is")
    preOrder(root)
    print()
    print("Your inOrder tree traversal is")
    inOrder(root)
    print()
    print("Your postOrder tree traversal is")
    postOrder(root)
    print()
    print("Level order")
    levelOrder(root)
    print()
    print("Diameter of tree", diameterOfTree(root))

    print()
    print("Height of the tree using heightOfTree function", heightOfTree(root))
