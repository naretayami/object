import pygame
from pygame.locals import *
import sys

def main():
    #pygameの初期設定
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面

    #UFOの初期設定
    ux = 200
    uy = 100
    uw = 150
    uh = 50
    uvx = 1
    uhp = 100

    #プレイヤの初期設定
    px = 120
    py = 500

    #タマの初期設定
    tx = px+25
    ty = py
    tvy = 0

    while True:
        #画面を消去
        screen.fill((255,255,255))                                    # 背景を白

        #UFOの処理と描画
        ux = ux + uvx
        if ux>700 or ux <0:
            uvx *= -1
        #当たり判定    
        if (ux <= tx <= ux + uw) and (uy <= ty <= uy + uh):
            uhp=0
        if uhp > 0:    
            pygame.draw.rect(screen, (0,255,0), Rect(ux,uy,uw,uh), 1)    # ■

        #タマの処理と描画
        ty = ty + tvy
        pygame.draw.circle(screen,(10,10,10),(tx,ty),5)              # ●

        #プレイヤの処理と描画
        pygame.draw.rect(screen, (255,0,0), Rect(px,py,50,50), 1)    # ■
        # イベント処理
        for event in pygame.event.get(): 
            if event. type == QUIT: 
                pygame.quit() 
                sys. exit()
            elif event.type == KEYDOWN: 
                if event.key == K_LEFT:
                    px -= 5  # 横方向
                    tx = px+25
                elif event.key == K_RIGHT:
                    px += 5  # 横方向
                    tx = px+25
                elif event.key == K_SPACE:
                    ty = py
                    tx = px+25
                    tvy = -1

        pygame.display.update()                                       # 画面更新

if __name__ == "__main__":
    main()