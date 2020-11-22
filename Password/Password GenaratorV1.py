"""Password Gen V1"""
import random
import string

def genp(upper_cha, lower_cha, number_cha):
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
    password_tosup = list(password)
    password = ""
    random.shuffle(password_tosup)
    for cha1 in password_tosup:
        password += cha1
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
        print("It's OK (YES/NO)")
        conf = input()
        if conf == "YES":
            break
        elif conf == "NO":
            current = 0
            print("Please Enter a New length :D")
    while True:
        password = genp(upper_cha, lower_cha, number_cha)
        print("Password is : %s" %password)
        print("You like New Password (YES/NO)")
        conf = input()
        if conf == "YES":
            print("I hope you like it.")
            break
        elif conf == "NO":
            print("I Will Gen a New once")

user()
