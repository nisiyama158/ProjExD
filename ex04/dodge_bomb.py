import pygame as pg
import sys
import random

def check_bound(obj_rct,scr_rct):
    #範囲内：+1/範囲外：-1
    yoko,tate= +1,+1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko,tate

def rand_cic():
    if random.randint(1,1000)>=996:
        return -1
    else: return +1

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg") #Scrface
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/6.png") #Scrface
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center=1050,400
    scrn_sfc.blit(tori_sfc,tori_rct) #blit

    #爆弾処理
    cic_sfc = pg.Surface((20,20))
    cic_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(cic_sfc, (255, 0, 0), (10,10), 10)
    cic_rct = cic_sfc.get_rect()
    cic_rct.centerx = random.randint(0,scrn_rct.width/2)
    cic_rct.centery = random.randint(0,scrn_rct.height)
    scrn_sfc.blit(cic_sfc, cic_rct)
    vx,vy = +2,+2

    while True:
        
        scrn_sfc.blit(bg_sfc,bg_rct) #blit
        for event in pg.event.get(): #イベント繰り返し
            if event.type == pg.QUIT:return #ウィンドウの×を押したら終了
        
        key_dct = pg.key.get_pressed() #キー入力取得
        if key_dct[pg.K_UP] or key_dct[pg.K_w]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN] or key_dct[pg.K_s]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT] or key_dct[pg.K_a]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT] or key_dct[pg.K_d]:
            tori_rct.centerx += 1
        scrn_sfc.blit(tori_sfc,tori_rct) #blit
        if check_bound(tori_rct,scrn_rct) != (+1,+1):
            if key_dct[pg.K_UP] or key_dct[pg.K_w]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN] or key_dct[pg.K_s]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT] or key_dct[pg.K_a]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT] or key_dct[pg.K_d]:
                tori_rct.centerx -= 1
            scrn_sfc.blit(tori_sfc,tori_rct)

        vx *= rand_cic()
        vy *= rand_cic()
        cic_rct.move_ip(vx,vy)
        scrn_sfc.blit(cic_sfc, cic_rct)
        yoko,tate=check_bound(cic_rct,scrn_rct)
        vx*=yoko
        vy*=tate

        if tori_rct.colliderect(cic_rct): #爆弾に当たったとき
            moe_sfc = pg.image.load("fig/syoukyaku_noyaki.png") #焼け野原の画像をScrface
            moe_rct = moe_sfc.get_rect()
            moe_rct.center=tori_rct.centerx,tori_rct.centery
            scrn_sfc.blit(moe_sfc,moe_rct)
            pg.display.update()
            pg.time.wait(1000) #1秒wait
            return #ウィンドウの破壊

        pg.display.update()
        clock.tick(1000)

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()