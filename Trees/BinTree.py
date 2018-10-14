class Node(object):

    def __init__(self, value=None, lchild=None, rchild=None):
        self.val = value
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self):
        return str(self.val)


class BinTree(object):
    def __init__(self, seq):
        if seq:
            seq = list(seq)
            self.root = Node(seq[0])
            seq.insert(0, '#')
            self._create(self.root, 1, seq)

        else:  # no data, no tree
            self.root = Node()

    def _create(self, root, idx, seq):
        # recursively create the Binary Tree
        if 2 * idx <= len(seq) - 1 and (seq[2 * idx] != '#'):
            root.lchild = Node(seq[2 * idx])
            self._create(root.lchild, 2 * idx, seq)

        if 2 * idx + 1 <= len(seq) - 1 and (seq[2 * idx + 1] != '#'):
            root.rchild = Node(seq[2 * idx + 1])
            self._create(root.rchild, 2 * idx + 1, seq)

    def _preorder(self, root):
        print(root.val)
        if root.lchild:
            self._preorder(root.lchild)
        if root.rchild:
            self._preorder(root.rchild)

    def preorder(self):
        self._preorder(self.root)


if __name__ == "__main__":
    seq = ('A',  # the sequence formed by layers of a Binary Tree
           'L', 'C',
           'B', 'E', '#', 'D',
           '#', '#', '#', '#', '#', '#', 'W', '#')
    tree = BinTree(seq)  # create the Binary Tree
    tree.preorder()
