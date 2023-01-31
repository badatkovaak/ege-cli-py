from typing import Iterator
from typing_extensions import Self


class TreeNode:
    def __init__(self, values: list[int], oper: str, children: list[Self], depth: int = 0, operlen: int = 0) -> None:
        self.values = values
        self.oper = oper
        self.children = children
        self.depth = depth
        self.operlen = operlen
        self.isWinning = False
        self.isOver = False

    def __repr__(self, level: int = 0, full: bool = False) -> str:
        res: str = ''
        # if level == 0:
        #     res += str(self.isWinning)+'\n'

        for i in range(level):
            res += '\t\t'
            type(i)
        if full:
            for value in self.values:
                res += str(value) + ','
            res += str(self.isWinning)
        else:
            if self.isOver:
                res += '(!) '
            else:
                for value in self.values:
                    res += str(value) + ','
        res += '\n'
        for child in self.children:
            res += child.__repr__(level+1, full)
        return res

    def performOper(self, oper: str, index: int) -> list[int]:
        arr: list[int] = self.values.copy()
        match oper[0]:
            case '+': arr[index] += int(oper[1:])
            case '*': arr[index] *= int(oper[1:])
            case '-': arr[index] -= int(oper[1:])
            case _: pass
        return arr

    def getLeaves(self) -> Iterator[Self]:
        node: Self = self
        stack: list[Self] = [node]

        while stack:
            node = stack.pop()
            if len(node.children) == 0:
                yield node
            else:
                for child in node.children:
                    stack.append(child)

    def getNodes(self) -> Iterator[Self]:
        node: Self = self
        stack: list[Self] = [node]

        while stack:
            node = stack.pop()
            yield node
            if len(node.children) == 0:
                continue
            else:
                for child in node.children:
                    stack.append(child)

    def getNthNodes(self, depth: int) -> Iterator[Self]:
        node: Self = self
        stack: list[tuple[Self, int]] = [(node, depth)]

        while stack:
            node, depth = stack.pop()
            if depth == 1:
                yield node
            if len(node.children) == 0:
                continue
            else:
                for child in node.children:
                    stack.append((child, depth-1))


def constructTree(startValues: list[int], oper: list[str], depth: int) -> TreeNode:
    st: str = '+'
    if oper[0][0] == '-':
        st = '-'
    root: TreeNode = TreeNode(startValues, st, [], depth)

    for i in range(1, depth):
        for child in root.getLeaves():
            if i == depth - 1:
                for j in range(len(child.values)):
                    child.children.append(
                        TreeNode(child.performOper(oper[-1], j), oper[-1], []))
            else:
                for j in range(len(child.values)):
                    for op in oper:
                        child.children.append(
                            TreeNode(child.performOper(op, j), op, []))

    return root
