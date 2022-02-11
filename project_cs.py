import mysql.connector as sql

conn = sql.connect(host = "localhost", user="root", passwd="", database="")
cursor = mycon.cursor()

def landing_page():
    print("Welcome to our Medical Website Project.")
    p_name = input("What is your name: ")
    print("Hi ", p_name, ", hope you are doing fine")


def showlist()
    print("Display all details of medicines available")
    df = cursor.execute(" Select medicine from medi_project") 
    print(df)
    
def sortedmedicines()
    print("These are the symptoms")
    print("Symptom 1")
    print("Symptom 2")
    print("Symptom 3")
    print("Symptom 4")
    print("Symptom 5")
    symptom = input("Type your symptom: ")
    age = int(input("Type your age: "))
    sex = input("Type your sex(m/f): ")
    dl = cursor.execute("select * from medi_project where symptoms = {}, age > {}".format(symptoms, age))
    print(dl)

def continue_page():
    continue_lpage = input(p_name," do you want to continue (press y for yes and n for no): ")
    if continue_lpage == "y":
        print(p_name," do you want to see the list of medines or do you want too find out the medicine required for you.")
        choice = input("Type "1" if its the first and type "2" if it is the 2nd")
            if choice == "1":
                showlist()
            elif choice == "2":
                sortedmedicines()
            else:
                print("please type the correct value ", p_name)
                continue_page()
    else:
        print("Ok. Hope you have a nice day ", p_name)

def payment_page():
    order = input("Enter your Medicine Code please : "))
    quant = input("Enter the quantity: "))
    if order == "m01":
        total_price = 150*x
        print("You have bought ")
        print("Your total is," total_price)
    elif order == "m02":
        total_price = 150*x
        print("You have bought ")
        print("Your total is," total_price)
    
    elif order == "m03":
        total_price = 150*x
        print("You have bought ")
        print("Your total is," total_price)
    
    elif order == "m04":
        total_price = 150*x
        print("You have bought ")
        print("Your total is," total_price)
        
    else:
        print("Enter the correct value")
        payment_page()

landing_page()
continue_page()
payment_page()



                    
