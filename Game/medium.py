# Medium Level

import menuu
import mysql.connector

def mediumlevel():
    
    import random

    # Create variables
    rand1 = 0  
    rand2 = 0
    rand3 = 0
    ques = 0
    num = 0
    num1 = 0
    oper = 0
    count = 0
    per = 0

    # Create a list
    score = []
    
    # Select level
    print()
    print()
    print("\t........ YOU SELECT MEDIUM LEVEL ........")

    # Getting user name
    name = input("\nEnter your name : ")
    
    # Number of questions
    num1 = int(input("\nHow many questions you want :"))
    print()
    
    for i in range (num1):
        
        # Generate numbers till 50
        rand1 = random.randrange(0,50)
        rand2 = random.randrange(0,50)

        # operators
        operators = ['+','-']
        
        # select operators randomly
        rand3 = random.choice(operators)

        # Geting correct answer
        if (rand3 == "+") :
            num = rand1 + rand2
        else :
            (rand3 == "-")
            num = rand1 - rand2
        
        # Displaying output and getting player answer
        ques = int(input(str(rand1) + str(rand3) + str(rand2) + " ? "))
       
        # Displaying game result
        if (ques == num):
            score.append(str(rand1) + str(rand3) + str(rand2) + " ? " + str(ques) + "   [Answer is " + str(num) + "]   [Correct] ")
            count += 1
        else:
            score.append(str(rand1) + str(rand3) + str(rand2) + " ? " + str(ques) + "   [Answer is " + str(num) + "]   [Incorrect] ")

    # Displaying game detail
    print()
    print("\t.....Game Result.....")
    print()
    print("Your name is",name,".")
    print("You played the game with Medium mode.")
    print("You answerd",num1,"questions.")
    print()

    # Displaying score
    for i in range(num1):
        print(score[i])
    
    # Displaying score
    print()
    print("You answered",num1,"questions with",count,"correct.")
     
    # Percentage of the score       
    per = (count/num1) * 100

    # Displaying Percentage
    print("Your score percentage is",per,"%.")

    # print past player's information
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="game_detail")
    player = ( name , num1 , count , per)
    mycursor = mydb.cursor()
    sqlFormula = "INSERT INTO players_result( name , Total_Questions , Correct_Questions , Percentage ) VALUES(%s,%s,%s,%s)"
    mycursor.execute(sqlFormula , player)
    mydb.commit()

    # print seperater
    print()
    print("__"*30)
    print()
    print()
    
    menuu.menu()
 








            
            
    
    
