import pygame as pg
import random 
import sys

#設定
# クロックのインスタンスを生成
clock = pg.time.Clock()
# fpsを設定、ここでは1秒間に60フレームを描画
fps = 60
# ゲーム画面の横幅
screen_width = 1600
# ゲーム画面の縦幅
screen_height = 900
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
#リスタートボタン
buttom_img = pg.image.load("fig/restart.png")




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
class tower(pg.sprite.Sprite):
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


class Button():
    def __init__(self, x, y, image):
        """
        初期化関数、インスタンス生成時に呼ばれる関数
        """
        # 画像を入れる変数
        self.image = image
        # ボタン画像を囲む四角形
        self.rect = self.image.get_rect()
        # ボタンの左上の座標を指定
        self.rect.topleft = (x, y)

    def draw(self):
        """
        描画関数
        """
        # アクションフラグ
        action = False

        # マウスの座標
        pos = pg.mouse.get_pos()

        # ボタンのクリック判定。マウスポインタの座標とボタン画像を囲む四角形との衝突判定。collide=衝突
        if self.rect.collidepoint(pos):
        # マウスをクリックした状態なら
            if pg.mouse.get_pressed()[0] == 1:
                # アクションフラグを更新
                action = True
        # 指定の場所にボタン画像を描画
        Screen.blit(self.image, (self.rect.x, self.rect.y))


    # アクションフラグを返す
        return action


def main():
    clock =pg.time.Clock()
    fps = 60
    bird_group = pg.sprite.Group()
    pipe_group = pg.sprite.Group()
    scr = Screen("Flappy bird", (1600,900), "fig/pg_bg.jpg")
    flappy = Bird("fig/bird1.png",(100, int(900 / 2)))
    bird_group.add(flappy)
    button = Button(1600 // 2 - 50, 900 // 2 - 100, buttom_img)

    while True:
        Screen.blit()



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()