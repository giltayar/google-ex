import unittest
from dag import Dag

class TestDag(unittest.TestCase):
    def test_djikstra(self):
        dag = Dag()
        a, b, c, d = dag.add_vertices(4)
        dag.add_edge(a, b, 3)
        dag.add_edge(a, c, 4)
        dag.add_edge(b, d, 4)
        dag.add_edge(c, d, 1)

        self.assertEqual(dag.djikstra(a, d), (5, [a, c, d]))

    def test_difficult_dag(self):
        dag = Dag()

        v = dag.add_vertices(10)

        dag.add_edge(v[0], v[1], 1)
        dag.add_edge(v[0], v[2], 2)
        dag.add_edge(v[1], v[2], 5)
        dag.add_edge(v[1], v[3], 1)
        dag.add_edge(v[2], v[4], 2)
        dag.add_edge(v[3], v[2], 3)
        dag.add_edge(v[3], v[4], 1)
        dag.add_edge(v[4], v[5], 2)

        self.assertEqual(dag.djikstra(v[0], v[5]), (5, [v[0], v[1], v[3], v[4], v[5]]))

        dag.add_edge(v[2], v[5], 1)
        self.assertEqual(dag.djikstra(v[0], v[5]), (3, [v[0], v[2], v[5]]))
