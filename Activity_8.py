element=list(input("Enter any number with comma seperated ").split(","))
print(element)
element_intValues=[]
'''for i in range(0,len(element)):
    element[i]=int(element[i])
print(element)    
print("First Number is :"+str(element[0]))
print("Last Number is :"+str(element[-1]))
if(element[0]==element[-1]):
    print("First and last number is same")
else:
    print("First and last number is different")'''
for element_value in element :
    element_intValues.append(int(element_value))
print (element_intValues)
