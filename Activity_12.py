
def recursive1(num):
    if(num):
        return num+recursive1(num-1)
    else:
        return 0    

result=recursive1(20)

print(result)        