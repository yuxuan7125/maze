import package_fuction

import pygame
import sys

pygame.init()

#   設定基本資料
WIDTH,HEIGHT=1500,850
screem=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("maze")
clock=pygame.time.Clock()
def FONT(size):
    return pygame.font.SysFont(None,size)

#   讓使用者設定迷宮大小
def set_R_C():
    R,C=20,20
    while True:
        clock.tick(20)
        screem.fill((200,200,200))
        screem.blit(FONT(40).render(f"R(5~100): {R}",True,(0,0,0)),(WIDTH/8,HEIGHT/8))
        screem.blit(FONT(40).render(f"C(5~100): {C}",True,(0,0,0)),(WIDTH/8,HEIGHT/8+40))
        screem.blit(FONT(40).render("R: up|down  C: left|right",True,(0,0,0)),(WIDTH/8,HEIGHT/8+80))

        size=int(min(WIDTH/1.5/C,HEIGHT/1.5/R))
        Xmid,Ymid=WIDTH/2,HEIGHT/1.6
        x0,y0=int(Xmid-size*C/2),int(Ymid-size*R/2)
        x1,y1=x0+size*C,y0+size*R
        for x in range(x0,x1,size):
            for y in range(y0,y1,size):
                pygame.draw.rect(screem,(0,0,0),(x,y,size,size),1)

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

R,C=set_R_C()

size=int(min((WIDTH-100)/C,(HEIGHT-100)/R))
maze=package_fuction.made_random_maze(R,C)
X0=int(WIDTH/2-C*size/2)
Y0=int(HEIGHT/2-R*size/2)

class player():
    def __init__(self):
        self.x=X0
        self.y=Y0
        self.r=0
        self.c=0
p1=player()

def set_gsme():
    while True:
        clock.tick(60)
        screem.fill((200,200,255))
        r=c=0
        for y in range(Y0,Y0+size*R,size):
            for x in range(X0,X0+size*C,size):
                if maze[r][c]==1:
                    pygame.draw.rect(screem,(0,0,0),(x,y,size,size))
                else:
                    pygame.draw.rect(screem,(100,255,100),(x,y,size,size))
                c+=1
            c=0
            r+=1

        pygame.draw.rect(screem,(255,255,0),(p1.x,p1.y,size,size))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and p1.r-1>=0 and maze[p1.r-1][p1.c]==0:
                    p1.r-=1
                    p1.y-=size
                if event.key==pygame.K_DOWN and p1.r+1<R and maze[p1.r+1][p1.c]==0:
                    p1.r+=1
                    p1.y+=size
                if event.key==pygame.K_LEFT and p1.c-1>=0 and maze[p1.r][p1.c-1]==0:
                    p1.c-=1
                    p1.x-=size
                if event.key==pygame.K_RIGHT and p1.c+1<C and maze[p1.r][p1.c+1]==0:
                    p1.c+=1
                    p1.x+=size

        pygame.display.flip()

set_gsme()


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
