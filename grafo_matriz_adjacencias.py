class Grafo:
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0] * vertices for i in range(vertices)] # matriz de adjacencias
    self.visitados = [False] * vertices
    print(self.visitados)

  # u é um ponto do arco, v é outro ponto
  def add_aresta(self, u, v):
    # grafo não-dirigido
    self.grafo[u - 1][v - 1] = 1
    self.grafo[v - 1][u - 1] = 1

  def show(self):
    for i in self.grafo:
      for j in i:
        print(j, end=' ')
      print('')

  def tem_ligacao(self, u, v):
    if self.grafo[v - 1][u - 1] == 1:
      return True
    return False

  def dfs(self, u):
    self.visitados[u - 1] = True
    print('%d visitado' % u)
    for i in range(1, self.vertices + 1):
      if self.grafo[u - 1][i - 1] == 1 and self.visitados[i - 1] == False:
        self.dfs(i)



g = Grafo(5)

# g.show()

# print('')

# g.add_aresta(1, 3) # irá adicionar arestas de 1 para 3 e de 3 para 1
# g.add_aresta(3, 4)
# g.add_aresta(2, 3)
# g.add_aresta(3, 5)
# g.add_aresta(4, 5)

# g.show()

# print('')

# print(g.tem_ligacao(1, 3)) # True
# print(g.tem_ligacao(1, 2)) # False

g.add_aresta(1, 4)
g.add_aresta(4, 2)
g.add_aresta(4, 5)
g.add_aresta(2, 5)
g.add_aresta(5, 3)

g.show()

print('')

g.dfs(1)