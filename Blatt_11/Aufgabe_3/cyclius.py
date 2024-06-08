
def checkCycle(graph, tosearch=0, nodes=None):
    if nodes is None:
        # 0 = unvisted, 1 = in search, 2 = visited
        nodes = {k:0 for k in list(graph.keys())}
        
    if nodes[tosearch] == 0:
        nodes[tosearch] = 1

    for child in graph[tosearch]:
        if nodes[child] == 0:
            checkCycle(graph, child, nodes)
        if nodes[child] == 1:
            print(f"cycle from node {tosearch} to {child}")

    nodes[tosearch] = 2



def main():
    graph = {
        0: [1, 2, 6],
        1: [3],
        2: [0, 3, 4],
        3: [6],
        4: [0, 8],
        5: [2, 3, 4],
        6: [7],
        7: [8],
        8: [5]
    }

    checkCycle(graph)


main()