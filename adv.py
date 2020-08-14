from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "Sprint-Challenge--Graphs/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, 'r').read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = ['w']

move_back = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

valid_directions = ['n', 's', 'e', 'w']

# initialize with starting direction
stack = ['w']

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


while len(stack) > 0:
    # popping current direction off 
    move = stack.pop()
    # telling player to travel that direction
    player.travel(move)

    # if the room that player JUST moved to is not visited..
    if player.current_room not in visited_rooms:
        # append the opposite direction of where he moved so we can traverse back once he's hit a dead end
        traversal_path.append(move_back[move])
        stack.append(move_back[move])
        # add the room to visited so we don't do this process again
        visited_rooms.add(player.current_room)
    # for each direction in ['n', 's', 'e', 'w'] that the player can go... 
    for direction in valid_directions:
        # set the next room for each valid direction in a variable 
        room = player.current_room.get_room_in_direction(direction)
        # if the room hasn't been visited..
        if room and room not in visited_rooms:
            # append the direction to our traversal path and to our stack
            traversal_path.append(direction)
            stack.append(direction)
            break

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
