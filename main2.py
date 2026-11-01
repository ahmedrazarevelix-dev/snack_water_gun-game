import random
'''
1 for snack 
-1 for water
0 for gun
'''
computer=random.choice([1, -1, 0])
you=input("Enter your choice:")
youdict={"s":1, "w":-1, "g":0}
reversedict={1:"Snack", -1:"water", 0:"gun"}
you=youdict[you]

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer==you):
    print("Its a draw")

else:
    if((computer-you)==-2 or (computer-you)==1):
        print("you win")
    
    else:
      print("you lose") 

