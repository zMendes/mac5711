def dfs (G):
    for u in V(G):
        color[u] = branco
    tempo = 0

    Q = []
    Q.add(V(G)[0])
    u = null
    while Q != null:
        v = Q.pop() # gets last element
        if color[v] = branco
            tempo = tempo + 1
            d[v] = tempo
            color[v] = cinza
            parent[v] = u
            Q.add(v)
            for i in V.adjacents:
                if color[i] = branco:
                    Q.add(i)
            u = v
        if color[v] = cinza:
            color[v] = preto
            tempo = tempo + 1
            f[v] = tempo
