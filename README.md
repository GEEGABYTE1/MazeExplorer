# MazeExplorer
Mini Maze made with graphs. Can you solve the maze with the lowest cost? 

# Controls 

Just type one of the options outputted in the command line! 


# Extras 

You can add your own rooms and customize the maze as well (Please check "Customization" part of the file) 

Made in Python 🐍

# Customization 

In order to customize, follow these steps. 

1) You first have to make a `Vertex` Class of the room name in `graph.py`. 
    - For example, `entrance = Vertex("entrance")` or `queens_room = Vertex("Queen's Room)` 

2) You will then need to establish the room into the "map". You can do this by this syntax in `graph.py`:
    - `graph.add_vertex(your_room_name)` where all you need to replace is `your_room_name` with the name of the room you want to add. 

3) The last step is to create a path between the new room and the rest of the rooms in the maze. The syntax follows: 
    - `your_room_name.add_edge(another_room_name, desired_cost)` or `another_room_name.add_edge(your_room_name, desired_cost)` where; 
      - `your_room_name`: The new room you added 
      - `another_room_name`: Another room in the map 
      - `desired_cost`: The cost it will take to travel (you can choose)


