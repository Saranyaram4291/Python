user1=input("Enter the player 1 name ")
user2=input("Enter the player 2 name ")
user1Option=input(user1+" Select either rock or scissors or paper ").lower()
user2Option=input(user2+" Select either rock or scissors or paper ").lower()
if(user1Option==user2Option):
    print("Its a tie")
elif(user1Option=='rock'):
    if(user2Option=='scissors'):
        print(user1+" Rock wins")
    elif(user2Option=='paper'):
        print(user2+" paper wins")  
elif(user1Option=='scissors'):
    if(user2Option=='paper'):
        print(user2+" paper wins")
    elif(user2Option=='rock'):
        print(user1+" scissors wins")    
elif(user1Option=='paper'):
    if(user2Option=='scissors'):
        print(user1+" paper wins")
    elif(user2Option=='rock'):
        print(user2+" rock wins")
else:
    print("Any one of the user entered invalid value")        

