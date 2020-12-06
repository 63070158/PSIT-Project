"""math Quiz"""
import random as rd
import string
def quiz_easy(name):
    """สุ่มเลขเเค่ 2 หลัก เป็นสุ่ม + - *"""
    print("Easy math !!!\nWe have 5 question *_*")
    symbol_foreasy = ["+", "-", "x"]
    score = 0
    for _ in range(5):
        s_now = rd.choice(symbol_foreasy)
        if s_now == "+":
            a = rd.randrange(0, 100)
            b = rd.randrange(0, 100)
            ans = int(a) + int(b)
        elif s_now == "-":
            a = rd.randrange(0, 100)
            b = rd.randrange(0, 100)
            ans = int(a) - int(b)
        elif s_now == "x":
            a = rd.randrange(0, 100)
            b = rd.randrange(0, 15)
            ans = int(a) * int(b)
        print("Question : %d %s %d = ?" %(a, s_now, b))
        print("Ans : ", end="")
        user_ans = int(input())
        if user_ans == ans:
            score += 1
        else:
            pass
    print("Total Score : %d" %score)
    print("%s Thx for play with us" %name)


def quiz_normal(name):
    """สุ่มเลข2หลักเหมือนeasyแต่เพิ่มยกกำลังหลักเดียวเข้าไป"""
    symbol_fornormal = ["+", "-", "x", "※"]
    score = 0
    for _ in range(5):
        s_now = rd.choice(symbol_fornormal)
        if s_now == "+":
            a = rd.randrange(0, 100)
            b = rd.randrange(0, 100)
            ans = int(a) + int(b)
        elif s_now == "-":
            a = rd.randrange(0, 100)
            b = rd.randrange(0, 100)
            ans = int(a) - int(b)
        elif s_now == "x":
            a = rd.randrange(0, 100)
            b = rd.randrange(0, 15)
            ans = int(a) * int(b)
        elif s_now == "※":
            a = rd.randrange(0, 5)
            b = rd.randrange(0, 5)
            ans = int(a) ** int(b)
        print("Question : %d %s %d = ?" %(a, s_now, b))
        print("Ans : ", end="")
        user_ans = int(input())
        if user_ans == ans:
            score += 1
        else:
            pass
    print("Total Score : %d" %score)
    print("%s Thx for play with us" %name)


def user():
    """ยังทำเเค่เเบบง่ายก่อนนะ"""
    print("Math Quiz V1")
    name = input("Plase Enter Name: ")
    print("เลือกระดับความยาก\n1 Easy\n2 Normal\n3 Hard(Not Ready)")
    diff = input()
    if diff == "1":
        quiz_easy(name)
    if diff == "2":
        pass
        quiz_normal(name)
    if diff == "3":
        pass
        #quiz_hard(name)

user()