import operator
import random

ops={"+":operator.add,
    "-":operator.sub,
    "*": operator.mul,
    "/":operator.truediv}
ops_keys = list(ops.keys())


def answer_check(x,y,op):
    tries=3
    while tries!=0:
        user_answer = int(input(f"how much would be ({x}){op}({y})?"))
        if user_answer == ops[op](x, y):
            print ("Good Job")
            break
        else:
            tries -= 1
            print(f"Your answer is wrong,you have {tries} more tries")

    else:
        print(f"Sorry, you are out of tries, the answer is ",ops[op](x, y))


def op_choise(level):
    if level<3:
        return random.choice(ops_keys[0:2])
    else:
        return random.choice(ops_keys)


def dev_ex():
    denomenators=[]
    x=random.choice([random.randint(-999, -100),random.randint(100, 999)])
    i=2
    while i<10:
        if x%i==0:
            denomenators.append(i)
            i+=1
        else:
            i+=1
    return x,denomenators

def level_1():
    x=random.randint(100, 899)
    op=op_choise(1)
    if op=="+":
        y=random.randint(100,1000-x)
    else:
        y=random.randint(100,x)
    answer_check(x, y, op)

def level_2(op=None):
    x = random.choice([random.randint(-899, -100),random.randint(100, 899)])
    if x<0:
        y=random.choice([random.randint(-1000-x, -99),random.randint(100,1000+x)])
    else:
        y=random.choice([random.randint(-1000+x, -99),random.randint(100,1000-x)])
    if op==None:
        op = op_choise(2)
    answer_check(x, y, op)

def level_3():
    op = op_choise(3)
    if op=="+" or op=="-":
        level_2(op)
    elif op=="*":
        x = random.choice([random.randint(-999, -100), random.randint(100, 999)])
        y=random.choice(range(2,10))
        answer_check(x, y, op)
    else:
        x,den=dev_ex()
        if not den:
            x, den = dev_ex()
        else:
            y=random.choice(den)
            answer_check(x, y, op)

def level_choise():
    try:
        level=int(input("Hello Player! please choose the level of desired practice:\n"
                    "1 - Addition & Reduction, Possitive numbers\n"
                    "2 - Addition & Reduction\n"
                    "3 - All Arithmetic Operators\n"))
    except:
        level = int(input("Please enter the desired level:\n"
                          "1 - Addition & Reduction, Possitive numbers\n"
                          "2 - Addition & Reduction\n"
                          "3 - All Arithmetic Operators\n"))
    if level==1:
        level_1()
    elif level==2:
        level_2()
    else:
        level_3()


level_choise()
#what should be dine next: create a loop which asks if the player wants to continuw to another game, and error handeling