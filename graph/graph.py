from collections import deque

def bfs(adj, src):
    # Inicia uma fila q
    q = deque([src])

    # Inicia o vetor de visitados
    visited = [False for _ in range(len(adj))]

    # Visita src
    visited[src] = True

    # Inicia o laço que verifica o atual e visita os vizinhos
    while q:
        u = q.popleft()  # Remove e retorna um elemento do lado esquerdo da fila
        print(u)  # Visita u

        # Visita os vizinhos de u
        for v in adj[u]:
            if not visited[v]:
                q.append(v)  # Adiciona v ao final da fila
                visited[v] = True  # Marca v como visitado

    return visited

# Lista de adjacências de exemplo
from collections import deque

def bfs(adj, src):
    # Inicia uma fila q
    q = deque([src])

    # Inicia o vetor de visitados
    visited = [False for _ in range(len(adj))]

    # Visita src
    visited[src] = True

    # Inicia o laço que verifica o atual e visita os vizinhos
    while q:
        u = q.popleft()  # Remove e retorna um elemento do lado esquerdo da fila
        print(u)  # Visita u

        # Visita os vizinhos de u
        for v in adj[u]:
            if not visited[v]:
                q.append(v)  # Adiciona v ao final da fila
                visited[v] = True  # Marca v como visitado

    return visited

# Lista de adjacências de exemplo
adj = [
    [1, 4],  # Vértice 0
    [0, 2, 4],  # Vértice 1
    [1, 3],  # Vértice 2
    [2, 4, 5],  # Vértice 3
    [0, 1, 3],  # Vértice 4
    [3, 6],  # Vértice 5
    [5, 7],  # Vértice 6
    [6, 8],  # Vértice 7
    [7]  # Vértice 8
]


# Executa o BFS a partir do vértice 0
bfs(adj, 0)

