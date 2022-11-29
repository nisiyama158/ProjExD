import tkinter as tk
import tkinter.messagebox as tkm 

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        isum = entry.get()
        entry.delete(0,tk.END)
        try:
            res = eval(isum)
            entry.insert(tk.END, res)

        except:
            entry.insert(tk.END, "error")
            tkm.showinfo("error",f"エラーが起こりました")
            entry.delete(0,tk.END)
    elif txt == "AC":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,txt)
        

root = tk.Tk()
root.title("calc")
root.geometry("380x500")

entry = tk.Entry(justify="right",width=11,font=("",50))
entry.grid(columnspan=10)
entry.grid()

r,c = 1,2
for i in range(10)[::-1]:
    button = tk.Button(root,text=i,font=("",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row = r,column = c)
    
    c -= 1
    if c == -1:
        c=2
        r+=1
        if r == 4:
            c=1

button = tk.Button(root,text="+",font=("",30),width=4,height=2)
button.bind("<1>",button_click)
button.grid(row = 2,column = 3)
button = tk.Button(root,text="=",font=("",30),width=4,height=2)
button.bind("<1>",button_click)
button.grid(row = 4,column = 3)
button = tk.Button(root,text="AC",font=("",30),width=4,height=2)
button.bind("<1>",button_click)
button.grid(row = 1,column = 3)

root.mainloop()