import random
comScoore = 0
playerScoore = 0
print("Well Come to Snack Water Gun ")
print("==================================")
flag = True
while flag:
    if flag==5:
        flag = False
    else:
        flag+=1
    rand = random.randint(1,3)
    # print(f"computer select : {rand}")
    print("1. Snack")
    print("2. Water")
    print("3. Gun")
    a = int(input("Select the corrent option : "))

    if a==1 and rand==1 or a==2 and rand==2 or a ==3 and rand==3:
        print("Draw")
        pass
    elif a==1 and rand==3 or a==2 and rand==1 or a==3 and rand==2:
        print("Computer Won")
        comScoore +=1
    else:
        print("Player won")
        playerScoore+=1


if comScoore== playerScoore:
    print("Draw")
elif comScoore>playerScoore:
    print("Finally Computer won")
    print
else:
    print("Finally You won")

print(f"Computer Scoore : {comScoore}")
print(f"Your Scoore : {playerScoore}")


