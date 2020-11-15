"""test use random in python 3.8"""
import random
### ใช้ในจำนวนเต็มนะ
def randrange():
    """randrange"""
    a = ""
    #for _ in range(20):
        #a += str(random.randrange(2))
    #print(a)
    for _ in range(20):
        a += str(random.randrange(4, 30, 2))#เริ่ม หยุด step
        a += " "
    print(a)

def randint():
    """randint"""
    a = ""
    for _ in range(20):
        a += str(random.randint(1, 10)) #เริ่ม (หยุด+1)
        a += " "
    print(a)

###ใช้สำหรับเลือก

###ใช้เลือก 1
def choice():
    """Functions for sequences"""
    saq = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10, 11, 12, 13, 14, 15]#เป็นstrก็ได้ range tuple
    a = random.choice(saq)
    print(a)

###เลือกหลายตัว
def choices():
    """choices"""
    saq = ["salt", "lucky", "normal", "money", "pot"]
    a = random.choices(saq, weights=[10, 5, 2, 1, 7], k=3)#เเหล่ง , ค่านำหนัก(นำหนักมากมีโอกาสเหลือกมาก) ไม่มีคือค่าเท่ากัน, ค่านำหนักสะสม, จำที่เลือกมา 
    print(a)

def suffle():
    """suffle"""
    saq = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10, 11, 12, 13, 14, 15]
    random.shuffle(saq)#ไม่returnนะ ถ้าให้ returnใช้ simple เเทนเเบบ 2 อันข้างล่าง
    print(saq)

def sample():
    """sample"""
    ###เเบบเเรก
    ###เลือกกลุ่มตัวอย่าง
    saaq = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10, 11, 12, 13, 14, 15]
    a = random.sample(saaq, k=5)###กลุ่มที่เลือก, k=จำนวนที่จะเลือก
    ###เเบบ 2
    ###เป็น suffle เเบบreturn ค่า
    saq = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10, 11, 12, 13, 14, 15]
    b = random.sample(saq, len(saq))
    print(a)
    print(b)

###สุ่มๆ
def rannn():
    """randomrandom"""
    a = random.random()###สุ่มเลขทศนิยมระหว่าง [0.0, 1)
    print(a)

def unifrom():
    """randomunifrom"""
    ###สุ่มเลขในช่วงเปง ทศนิยม
    a = random.uniform(0, 4.95)###ใส่ สองค่า
    print(a)

def triangular():
    """random triangular"""
    ### สุ่มค่าในช่วง โดยมี modeช่วยสุ่มค่กระจายในช่วงนั้น
    for _ in range(20):
        a = random.triangular(100, 50, 25)###เลข, เลข, mode
        print(a)

###การสุ่มเเบบการกระจายค่ามนเเบบต่างๆ

def betavariate():
    """random betavariate"""
    ###เกี่ยวกับ Beta distribution
    a = random.betavariate(5, 10)###ใช้สองค่าที่มากกว่า 0
    print(a)

def expovariate():
    ###สุ่มการกระจายเลขชี้กำลัง
    """random expovariate"""
    a = random.expovariate(1.5)###เลข + สุ่ม[0, inf) เลข - สุ่ม(inf, 0]
    print(a)

def gamma():
    ###เกี่ยวกับ Gamma distribution
    """random gammavariate"""
    a = random.gammavariate(5, 10)###ใช้สองค่าที่มากกว่า 0
    print(a)

def gauss():
    """random gauss กับ normalvariate"""
    ###เกี่ยวกับ Normal distribution
    a = random.gauss(100, 50)###อันนี้เร็วกว่า
    b = random.normalvariate(100, 50)
    print(a)
    print(b)

def logno():
    """random lognormvariate"""
    ###เกี่ยวกับ Log-normal distribution
    a = random.lognormvariate(0, 0.5)###เลข
    print(a)

def vondo():
    """random vonmisesvariate"""
    ###เกี่ยวกับ von Mises distribution
    a = random.vonmisesvariate(0, 4)###เลข
    print(a)

def pareto():
    """random paretovariate"""
    ###เกี่ยวกับ Pareto distribution
    a = random.paretovariate(1)###เลข
    print(a)

def weibu():
    """random weibullvariate"""
    ###เกี่ยวกับ Weibull distribution
    a = random.weibullvariate(0.1, 5)###เลข
    print(a)
