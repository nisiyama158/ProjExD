import tkinter as tk
import tkinter.messagebox as tkm 

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}のボタンが押されました")

root = tk.Tk()
root.title("calc")
root.geometry("300x500")



root.mainloop()