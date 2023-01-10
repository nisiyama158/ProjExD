import pygame as pg
import random 
import sys

#設定
# 地面のスクロールを管理する変数
ground_scroll = 0
# スクロールの速さ
scroll_speed = 4
# 飛行中かどうかのフラグ
flying = False
# ゲームオーバーのフラグ
game_over = False
# 土管の間の距離
pipe_gap = 350
# 土管の頻度
pipe_frequency = 1500
# 最後の土管
last_pipe = pg.time.get_ticks() - pipe_frequency
# スコア
score = 0
# 土管の通過フラグ
pass_pipe = False




#画面
class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


#鳥
class Bird:
    def __init__(self,img_path, xy):
        self.sfc = pg.image.load(img_path)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.vel = 0
        self.clicked = False

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self):
        self.vel += 0.5
        if self.vel > 10:
            # 最高速度以上に速度はあがらない
            self.vel = 10
        if self.rect.bottom < 768:
            self.rect.y += int(self.vel)
        #クリック機構
        if game_over == False:
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False
            self.image = pg.transform.rotate(self.img_path, self.vel * -2)
        else:
            self.image = pg.transform.rotate(self.img_path, -90)


#土管
class tower:
    def __init__(self,img,x,y,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        # position=1のときは上の土管
        if pos == 1:
        # 土管の画像を上下反転させる
            self.image = pg.transform.flip(self.image, False, True)
            # 隙間を考慮して配置
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]

        # position=-1のときは下の土管
        if pos == -1:
            # 隙間を考慮して配置
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()





def main():
    clock =pg.time.Clock()
    fps = 60
    scr = Screen("Flappy bird", (1600,900), "fig/pg_bg.jpg")


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()