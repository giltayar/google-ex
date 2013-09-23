class Dag:
    class Vertice:
        def __init__(self, name):
            self.edges = {}
            self.name = name
        def __repr__(self):
            return 'Vertice({})'.format(self.name)

    def __init__(self):
        self.vertices = set()

    def add_vertices(self, n):
        res = []
        for i in range(n):
            v = Dag.Vertice(len(self.vertices) + 1)
            res.append(v)
            self.vertices.add(v)
        return res

    def add_edge(self, s, t, w):
        s.edges[t] = w
    
    def dsg(self, s, t):
        def get_path(prevs):
            res = [t]
            curr = prevs.get(t)
            while curr is not None:
                res.append(curr)
                curr = prevs.get(curr)
            return res[::-1]
        distance_to_s = {s: 0}
        unvisited = self.vertices.copy()

        def find_smallest():
            return min(((v, distance_to_s.get(v, float('inf'))) for v in unvisited), 
                    key=lambda pair: pair[1])[0]

        prevs = {}
        curr = None
        while unvisited:
            print("unvisited={0}".format(unvisited))
            curr = find_smallest()
            unvisited.remove(curr)
            if curr == t:
                return distance_to_s[t], get_path(prevs)
            if curr is None:
                return float('inf'), None
            for neighbor, weight in curr.edges.items():
                neighbor_distance = distance_to_s.get(neighbor, float('inf'))
                distance_to_s[neighbor] = min(neighbor_distance, distance_to_s[curr] + weight)
                prevs[neighbor] = curr

        return float('inf')
