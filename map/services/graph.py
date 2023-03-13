class Vertex:
  def __init__(self, el) -> None:
    self.__element = el

  def __str__(self):
    """ Return a string representation of the vertex. """
    return str(self.__element)

  def element(self) -> any:
    return self.__element


class Edge:
  def __init__(self, v1: Vertex, v2: Vertex, cost: float) -> str:
    self.__vertices = (v1, v2)
    self.__cost = cost

  def __str__(self):
    """ Return a string representation of this edge. """
    return ('(' + str(self.__vertices[0]) + ' --> '
                + str(self.__vertices[1]) + ' : '
                + str(self.__cost) + ')')

  def cost(self) -> float:
    return self.__cost

  def start(self):
    return self.__vertices[0]

  def end(self):
    return self.__vertices[1]
  
  def opposite_to(self, vertex):
    ''' Returns the opposite vertex to the given `vertex` if it exists in this Edge '''
    if self.__vertices[0] == vertex:
      return self.__vertices[1]
    
    elif self.__vertices[1] == vertex:
      return self.__vertices[0]
    
    else:
      return None
  
  def vertices(self):
    return self.__vertices


class Graph:
  ''' Graph implementation with Adjacency List '''
  def __init__(self) -> None:
    self._adj_map = dict()

  def __str__(self):
    result = ""
    for vertex in self._adj_map:
        result += f"{vertex}: {self._adj_map[vertex]}\n"
    return result

  def vertices(self) -> list:
    ''' Returns a list of all vertices in the graph '''
    return list(self._adj_map.keys())

  def edges(self) -> list:
    ''' Returns a list of all edges in the graph '''
    all_edges = []

    for v in self._adj_map:
      for w in self._adj_map[v]:
        if self._adj_map[v][w].start() == v:
          all_edges.append(self._adj_map[v][w])

    return all_edges

  def num_vertices(self) -> int:
    ''' Returns the vertices of edges in the graph '''
    return len(self._adj_map)

  def num_edges(self) -> int:
    ''' Returns the number of edges in the graph '''
    count = 0
    for v in self._adj_map:
      count += len(self._adj_map[v])
    return count // 2

  def get_edges_on(self, v: Vertex) -> list:
    ''' Returns a list of the edges incident on `v` (a vertex) '''
    if v in self._adj_map:
      all_edges = []

      for w in self._adj_map[v]:
        all_edges.append(self._adj_map[v][w])
      return all_edges
    
    return None

  def degree(self, v: Vertex):
    ''' Returns the degree of vertex `v` '''
    return len(self._adj_map[v])

  def add_vertex(self, el: any):
    ''' Adds new vertex to the Graph with element `e` '''
    new_vertex = Vertex(el)
    self._adj_map[new_vertex] = dict()
    return new_vertex

  def add_edge(self, v1: Vertex, v2: Vertex, el: any):
    ''' Adds a new edge between vertices `x` and `y`, with element `e` '''
    if v1 not in self._adj_map or v2 not in self._adj_map:
      return None
    
    new_edge = Edge(v1, v2, el)
    self._adj_map[v1][v2] = new_edge
    self._adj_map[v2][v1] = new_edge
    return new_edge
  
  def get_vertex_by_label(self, el: any):
    for vertex in self.vertices():
      if vertex.element() == el:
        return vertex
    return None
  
