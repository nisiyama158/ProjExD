import tkinter as tk
import tkinter.messagebox as tkm 

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    new_func(txt)

def new_func(txt):
    entry.insert(tk.END,txt)

def button_sum(event):
    pass

root = tk.Tk()
root.title("calc")
root.geometry("300x500")

entry = tk.Entry(justify="right",width=10,font=("",40))
entry.grid(columnspan=3)
entry.grid()

r,c = 1,0
for i in range(10)[::-1]:
    button = tk.Button(root,text=i,font=("",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row = r,column = c)
    
    c += 1
    if c==3:
        c=0
        r+=1

button = tk.Button(root,text="+",font=("",30),width=4,height=2)
button.bind("<1>",button_click)
button.grid(row = r,column = c)
c+=1
button = tk.Button(root,text="=",font=("",30),width=4,height=2)
button.bind("<1>",button_sum)
button.grid(row = r,column = c)

root.mainloop()