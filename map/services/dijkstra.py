from map.services.apq import BinaryHeapAPQ, UnsortedAPQ
from map.services.graph import Graph, Vertex

def dijkstra(graph: Graph, s: Vertex, d = None, binary_heap: bool = True):
  ''' Find the shortest path from the start vertex `s`
      Optional: `d` is the destination 
  '''
  if binary_heap:
    open = BinaryHeapAPQ()
  else:
    open = UnsortedAPQ()
  locs = dict()
  closed = dict()
  preds = dict()
  preds[s] = None

  s_apq = open.add_item(0, s)
  locs[s] = s_apq

  while len(open) > 0:
    # remove the min element v and its cost (key) from open
    (cost, vertex) = open.remove_min() # Returns v in form (key, vertex)

    # remove the entry for v from locs and preds (which returns predecessor)
    predecessor = preds[vertex]
    preds.pop(vertex)
    locs.pop(vertex)

    # add an entry for v:(cost, predecessor) into closed
    closed[vertex] = (cost, predecessor)

    if vertex == d:
      break

    # for each edge e from v
    edges = graph.get_edges_on(vertex)
    for e in edges:
      opposite = e.opposite_to(vertex)

      if opposite not in closed:
        # new_cost is v's key plus e's cost     
        new_cost = cost + e.cost()

        # if w is not in locs //i.e. not yet added into open
        if opposite not in locs:
          preds[opposite] = vertex
          o_apq = open.add_item(new_cost, opposite)
          locs[opposite] = o_apq

        elif new_cost < open.get_key(locs[opposite]):
          # else if newcost is better than w's oldcost
          preds[opposite] = vertex
          open.update_key(locs[opposite], new_cost)
  return closed