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

  def bfs(self, v):
    self.visitados[v - 1] = True
    fila = [v - 1]

    while len(fila) > 0:
      v = fila[0]

      for u in range(self.vertices):
        if self.grafo[v][u] == 1:
          if self.visitados[u] == False:
            self.visitados[u] = True
            fila.append(u)
            print('%d visitado' % (u + 1))

      fila.pop(0)



g = Grafo(10)

g.show()

print('')

g.add_aresta(1, 2)
g.add_aresta(1, 3)
g.add_aresta(1, 4)
g.add_aresta(2, 5)
g.add_aresta(3, 6)
g.add_aresta(3, 7)
g.add_aresta(4, 8)
g.add_aresta(5, 9)
g.add_aresta(6, 10)

g.show()

print('')

g.bfs(1)
