# -*- coding:utf-8 -*-
import pygame
import time
import random
from pygame.locals import *


class BasePlane(object):#抽出的基类
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.bullet_list = []  # 存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断字段是否越界
                self.bullet_list.remove(bullet)

class BaseBullet(object):#抽出的基类
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class HeroPlane(BasePlane):#飞机
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,190,700,"./feiji/hero.gif")
    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class EnemyPlan(BasePlane):#敌机
    def __init__(self, screen_temp):
        BasePlane.__init__(self,screen_temp, 0, 0, "./feiji/enemy0.png")
        self.direction='right'#用来存储飞机默认的显示方向
    def move(self):
        if(self.direction=='left'):
            self.x-=5
        elif(self.direction=='right'):
            self.x+=5

        if(self.x>430):
            self.direction='left'
        elif(self.x<0):
            self.direction='right'

    def fire(self):
        if random.randint(1,15)==5:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class Bullet(BaseBullet):#子弹
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+40,y-20,"./feiji/bullet.png")

    def move(self):
        self.y-=10

    def judge(self):#判断子弹越界
        if(self.y<0):
            return True
        else:
            return False

class EnemyBullet(BaseBullet):#子弹
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self, screen_temp, x + 25, y + 40, "./feiji/bullet1.png")

    def move(self):
        self.y+=10

    def judge(self):#判断子弹越界
        if(self.y>852):
            return True
        else:
            return False

def key_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()

def main():
    #1.创建窗口
    screen=pygame.display.set_mode((480,852),0,32)

    #2.创建一个背景图片
    background=pygame.image.load("./feiji/background.png")

    #3.创建一个飞机对象
    hero=HeroPlane(screen)

    #4.创建一个敌机
    enemy= EnemyPlan(screen)

    while(True): #3.贴图片到背景
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()#敌机移动
        enemy.fire()#敌机开火
        key_control(hero)
        pygame.display.update()
        time.sleep(0.01)

if __name__=="__main__":
    main()