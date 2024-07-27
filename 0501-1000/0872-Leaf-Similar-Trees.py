class Solution(object):
    def leafSimilar(self, root1, root2):
        def leafSequence(node):
            if not node:
                return []
            if not (node.left or node.right):
                return [node.val]
            else:
                return leafSequence(node.left) + leafSequence(node.right)

        seq1 = leafSequence(root1)
        seq2 = leafSequence(root2)

        return len(seq1) == len(seq2) and all([seq1[i] == seq2[i] for i in range(len(seq1))])
