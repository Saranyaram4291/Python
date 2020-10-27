listFirst=[10,9,8,7,6]
listSecond=[2,3,4,5,6]
listThird=[]

for oddValues in listFirst :
    if(oddValues%2!=0):
        listThird.append(oddValues)

for evenValues in listSecond :
    if(evenValues%2==0):
        listThird.append(evenValues)
print(str(listThird))