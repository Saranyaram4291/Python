inputValue=tuple(input("Enter the values seperated by comma").split(","))
print(str(inputValue))
for checkValue in inputValue :
    if(int(checkValue)%5==0):
        print(str(checkValue)+" number is divisble by 5")
    else:
        print(str(checkValue)+" number is not divisble by 5")    
