from vertex import Vertex

class Graph:
  def __init__(self):
    self.graph_dict = {}

  def add_vertex(self, node):
    self.graph_dict[node.value] = node

  def add_edge(self, from_node, to_node, weight = 0):
    self.graph_dict[from_node.value].add_edge(to_node.value, weight)
    self.graph_dict[to_node.value].add_edge(from_node.value, weight)

  def explore(self):
    print("Exploring the graph....\n")
    
    current_room = 'entrance'
    path_total = 0
    print("\nStarting off at the {zero}\n".format(zero=current_room))

    while current_room != 'treasure room':
      node = self.graph_dict[current_room]

      for connected_room, weight in node.edges.items():
        key = connected_room.value[:1]
        print("enter {zero} for {one}: {two} cost".format(zero=key, one=connected_room.value, two=weight))
      
      valid_choices = [i.value[:1] for i in node.edges.keys()]
      print("\nYou have accumulated: {zero} cost".format(zero=path_total))

      choice = input("\nWhich room do you move to? ")

      if not choice in valid_choices:
        print("please select from these letters: {zero}".format(zero=valid_choices))
      else:
        for room in node.edges.keys():
          if room.value.startswith(choice):
            current_room = room.value
            #print(node.edges)
            path_total += node.edges[room]
        print("*** You have chosen: {zero} ***\n".format(zero=current_room))
    print("Made it to the treasure room with {0} cost".format(path_total))



  def print_map(self):
    print("\nMAZE LAYOUT\n")
    for node_key in self.graph_dict:
      print("{0} connected to...".format(node_key))
      node = self.graph_dict[node_key]
      for adjacent_node, weight in node.edges.items():
        print("=> {0}: cost is {1}".format(adjacent_node.value, weight))
      print("")
    print("")

def build_graph():
  graph = Graph()
  
  # MAKE ROOMS INTO VERTICES BELOW...
  entrance = Vertex("entrance")
  ante_chamber = Vertex("ante-chamber")
  kings_room = Vertex("king's room")
  grand_gallery = Vertex("grand gallery")
  treasure_room = Vertex("treasure room")

  # ADD ROOMS TO GRAPH BELOW...
  graph.add_vertex(entrance)
  graph.add_vertex(ante_chamber)
  graph.add_vertex(kings_room)
  graph.add_vertex(grand_gallery)
  graph.add_vertex(treasure_room)
  
  # ADD EDGES BETWEEN ROOMS BELOW...
  entrance.add_edge(ante_chamber, 7)
  entrance.add_edge(kings_room, 3)
  ante_chamber.add_edge(grand_gallery, 5)
  ante_chamber.add_edge(entrance, 7)
  kings_room.add_edge(ante_chamber, 1)
  kings_room.add_edge(entrance, 3)
  grand_gallery.add_edge(ante_chamber, 2)
  grand_gallery.add_edge(kings_room, 2)
  grand_gallery.add_edge(treasure_room, 4)
  treasure_room.add_edge(ante_chamber, 6)
  treasure_room.add_edge(grand_gallery, 4)

  
  graph.print_map()
  return graph
