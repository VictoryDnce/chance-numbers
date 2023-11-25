import random

print("do you feel lucky today?\n1 = YES or 2 = NO")


while True:
    answer = int(input())
    if answer != 1 and answer != 2:
        print("You cannot write numbers other than 1 or 2.. ")
        continue
    if answer == 1:
        print('lets check !!!')
        break
    else:
        print("another time babe !!!")
        exit()
        

print("reminder: you have 3 chances and numbers between 1 to 10 ..")
remainder = 3        
estimation = random.randint(1,10)
#print(estimation)

while remainder > 0:
    entering_number = int(input('enter an integer between 1 to 10: '))
    if entering_number < 1 or  entering_number > 10:
        print("you cannot enter number that not except 1 to 10")
        continue
    remainder -=1
    
    if entering_number == estimation:
            
        print("you won".center(50,"*"))
        break   
    elif entering_number < estimation:
        print("enter a bigger number")
           
    else:
        print("enter a smaller number")
      
    if remainder == 0:    
        print(f"you don`t have a hot hand. the number held was: {estimation}")
    
            

