#Products list
products = [ "hamburger","cheeseburger","fries"]
products_cost = [0.99,1.29,1.49]
products_amount = [10,5,20]

#Defining search, list, add, remove, update, report or quit
def s():
    p_name=input("Enter a product name: ")
    if p_name in products:
        location=products.index(p_name)
        print("We sell",p_name,"at",products_cost[location],"per unit")
        print("We currently have",products_amount[location],"in stock")

    else:
        print("Sorry we don't sell",p_name)
    print()
    
def l():
    print(format("Product","<25s"),format("Price","<5s"),format("Quantity","<3s"))
    for i in range(len(products)):
        print(format(products[i],"<25s"),format(products_cost[i],"<5"),format(products_amount[i],"<3"))
    print()
    
def a():
    p_name=str(input("Enter a new product name: "))
    while p_name in products:
        print("Sorry, we already sell that product. Try again.")
        p_name=input("Enter a new product name: ")
    products.append(p_name)
    
    p_cost =float(input("Enter a product cost: "))
    while p_cost<=0:
        print("Invalid cost. Try again. ")
        p_cost =float(input("Enter a product cost: "))
    products_cost.append(p_cost)

    p_amount=int(input("How many of these products do we have? "))
    while p_amount<0:
        print("Invalid quantity. Try again. ")
        p_amount=int(input("How many of these products do we have? "))
    products_amount.append(p_amount)

    print("Product added! ")
    print()
    #print(products)
    #print(products_cost)
    #print(products_amount)

    
def r():
    remove_p_name=input("Enter a product name: ")
    if remove_p_name in products:
        location=products.index(remove_p_name)
        del products_cost[location]
        del products_amount[location]
        del products[location]
        print("Prodcut removed!")
        print()
    else:
        print("Product doesn't exist. Can't remove. ")
        print()


def u():
    p_name=input("Enter a product name: ")
    if p_name in products:
        location=products.index(p_name)
        print("What would you like to update? ")
        whatupdate=input("(n)ame, (c)ost, or (q)uantity: ")
        #updating name
        if whatupdate=="n":
            new_name=input("Enter a new name: ")
            while new_name in products:
                print("Duplicate name! ")
                new_name=input("Enter a new name: ")
            else:
                products[location]=new_name
                print("Product name has been updated")
                print()
        #updating cost
        elif whatupdate=="c":
            new_cost=float(input("Enter a new cost: "))
            while new_cost<=0:
                print("Invalid cost! ")
                new_cost=float(input("Enter a new cost: "))
            else:
                products_cost[location]=new_cost
                print("Product cost has been updated ")
                print()
                
        #updating quantity    
        elif whatupdate=="q":
            new_q=int(input("Enter a new quantity: "))
            while new_q<0:
                print("Invalid quantity!")
                new_q=int(input("Enter a new quantity: "))
            else:
                products_amount[location]=new_q
                print("Product quantity has been updated")
                print()
        #The case where what to update is not valid 
        else:
            print("Invalid option")
            print()
            
    else:
        print("Product doesn't exist. Can't update. ")
        print()


def e():
    loc_expensive = products_cost.index(max(products_cost))
    loc_cheap = products_cost.index(min(products_cost))
    print(format("Most expensive product: ","<40s"),max(products_cost)," (",products[loc_expensive],")",sep='')
    print(format("Least expensive product: ","<40s"),min(products_cost)," (",products[loc_cheap],")",sep='')
    total=0
    for i in range(len(products)):
        p=products_cost[i]*products_amount[i]
        total+=p
    print(format("Total value of all products: ",'<39s'),format(total,".2f"))
    print()

def q():
    print("See you soon!")

while True:
    answer=input("(s)earch, (l)ist,(a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    if answer=="s":
        s()
    elif answer=="l":
        l()
    elif answer=="a":
        a()
    elif answer=="r":
        r()
    elif answer=="u":
        u()
    elif answer=="e":
        e()
    elif answer!="s" and answer!="l" and answer!="a" and answer!="e" and answer!="u" and answer!="r" and answer!="q":
        print("Invalid option, try again")
        print()
    elif answer=="q":
        q()
        break
    
    
