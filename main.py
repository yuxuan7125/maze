import copy

import package_fuction

maze=package_fuction.made_randomimport package_fuction
#from package_fuction.make_random_maze import 

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

size=min((WIDTH-100)/C,(HEIGHT-100)/R)
maze=package_fuction.made_random_maze(R,C)



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
'''_maze()
shortest_answer_maze=copy.deepcopy(maze)
shortest_answer_maze,shortest_len=package_fuction.find_shortest_answer_maze(shortest_answer_maze)
maze=package_fuction.make_color_maze(maze)
shortest_answer_maze=package_fuction.make_color_maze(shortest_answer_maze)
for row in maze:
    print(*row,sep="")
print(shortest_len)
for row in shortest_answer_maze:

    print(*row,sep="")
