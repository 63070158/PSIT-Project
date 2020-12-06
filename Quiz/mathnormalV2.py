"""math Quiz"""
import random as rd
import string
import time as time_count
def print_time(sec):
    """คำนวนเวลาที่ใช้ในการทำ Quiz"""
    sec = int(sec)
    minute = sec // 60
    second = sec % 60
    if minute > 0:
        print("Time use: %d Minute and %d Second" %(minute, second))
    else:
        print("Time use: %d Second" %second)

def quiz_easy(name):
    """สุ่มเลขเเค่ 2 หลัก เป็นสุ่ม + - *"""
    print("Easy math !!!\nWe have 5 question *_*")
    symbol_foreasy = ["+", "-", "x"]
    score = 0
    time_start = time_count.time()
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
    time_stop = time_count.time()
    time_use = abs(time_stop - time_start)
    print_time(time_use)
    print("Total Score : %d" %score)
    print("%s Thx for play with us" %name)


def quiz_normal(name):
    """สุ่มเลข2หลักเหมือนeasyแต่เพิ่มยกกำลังหลักเดียวเข้าไป"""
    symbol_fornormal = ["+", "-", "x", "※"]
    score = 0
    time_start = time_count.time()
    for _ in range(5):
        s_now = rd.choice(symbol_fornormal)
        if s_now == "+":
            a = rd.randrange(0, 2000)
            b = rd.randrange(0, 2000)
            ans = int(a) + int(b)
        elif s_now == "-":
            a = rd.randrange(0, 2000)
            b = rd.randrange(0, 2000)
            ans = int(a) - int(b)
        elif s_now == "x":
            a = rd.randrange(0, 100)
            b = rd.randrange(0, 15)
            ans = int(a) * int(b)
        elif s_now == "※":
            a = rd.randrange(0, 10)
            b = rd.randrange(0, 5)
            ans = int(a) ** int(b)
        print("Question : %d %s %d = ?" %(a, s_now, b))
        print("Ans : ", end="")
        user_ans = int(input())
        if user_ans == ans:
            score += 1
        else:
            pass
    time_stop = time_count.time()
    time_use = abs(time_stop - time_start)
    print_time(time_use)
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