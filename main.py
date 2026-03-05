import copy

import package_fuction

maze=package_fuction.made_random_maze()
shortest_answer_maze=copy.deepcopy(maze)
shortest_answer_maze,shortest_len=package_fuction.find_shortest_answer_maze(shortest_answer_maze)
maze=package_fuction.make_color_maze(maze)
shortest_answer_maze=package_fuction.make_color_maze(shortest_answer_maze)
for row in maze:
    print(*row,sep="")
print(shortest_len)
for row in shortest_answer_maze:
    print(*row,sep="")