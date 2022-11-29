import tkinter as tk
import tkinter.messagebox as tkm 

#クリック動作
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        isum = entry.get()
        entry.delete(0,tk.END)
        try:
            res = eval(isum)
            entry.insert(tk.END, res)
        except NameError:
            entry.insert(tk.END, "error")
            tkm.showinfo("error",f"文字列が入力されました")
        except ZeroDivisionError:
            entry.insert(tk.END, "error")
            tkm.showinfo("error",f"0で割ることは出来ません")

        except:
            entry.insert(tk.END, "error")
            tkm.showinfo("error",f"エラーが起こりました")
    elif txt == "AC":
        entry.delete(0,tk.END)
    elif txt == "C":
        ##entry.delete(int(tk.END)-1,tk.END)　未実装
        pass
    else:
        entry.insert(tk.END,txt)
        
#ウィンドウサイズ
root = tk.Tk()
root.title("calc")
root.geometry("500x500")

#テキストバー
entry = tk.Entry(justify="right",width=11,font=("",50))
entry.grid(columnspan=10)
entry.grid()

#ボタン部分（数字）
r,c = 1,2
for i in range(10)[::-1]:
    button = tk.Button(root,text=i,font=("",30),width=4,height=2,bg="#ffffff")
    button.bind("<1>",button_click)
    button.grid(row = r,column = c)
    
    c -= 1
    if c == -1:
        c=2
        r+=1
        if r == 4:
            c=1

li = ["AC","+","-"]
for n,x in enumerate(li):
    button = tk.Button(root,text=x,font=("",30),width=4,height=2,bg="#ffa0a0")
    button.bind("<1>",button_click)
    button.grid(row = n+1,column = 3)

li2 = ["C","*","/","="]
for m,y in enumerate(li2):
    button = tk.Button(root,text=y,font=("",30),width=4,height=2,bg="#ffa0a0")
    button.bind("<1>",button_click)
    button.grid(row = m+1,column = 4)

#小数点
button = tk.Button(root,text=".",font=("",30),width=4,height=2,bg="#ffffff")
button.bind("<1>",button_click)
button.grid(row = 4,column = 2)

#実行
root.mainloop()