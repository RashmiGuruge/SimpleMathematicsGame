import menuu
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="game_detail")
mycursor = mydb.cursor()


def playersdb():
    
    # Select level
    print()
    print("\t........ YOU SELECT PAST PLAYER RESULTS ........")
    print()
    print(" Name , Total questions , Correct questions , Percentage% ")
    print()
    mycursor.execute(" SELECT * FROM players_result ")

    myresults = mycursor.fetchall()

    for x in myresults:
        print(x)
            
    # print seperater
    print()
    print("__"*30)
    print()
    print()
        
    menuu.menu()
