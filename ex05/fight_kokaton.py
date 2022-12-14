import random
import sys

import pygame as pg
import tkinter as tk
from tkinter import messagebox


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
        pg.K_w:     [0, -1],
        pg.K_s:     [0, +1],
        pg.K_a:     [-1, 0],
        pg.K_d:     [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width/2)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        rans = []
        for ran in range(2):
            if random.randint(1,1000) >= 996:
                rans.append(-1)
            else:
                rans.append(1)
        self.vx *= rans[0]
        self.vy *= rans[1]
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


#class boost:
#    def __init__(self,li):
#        key_dcts = pg.key.get_pressed()
#        if pg.K_SPACE in key_dcts:
#            li.pop()
        

def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()

    # 練習１
    scr = Screen("負けるな！こうかとん", (1600,900), "fig/pg_bg.jpg")

    # 練習３
    kkt = Bird("fig/6.png", 2.0, (1000,400))
    kkt.update(scr)

    # 練習５
    bombs = []
    for i in range(random.randint(5,15)): #ボムの個数、色、移動方向決め
        sx,sy = random.choice([-1,+1]),random.choice([-1,+1])
        br,bg,bb = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        bombs.append(Bomb((br,bg,bb), 10, (sx,sy), scr))
        #bkd.update(scr)

    # 練習２
    while True:        
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                root = tk.Tk() 
                root.withdraw() #メッセージと一緒に出る謎のウィンドウを消すやつ
                ret = messagebox.askyesno('確認', '本当にウィンドウを閉じますか？')
                if ret == True: #ウィンドウを消そうとすると消すかどうか聞く
                    ret2 = messagebox.askyesno('確認', '……マジ？')
                    if ret2 == True: #二段構え
                        return

        kkt.update(scr)
        for bv in bombs:
            bv.update(scr)
            if kkt.rct.colliderect(bv.rct):
                #root = tk.Tk()  #なんかメッセージ表示出来なくて草
                #root.withdraw()
                #messagebox.showinfo('げーむおーばー', f"{pg.time.get_ticks/1000}秒生き残った！")
                moe_sfc = pg.image.load("fig/syoukyaku_noyaki.png") #焼け野原の画像をScrface
                moe_rct = moe_sfc.get_rect()
                moe_rct.center = kkt.rct.centerx,kkt.rct.centery
                scr.sfc.blit(moe_sfc,moe_rct)
                pg.display.update()
                pg.time.wait(1000)

                #動画を差し込もうとしたがpygame.movieモジュールがwindows環境で動作しないらしく
                #ただの文字列と化した図
                #pg.movie.Movie("MEME.mp4")
                #pg.Movie.play(loops=0)
            
                return

        #boost(bombs)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()