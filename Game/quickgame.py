# Quick Game

import menuu
import mysql.connector

def quick():

    import random
    
    print("\t......... YOU SELECT QUICK GAME .........")

    # Create variables
    rand1 = 0
    rand2 = 0
    ques = 0
    ans = 0
    num = 0
    count = 0
    per = 0
    abc = 5

    # create a list
    score = []
    
    # Getting user name
    name = input("\nEnter your name : ")
    print()
    
    for i in range (5):
        
        # Generate numbers till 10
        rand1 = random.randrange(10)
        rand2 = random.randrange(10)
        
        # Displaying the correct answer
        num = rand1 + rand2
        
        # Displaying output and getting player answer 
        ques = int(input(str(rand1) + " + " + str(rand2) + " ? "))

        # Displaying game result
        if (ques == num):
            score.append( str(rand1) + " + " + str(rand2) + " ? " + str(ques) + "   [Answer is " + str(num) + "]   [Correct] ")
            count += 1
        else:
            score.append( str(rand1) + " + " + str(rand2) + " ? " + str(ques) + "   [Answer is " + str(num) + "]   [Incorrect] ")

    # Displaying game detail
    print()
    print("\t.....Game Result.....")
    print()
    print("Your name is",name,".")
    print("You played the game with Quick game.")
    print("You answerd 5 questions.")
    print()

    # Displaying score
    for i in range(5):
        print(score[i])
    
    # Displaying score
    print()
    print("You answered 5 questions with",count,"correct.")
     
    # Percentage of the score       
    per = (count/5) * 100

    # Displaying Percentage
    print("Your score percentage is",per,"%.")

    # print past player's information
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="game_detail")
    player = (name , abc , count , per)
    mycursor = mydb.cursor()
    sqlFormula = "INSERT INTO players_result( name , Total_Questions , Correct_Questions , Percentage) VALUES(%s,%s,%s,%s)"
    mycursor.execute(sqlFormula , player)
    mydb.commit()

    # print seperater
    print()
    print("__"*30)
    print()
    print()
    
    menuu.menu()
    

            
        
    

        
    
        
    
    
    

    
    
    
    
