# Name:                 MenuOrder.py
# Author:               Meetkumar Patel
# Date Created:         March 01, 2022
# Date Last Modified:   March 31, 2022 

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
#In this program have modified so that the receipt is saved in a .txt file and also adjust the code with try and except block so that it does not crash in anyway unless interupted by th user.

#This is module that is imported to save the result in a file
import os
#Variables used in this program.
filename = "Receipt.txt"
delivery = 5
hst = "Tax (13%)"
discount = "{0:<s}{1:s}".format("10%".ljust(4),"student savings")
studentDisc = 0.1 
tax = 0.13
#This an empty dictionary which is used in the program to store user's order info.
orderInfo ={}
receipt = ""
orderdict1 = {} # This is the aditional dictionary to store the order of the user selection.

#Functions used.
#
#Function: receipts
#Description: This function will help in printing some lines which are usually repeated in all the sitution
#Parameters: 
#           hst,tax,total
#Return value:
#           hst,tax,total 
#In this function there is no need for returning any value as its just printing out.
def receipts(hst,tax , total, receipt):
    print(
    "{0:>43}{1:>6}{2:>5.2f}\n".format(hst, "$" , tax),
    "{0:>53}\n".format("------"),
    "{0:>42}{1:>6}{2:>5.2f}".format("TOTAL", "$", total)) 
    receipt += "{0:>43}{1:>6}{2:>5.2f}".format(hst, "$" , tax)
    receipt += "\n{0:>53}".format("------")
    receipt += "\n{0:>42}{1:>6}{2:>5.2f}".format("TOTAL", "$", total)
    return receipt

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

#
#Function: emptyInputChecker
#Description: This function will help in identifying any empty input and get the input again otherwise just continue
#Parameters: 
#           x(this the input to be shown)
#Return value:
#           j(returns the input given by the user)
#In this function there is no need for returning any value as its just printing out.
def emptyInputChecker(x):
    j = ""
    while True:
        j = input(x).strip().title()
        if j:
            return j

#
#Function: total
#Description: This function helps in unpacking the dictionary and it matchs the key of the order key and menu key thus then printing the order.
#Parameters: 
#           dict0 - this is the first dictionary
#           dict1 - this is the secound dictionary 
#           ordconut - this is the ordercount where it gives in how much the order is needed
#            receipt - this is the parameter for saving the results into a file.
#Return value:
#           v - this is the cumulative total for the order.
#           receipt -  this is the print for the saving of file.
#In this function there is no need for returning any value as its just printing out.

def total(dict0,dict1,ordconut,receipt):
    v = 0
    for x,y in dict0.items():
        for x0,y0 in dict1.items():
            for x1 in y:
                multi = (y[x1]*ordconut)
                if y0 == y:
                    print("{0:^s}{1:>18.0f}{2:>9d}{3:>10s}{4:>5.2f}".format(x1.ljust(10),ordconut, y[x1],"$",multi))
                    receipt += "\n{0:^s}{1:>18.0f}{2:>9d}{3:>10s}{4:>5.2f}".format(x1.ljust(10),ordconut, y[x1],"$",multi)
                    
                    v += multi

    return v,receipt

#This is the welcome screen for the user.
print(
    "{0:~^55s}\n".format("Welcome Users!!!"),
    "{0:^50s}".format("To ARNOLD'S AMAZING EATS"),
    "{0:}".format("\nThis program will help you place you order faster So without wasting time\n"),
    "\t{0:^40}\n".format("Please fill the customer details"),
    "{0:-^100}".format("")
    )

#User information Page (Wgere also the user details are gathered in a separate list.)

firstName = emptyInputChecker("**Enter your First Name:**\n")
lastName = emptyInputChecker("**Enter you Last Name:**\n")
deliveryAddress = input("**Enter your full address that is: Street Number, Street Name, Unit(OPTIONAL)**\n").strip().title()
city = emptyInputChecker("**Enter Your City:**\n")
province = emptyInputChecker("**Enter Your Province:**\n")
post = emptyInputChecker("**Enter Your Poastol Code:**\n")
addtionalInfo = input("**Delivery Instruction(Optional): **\n").strip().title()
phone = emptyInputChecker("**Enter Your Phone Number:**\n")
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
#This is the menu which is stored in a nested dictionary where the key are numbers and the value has the items and price in it.
menu = {
    "1" : {"Fries".ljust(12): 3},
    "2" : {"Rice".ljust(12): 7},
    "3" : {"Lays".ljust(12): 1},
    "4" : {"Toast".ljust(12): 4},
    "5" : {"Water".ljust(12): 10},
    "6" : {"Coffee".ljust(12): 2}
}

