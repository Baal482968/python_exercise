class TreeNode:

    def __init__(self, key, value, leftChild = None, rightChild = None, parent = None):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

    def isRoot(self):
        if not self.parent:
            return True
        return False

    def hasLeftChild(self):
        if self.leftChild:
            return True
        return False

    def hasRightChild(self):
        if self.rightChild:
            return True
        return False

    def hasAnyChildren(self):
        if self.leftChild or self.rightChild:
            return True
        return False

    def isLeaf(self):
        if self.leftChild or self.rightChild:
            return False
        return True

    def isLeftChild(self):
        if self.parent:
            if self.parent.leftChild == self:
                return True
            return False
        return False

    def isRightChild(self):
        if self.parent:
            if self.parent.rightChild == self:
                return True
            return False
        return False

    def replaceRoot(self, key, value, leftChild, rightChild): # using in delete
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        if self.hasLeftChild(): # set child's new parent
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self._put(key, value, self.root)
        self.size += 1

    def _put(self, key, value, currentNode):
        if key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent = currentNode)
        elif key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent = currentNode)
        else:
            currentNode.value = value # Same key: replace old value

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        else:
            if key == currentNode.key:
                return currentNode
            elif key > currentNode.key:
                return self._get(key, currentNode.rightChild)
            else:
                return self._get(key, currentNode.leftChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        return False

    def delete(self, key):
        if self.size < 1:
            raise KeyError('Node not found!')
        elif self.size == 1:
            if key == self.root.key:
                self.remove(self.root)
                self.size -= 1
            else:
                raise KeyError('Node not found!')
        else:
            nodeNeedRemove = self._get(key, self.root)
            if nodeNeedRemove:
                self.remove(nodeNeedRemove)
                self.size -= 1
            else:
                raise KeyError('Node not found!')

    def remove(self, nodeRm):
        if nodeRm.isLeaf():
            if nodeRm.isLeftChild():
                nodeRm.parent.leftChild = None
            else:
                nodeRm.parent.rightChild = None
        elif nodeRm.hasBothChildren():
            successor = nodeRm.findSuccessor()
            nodeRm.key = successor.key
            nodeRm.value = successor.value
            successor.delSuccessor()
        else:
            if nodeRm.isLeftChild():
                if nodeRm.hasLeftChild():
                    nodeRm.leftChild.parent = nodeRm.parent
                    nodeRm.parent.leftChild = nodeRm.leftChild
                else:
                    nodeRm.rightChild.parent = nodeRm.parent
                    nodeRm.parent.leftChild = nodeRm.rightChild
            elif nodeRm.isRightChild():
                if nodeRm.hasLeftChild():
                    nodeRm.leftChild.parent = nodeRm.parent
                    nodeRm.parent.rightChild = nodeRm.leftChild
                else:
                    nodeRm.rightChild.parent = nodeRm.parent
                    nodeRm.parent.rightChild = nodeRm.rightChild
            else: # nodeRm is root
                if nodeRm.hasLeftChild():
                    newR = nodeRm.leftChild
                    nodeRm.replaceRoot(newR.key, newR.value, newR.leftChild, newR.rightChild)
                else:
                    newR = nodeRm.rightChild
                    nodeRm.replaceRoot(newR.key, newR.value, newR.leftChild, newR.rightChild)

    def findSuccessor(self):
        successor = self.rightChild.findMin()
        return successor

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def delSuccessor(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        else:
            if self.hasLeftChild():
                self.leftChild.parent = self.parent
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
            if self.hasRightChild():
                self.rightChild.parent = self.parent
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild

    def __delitem__(self, key):
        self.delete(key)



mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="bee"

# mytree.delete(6)
# mytree[6] = 'Baal'
# mytree[6] = 'Nico'

# if 5 in mytree:
#     print("Yes it is in BST")
# else:
#     print("Not found in BST")
