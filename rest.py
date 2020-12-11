store = {"MCCHICKEN":45,"HAPPY MEAL":60,"MCVEGGIE":70,"MCFLURRY":625,"CHICKEN NUGGETS":420}
bill = {}
print("-"*30)
print("Welcome to McDonalds!")
print("-"*30)
print("Here's the menu:")
print("-"*30)
print("Item\t\t  Price")
print("-"*30)
for x in store.keys():
    print('{:10s}\t{:4.0f}'.format(x,store[x]))
print("-"*30)
total = 0
user = "y"
while user == "Y" or user == "y":
    a = input("Enter the item you want to buy: ")
    a = a.upper()
    if a in bill:
        bill[a] += store[a]
        user = input("Do you want to CONT(Y/N):")
        total += (store[a])
    elif a in store:
        total += (store[a])
        user = input("Do you want to continue(Y/N):")        
        bill[a] = store[a]
    else:
        print("Sorry!, we don't have",a)
        user = input("Do you want to continue(Y/N):")
print("Here's your bill: ")
print("-"*30)
for y in bill.keys():
    print('{:10s}\t{:4.0f}'.format(y,bill[y]))
print("="*30)
print("Total\t\t",total)
print("="*30)
print("Enjoy your meal! :)")