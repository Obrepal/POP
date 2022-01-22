class Path(object):

    def  __init__(self, road = [], last_node = 0, goal_function = 0 ,fuel_end = 0):
        
      self.road = road
      self.goal_function = goal_function
      self.fuel_end = fuel_end
      self.last_node = last_node

    def append_road(self,next_node):
      self.road.append(next_node)

    def get_road(self):
      return self.road

    def get_goal_function(self):
      return self.goal_function

    def get_fuel_end(self):
      return self.fuel_end
    
    def get_last_node(self):
      return self.road[-1]

    def set_goal_function(self, new_goal_function):
      self.goal_function = new_goal_function

    def set_fuel_end(self, new_fuel_end):
      self.fuel_end = new_fuel_end
    
    
  

     


