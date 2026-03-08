import package_fuction

import pygame
import sys

pygame.init()

#   設定基本資料
WIDTH,HEIGHT=1500,850
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("maze")
clock=pygame.time.Clock()
def FONT(size):
    return pygame.font.SysFont(None,size)
FONT40=FONT(40)
class Player:
    def __init__(self,r,c):
        self.r=r
        self.c=c

#   讓使用者設定迷宮大小
def set_R_C():
    R,C=20,20
    while True:
        clock.tick(20)
        screen.fill((200,200,200))
        screen.blit(FONT40.render(f"R(5~100): {R}",True,(0,0,0)),(WIDTH/8,HEIGHT/8))
        screen.blit(FONT40.render(f"C(5~100): {C}",True,(0,0,0)),(WIDTH/8,HEIGHT/8+40))
        screen.blit(FONT40.render("R: up|down  C: left|right",True,(0,0,0)),(WIDTH/8,HEIGHT/8+80))

        size=int(min(WIDTH/1.5/C,HEIGHT/1.5/R))
        Xmid,Ymid=WIDTH/2,HEIGHT/1.6
        x0,y0=int(Xmid-size*C/2),int(Ymid-size*R/2)
        x1,y1=x0+size*C,y0+size*R
        for x in range(x0,x1,size):
            for y in range(y0,y1,size):
                pygame.draw.rect(screen,(0,0,0),(x,y,size,size),1)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return R,C

        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            R=min(R+1,100)
        if keys[pygame.K_DOWN]:
            R=max(R-1,5)
        if keys[pygame.K_LEFT]:
            C=max(C-1,5)
        if keys[pygame.K_RIGHT]:
            C=min(C+1,100)

        pygame.display.flip()


def set_game():

    R,C=set_R_C()
    rs,cs,re,ce=0,0,R-1,C-1

    size=int(min((WIDTH-100)/C,(HEIGHT-100)/R))
    maze=package_fuction.made_random_maze(R,C,rs,cs,re,ce)
    X0,Y0=int(WIDTH/2-C*size/2),int(HEIGHT/2-R*size/2)
    p1=Player(rs,cs)
    start_time=pygame.time.get_ticks()

    while True:
        clock.tick(60)
        screen.fill((200,200,255))
        
        # 時間系統
        second=(pygame.time.get_ticks()-start_time)//1000
        screen.blit(FONT40.render(f"time: {second} s",True,(0,0,0)),(10,10))

        # 事件處理
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type==pygame.KEYDOWN:

                # 方向控制
                if event.key==pygame.K_UP and p1.r-1>=0 and maze[p1.r-1][p1.c]==0:
                    p1.r-=1
                if event.key==pygame.K_DOWN and p1.r+1<R and maze[p1.r+1][p1.c]==0:
                    p1.r+=1
                if event.key==pygame.K_LEFT and p1.c-1>=0 and maze[p1.r][p1.c-1]==0:
                    p1.c-=1
                if event.key==pygame.K_RIGHT and p1.c+1<C and maze[p1.r][p1.c+1]==0:
                    p1.c+=1

        # 繪製迷宮
        for r in range(R):
            for c in range(C):
                x=X0+c*size
                y=Y0+r*size
                if (r,c)==(p1.r,p1.c):
                    color=(255,255,0)
                elif (r,c)==(rs,cs):
                    color=(0,0,255)
                elif (r,c)==(re,ce):
                    color=(255,0,0)
                elif maze[r][c]==1:
                    color=(0,0,0)
                else:
                    color=(100,255,100)
                pygame.draw.rect(screen,color,(x,y,size,size))

        # 終點抵達
        if (p1.r,p1.c)==(re,ce):
            pygame.display.flip()
            return

        pygame.display.flip()

# ---main---
while True:
    set_game()

pygame.quit(); sys.exit()

'''
shortest_answer_maze=copy.deepcopy(maze)
shortest_answer_maze,shortest_len=package_fuction.find_shortest_answer_maze(shortest_answer_maze)
maze=package_fuction.make_color_maze(maze)
shortest_answer_maze=package_fuction.make_color_maze(shortest_answer_maze)
for row in maze:
    print(*row,sep="")
print(shortest_len)
for row in shortest_answer_maze:
    print(*row,sep="")
'''
