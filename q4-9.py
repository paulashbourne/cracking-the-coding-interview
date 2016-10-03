# Question 4.9
# BST Sequences
from bst import BST, TreeNode

def weave(leftSequences, rightSequences):
    # Weave together left and right sequences
    # If n = len(left) + len(right), then there are 2^n
    # Different ways to weave them together
    # Because we can choose either from left or right (1/0)
    # for each position
    if not leftSequences or not rightSequences:
        # One of them is empty, so no weaving to be done
        yield leftSequences + rightSequences
    else:
        for left in leftSequences:
            for right in rightSequences:
                n = len(left) + len(right)
                # Pick the positions of the LEFT elements
                import itertools
                for leftIndices in itertools.combinations(xrange(n), len(left)):
                    result = []
                    leftIdx = rightIdx = 0
                    for i in xrange(n):
                        if len(leftIndices) > leftIdx and i == leftIndices[leftIdx]:
                            result.append(left[leftIdx])
                            leftIdx += 1
                        else:
                            result.append(right[rightIdx])
                            rightIdx += 1
                    yield result

# Node is a TreeNode
def getBSTSequences(node):
    sequences = []
    if node is None:
        return sequences
    left  = getBSTSequences(node.left)
    right = getBSTSequences(node.right)
    for row in weave(left, right):
        sequences.append([node.value] + row)
    return sequences

def test1():
    tree = BST(TreeNode(2))
    tree.insert(TreeNode(1))
    tree.insert(TreeNode(3))
    return getBSTSequences(tree.root)

def test2():
    tree = BST(TreeNode(50))
    for n in [20, 60, 10, 25, 70, 5, 15, 65, 80]:
        tree.insert(TreeNode(n))
    return getBSTSequences(tree.root)

def main():
    print test1()
    print test2()

if __name__ == "__main__":
    main()
