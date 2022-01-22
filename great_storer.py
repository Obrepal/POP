class Great_storer(object):
  def __init__(self, G, current_roads = []):
    self.current_roads = current_roads
    self.G = G
  
  def add_new_road(self, path):
    self.current_roads.append(path) 
  
  def get_current_roads(self):
    return self.current_roads

  def createPath(self, oldPath, newNode):

    fuel = oldPath.get_fuel_end() + self.G[oldPath.get_last_node()][newNode]['weight']
    if newNode not in oldPath.get_road():
      # print("CHECKE",oldPath.get_road(), newNode)
      fuel -= self.G.nodes[newNode]['spice']
      
      
    goal_function  = oldPath.get_goal_function() - self.G.nodes[newNode]['spice']  - 2* (self.G[oldPath.get_last_node()][newNode]['weight'])
    
    Road = oldPath.get_road() + [newNode]
    newPath = Path(Road, newNode, goal_function, fuel) # na zmęczeniu poprawiłem na [] oraz dodałem linikję pod
    # newPath.append_road(newNode)
    self.current_roads.append(newPath)

  def find_lowest_goal_function(self):
    self.current_roads.sort(key=lambda x: x.get_goal_function(), reverse=True)
    #curr.sort(key=lambda x: x.get_goal_function(), reverse=True)
    return self.current_roads.pop(0)

  def sort_roads(self):
         self.current_roads.sort(key=lambda x: x.get_goal_function(), reverse=True)
        #curr.sort(key=lambda x: x.get_goal_function(), reverse=True)


 
