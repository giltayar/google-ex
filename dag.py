class Dag:
    class Vertice:
        def __init__(self):
            self.edges = {}
    def __init__(self):
        self.vertices = set()

    def add_vertices(self, n):
        res = []
        for i in range(n):
            v = Dag.Vertice()
            res.append(v)
            self.vertices.add(v)
        return res

    def add_edge(self, s, t, w):
        s.edges[t] = w
    
    def dsg(self, s, t):
        distance_to_s = {s: 0}
        unvisited = self.vertices.copy()

        def find_smallest():
            return min(((v, distance_to_s.get(v, float('inf'))) for v in unvisited), 
                    key=lambda pair: pair[1])[0]

        while unvisited:
            print("unvisited={0}".format(unvisited))
            curr = find_smallest()
            if curr == t:
                return distance_to_s[t]
            if curr is None:
                return float('inf')
            unvisited.remove(curr)
            for neighbor, weight in curr.edges.items():
                neighbor_distance = distance_to_s.get(neighbor, float('inf'))
                distance_to_s[neighbor] = min(neighbor_distance, distance_to_s[curr] + weight)

        return float('inf')
