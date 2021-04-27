import random

# snake, water or gun // rock, paperor scissors
def gameWin(comp,you):

# if two values are  equal declare tie
    if comp==you:
        return None
# check all possibilities when computer choose 's' 
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

# check all possibilities when computer choose 'w' 
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True

# check all possibilities when computer choose 'g' 
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("computer turn: snake(s), water(w), gun(g)? ")
ranNo=random.randint(1,3)
if ranNo==1:
        comp ='s'
elif ranNo==2:
        comp ='w'
elif ranNo==3:
        comp ='g'
you=input("your turn: snake(s), water(w), gun(g)? ")
a= gameWin(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")

if a==None:
    print("Game is a tie!")
elif a:
    print("you win!")
else:
    print("You lose!")