"""Password Gen V1"""
import random
import string

def genp(upper_cha, lower_cha, number_cha, pun_chr):
    """ส่วนที่ทำ Pass"""
    password = ""
    for _ in range(upper_cha):
        cha = random.choice(string.ascii_uppercase)
        password += cha
    for _ in range(lower_cha):
        cha = random.choice(string.ascii_lowercase)
        password += cha
    for _ in range(number_cha):
        cha = random.choice(string.digits)
        password += cha
    for _ in range(pun_chr):
        cha = random.choice(string.punctuation)
        password += cha
    password_tosup = list(password)
    password = ""
    random.shuffle(password_tosup)
    password = "".join(password_tosup)
    return password

def user():
    """ส่วนของการรับค่า ยังไม่เอาตัวอักศรพิเศษ"""
    current = 0
    print("Password GenV.1")
    print("Recommend Password Up to 12 cha")
    while True:
        upper_cha = int(input("Number of Upper Character: "))
        current += upper_cha
        print("Current length Password: %d" %current)
        lower_cha = int(input("Number of Lower Character: "))
        current += lower_cha
        print("Current length Password: %d" %current)
        number_cha = int(input("Number of  Character: "))
        current += number_cha
        print("Password length is %d Character" %current)
        print("You need a punctuation in Your password (YES/NO)")
        conf = input().upper()
        if conf == "YES":
            pun_chr = int(input("Current length Punctuation: "))
            current += pun_chr
            print("Password length is %d Character" %current)
        else:
            pun_chr = 0
        print("It's OK (YES/NO)")
        conf = input().upper()
        if conf == "YES":
            break
        elif conf == "NO":
            current = 0
            print("Please Enter a New length :D")
    while True:
        password = genp(upper_cha, lower_cha, number_cha, pun_chr)
        print("Password is : %s" %password)
        print("You like New Password (YES/NO or RESTART)")
        conf = input().upper()
        if conf == "YES":
            print("I hope you like it.")
            break
        elif conf == "NO":
            print("I Will Gen a New once")
        elif conf == "RESTART":
            user()
            break

user()
