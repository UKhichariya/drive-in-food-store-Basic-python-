store = {"MCCHICKEN":45,"HAPPY MEAL":60,"MCVEGGIE":70,"MCFLURRY":625,"CHICKEN NUGGETS":420}
bill = {}
print("-"*30)#1st dotted line for menu
print("Welcome to McDonalds!")
print("-"*30)#2nd dotted line for menu
print("Here's the menu:")
print("-"*30)#3rd dotted line for menu
print("Item\t\t  Price")
print("-"*30)#4th dotted line for menu
for x in store.keys():
    print('{:10s}\t{:4.0f}'.format(x,store[x]))
print("-"*30)
total = 0
user = "y"
while user == "Y" or user == "y":
    a = input("Enter the Name of item you want to buy: ")#input of the item user wants
    a = a.upper()
    if a in bill:
        bill[a] += store[a]
        user = input("Do you want to Continue(Y/N):")
        total += (store[a])
    elif a in store:
        total += (store[a])
        user = input("Do you want to Continue(Y/N):")#if user want to continue ordering more items        
        bill[a] = store[a]
    else:
        print("Sorry, we don't have",a)#if store doesnt have that Item user entered.
        user = input("Do you want to Continue(Y/N):")
print("-"*30)
print("Here's your bill: ")
print("-"*30)
for y in bill.keys():
    print('{:10s}\t{:4.0f}'.format(y,bill[y]))
print("="*30)
print("Total\t\t",total)
print("="*30)
print("Enjoy your meal! :)")
