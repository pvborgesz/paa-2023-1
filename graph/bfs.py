from collections import deque
import heapq

class Graph:

  def __init__(self, V):
    self.V = V
    self.E = 0
    self.adj = [[] for _ in range(V)]

  def addEdge(self, u, v, w=1):
    self.adj[u].append((v, w))
    self.E += 1

  def addNonDirectedEdge(self, u, v, w=1):
    self.addEdge(u, v, w)
    self.addEdge(v, u, w)

  def bfs(self, src):
    q = [src]
    visited = [False] * self.V
    visited[src] = True
    while len(q) > 0:
      atual = q[0]
      q.pop(0)
      #visita
      print(atual)
      for neigh, _ in self.adj[atual]:
        if not visited[neigh]:
          q.append(neigh)
          visited[neigh] = True

  def dfs(self, src):
    visited = [False] * self.V
    visited[src] = True

    def visit(self, node):
      #visitar o node
      print(node)
      for neigh, _ in self.adj[node]:
        if not visited[neigh]:
          visited[neigh] = True
          visit(self, neigh)

    visit(self, src)

  def bicoloring(self):
    NOCOLOR = -1
    GREEN = 0
    RED = 1
    color = [NOCOLOR] * self.V

    def visit(self, node, myColor):
      if color[node] != NOCOLOR:
        return color[node] == myColor

      color[node] = myColor
      if myColor == GREEN:
        otherColor = RED
      else:
        otherColor = GREEN
      #visitar o node
      print(node)
      for neigh, _ in self.adj[node]:
        if not visit(self, neigh, otherColor):
          return False
      return True

    return visit(self, 0, GREEN)

  def topsort(self) -> List:
    # passo 1: inicia o indegree
    inDegree = [0] * self.V
    for u in range(self.V):
      for v in self.adj[u]:
        inDegree[v] += 1
    #passo 2: inicia a fila q
    q = deque()
    for u, degree in enumerate(inDegree):
      if degree == 0:
        q.append(u)
    #passo 3: loop principal na fila q
    ret = []
    while (len(q) > 0):
      w = q.popleft()
      ret.append(w)
      for neigh, _ in self.adj[w]:
        inDegree[neigh] -= 1
        if inDegree[neigh] == 0:
          q.append(neigh)
    #passo 4: retorna o ret
    return ret

  def dijkstra(self, src):
    #passo 1: inicia d, ant, visited
    d = [float("inf")] * self.V
    ant = [None] * self.V
    visited = [False] * self.V
    d[src] = 0  #marca distancia de src para si mesmo como zero

    q = []
    heapq.heappush(q, (0, src))
    while len(q)>0:
      #passo 2: escolher o no de trabalho w
      '''for u, dCost in enumerate(d):
        if w == None:
          if visited[u] == False:
            w = u
        elif visited[u] == False and d[u] < d[w]:
          w = u
      if w==None or d[w]==float("inf"): #todos os nos foram visitados
        break
      '''
      _, w = heapq.heappop(q)
      if visited[w]:
        continue
      visited[w] = True
      #passo 3: atualizar d e ant dos vizinhos de w
      for neigh, weight in self.adj[w]:
        if d[w]+weight < d[neigh]:
          d[neigh] = d[w]+weight
          ant[neigh] = w
          heapq.heappush(q, (d[neigh], neigh))
    return d

  def kruskal(self):
    edges = []
    for src in range(self.V):
      for dst, weight in self.adj[src]:
        if dst>=src:
          edges.append( (weight, src, dst) )
    edges.sort()

    color = []
    for u in range(self.V):
      color.append(u)
    
    sum = 0
    for weight, src, dst in edges:
      if color[src]!=color[dst]:
        sum += weight
        aux = color[dst]
        for i in range(self.V):
          if color[i]==aux:
            color[i] = color[src]
        
    
    return sum

  def Prim(self):
    d = [float('inf')]*self.V
    visited = [False]*self.V
    d [0] = 0
    h = [(0,0)]

    ret = 0
    while h:
      _, w = heapq.heappop(h)
      if visited[w]:
        continue
      visited[w] = True
      ret += d[w]

      for neigh, neighCost in self.adj[w]:
        if neighCost<d[neigh]:
          d[neigh] = neighCost
          heapq.heappush(h, (d[neigh], neigh))

    return ret

g = Graph(5)

print(g.adj)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 4)
g.addEdge(1, 0)
g.addEdge(1, 3)
g.addEdge(2, 0)
g.addEdge(3, 1)
g.addEdge(3, 4)
g.addEdge(4, 0)
g.addEdge(4, 3)
print(g.adj)
#G = [ [1, 4, 2], [0, 3], [0],[4, 1],[3, 0]]

#g.bfs(0)

g.dfs(0)

print(g.bicoloring())

g.addEdge(2, 4)
g.addEdge(4, 2)

print(g.bicoloring())
