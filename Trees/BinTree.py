from Trees.Visualizer import draw_tree


class Node(object):

    def __init__(self, value=None, lchild=None, rchild=None):
        self.val = value
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self):
        return str(self.val)


class BinTree(object):
    """
    A class and reference implementation of binary trees
    """

    def __init__(self, seq):
        """

        seq: values of tree nodes from the top layer to the bottom one,
                and from the left to the right in each layer.
        example: let's see we want to create the following tree('#' means empty node),
                 we should pass seq as [1,2,3,4,5,'#',7]
                    1
                   / \
                  2   3
                 /\  / \
                4 5 #  7

        """
        if seq:
            seq = list(seq)
            self.root = Node(seq[0])
            seq.insert(0, -1)
            self._create(self.root, 1, seq)

        else:  # no data, empty tree
            self.root = Node()

    def _create(self, root, idx, seq):
        # recursively create the Binary Tree
        if 2 * idx <= len(seq) - 1 and (seq[2 * idx] != '#'):
            root.lchild = Node(seq[2 * idx])
            self._create(root.lchild, 2 * idx, seq)

        if 2 * idx + 1 <= len(seq) - 1 and (seq[2 * idx + 1] != '#'):
            root.rchild = Node(seq[2 * idx + 1])
            self._create(root.rchild, 2 * idx + 1, seq)

    def _preorder(self, root, result):

        result.append(root.val)

        if root.lchild:
            self._preorder(root.lchild, result)
        if root.rchild:
            self._preorder(root.rchild, result)

    def _midorder(self, root, result):
        if root.lchild:
            self._midorder(root.lchild, result)

        result.append(root.val)

        if root.rchild:
            self._midorder(root.rchild, result)

    def _postorder(self, root, result):
        if root.lchild:
            self._postorder(root.lchild, result)

        if root.rchild:
            self._postorder(root.rchild, result)

        result.append(root.val)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def midorder(self):
        result = []
        self._midorder(self.root, result)
        return result

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _height(self, node):
        """
        node: can be regarded as the root of a tree. Every time we recursively
        invoke this function, it returns the height of the tree with node being its root.
        """
        if not node:
            return 0
        else:
            lt = self._height(node.lchild)
            rt = self._height(node.rchild)
            return 1 + (lt if lt > rt else rt)

    def height(self):
        return self._height(self.root)

    def _size(self, node):
        """
        node: can be regarded as the root of a tree. Every time we recursively
        invoke this function, it returns the size of the tree with node being its root.
        In particular, the size of such a tree equals
        1(root node)+ size of its left subtree + size of its right subtree
        """
        if not node:
            return 0
        else:
            return 1 + self._size(node.lchild) + self._size(node.rchild)

    def size(self):
        return self._size(self.root)

    def insert_left(self, val):
        if self.root.lchild is None:
            self.root.lchild = Node(val)
        else:
            new_left = Node(val)
            new_left.lchild = self.root.lchild
            self.root.lchild = new_left

    def insert_right(self, val):
        if self.root.rchild is None:
            self.root.rchild = Node(val)
        else:
            new_right = Node(val)
            new_right.rchild = self.root.rchild
            self.root.rchild = new_right

    def get_right(self):
        return self.root.rchild

    def get_light(self):
        return self.root.lchild


if __name__ == "__main__":
    seq = ('A',  # the sequence formed by layers of a Binary Tree
           'L', 'C',
           'B', 'E', '#', 'D',
           '#', '#', '#', '#', '#', '#', 'W', '#')
    tree = BinTree(seq)  # create the Binary Tree
    print(tree.preorder())
    print("size: ", tree.size())
    print("height: ", tree.height())

    draw_tree(tree.root)
    tree.insert_left(1000)  # test insert function
    draw_tree(tree.root)  # draw the altered tree

    tree.insert_right('Hello')
    draw_tree(tree.root)
