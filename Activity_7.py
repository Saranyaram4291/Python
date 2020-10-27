element=list(input("Enter a sequence of comma separated values: ").split(","))

print (element)
sum=0
for element_values in element:
    sum+=int(element_values)
print (sum)
