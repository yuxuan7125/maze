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
R,C=20,20
def set_R_C():
    global R,C
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

    # 設定基本資料
    R,C=set_R_C()
    rs,cs,re,ce=0,0,R-1,C-1

    size=int(min((WIDTH-100)/C,(HEIGHT-100)/R))
    maze=package_fuction.made_random_maze(R,C,rs,cs,re,ce)
    X0,Y0=int(WIDTH/2-C*size/2),int(HEIGHT/2-R*size/2)
    p1=Player(rs,cs)
    start_time=pygame.time.get_ticks()

    # 制作迷宮畫布
    maze_surface=pygame.Surface((C*size,R*size))
    maze_surface.fill((100,255,100))
    for r in range(R):
        for c in range(C):
            if maze[r][c]==1:
                pygame.draw.rect(maze_surface,(0,0,0),(c*size,r*size,size,size))
    pygame.draw.rect(maze_surface,(50,50,255),(cs*size,rs*size,size,size))
    pygame.draw.rect(maze_surface,(255,50,50),(ce*size,re*size,size,size))

    while True:
        clock.tick(60)
        screen.fill((200,200,255))
        screen.blit(maze_surface,(X0,Y0))
        
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

        # 繪製玩家
        x=X0+p1.c*size
        y=Y0+p1.r*size
        pygame.draw.rect(screen,(255,255,0),(x,y,size,size))

        # 終點抵達
        if (p1.r,p1.c)==(re,ce):
            translucent_surface=pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
            translucent_surface.fill((255,255,255,180))
            screen.blit(translucent_surface,(0,0))
            #pygame.draw.rect(screen,(255,255,255),(WIDTH/2-200,HEIGHT/2-20,400,40))
            screen.blit(FONT40.render(f"you completed the maze in {second} seconds",True,(0,0,0)),(WIDTH/2-230,HEIGHT/2-40))
            screen.blit(FONT40.render("press enter for next round",True,(0,0,0)),(WIDTH/2-180,HEIGHT/2))
            pygame.display.flip()
            while True:
                clock.tick(10)
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit(); sys.exit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            return
                        
        pygame.display.flip()

# ---main---
while True:
    set_game()

pygame.quit(); sys.exit()
