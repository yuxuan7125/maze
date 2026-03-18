from package_fuction.make_random_maze import add_d


def visit_maze(maze,R,C,re,ce):          #找出迷宮最短的解答

    # BFS主體
    r,c=re,ce
    visit=[{"r":r, "c":c}]
    i=0
    while i<len(visit) :
        maze[r][c]=2                # 2表示已走訪過
        add_d(r,c,maze,visit,0,i)
        if "up" in visit[i]["dirs"]:
            visit.append({"r":r-1, "c":c, "son":(r,c)})
        if "left" in visit[i]["dirs"]:
            visit.append({"r":r, "c":c-1, "son":(r,c)})
        if "down" in visit[i]["dirs"]:
            visit.append({"r":r+1, "c":c, "son":(r,c)})
        if "right" in visit[i]["dirs"]:
            visit.append({"r":r, "c":c+1, "son":(r,c)})
        i+=1
        if i==len(visit):
            break
        r,c=visit[i]["r"],visit[i]["c"]
    
    # 將maze還原
    for a in range(R):
        for b in range(C):
            if maze[a][b]==2:
                maze[a][b]=0

    return visit
        

def find_road(visit,rs,cs,re,ce):

    # 回推最短路
    shortest_path=list()
    r,c=rs,cs
    for k in range(len(visit)-1,-1,-1):
        if (r,c)==(re,ce):
            break
        if (visit[k]["r"],visit[k]["c"])==(r,c):
            shortest_path.append((r,c))
            r,c=visit[k]["son"]

    return shortest_path
