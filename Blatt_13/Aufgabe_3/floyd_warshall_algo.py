import copy


inf = float("inf")
null = "NULL"

class InputGraph:
    def __init__(self):
        self.edges = [
            [inf, inf, inf, inf,  -1, inf,],
            [1,   inf, inf, 2,   inf, inf,],
            [inf, 2,   inf, inf, inf, -8, ],
            [-4,  inf, inf, inf, 3,   inf,],
            [inf, 7,   inf, inf, inf, inf,],
            [inf, 5,   10,  inf, inf, inf,],
        ]


class SolveFloyd:
    def __init__(self, initgraph):
        self.initgraph = initgraph
        self.edges = self.constructEdges()
        self.distmatrix = copy.deepcopy(self.initgraph.edges)
        self.vorgaengermatrix = [[null]*len(initgraph.edges)
                                 for _ in range(len(initgraph.edges))]
        
        for node, edges in self.edges.items():
            for destNode in edges.keys():
                self.vorgaengermatrix[node][destNode] = node


    def constructEdges(self):
        edges = {node: {edge: value for edge, value in enumerate(self.initgraph.edges[node]) if value != inf}
                 for node in range(len(self.initgraph.edges))}

        return edges

    def solve(self):
        vlen = len(self.edges.keys()) 
        for k in range(vlen):
            for i in range(vlen):
                for j in range(vlen):
                    self.distmatrix

        

    def printState(self):

        print("dist matrix:")
        print("|     |  1  |  2  |  3  |  4  |  5  |  6  |")
        for i, vec in enumerate(self.distmatrix):
            vec2str = "|".join([f"{elem:^5}" for elem in vec])
            print(f"|{i+1:^5}|{vec2str}|")
        print()

        print("vorgänger matrix:")
        print("|     |  1  |  2  |  3  |  4  |  5  |  6  |")
        for i, vec in enumerate(self.vorgaengermatrix):
            vec2str = "|".join([f"{elem+1:^5}" if type(elem) ==
                               int else f"{elem:^5}" for elem in vec])
            print(f"|{i+1:^5}|{vec2str}|")
        print()


def main():
    inp = InputGraph()
    solve = SolveFloyd(inp)
    solve.solve()


main()
