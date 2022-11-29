import tkinter as tk
import tkinter.messagebox as tkm 

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}のボタンが押されました")

root = tk.Tk()
root.title("calc")
root.geometry("300x500")
r,c = 0,0
for i in range(10)[::-1]:
    button = tk.Button(root,text=i,font=("",30),widht = 4,height = 2)
    button.grid(row = r,column = c)
    button.bind("<1>",button_click)
    button.pack()
    c += 1
    if c==3:
        c=0
        r+=1


root.mainloop()