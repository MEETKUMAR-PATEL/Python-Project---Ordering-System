# This is the script you will use for your Assignment #1.
# Name:                 MenuOrder.py
# Author:               Meetkumar Patel
# Date Created:         January 31, 2022
# Date Last Modified:   February 04, 2022 

# Purpose:
#This program is a MenuOrder.
#This program will take input from the user and generate a bill and take orders.
#First there will be a welcome screen Where the customer will be explained.
#Then user input will be done the first and last name and the full address
#Also the city, province , postal code , special instructions and the phone nemuber
#Then there will be 2 dinner options for the menu and the user has to select betweent them
#Then the confirmation of the order then displaying the receipt with hst tax calculated prior.
#then end the program otherwise if input is wrong keep on looping.


#Variables Used in the program.
name_1 = "Fries"
name_2 = "Sandwhich"
menu_1 = "FRIES{0:-^17s}".format("-")
menu_2 = "SANDWHICH{0:-^17s}".format("-")
price_1 = 3
price_2 = 7
studentDisc = -0.1
tax = 0.13

#This block of code runs The welcome interface of the menu and explaining
#About the program menu.
print(
    "{0:~^50s}".format("Welcome Users!!!") , "\n" ,
    "{0:^50s}".format("To ARNOLD'S AMAZING EATS") , "\n" ,
    "This program will help you place you order faster So without wasting time\n\
     please fill the customer details\n" , "\n" ,
    "{0:-<100s}".format("")
    )

#User information Page (WHERE USER DETAILS ARE GATHERED.)
firstName = input("**Enter your First Name:**\n")
lastName = input("**Enter you Last Name:**\n")
deliveryAddress = input("**Enter your full address that is: Street Number, Street Name, Unit(OPTIONAL)**\n")
city = input("**Enter Your City:**\n")
province = input("**Enter Your Province:**\n")
post = input("**Enter Your Poastol Code:**\n")
addtionalInfo = input("**Please Provide us with any Additional Infomation You would like to add:**\n")
phone = input("**Enter Your Phone Number:**\n")

#This is the end for the personal information.
print("{0:-^100s}".format("Thank you for the information"))

#order section.
confirmation_1 = "N"
#To create a loop
while confirmation_1 == "N" or confirmation_1 == "n": #Here the code will only run again if the user enters the confirmation to be no
    print("In todays Dinner there are two items served")

    print("Menu:\n")
    #This will print the menu and show the user.
    print(menu_1+"$"+str(price_1)+"\n"+menu_2+"$"+str(price_2))

    #Customer Selection out of the two options given 
    orderSelection = int(input("Select which order to place(EITHER 1 OR 2):"))
    orderCount = int(input("How many of this order would you like?"))
    #CONFIRMATION AND PRINTING AND LOOPING IF NO

    total_1 = price_1 * orderCount
    total_2 = price_2 * orderCount
    #Here is the condition function IF , where output is according to the users input.
    if orderSelection == 1:
        print("The order is as followes:\n\
            " + menu_1 + str(total_1) + "$")
    else:
        print("The order is as followes:\n\
            " + menu_2 + str(total_2) + "$")
    #Here the user is asked to Confirm the order and of the user is a student or not.
    confirmation_1 = input("Please Confirm this order is correct [Y or N]:")
    student = input("Confirm If you are a student [Y or N]:")
    # This code of block runs according to the users input and calculates the final cost and other applicable calculation to be in the receipt
    if orderSelection == 1:
        if student == "y" or student == "Y":
            stdDisc = total_1 * studentDisc
            subTotal = total_1 + stdDisc
            tax = tax *subTotal
            subTotal = tax + subTotal
            fullTotal = tax + subTotal
        else:
            subTotal = total_1
            tax = tax * subTotal
            subTotal = tax + subTotal
            fullTotal = tax + subTotal

    elif orderSelection == 2:
        if student == "y" or student == "Y":
            stdDisc = total_2 * studentDisc
            subTotal = total_2 + stdDisc
            tax = tax * subTotal
            subTotal = tax + subTotal
            fullTotal = tax + subTotal

        else:
            subTotal = total_2
            tax = tax * subTotal
            subTotal = tax + subTotal
            fullTotal = tax + subTotal
    # This condition will be also running according to the users input and generate the receipts accordingly.
    if confirmation_1 == "Y" or  confirmation_1 == "y":
        print(
        "Here is your receipt:" , "\n",
        "Customer Details" , "\n" ,
        firstName + lastName , "\n" ,
        deliveryAddress , "\n" ,
        city , province , post , "\n" ,
        addtionalInfo , "\n" ,
        " " , "\n" ,
        "{0:*^50s}".format(" ") , "\n" ,
        "receipt\n{0:^25s}".format(" ") , "\n" ,
        "{0:>15s}""{1:>9s}".format("Item","Item") , "\n" ,
        "Order","{0:>9s}""{1:>9s}""{2:>9s}".format("Amt","Price","Total")) 
        if orderSelection == 1:
            print(name_1 , "{0:>9d}".format(orderCount) , "{0:>7d}".format(price_1) , "{0:>11d}".format(total_1))
            if student == "Y" or student == "y":
                print( 
                "{0:>26}{1:>4}{2:>}{3:.2f}".format("10% Student Savings" , " " , "$" ,stdDisc) , "\n" , 
                "{0:>25}{1:>5}{2:>}{3:.2f}".format("Sub-Total", " " , "$" , subTotal) , "\n" , 
                "{0:>25}{1:>5}{2:>}{3:.2f}".format("TAX(13%)" , " " , "$" , tax) , "\n" ,
                "{0:>25}{1:>5}{2:>}{3:.2f}".format("TOTAL" , " " , "$", fullTotal)
                    )           
            else:
                print(
                "{0:>26}{1:>5}{2:>}{3:.2f}".format("Sub-Total" , " " , "$",subTotal) , "\n" ,
                "{0:>25}{1:>5}{2:>}{3:.2f}".format("TAX(13%)" , " " ,"$", tax) , "\n" ,
                "{0:>25}{1:>5}{2:>}{3:.2f}".format( "TOTAL" , " " ,"$", fullTotal)
                    )
        elif orderSelection == 2:
            print(name_2 , "{0:>6d}".format(orderCount) , "{0:>7d}".format(price_2) , "{0:>9d}".format(total_2))
            if student == "Y" or student == "y":
                print(
                "{0:>26}{1:>4}{2:>}{3:.2f}".format("10% Student Savings" , " " , "$",stdDisc) , "\n" , 
                "{0:>25}{1:>5}{2:>}{3:.2f}".format("Sub-Total", " " , "$",subTotal) , "\n" , 
                "{0:>25}{1:>5}{2:>}{3:.2f}".format("TAX(13%)" , " " , "$", tax) , "\n" ,
                "{0:>25}{1:>5}{2:>}{3:.2f}".format("TOTAL" , " " , "$", fullTotal)
                    )
            else:
                print(
                "{0:>26}{1:>5}{2:>}{3:.2f}".format("Sub-Total" ," " , "$", subTotal) , "\n" ,
                "{0:>25}{1:>5}{2:>}{3:.2f}".format("TAX(13%)" , " " , "$", tax) , "\n" ,
                "{0:>25}{1:>5}{2:>}{3:.2f}".format( "TOTAL" , " " , "$", fullTotal)
                    )
            

