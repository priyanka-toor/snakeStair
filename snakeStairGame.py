from random import randint
print("Let's Play snake stair game.....")
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
for i in range(0,30):
    if(i<5):
        l1.append(i+1)
    if(i>=5 and i<10):
        l2.append(i+1)
    if(i>=10 and i<15):
        l3.append(i+1)
    if(i>=15 and i<20):
        l4.append(i+1)
    if (i>=20 and i<25):
        l5.append(i+1)
    if (i>=25 and i<30):
        l6.append(i+1)

print(l6[::-1])
print(l5)
print(l4[::-1])
print(l3)
print(l2[::-1])
print(l1)

# p1 and p2 are player 1 and player 2 
p1=0
p2=0
while(p1<30 and p2<30):
    r1=eval(input("Enter a number b/w 1 and 6 "))
    print("************Player1 turn*************\nAfter tossing a dice you get no.",r1)
    p1=p1+r1
    if(p1<30):
     if(p1==1):
        p1=p1+16
        print("wow! you get stair to jump at 17")
     elif(p1==5):
        p1=p1+7
        print("wow! you get stair to jump at 12")
     elif(p1==9):
        p1=p1-6
        print("Opps! you caught by snake and drop to 6")
     elif(p1==11):
        p1=p1+17
        print("wow! you get stair to jump at 28")
     elif(p1==18):
        p1=p1-11
        print("Opps! you caught by snake and drop to 7")
     elif(p1==22):
        p1=p1+4
        print("wow! you get stair to jump at 26")
     elif(p1==29):
        p1=p1-14
        print("Opps! you caught by snake you drop to 15")
     else:
        print("wow! you jump to",p1)
     print("Total Score of player1 :",p1)
    r2=randint(1,6)
    print("************Player2 turn*************\nAfter tossing a dice you get no.",r2)
    p2=p2+r2
    if(p2<30):
     if(p2==1):
        p2=p2+16
        print("wow! you get stair to jump at 17")
     elif(p2==5):
        p2=p2+7
        print("wow! you get stair to jump at 12")
     elif(p2==9):
        p2=p2-6
        print("Opps! you caught by snake and drop to 6")
     elif(p2==11):
        p2=p2+17
        print("wow! you get stair to jump at 28")
     elif(p2==18):
        p2=p2-11
        print("Opps! you caught by snake and drop to 7")
     elif(p2==22):
        p2=p2+4
        print("wow! you get stair to jump at 26")
     elif(p2==29):
        p2=p2-14
        print("Opps! you caught by snake you drop to 15")
     else:
        print("wow! you jump to",p2)
     print("Total score of player2 :",p2)
     print("")
     print("")
     print("NEXT TURN ........")
    
if(p1>=30):
    print("Player1 is winner")
else:
    print("Player2 is winner")
    
