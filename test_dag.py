import unittest
from dag import Dag

class TestDag(unittest.TestCase):
    def test_dsg(self):
        dag = Dag()
        a, b, c, d = dag.add_vertices(4)
        dag.add_edge(a, b, 3)
        dag.add_edge(a, c, 4)
        dag.add_edge(b, d, 4)
        dag.add_edge(c, d, 1)

        self.assertEqual(dag.dsg(a, d), 5)
