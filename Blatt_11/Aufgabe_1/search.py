def breitensuche(graph):
    # 0 = unvisted, 1 = in search, 2 = visited
    nodes = {k:0 for k in list(graph.keys())}

    nodequeue = [0]
    visitedNodes = []

    while nodequeue:
        currentNode = nodequeue.pop(0)
        state = nodes[currentNode]
        if state == 0:
            nodes[currentNode] = 1
            state = 1
        

        if state == 1:
            visitedNodes.append(currentNode)
            nodes[currentNode] = 2
            childNodes = graph[currentNode]
            for child in childNodes:
                if nodes[child] == 0:
                    nodequeue.append(child)
                    nodes[child] = 1
        
        if state == 2:
            # node already visted
            pass

    return visitedNodes



def tiefensuche(graph, tosearch=0, nodes=None, visited=None):
    if nodes is None:
        # 0 = unvisted, 1 = in search, 2 = visited
        nodes = {k:0 for k in list(graph.keys())}
    
    if visited is None:
        visited = []
    
    if nodes[tosearch] == 0:
        nodes[tosearch] = 1

    for child in graph[tosearch]:
        if nodes[child] == 0:
            tiefensuche(graph, child, nodes, visited)

    nodes[tosearch] = 2
    visited.append(tosearch)
    return visited



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

    print("breitensuche: ")
    visitSeq = breitensuche(graph)
    print(visitSeq)

    print("tiefensuche: ")
    visitSeq = tiefensuche(graph)
    print(visitSeq)


main()