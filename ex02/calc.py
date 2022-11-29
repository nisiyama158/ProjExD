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
    else:
        entry.insert(tk.END,txt)
        

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
button.bind("<1>",button_click)
button.grid(row = r,column = c)

root.mainloop()