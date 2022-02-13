import mysql.connector as sql

conn = sql.connect(host = "localhost", user="root", passwd="password", database="mysql")
cursor = conn.cursor()

def landing_page():
    print("Welcome to our Medical Website Project.")
    p_name = input("What is your name: ")
    print("Hi ", p_name, ", hope you are doing fine")
    print("  ")

def showlist():
    print("Display all details of medicines available")
    print("  ")
    cursor.execute(" Select medicine,code from medi_project")
    df = cursor.fetchall()
    print(df)

def sortedmedicines():
    print("These are the symptoms")
    print("headache")
    print("fever")
    print("aches and pain")
    print("cold")
    print("nausea")
    symptoms = input("Type your symptom: ")
    print("  ")
    cursor.execute("select medicine,code from medi_project where symptoms = '{}' ".format(symptoms,))
    dl= cursor.fetchall()
    print(dl)

def continue_page():


    print(" do you want to see the list of medines or do you want too find out the medicine required for you.")
    print("  ")
    choice = input("Type 1 if its the first and type 2 if it is the 2nd: ")
    if choice == "1":
        showlist()
    elif choice == "2":
        sortedmedicines()
    else:
        print("please type the correct value ", p_name)
        continue_page()


def payment_page():
    print("  ")
    order = input("Enter your Medicine Code please : ")
    quant = int(input("Enter the quantity: "))
    if order == "m01":
        total_price = 150*quant
        print("You have bought ")
        print("Your total is,",total_price)
    elif order == "m02":
        total_price = 150*quant
        print("You have bought ")
        print("Your total is,",total_price)

    elif order == "m03":
        total_price = 150*quant
        print("You have bought ")
        print("Your total is,",total_price)

    elif order == "m04":
        total_price = 150*quant
        print("You have bought ")
        print("Your total is,",total_price)

    else:
        print("Enter the correct value")
        payment_page()

landing_page()
continue_page()
payment_page()
