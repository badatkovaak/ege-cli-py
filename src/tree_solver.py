import src.tree_node as tn
from enum import Enum


class Mode(Enum):
    D = 'does'
    M = 'might'
    DnM = 'doesAndMight'


class TreeSolver:
    def __init__(self) -> None:
        pass

    @staticmethod
    def evalNodes(root: tn.TreeNode, max: int) -> None:
        isDescending: bool = root.oper[0] == '-'
        for node in root.getNodes():
            if isDescending:
                if sum(node.values) < max:
                    node.isOver = True
            else:
                if sum(node.values) > max:
                    node.isOver = True

    @staticmethod
    def solveTree(root: tn.TreeNode, max: int, mode: Mode, depth: int = 3):
        def solveSimpleCase(root: tn.TreeNode, mode: str, depth: int = -1):
            if depth == -1:
                depth = root.depth

            for i in reversed(range(1, depth + 1)):
                condition = i % 2 == depth % 2
                for node in root.getNthNodes(i):
                    if node.isOver:
                        if condition:
                            node.isWinning = True
                        else:
                            node.isWinning = False
                    elif i == depth:
                        if node.isOver:
                            node.isWinning = True
                        else:
                            node.isWinning = False
                    else:
                        if not condition and mode == 'does':
                            if len(list(filter((lambda child: child.isWinning), node.children))) > 0:
                                node.isWinning = True
                            else:
                                node.isWinning = False
                        elif condition and mode == 'does':
                            if len(list(filter((lambda child: not child.isWinning), node.children))) == 0:
                                node.isWinning = True
                            else:
                                node.isWinning = False
                        elif mode == 'might':
                            mylen = len(
                                list(filter((lambda child: child.isWinning), node.children)))
                            if mylen > 0:
                                node.isWinning = True
                            else:
                                node.isWinning = False

        TreeSolver.evalNodes(root, max)
        result: bool = True
        match mode:
            case Mode.D:
                solveSimpleCase(root, 'does', 2)
                result = not root.isWinning
                solveSimpleCase(root, 'does')
            case Mode.M:
                solveSimpleCase(root, 'might')
            case Mode.DnM:
                solveSimpleCase(root, 'does', depth)
                result = not root.isWinning
                solveSimpleCase(root, 'does')
            case _: pass
        return result and root.isWinning
