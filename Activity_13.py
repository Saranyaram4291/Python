def calculateList(numbers):
    sum=0
    for listValue in numbers:
        sum+=listValue
    return sum  
numbers=[10,20,20,20]
print(calculateList(numbers))