import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def test_height(self):
        self.assertEqual(1, Tree(4).height())

        self.assertEqual(2, Tree(1, 
            Tree(0)).height())

        self.assertEqual(3, Tree(10, Tree(5, Tree(3), Tree(7)), Tree(15)).height())

    def test_as_list(self):
        self.assertEqual(Tree(10).as_list(), [10])
        self.assertEqual(Tree(10, Tree(5, Tree(3), Tree(7)), Tree(15)).as_list(), [3, 5, 7, 10, 15])

    def test_add_mutable(self):
        self.assertEqual(Tree(10).add_mutable(15, 5, 3, 7).as_list(), [3, 5, 7, 10, 15])
        self.assertEqual(Tree(1).add_mutable(2, 3, 4, 5).as_list(), [1, 2, 3, 4, 5])

    def test_add_immutable(self):
        self.assertEqual(Tree(10).add_immutables(15, 5, 3, 7).as_list(), [3, 5, 7, 10, 15])
        self.assertEqual(Tree(1).add_immutables(2, 3, 4, 5).as_list(), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
