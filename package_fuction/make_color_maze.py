from package_fuction.find_shortest_answer_maze import R,C

def make_color_maze(maze):          #將迷宮上色
    color={
        0:"\033[42m   \033[0m",#路染綠色
        1:"\033[40m   \033[0m",#牆染黑色
        's':"\033[1;42m s \033[0m",
        'e':"\033[1;42m e \033[0m",
        'v':"\033[42m v \033[0m"
    }
    for a in range(R):
        for b in range(C):  
            maze[a][b]=color[maze[a][b]]
    return maze