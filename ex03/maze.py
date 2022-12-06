import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx,cy
    if key == "Up":cy-=5
    if key == "Down":cy+=5
    if key == "Left":cx-=5
    if key == "Right":cx+=5
    canvas.coords("koukaton",cx,cy)
    root.after(10,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_lst)

    tori=tk.PhotoImage(file="fig/8.png")
    cx,cy = 300,400
    canvas.create_image(cx,cy,image=tori,tag="koukaton")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()