from map.services.dijkstra import dijkstra
from map.services.graph import Graph
from math import radians, cos, sin, asin, sqrt

class Vertex:
  ''' Standard vertex class modified to include point coordinates '''
  def __init__(self, id: int, latitude: float, longitude: float) -> None:
    self.__id = id
    self.__latitude = latitude
    self.__longitude = longitude

  def __str__(self):
    """ Return a string representation of the vertex. """
    return f"{self.__id} - {self.coordinates()}"

  def element(self) -> any:
    return self.__id
  
  def coordinates(self) -> tuple:
    return (self.__latitude, self.__longitude)


class RouteMap(Graph):
  ''' Graph implementation with Adjacency List '''
  def __init__(self, filename) -> None:
    super().__init__()
    self._label_map = dict()
    self.__process_graph(filename)

  def add_vertex(self, id: int, latitude: float, longitude: float):
    ''' Adds new vertex to the Graph with element `e` '''
    new_vertex = Vertex(id, latitude, longitude)
    self._adj_map[new_vertex] = dict()
    self._label_map[id] = new_vertex
    return new_vertex
  
  def get_vertex_by_id(self, id: float):
    return self._label_map[id]
  
  def __process_graph(self, filename):
    file = open(filename)
    line = file.readline()

    while line == 'Node\n':
      id = file.readline()
      id = int(id.split()[1])

      gps = file.readline().split()
      latitude, longitude = float(gps[1]), float(gps[2])
      self.add_vertex(id, latitude, longitude)
      line = file.readline()

    while line == 'Edge\n':
      from_id = file.readline()
      from_id = int(from_id.split()[1])
      v1 = self.get_vertex_by_id(from_id)

      to_id = file.readline()
      to_id = int(to_id.split()[1])
      v2 = self.get_vertex_by_id(to_id)

      length = file.readline()
      length = float(length.split()[1])

      time = file.readline()
      time = float(time.split()[1])

      self.add_edge(v1, v2, time)

      file.readline()
      line = file.readline()
  
  def find_route(self, source, target) -> tuple:
    '''
      Finds the shortest route between the `source` and the `target`. The input parameters must both be either:

      - `integers` where each int represents a Vertex ID
      - `tuples` in the format (longitude, latitude), which represents the coordinates of each point

      Returns tuple in format `(list of vertices, distance)`
    '''
    # Type validate the parameters
    if type(source) == tuple and type(target) == tuple:
      start = self.__find_closest_vertex(source[0], source[1])
      destination = self.__find_closest_vertex(target[0], target[1])

    elif type(source) == int and type:
      start = self.get_vertex_by_id(source)
      destination = self.get_vertex_by_id(target[0], target[1])

    else:
      raise TypeError("Source and target parameters must be of the same type of either int or tuple.")
    
    results = dijkstra(self, start, destination, True)

    path = [destination]
    v = destination

    while v is not start:
      v = results[v][1]
      path.append(v)

    path.reverse()
    return (path, results[destination][0])
  
  def __find_closest_vertex(self, latitude: float, longitude: float):
    closest_vertex = None
    closest_distance = None

    for v in self.vertices():
      v_lat, v_long = v.coordinates()
      distance = self.__calculate_haversine_distance(latitude, longitude, v_lat, v_long)

      if closest_distance == None or distance < closest_distance:
        closest_distance = distance
        closest_vertex = v

    return closest_vertex
  
  def __calculate_haversine_distance(self, latitude1: float, longitude1: float, latitude2: float, longitude2: float):
    # Source: https://medium.com/analytics-vidhya/finding-nearest-pair-of-latitude-and-longitude-match-using-python-ce50d62af546
    lat1, long1, lat2, long2 = map(radians, [latitude1, longitude1, latitude2, longitude2])
    
    diff_long = long2 - long1
    diff_lat = lat2 - lat1

    a = sin(diff_lat/2)**2 + cos(lat1) * cos(lat2) * sin(diff_long/2)**2
    c = 2 * asin(sqrt(a)) 
    metres = 6.371 * c
    return metres