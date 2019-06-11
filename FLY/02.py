import pygame
from pygame.locals import *
import time

#英雄的飞机类
class heroPlan(object):
    def __init__(self,screen_Temp):
        self.x=210
        self.y=550
        self.image=pygame.image.load("E:\\飞机大战\\feiji\\hero1.png")
        self.screen=screen_Temp
        self.bullet_list=[]
    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5
    def move_up(self):
        self.y-=5
    def move_Down(self):
        self.y+=5
    def ShowImage(self):
        self.screen.blit(self.image,(self.x,self.y))

        for bullet in self.bullet_list:
            bullet.show_bullet()
            bullet.move()

    def fire(self):
        self.bullet_list.append(Bullet_hero(self.screen,self.x,self.y))


class EnemyPlane(object):
    def __init__(self,screen_Temp):
        self.x=0
        self.y=0
        self.image=pygame.image.load("E:\\飞机大战\\feiji\\enemy-1.png")
        self.screen=screen_Temp
        self.bullet_list=[]
    def move(self):
        if self.x==0&self.x<480:
            self.x+=10
        else:
            if self.x==480&slef.x>0:
                 self.x-=10
    def ShowImage(self):
        self.screen.blit(self.image,(self.x,self.y))

        # for bullet in self.bullet_list:
        #     bullet.show_bullet()
        #     bullet.move()

    def fire(self):
        self.bullet_list.append(Bullet_hero(self.screen,self.x,self.y))



class Bullet_hero(object):
    def __init__(self,screen_Temp,x,y):
        self.x=x+40
        self.y=y-20
        self.image=pygame.image.load("E:\\飞机大战\\feiji\\bullet.png")
        self.screen=screen_Temp
    def show_bullet(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y-=5


#按键监听
def key_control(hero):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                hero.move_left()
            elif event.key == K_d:
                hero.move_right()
            elif event.key == K_w:
                hero.move_up()
            elif event.key == K_s:
                hero.move_Down()
            elif event.key == K_SPACE:
                hero.fire()
        else:
            if event.type == QUIT:
                exit()
def main():
    #创建一个窗口
    screen=pygame.display.set_mode((480,700),0,32)
    #创建背景图片
    background=pygame.image.load("E:\\飞机大战\\feiji\\background.png")
    hero=heroPlan(screen)
    enemy=EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0))

        hero.ShowImage()
        enemy.ShowImage()
        pygame.display.update()

        key_control(hero)

        time.sleep(0.01)


if __name__=="__main__":
    main()