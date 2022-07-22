# Return false if there's a negative cycle
def apsp(graph):
    n = len(graph)
    spaths = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if spaths[i][k] + spaths[k][j] < spaths[i][j]:
                    spaths[i][j] = spaths[i][k] + spaths[k][j]
    for i in range(len(spaths)):
        if spaths[i][i] < 0:
            return False
    return spaths