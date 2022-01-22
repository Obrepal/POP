#inicjalizacja
path = Path( [3], 0,  40, 20)
#dodajemy pierwszy, do strera
great_storer = Great_storer(G,[path])
#wyznaczamy sąsiadów
G.neighbors(curr_path.get_last_node())

for i in range(0,1000):
  #oblicamy obecny najniższy 
    curr_path = copy.copy(great_storer.find_lowest_goal_function())

    for i in G.neighbors(curr_path.get_last_node()):
      great_storer.createPath(curr_path,i)
      if i == 3 and great_storer.get_current_roads()[-1].get_fuel_end() <= 0:
        print(i,great_storer.get_current_roads()[-1].get_fuel_end(),great_storer.get_current_roads()[-1].get_road())
        break
    else:
      continue  # only executed if the inner loop did NOT break
    break


# for n in great_storer.get_current_roads():
#   print(n.get_road(),n.get_fuel_end())