#This is the end for the personal information.
print("{0:-^100s}\n".format("Thank you for the information"))
orderInfo = {}
confirmation = "N"
while confirmation == "N":
    #This part shows the menu using a for loop 
    print("In todays Dinner there are two items served")
    print()
    for num, menuItem in menu.items():
        for key in menuItem:
            print("\n{0}.""{1}"""'$'"{2}".format(num, key, menuItem[key]))

    while True:
        #this try block ensures that the input given is not empyty and also checks that the input given is "1,2,3,4,5,6"
        #otherwise raises an expection and gives the message of error 
        try:
            orderSelection = emptyInputChecker("Select which order to place from the above (Choose a number of the order): ")
            if orderSelection not in "1,2,3,4,5,6":
                raise Exception("The order selected is not in the list")
            else:
                None
            break
        except Exception as msg:
            print(msg)
    #This stores the user input order selected into a listt and then updates into the orderInfo dictionary.        
    j = list(map(str, orderSelection.split(",")))
    orderInfo.update({1:j})
    while True:
        try:
            orderCount = float(input("How many of this order would you like: "))
            break
        except ValueError:
            print("The given input is not valid")
    orderInfo.update({2:orderCount})
    student = userWordChecker("Confirm If you are a student [Y or N]: ", ("Y","N"))
    orderInfo.update({3:student})

    #In This for loop ; the first loop is from the orderinfo and then secound is the menu dict then\
    #condition checks id the key of menu dict matches the value in orderInfo and if it matches print the result and tell user to confirm.
    print("The order is as follows:")
    for x,y in orderInfo.items():
        if x == 1:
            for order in y:
                for num,orde in menu.items():
                    if num == order:
                        for item,price in orde.items():
                            orderdict1.update({num:{item:price}})

                print("{0:}""{1:}""$""{2:s}".format(" \n\n\t", item, str(price * orderCount)))

    #Here the function userWordChecker is called and checks if user enters "Y" or "N". if "Y" it continues otherwise ends
    confirmation = userWordChecker("Please Confirm This order is correct [Y or N]: ", ("Y","N"))
    orderInfo.update({4:confirmation})
    if confirmation == "Y":
        while True:
            #this try block checks that the user input given is not any other but "1" and  "2".
            #otherwise the loop continues.
            try:
                ordertype = emptyInputChecker("Please Select the order delivery [1.Pickup 2.Delivery]: ")
                if ordertype not in ("1","2"):
                    raise Exception("The value given is not valid")
                else:
                    None
                break
            except Exception as msg:
                print(msg)
        orderInfo.update({5:ordertype})
        #Here the code checks the order type if its delivery or pickup if delivery the tip is included otherewise jumps.   
        if ordertype == "2":
            while True:
                try:
                    tip = int(emptyInputChecker("Please give a tip of 10,15 or 20%: "))
                    if tip not in (10,15,20):
                        raise Exception("The value given is not correct")
                    else:
                        None
                    break
                except Exception as msg:
                    print(msg)
            orderInfo.update({6:tip})
        else:
            None
    else:
        continue

    #This is where the customer details are printed.
    print("\n{0:}\n\n{0:}\n\n".format("Here is your receipt","Customer Details"),
    "{0:s}{1:}{2:s}\n".format(custormerInfo[0]," ",custormerInfo[1] ),
    "{0:s}".format(custormerInfo[7]))
    #Here condition is checked if ordertype is delivery then address are displayed otherwise passed.
    if ordertype == "2":
        print("{0:}{1:}{2:}\n{3:}{4:}{5:}{6:}\n\n".format(" ",custormerInfo[2],custormerInfo[3]," ", custormerInfo[4], custormerInfo[5], custormerInfo[6]))
    else:
        pass
    print()
    print(
    "{0:*^50s}\n\n".format(""),
    "{0:>31s}{1:>13s}\n\n".format("Item".center(5),"Item".center(10)),
    "{0:}{1:>26s}{2:>11s}{3:>11s}\n".format("Order".ljust(4),"Amt".center(4),"Price".center(5),"Total".rjust(5)),
    "{0:}{1:>17}{2:>12}{3:>11}\n".format("-------------","----","------","--------"))

    #Here i am calling function for giving back the cumulative total for the order.
