import random
import datetime


if __name__ == "__main__":
    num = tuple()
    while True:
        k = random.randint(65,90)
        num.add(k)
        if len(num) == 26:
            break
        j = random.randint(0,1)
        if j == 1:
            break

    for i in num:
        print(i+" ",end="")
    print("")