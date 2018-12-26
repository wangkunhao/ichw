#!/usr/bin/env python3

"""planets.py: Description of the moving plants around the sun.

__author__ = "WangKunhao"
__pkuid__  = "1800011715"
__email__  = "1800011715@pku.edu.cn"
"""
def judge(m, n, a, b, i):
    if i % m + a > m or i // m + b > n:
        return False
    for p in range(b):
        for r in states[i + p*m : i + p*m + a]:
            if r != 0:
                return False
    return True
def put(m, n, a, b, i=0):
    ans = []
    cantput = True
    if i >= m*n:
        return [[]]
    while states[i] != 0:
        i += 1
        if i == m*n:
            return [[]]
    for (a, b) in [(a, b), (b, a)]:
        if judge(m ,n, a, b, i):
            for p in range(b):
                states[i + p*m : i + p*m + a] = [1] * a
            parts = put(m, n, a, b, i)
            bricks = tuple([brick for q in range(b)
                                      for brick in range(i + q * m , i + q * m + a)])
            for part in parts:
                part.append(bricks)
            ans.extend(parts)
            for p in range(b):
                states[i + p*m : i + p*m + a] = [0] * a
    return ans
def tile(m, n, a, b):
    anss = list(set([tuple(ans) for ans in put(m, n, a, b)]))
    return anss
def draw(ans, m, n):
    import turtle
    s0 = int(600 / max(m, n))
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(10)
    t.color("blue")
    for i in range(n + 1):
        t.pu()
        t.goto(s0 * (-m/2), s0 * (n/2 - i))
        t.pd()
        t.fd(s0 * m)
    t.rt(90)
    for i in range(m + 1):
        t.pu()
        t.goto(s0 * (-m/2 + i), s0 * (n/2))
        t.pd()
        t.fd(s0 * n)
    t.lt(90)
    t.color("purple")
    for i in range(m):
        for j in range(n):
            t.pu()
            t.goto(s0 * (-m/2 +0.2 + i), s0 * (n/2 - 0.9 - j))
            t.write(str(i + j*m), "center")
    t.color("black")
    t.pensize(3)
    for i in range(len(ans)):
        t.pu()
        site = ans[i][0]
        t.goto(s0 * (-m/2 + site%m),s0 * (n/2 - site//m))
        t.pd()
        j = 0
        while site in ans[i]:
            j += 1
            site += 1
            if j >= m:
                break
        lena = j * s0
        site -= 1
        j = 0
        while site in ans[i]:
            j += 1
            site += m
        lenb = j * s0
        for k in range(2):
            t.fd(lena)
            t.rt(90)
            t.fd(lenb)
            t.rt(90)
    turtle.done()
def main(m, n, a, b):
    area = tile(m, n, a, b)
    if area == []:
        print("error")
    else:
        print("共有", len(area), "组解，展示如下")
        if len(area) == 1:
            print(area[0], ":", area[int(area[0]) - 1])
        else:
            for (i, ans) in enumerate(area):
                print( i + 1, ":", ans)
        n_ans = int(input("请输入要画出的解的序号："))
        while True:
            if n_ans <= len(area):
                draw(area[n_ans - 1], m, n)
                break
            else:
                n_ans = int(input("error"))
if __name__ == "__main__":
    m=int(input("m="))
    n=int(input("n="))
    a=int(input("a="))
    b=int(input("b="))
    states = [0] * m * n
    main(m, n, a, b)