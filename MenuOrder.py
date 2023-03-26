# Your code for Assignment 2 will go into this file. 
# Name:                 MenuOrder.py
# Author:               Meetkumar Patel
# Date Created:         March 01, 2022
# Date Last Modified:   March 05, 2022 

# Purpose:
#
#This program is a MenuOrder.
#This program will take input from the user and generate a bill and take orders.
#First, there will be a welcome screen to explain to the customer.
#Then user input will be done the first and last name and the full address
#Also, the city, province, postal code, special instructions, and the phone number then it will be stored in a list
#Then there will be six dinner options for the menu, and the user has to select between them; for this program, the user can only choose one item from the menu.
#Also, the user will be asked questions like assignment one had confirmation, order selection, a student or not, and others the same applies to this assignment
#In this assignment, two questions are added: the delivery options and choice of how much tip to give.
#Then the receipt is printed accordingly with the user selects the receipt will only be published if confirmation is yes otherwise, it will end.

#Variables used in this program.
    #These are the 6 items used in the menu
name1 = "Fries".ljust(12)
name2 = "Rice".ljust(12)
name3 = "Lays".ljust(12)
name4 = "Toast".ljust(12)
name5 = "Water".ljust(12)
name6 = "Coffee".ljust(12)
    #These are there respective prices
price1 = 3
price2 = 7
price3 = 1
price4 = 4
price5 = 10
price6 = 2
delivery = 5
    #Tax and student discount
hst = "Tax (13%)"
discount = "{0:<s}{1:s}".format("10%".ljust(4),"student savings")
studentDisc = 0.1 
tax = 0.13
    #This an empty dictionary which is used in the program to store user's order info.
orderInfo ={}

#Functions used.
#
#Function: receipts
#Description: This function will help in printing some lines which are usually repeated in all the sitution
#Parameters: 
#           hst,tax,total
#Return value:
#           hst,tax,total 
#In this function there is no need for returning any value as its just printing out.
def receipts(hst,tax , total):
    print(
    "{0:>43}{1:>6}{2:>5.2f}".format(hst, "$" , tax) , "\n" ,
    "{0:>53}".format("------"), "\n",
    "{0:>42}{1:>6}{2:>5.2f}".format("TOTAL", "$", total)) 
    return hst, tax, total

#
#Function: userIntergerChecker
#Description: This function will help to check if the user entered the correct value(Integer) and if not it will keep looping till user doesnot 
#enter correct value
#Parameters: 
#           z is prompt wanted to be showed on display
#           y is the checking part where the input is checked if those value are matching or not (condition such as (1,2,3,4))
#Return value:
#           x is the value we will get from user.
def userIntergerChecker(z,y):
    x = input(z)
    x = int(x)
    while x not in y:
        x = input(z)
        x = int(x)
        
    return (x)

#
#Function: userWordChecker
#Description: This function will help in check if the user has entered correct value("Y" OR "N") if not it will keep looping
#Parameters: 
#           z is prompt wanted to be showed on display
#           y is the checking part where the input is checked if those value are matching or not (condition such as ("Y","N"))
#Return value:
#           w is the value we will get from user.
def userWordChecker(z,y):
    w = input(z)
    w = w.upper().strip()
    while w not in y:
        w = input(z)
        w= w.upper().strip()
    

    return(w)

#This block of code runs The welcome interface of the menu and explaining what we have on orders and taking their orders
#About the program menu.
print(
    "{0:~^50s}".format("Welcome Users!!!\n") , 
    "{0:^50s}".format("To ARNOLD'S AMAZING EATS\n") ,
    "This program will help you place you order faster So without wasting time\n\
     please fill the customer details\n" , "\n" ,
    "{0:-<100s}".format("")
    )

#User information Page (WHERE USER DETAILS ARE GATHERED.)
firstName = input("**Enter your First Name:**\n").strip().title()
lastName = input("**Enter you Last Name:**\n").strip().title()
deliveryAddress = input("**Enter your full address that is: Street Number, Street Name, Unit(OPTIONAL)**\n").strip().title()
city = input("**Enter Your City:**\n").strip().title()
province = input("**Enter Your Province:**\n").strip().title()
post = input("**Enter Your Poastol Code:**\n").strip().title()
addtionalInfo = input("**Delivery Instruction(Optional): **\n").title().strip().title()
phone = input("**Enter Your Phone Number:**\n").strip()
#Then the user details are sent in a list using the append method.
custormerInfo = []
custormerInfo.append(firstName)
custormerInfo.append(lastName)
custormerInfo.append(deliveryAddress)
custormerInfo.append(city)
custormerInfo.append(province)
custormerInfo.append(post)
custormerInfo.append(addtionalInfo)
custormerInfo.append(phone)
#This is the menu which is stored in a nested dictionary where the key are numbers and the value has the items in it.
menu = {
    1 : {name1: price1} ,
    2 : {name2: price2} ,
    3 : {name3: price3} , 
    4 : {name4: price4} , 
    5 : {name5: price5} ,
    6 : {name6: price6}
}

#This is the end for the personal information.
print("{0:-^100s}".format("Thank you for the information"))
print()

#This part shows the menu using a for loop 
print("In todays Dinner there are two items served")
print()
for num, menuItem in menu.items():
    for key in menuItem:
        print()
        print("{0}.""{1}"""'$'"{2}".format(num, key, menuItem[key]),"\n")

