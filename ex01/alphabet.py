import random
import datetime




def af():
    num = set()
    while True:
        k = random.randint(65,90)
        num.add(k)
        if len(num) == 26:
            break
        j = random.randint(0,1)
        if j == 1:
            break
    return num


#グローバル変数：
#全てメインの中にあります。




if __name__ == "__main__":
    st = datetime.datetime.now()
    n = af() #対象文字
    print("対象文字：")
    for i in n:
        print(chr(i),end=" ")
    print(" ")

    #デバッグ用
    print("欠損")
    l = random.randint(1,len(n)-1)
    n_c = set(n) #表示文字用変数
    n_v = set() #欠損文字
    for _ in range(l):
        ja = random.choice(n_c)
        n_c.remove(ja)
        n_v.add(ja)
    print(chr(n_v))
    print("表示文字")
    for h in n:
        print(chr(h),end=" ")
    print(" ")
    while True:
        try:
            d = int(input("欠損文字はいくつあるでしょうか？"))
            if d == len(n_v):
                print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
                n_vc = n_v
                for df in range(len(n_v)):
                    kai = int(input(f"{df}つ目の文字を入力してください："))
                    if ord(kai) in n_vc:
                        print("正解です")
                    else:
                        print("間違いです。やり直してください")
                        break
                break
            break
        except:
            print("数字を入力してください")

    gt = datetime.datetime.now()
    print(gt-st,"秒")