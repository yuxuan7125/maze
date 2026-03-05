from package_fuction.make_random_maze import add_d,R,C,rs,re,cs,ce


def find_shortest_answer_maze(maze):          #找出迷宮最短的解答
    maze[rs][cs],maze[re][ce]=0,0
    r,c=rs,cs
    path=[{"r":r, "c":c, "dist":0}]
    i=0
    dist=1
    while r!=re or c!=ce :
        maze[r][c]=2
        add_d(r,c,maze,path,0,i)
        if 1 in path[i]["dirs"]:
            path.append({"r":r-1, "c":c, "dist":dist})
        if 2 in path[i]["dirs"]:
            path.append({"r":r, "c":c-1, "dist":dist})
        if 3 in path[i]["dirs"]:
            path.append({"r":r+1, "c":c, "dist":dist})
        if 4 in path[i]["dirs"]:
            path.append({"r":r, "c":c+1, "dist":dist})
        i+=1
        r,c,dist=path[i]["r"],path[i]["c"],path[i]["dist"]+1
    shortest_path=list()
    r,c=re,ce
    for k in range(len(path)-1,-1,-1):
        if path[k]["r"]==re and path[k]["c"]==ce:
            shortest_len=path[k]["dist"]
            dist-=2
        if path[k]["dist"]==dist and abs(r-path[k]["r"])+abs(c-path[k]["c"])==1:
            shortest_path.append([path[k]["r"],path[k]["c"]])
            dist-=1
            r,c=path[k]["r"],path[k]["c"]
    for a in range(R):
        for b in range(C):
            if maze[a][b]==2:
                maze[a][b]=0
    maze[rs][cs]='s'
    maze[re][ce]='e'
    for a,b in shortest_path[:len(shortest_path)-1]:
        maze[a][b]='v'
    return maze,shortest_len