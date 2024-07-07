import random 

a = 0
b = 0
c = 0 

select = int(input("Select Box \nA(1) \nB(2) \nC(3) \nEnter number here: "))
openrandoor = random.randint(1, 2)
ran = random.randint(1, 3)

#This is the part gem(1) adding to hide 
if ran == 1:
    a = a + 1
elif ran == 2:
    b = b + 1
elif ran == 3:
    c = c + 1
else:
    print("err")

#lock selected variable using adding another 2 

if select == 1:
    if openrandoor == 1:
        if b == 1:
            print("randomply open b, gem in B")
        elif b != 1:
            print("randomely open b door there is no gem")
            b = b + 2 
        else:
            print("err")
    elif openrandoor == 2:
        if c == 1:
            print("randomly c open and gem here")
        elif c != 1:
            print("randomly open c door and threre is no gem ")
            c = c + 2
        else:
            print("err")
    else:
        print("err")
elif select == 2:
    if openrandoor == 1:
        if a == 1:
            print("randomply open A, gem in A")
        elif a != 1:
            print("randomely open A door there is no gem")
            a = a + 2
        else:
            print("err")
    elif openrandoor == 2:
        if c == 1:
            print("randomly c open and gem here")
        elif c != 1:
            print("randomly open c door and threre is no gem ")
            c = c + 2
        else:
            print("err")
    else:
        print("err")
elif select == 3:
    if openrandoor == 1:
        if a == 1:
            print("randomply open A, gem in A")
        elif a != 1:
            print("randomely open A door there is no gem")
            a = a + 2
        else:
            print("err")
    elif openrandoor == 2:
        if b == 1:
            print("randomly B open and gem here")
        elif b != 1:
            print("randomly open B door and threre is no gem ")
            b = b + 2
        else:
            print("err")
    else:
        print("err")
else:
    print("err")


if b == 2:
    print("Randomly \"B\" Box is opened but no gem in here")
    select2 = int(input("Plz select A or C : "))
    if select2 == 1:
        if a == 1:
            print("You selected A and gem in there")
        elif c == 1:
            print("sorry gem in C")
        else:
            print("err")
    elif select2 == 2:
        if a == 1:
            print("You selected Gen in A")
        elif c == 1:
            print("you select c and gem in c")
    else:
        print("err")
elif a == 2:
    print("Randomly A is oppend but no gem in here")
    select2 = int(input("Plz select B or C : "))
    if select2 == 1:
        if b == 1:
            print("you select b and gem in b")
        elif c == 1:
            print("you b and gem in c")
        else:
            print("err")
    if select2 == 2:
        if b == 1:
            print("you select c and gem in b")
        elif c == 1:
            print("you select c and gem in c")
        else:
            print("err")
    else:
        print("err")
elif c == 2:
    print("Randomly C is oppend but no gem in here")
    select2 = int(input("Plz select A or B : "))
    if select2 == 1:
        if a == 1:
            print("you select a and gem in a")
        elif b == 1:
            print("you w and gem in b")
        else:
            print("err")
    if select2 == 2:
        if a == 1:
            print("you select b and gem in a")
        elif b == 1:
            print("you select b and gem in b")
        else:
            print(" ")
    else:
        print(" ")
else:
    print(" ")