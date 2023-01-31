import unittest as ut
import src.tree_node as tn
import src.tree_solver as ts


class TestSolver(ut.TestCase):
    def test_all_descending_one_pile(self):
        oper: list[str] = ['-1', '-3']
        arr: list[int] = []
        for i in range(8, 31):
            tree = tn.constructTree([i], oper, 5)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 8, ts.Mode.DnM):
                arr.append(i)
        self.assertEqual(arr, [13, 15])
        arr = []

        for i in range(8, 31):
            tree = tn.constructTree([i], oper, 4)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 8, ts.Mode.D):
                arr.append(i)
        self.assertEqual(arr, [12, 14])
        arr = []

        for i in range(8, 31):
            tree = tn.constructTree([i], oper, 3)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 8, ts.Mode.M):
                arr.append(i)
        self.assertEqual(arr, [9, 10, 11, 12, 13])

    def test_all_one_pile1(self):
        arr: list[int] = []
        oper: list[str] = ['+1', '*2']
        for i in range(1, 30+1):
            tree = tn.constructTree([i], oper, 5)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 30, ts.Mode.DnM):
                arr.append(i)
        self.assertEqual(arr, [13])
        arr = []

        for i in range(1, 30+1):
            tree = tn.constructTree([i], oper, 4)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 30, ts.Mode.D):
                arr.append(i)
        self.assertEqual(arr, [14])
        arr = []

        for i in range(1, 30+1):
            tree = tn.constructTree([i], oper, 2)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 30, ts.Mode.M):
                arr.append(i)
        self.assertEqual(arr, list(range(16, 31)))

    def test21_one_pile2(self):
        arr: list[int] = []
        oper: list[str] = ['+2', '*2']
        for i in range(1, 54+1):
            tree = tn.constructTree([i], oper, 5)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 54, ts.Mode.DnM):
                arr.append(i)
        self.assertEqual(arr, [22, 23])

    def test21_one_pile3(self):
        arr: list[int] = []
        oper: list[str] = ['+1', '*3']
        for i in range(1, 70+1):
            tree = tn.constructTree([i], oper, 5)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 70, ts.Mode.DnM):
                arr.append(i)
        self.assertEqual(arr, [21])

    def test21_two_piles1(self):
        arr: list[int] = []
        oper: list[str] = ['+1', '*2']
        for i in range(1, 42+1):
            tree = tn.constructTree([4, i], oper, 5)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 46, ts.Mode.DnM):
                arr.append(i)
        self.assertEqual(arr, [18])

    def test21_two_piles2(self):
        arr: list[int] = []
        oper: list[str] = ['+2', '*3']
        for i in range(1, 55+1):
            tree = tn.constructTree([7, i], oper, 5)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 62, ts.Mode.DnM):
                arr.append(i)
        self.assertEqual(arr, [17])

    def test21_two_piles3(self):
        arr: list[int] = []
        oper: list[str] = ['+1', '*2']
        for i in range(1, 43+1):
            tree = tn.constructTree([4, i], oper, 5)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 47, ts.Mode.DnM):
                arr.append(i)
        self.assertEqual(arr, [20])

    def test_all_one_pile_27416(self):
        arr: list[int] = []
        oper: list[str] = ['+1', '*2']
        for i in range(1, 69+1):
            tree = tn.constructTree([7, i], oper, 5)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 76, ts.Mode.DnM):
                arr.append(i)
        self.assertEqual(arr, [30, 33])
        arr = []

        for i in range(1, 69+1):
            tree = tn.constructTree([7, i], oper, 4)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 76, ts.Mode.D):
                arr.append(i)
        self.assertEqual(arr, [31, 34])
        arr = []

        for i in range(1, 69+1):
            tree = tn.constructTree([7, i], oper, 3)
            # print(tree.__repr__(0, True))
            if ts.TreeSolver.solveTree(tree, 76, ts.Mode.M):
                arr.append(i)
        self.assertEqual(arr, list(range(18, 69)))


if __name__ == '__main__':
    ut.main()
