import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def count_up():
    global tmr
    tmr=tmr+1
    root.after(1000,count_up)

#キーと連動した動き
def main_proc():
    global cx,cy,mx,my
    if key == "Up"or key=="w":my-=1
    if key == "Down"or key=="s":my+=1
    if key == "Left"or key=="a":mx-=1
    if key == "Right"or key=="d":mx+=1
    if maze_lst[mx][my] == 1:#移動先が壁の場合
        if key == "Up"or key=="w":my+=1
        if key == "Down"or key=="s":my-=1
        if key == "Left"or key=="a":mx+=1
        if key == "Right"or key=="d":mx-=1
    cx,cy = mx*100+50,my*100+50
    canvas.coords("santa",cx,cy)
    if cx==1350 and cy==750:
        canvas.create_image(cx,cy,image=santa_neo,tag="santa_neo")
        canvas.delete("santa")
        tkm.showinfo("ゲームのヒント",f"ゴール！{tmr}秒でゴールしたよ！\n遊んでくれてありがとう！")
        root.title(f"{tmr}秒でゴール！")
    else:
        root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("サンタが町にやってきた！")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_lst)

    ie=tk.PhotoImage(file="Fig/house_1f.png")
    santa=tk.PhotoImage(file="fig/christmas_santa.png")
    santa_neo=tk.PhotoImage(file="fig/christmas_santa_present.png")
    tmr=0
    mx,my = 1,1
    cx,cy = mx*100+50,my*100+50
    canvas.create_image(1350,750,image=ie,tag="ie")
    canvas.create_image(cx,cy,image=santa,tag="santa")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    count_up()
    main_proc()
    root.mainloop()
