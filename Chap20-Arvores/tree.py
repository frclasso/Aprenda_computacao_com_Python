#!/usr/bin/env python3


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left =left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def total(tree):
        if tree == None: return 0
        return Tree.total(tree.left) + Tree.total(tree.right) + tree.cargo

    def printTree(tree):
        if tree == None: return
        print(tree.cargo,end=' ')
        Tree.printTree(tree.left)
        Tree.printTree(tree.right)

    def printTreePostOrder(tree):
        if tree == None: return
        Tree.printTreePostOrder(tree.left)
        Tree.printTreePostOrder(tree.right)
        print(tree.cargo, end=' ')

    def printTreeInOrder(tree):
        if tree == None: return
        Tree.printTreeInOrder(tree.left)
        print(tree.cargo, end=' ')
        Tree.printTreeInOrder(tree.right)

    def printTreeIdented(tree, level=0):
        if tree == None: return
        Tree.printTreeIdented(tree.right, level+1)
        print('  '*level + str(tree.cargo))
        Tree.printTreeIdented(tree.left, level+1)

    def getToken(tokenList, expected):
        if tokenList [0] == expected:
            tokenList[0:1] = [] # remove the token
            return 1
        else: return 0

    def getNumber(tokenList):
        if Tree.getToken(tokenList, '('):
            x = Tree.getSum(tokenList) # get subexpression
            if not Tree.getToken(tokenList, ')'):
                raise ('BadExpression', 'missing parenthesis')
            # Tree.getToken(tokenList, ')')
            return x
        else:
            x = tokenList[0]
            if type(x) != type(0): return None
            tokenList[0:1] = [] # remove the token
            return Tree(x, None, None) # return a leaf with the number

    def getProduct(tokenList):
        a = Tree.getNumber(tokenList)
        if Tree.getToken(tokenList, '*'):
            # b = Tree.getNumber(tokenList)
            b = Tree.getProduct(tokenList) # this line changed
            return Tree('*', a,b)
        else: return a

    def getSum(tokenList):
        a = Tree.getProduct(tokenList)
        if Tree.getToken(tokenList, '+'):
            b = Tree.getSum(tokenList)
            return Tree('+', a, b)
        else:return a

left = Tree(2)
right = Tree(3)

# tree = Tree(1, left, right)

# tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
# Tree.printTree(tree)  # + 1 * 2 3 notacao Prefixa
# print()
# Tree.printTreePostOrder(tree) # 1 2 3 * + notacao Posfixa
# print()
# Tree.printTreeInOrder(tree) # notacao infixa    1 + 2 * 3
# print()
# print(Tree.printTreeIdented(tree))

# tokenList = [9, 11, 'end']
# x = Tree.getNumber(tokenList)
# Tree.printTreePostOrder(x)  # 9
# print()
# print(tokenList) # [11, 'end']
#
# tokenList = [9, '*', 11, 'end']
# tree = Tree.getProduct(tokenList)
# Tree.printTreePostOrder(tree)  # 9 11 *
# print()
#
# tokenList = [9, '+', 11, 'end']
# tree = Tree.getProduct(tokenList)
# Tree.printTreePostOrder(tree) # 9


# tokenList = [2, '*', 3, '*', 5 , '*', 7, 'end']
# tree = Tree.getProduct(tokenList)
# Tree.printTreePostOrder(tree) # 2 3 5 7 * * *
# print()
#
# tokenList = [9, '*', 11,'+', 5, '*', 7, 'end']
# tree = Tree.getSum(tokenList)
# Tree.printTreePostOrder(tree)  # 9 11 * 5 7 * +
# print()

# tokenList = [9, '*', '(', 11,'+', 5,')', '*', 7, 'end']
# tree = Tree.getSum(tokenList)
# Tree.printTreePostOrder(tree) # 9 11 5 + 7 * *