#Here I have used the integer cheker function to check that the number entered is valid or not.
orderSelection = userIntergerChecker("Select which order to place from the above (Choose a number of the order): ",(1,2,3,4,5,6))


orderCount = float(input("How many of this order would you like: "))

student = userWordChecker("Confirm If you are a student [Y or N]: ", ("Y","N"))

#Here the orderinfo dictionary stores : orderSelection,orderCount and student info.
orderInfo = {
    1:orderSelection, 
    2:orderCount, 
    3:student}

#In This for loop ; the first loop is from the orderinfo and then secound is the menu dict then\
#condition checks id the key of menu dict matches the value in orderInfo and if it matches print the result and tell user to confirm.
for num, value1 in orderInfo.items():
    for x,y in menu.items():
        if x == value1:
            for item, price in y.items():
                print()
                print("{0:}""{1:}""$""{2:s}".format("The order is as follows: \n\n\t", item, str(price * orderCount)))
                print()
    break

#Here the function userWordChecker is called and checks if user enters "Y" or "N". if "Y" it continues otherwise ends
confirmation = userWordChecker("Please Confirm This order is correct [Y or N]: ", ("Y","N"))
if confirmation == "Y":
    ordertype = userIntergerChecker("Please Select the order delivery [1.Pickup 2.Deliver]: ", (1, 2))
    #Here the code checks the order type if its delivery or pickup if delivery the tip is included otherewise jumps.   
    if ordertype == 2:
        tip = userIntergerChecker("Please give a tip of 10,15 or 20%: ", (10,15,20))
    else:
        pass

    #This is where the list customerdetails is being unpacked and stored in individual variables and then used in printing the customer receipts.
    separator = " "
    customerDetail = []
    for x in custormerInfo:
        customerDetail.append(str(x))
    lst1 = "".join(customerDetail[0])
    lst2 = "".join(customerDetail[1])
    lst3 = "".join(customerDetail[2])
    lst4 = "".join(customerDetail[3])
    lst5 = "".join(customerDetail[4])
    lst6 = "".join(customerDetail[5])
    lst7 = "".join(customerDetail[6])
    lst8 = "".join(customerDetail[7])

    #This is where the customer details are printed.
    print("\n","Here is your receipt\n" , "\n", "Customer Details\n" , "\n" ,
    "{0:s}{1:>6s}".format(lst1,lst2 ), "\n",
    "{0:}".format(lst8))
    #Here condition is checked if ordertype is delivery then address are displayed otherwise passed.
    if ordertype == 2:
        print("{0:}{1:}{2:}{3:}{4:}{5:}{6:}{7:}".format(lst3, "\n" , lst4, lst5, lst6 ,"\n",lst7, "\n"))
    else:
        pass
    print()
    print(
    "{0:*^50s}".format(" ") , "\n" , "\n"
    "{0:>31s}{1:>15s}".format("Item".center(5),"Item".center(10)) , "\n" , "\n",
    "{0:}{1:>26s}{2:>11s}{3:>11s}".format("Order".ljust(4),"Amt".center(4),"Price".center(5),"Total".rjust(5)), "\n" ,
    "{0:}{1:>17}{2:>12}{3:>11}".format("-------------","----","------","--------"))

    #This is the main code block where the for loop is executed as we need to match the key of order info and key in menu then get its name and price of ther item
    #Then do the calucaltions accordingly as this is in a loop there is no need of if and elif statement
    for num, value1 in orderInfo.items():
        for num1,Item in menu.items():
            if num1 == value1:
                for item, price in Item.items():
                    print()
                    total = price * orderCount
                    print("{0:^s}{1:>18.0f}{2:>9d}{3:>10s}{4:>5.2f}".format(item.ljust(10),orderCount, price,"$",total))
                    print()
                    #Here the condition checks if the student is a student or not if a student then calculations are done accordingly.
                if student == "Y":
                    stdDisc = total * studentDisc
                    subTotal = total - stdDisc
                    print("{0:s}{1:>30}{2:>5.2f}".format(discount,"-$",stdDisc) , "\n" , "\n")
                else:
                    subTotal = total
                print("{0:>43}{1:>6}{2:>5.2f}".format("Sub-Total", "$", subTotal), "\n" )
                        
                tax = tax * subTotal
                #Here the condition checka if the ordertype selected is a delivery then the calculations are done otherwise done the normal way 
                if ordertype == 2:
                    tips = (tip/100) * subTotal
                    print("{0:}""{1:d}%""{2:>36s}""{3:>5.2f}".format("Tip given".ljust(10),tip,"$",tips))
                    # Here the condtion checks that the if the subtotal is less than or equal to 30 then delivery charges are applied otherwise the charges are waived.
                    if subTotal <=30:
                        fullTotal = tax + subTotal + delivery + tips
                        print("{0:}{1:>33s}{2:>5.2f}".format("Delivery charges","$",delivery), "\n")
                        receipts(hst, tax, fullTotal)  
                    else:
                        fullTotal = tax + subTotal + tips
                        print( "{0:}{1:}{2:>37s}".format("Delivery charges", " ", "Waived"), "\n") 
                        receipts(hst, tax, fullTotal)
                else:
                    fullTotal = subTotal + tax
                    receipts(hst, tax, fullTotal)
                break
        break
else:
    print("Order Not confirmed!!!!!")