import pygame
import sys
from pygame.locals import *
import time
import random
class BasePlane(object):
    def __init__(self, screen_Temp,x,y,image):
        self.x = x
        self.y =y
        self.image = pygame.image.load(image)
        self.screen = screen_Temp
        self.bullet_list = []
    def ShowImage(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.show_bullet()
            bullet.move()
            if bullet.Transboundary()==True:
                self.bullet_list.remove(bullet)


class BaseBullet(object):
    def __init__(self,screen_Temp,x,y,image):
        self.x=x
        self.y=y
        self.image=pygame.image.load(image)
        self.screen=screen_Temp
    def show_bullet(self):
        self.screen.blit(self.image, (self.x, self.y))


#英雄的飞机类
class heroPlan(BasePlane):
    def __init__(self,screen_Temp):
        super().__init__(screen_Temp,210,550,"E:\\飞机大战\\飞机\\hero1.png")
        self.imageBlowup=pygame.image.load("E:\\飞机大战\\飞机\\hero_blowup_n3.png")
        self.imageDead=pygame.image.load("E:\\飞机大战\\飞机\\hero_blowup_n4.png")
        self.hp=100
        self.score=0
        self.dead=False
        #self.enemy=None
    def getEnemy(self,enmeyType):
        self.enemy=enmeyType
    def ShowImage(self):
        if self.hp<=0:
            self.ShowBlowup(2)
            self.dead=True#英雄死了
        else:
            self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.show_bullet()
            bullet.move()
            if bullet.Transboundary()==True:
                self.bullet_list.remove(bullet)

    def ShowBlowup(self,n):
        if n==1:
            self.screen.blit(self.imageBlowup,(self.x,self.y))
        elif n==2:
            self.screen.blit(self.imageDead, (self.x, self.y))
    def move_left(self):
        if self.x<=0:
            self.x=0
        else:
          self.x-=10
    def move_right(self):
        if self.x>=400:
            self.x=400
        else:
            self.x+=10
    def move_up(self):
        if self.y<=0:
            self.y=0
        else:
            self.y-=10
    def move_Down(self):
        if self.y >= 600:
            self.y = 600
        else:
            self.y+=10
    def fire(self):
        self.bullet_list.append(Bullet_hero(self.screen,self.x,self.y,self.enemy,self))

class EnemyPlane(BasePlane):
    """敌机"""
    def __init__(self,screen_Temp,heroPlane):
        super().__init__(screen_Temp,0,0,"E:\\飞机大战\\飞机\\enemy-1.gif")
        self.imageBlowup = pygame.image.load("E:\\飞机大战\\飞机\\enemy0_down2.png")
        self.imageDead = pygame.image.load("E:\\飞机大战\\飞机\\enemy0_down3.png")
        self.isRight=False
        self.heroPlan=heroPlane
        self.hp=80
        self.dead=False
    def ShowImage(self):
        if self.hp<=0:
            self.ShowBlowup(2)
            self.dead=True#敌人死了
        else:
            self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.show_bullet()
            bullet.move()
            if bullet.Transboundary()==True:
                self.bullet_list.remove(bullet)

    def ShowBlowup(self, n):
        if n == 1:
            self.screen.blit(self.imageBlowup, (self.x, self.y))
        elif n == 2:
            self.screen.blit(self.imageDead, (self.x, self.y))
    def move_right(self):
        if self.isRight==False:
             if self.x<450:
                 self.x+=5
             else:
                self.x=450
                self.isRight=True
        elif self.isRight==True:
            if self.x>0:
                self.x-=5
            else:
                self.x=0
                self.isRight = False
    def fire(self):
        randem_num=random.randint(1,100)
        if randem_num==10 or randem_num==20:
            self.bullet_list.append(Bullet_enemy(self.screen,self.x,self.y,self.heroPlan))


class Bullet_hero(BaseBullet):
    """英雄的子弹"""
    def __init__(self,screen_Temp,x,y,enemyPlan,herotype):
        super().__init__(screen_Temp,x+40,y-20,"E:\\飞机大战\\飞机\\bullet.png")
        self.enemyPlane=enemyPlan
        self.hero=herotype
        self.dead=False
    def move(self):
        self.y-=5
        if self.y>=self.enemyPlane.y and self.y<self.enemyPlane.y+39 and self.x>self.enemyPlane.x and self.x<=self.enemyPlane.x+51:
            self.dead=True
            self.hero.score+=15
            attack=random.randint(10,50)
            self.enemyPlane.hp-=attack
            if self.enemyPlane.hp>0:
               self.enemyPlane.ShowBlowup(1)
    def Transboundary(self):
        if self.y < 0 or self.dead == True:
            return True
        else:
            return False

class Bullet_enemy(BaseBullet):
    """敌人的子弹"""
    def __init__(self,screen_Temp,x,y,heroPlan):
        super().__init__(screen_Temp,x+20,y+20,"E:\\Python\\feiji\\飞机\\bullet2.png")
        self.heroPlan=heroPlan
        self.dead=False

    def move(self):
        self.y+=5
        if self.y>=self.heroPlan.y and self.y<self.heroPlan.y+124 and self.x>self.heroPlan.x and self.x<=self.heroPlan.x+100:
            self.dead=True
            attack=random.randint(10,50)
            self.heroPlan.hp-=attack
            if self.heroPlan.hp>0:
                self.heroPlan.ShowBlowup(1)

    def Transboundary(self):
        if self.y >700 or self.dead==True:
            return True
        else:
            return False

#按键监听
def key_control(hero):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a or event.key==K_LEFT:
                hero.move_left()
            elif event.key == K_d or event.key==K_RIGHT:
                hero.move_right()
            elif event.key == K_w or event.key==K_UP:
                hero.move_up()
            elif event.key == K_s or event.key==K_DOWN:
                hero.move_Down()
            elif event.key == K_SPACE:
                hero.fire()
        else:
            if event.type == QUIT:
                exit()
def onMouse_leftdown():
    # 监听鼠标左键按下事件
     for event in pygame.event.get():
       if event.type == MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            for index in range(len(pressed_array)):
                 if index==0:
                    return True
     return False
    # 返回 True 表示响应此事件，False表示拦截
def mouse_control(isMouseLeft):#鼠标监听
    x,y=pygame.mouse.get_pos()
    # print("x:"+str(x))
    # print("y:"+str(y))
    # print(isMouseLeft)
    if x>100 and x<210 and y>630 and y<654 and isMouseLeft==True:
        exit()
    if x>300 and x<412 and y>630 and y<658 and isMouseLeft==True:
        main()

def main():
    hightScore=0
    pygame.init()
    #创建一个窗口
    BLACK = (0, 0, 0)
    screen=pygame.display.set_mode((480,700),0,32)
    #创建背景图片
    background=pygame.image.load("E:\\Python\\feiji\\飞机\\background.png")
    gameOver=pygame.image.load("E:\\Python\\feiji\\飞机\\gameover.png")
    quitgame=pygame.image.load("E:\\Python\\feiji\\飞机\\quit_nor.png")
    resgame=pygame.image.load("E:\\Python\\feiji\\飞机\\restart_nor.png")
    my_font = pygame.font.SysFont("arial", 25)

    hero=heroPlan(screen)
    enemy=EnemyPlane(screen,hero)
    hero.getEnemy(enemy)

    while True:
        if hero.dead==True or enemy.dead==True:
            if hightScore<hero.score:
                hightScore=hero.score
            screen.blit(gameOver, (0, 0))
            screen.blit(quitgame, (100, 630))
            screen.blit(resgame, (300, 630))
            hightScore_text=my_font.render("Score : %s" % str(hightScore), True, BLACK)
            screen.blit(hightScore_text, (200, 300))

            score_text = my_font.render("Score : %s" % str(hero.score), True, BLACK)
            screen.blit(score_text, (200, 600))

            isMouseLeft = onMouse_leftdown()
            # print(isMouseLeft)
            mouse_control(isMouseLeft)

        else:
            screen.blit(background,(0,0))
            hero.ShowImage()
            score_text = my_font.render("Score : %s" % str(hero.score), True, BLACK)
            hp_text = my_font.render("HP : %s" % str(hero.hp), True, BLACK)
            screen.blit(score_text, (10, 650))
            screen.blit(hp_text, (390, 650))
            enemy.ShowImage()

            if enemy.hp>0:
                enemy.move_right()
                enemy.fire()

            # pygame.display.update()
            #
            # key_control(hero)

            time.sleep(0.01)
        pygame.display.update()

        key_control(hero)


if __name__=="__main__":
    main()