v,r = total(menu, orderdict1, orderCount, receipt="")
    #Here the condition checks if the student is a student or not if a student then calculations are done accordingly.
if student == "Y":
    stdDisc = v * studentDisc
    subTotal = v - stdDisc
    print("{0:s}{1:>30}{2:>5.2f}\n".format(discount,"-$",stdDisc))
    print("{0:>43}{1:>6}{2:>5.2f}\n".format("Sub-Total","$",subTotal))

else:
    subTotal = v
    print("{0:>43}{1:>6}{2:>5.2f}".format("Sub-Total", "$", subTotal), "\n")
                    
tax = tax * subTotal
#Here the condition checka if the ordertype selected is a delivery then the calculations are done otherwise done the normal way 
if ordertype == "2":
    tips = (tip/100) * subTotal
    print("{0:}""{1:d}%""{2:>36s}""{3:>5.2f}\n".format("Tip given".ljust(10),tip,"$",tips))
    # Here the condtion checks that the if the subtotal is less than or equal to 30 then delivery charges are applied otherwise the charges are waived.
    if subTotal <= 30:
        fullTotal = tax + subTotal + delivery + tips
        print("{0:}{1:>33s}{2:>5.2f}\n".format("Delivery charges","$",delivery))
    else:
        fullTotal = tax + subTotal + tips
        print("{0:}{1:}{2:>37s}\n".format("Delivery charges", " ", "Waived"))
else:
    fullTotal = subTotal + tax
v = receipts(hst, tax, fullTotal, receipt)

#This is will show the end of receipt and also show where the receipt has been saved on which folder.
print("Thank you")
print("Your file has been saved on\n\t{}\n\n".format(os.path.join(os.getcwd(), filename)))

#This section is where all the out is saved on in the receipt 
receipt += "{}{}".format("\nHere is your receipt\n" , "\nCustomer Details\n\n")
receipt += "{0:s}{1:}{2:s}\n".format(custormerInfo[0]," ",custormerInfo[1] )
receipt += "{0:s}".format(custormerInfo[7])
    #Here condition is checked if ordertype is delivery then address are displayed otherwise passed.
if ordertype == "2":
    receipt += "{0:}{1:}\n{2:}{3:}{4:}{5:}".format(" ",custormerInfo[2],custormerInfo[3], custormerInfo[4], custormerInfo[5], custormerInfo[6])
else:
    None
receipt += "\n{0:*^50s}\n\n".format("")
receipt += "\n{0:>31s}{1:>13s}\n".format("Item".center(5),"Item".center(10))
receipt += "\n{0:}{1:>26s}{2:>11s}{3:>11s}".format("Order".ljust(4),"Amt".center(4),"Price".center(5),"Total".rjust(5))
receipt += "\n{0:}{1:>17}{2:>12}{3:>11}".format("-------------","----","------","--------") 
receipt += "\n{0}".format(r)
if student == "Y":
    receipt += "\n{0:s}{1:>30}{2:>5.2f}\n".format(discount,"-$",stdDisc)
    receipt += "\n{0:>43}{1:>6}{2:>5.2f}\n".format("Sub-Total","$",subTotal)

    if ordertype == "2":
        receipt += "\n{0:}""{1:d}%""{2:>36s}""{3:>5.2f}".format("Tip given".ljust(10),tip,"$",tips)
        if subTotal <= 30:
            receipt += "\n{0:}{1:>33s}{2:>5.2f}".format("Delivery charges","$",delivery, "\n")
        else:
            receipt += "\n{0:}{1:}{2:>37s}{3:}".format("Delivery charges", " ", "Waived", "\n")
else:
    receipt += "\n{0:}".format(v)
    
receipt += "\n{0:}".format(v)

#This section is where the file will be opened and can be read and also closed as there is use of the keyword "with"
with open(filename, "a") as outputFile:
    outputFile.write(receipt)