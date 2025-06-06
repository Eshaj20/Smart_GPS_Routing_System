class UnionFind:
    """ Implements Union-Find (Disjoint Set) for cycle detection. """
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, node):
        """ Finds the root of the node with path compression. """
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        """ Merges two subsets into one. """
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            self.parent[root2] = root1
