fruit={
    "apple":10,
    "banana":15,
    "grapes":20,
    "chikku":56
}
choice=input("Enter any fruit name").lower()
if(choice in fruit):
    print(choice+" fruit is present with value ",fruit.get(choice))
else:
    print(choice+" fruit is not present")     