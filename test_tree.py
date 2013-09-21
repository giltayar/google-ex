import unittest
import random
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

    def test_as_balanced(self):
        self.assertEqual(Tree(1).add_immutables(2, 3, 4, 5, 6, 7).as_balanced().height(), 3)
        self.assertEqual(Tree(1).add_immutables(2, 3, 4, 5, 6, 7, 8).as_balanced().height(), 4)
        self.assertEqual(Tree(10).add_mutable(15, 12, 11, 20, 25, 5, 3, 7, 
                1, 4, 6, 8).as_balanced().height(), 4)


    def test_add_mutable(self):
        self.assertEqual(Tree(10).add_mutable(15, 5, 3, 7).as_list(), [3, 5, 7, 10, 15])
        self.assertEqual(Tree(1).add_mutable(2, 3, 4, 5).as_list(), [1, 2, 3, 4, 5])

    def test_add_immutable(self):
        self.assertEqual(Tree(10).add_immutables(15, 5, 3, 7).as_list(), [3, 5, 7, 10, 15])
        self.assertEqual(Tree(1).add_immutables(2, 3, 4, 5).as_list(), [1, 2, 3, 4, 5])

    def test_del_mutable(self):
        t = Tree(10).add_immutables(15, 5, 3, 7) 
        self.assertEqual(t.del_mutable(15).as_list(),
                         [3, 5, 7, 10])
        self.assertEqual(t.del_mutable(5).as_list(),
                         [3, 7, 10])
        self.assertEqual(t.del_mutable(10).as_list(),
                         [3, 7])

        t = Tree(10).add_mutable(15, 12, 11, 20, 25, 5, 3, 7, 
                1, 4, 6, 8)

        self.assertEqual(t.as_list(),
                [1, 3, 4, 5, 6, 7, 8, 10,
                    11, 12, 15, 20, 25])
        self.assertEqual(t.del_mutable(25).as_list(),
                [1, 3, 4, 5, 6, 7, 8, 10,
                    11, 12, 15, 20])
        self.assertEqual(t.del_mutable(11).as_list(),
                [1, 3, 4, 5, 6, 7, 8, 10,
                    12, 15, 20])
        self.assertEqual(t.del_mutable(8).as_list(),
                [1, 3, 4, 5, 6, 7, 10,
                    12, 15, 20])
        self.assertEqual(t.del_mutable(1).as_list(),
                [3, 4, 5, 6, 7, 10,
                    12, 15, 20])
        self.assertEqual(t.del_mutable(7).as_list(),
                [3, 4, 5, 6, 10,
                    12, 15, 20])
        self.assertEqual(t.del_mutable(3).as_list(),
                [4, 5, 6, 10,
                    12, 15, 20])
        self.assertEqual(t.del_mutable(10).as_list(),
                [4, 5, 6,
                    12, 15, 20])

    def test_del_immutable(self):
        t = Tree(10).add_immutables(15, 5, 3, 7) 
        t = t.del_mutable(15)
        self.assertEqual(t.as_list(),
                         [3, 5, 7, 10])
        t = t.del_mutable(5)
        self.assertEqual(t.as_list(),
                         [3, 7, 10])
        t = t.del_mutable(10)
        self.assertEqual(t.as_list(),
                         [3, 7])

        t = Tree(10).add_mutable(15, 12, 11, 20, 25, 5, 3, 7, 
                1, 4, 6, 8)

        self.assertEqual(t.as_list(),
                [1, 3, 4, 5, 6, 7, 8, 10,
                    11, 12, 15, 20, 25])
        t = t.del_mutable(25)
        self.assertEqual(t.as_list(),
                [1, 3, 4, 5, 6, 7, 8, 10,
                    11, 12, 15, 20])
        t = t.del_mutable(11)
        self.assertEqual(t.as_list(),
                [1, 3, 4, 5, 6, 7, 8, 10,
                    12, 15, 20])
        t = t.del_mutable(8)
        self.assertEqual(t.as_list(),
                [1, 3, 4, 5, 6, 7, 10,
                    12, 15, 20])
        t = t.del_mutable(1)
        self.assertEqual(t.as_list(),
                [3, 4, 5, 6, 7, 10,
                    12, 15, 20])
        t = t.del_mutable(7)
        self.assertEqual(t.as_list(),
                [3, 4, 5, 6, 10,
                    12, 15, 20])
        t = t.del_mutable(3)
        self.assertEqual(t.as_list(),
                [4, 5, 6, 10,
                    12, 15, 20])
        t = t.del_mutable(10)
        self.assertEqual(t.as_list(),
                [4, 5, 6,
                    12, 15, 20])

    def test_random_mutable_adds_and_deletes(self):
        t = Tree(10)
        s = {10}
        for _ in range(100):
            r = random.randint(0, 100000000)
            t.add_mutable(r)
            s.add(r)

            self.assertEqual(t.as_list(), sorted(s))

        for i in range(99):
            r = random.choice(list(s))
            t.del_mutable(r)
            s.remove(r)

            self.assertEqual(t.as_list(), sorted(s), "problem in {}th delete".format(i))

    def test_random_immutable_adds_and_deletes(self):
        t = Tree(10)
        s = {10}
        for _ in range(100):
            r = random.randint(0, 100000000)
            t = t.add_mutable(r)
            s.add(r)

            self.assertEqual(t.as_list(), sorted(s))

        for i in range(99):
            r = random.choice(list(s))
            t = t.del_mutable(r)
            s.remove(r)

            self.assertEqual(t.as_list(), sorted(s), "problem in {}th delete".format(i))
if __name__ == '__main__':
    unittest.main()
