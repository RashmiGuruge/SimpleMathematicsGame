
import menuu
import mysql.connector
from mysql.connector import Error

# Check Connectivity 
try:
    conn = mysql.connector.connect(host='localhost',user='root',password='')
    if conn.is_connected():
        print("Connection Successfull")
except Error as e:
    print("Oops!")
    print("Connection fails")
    print(e)

# Title
print()
title = "\t\tA Simple Mathematics Game"
print()
print("**" * len(title))
print(title)
print("**" * len(title))
print()
print()

# Check the player play this game before
print("  Have you played this game on this device before ?")
print(" \t1. YES")
print(" \t2. NO")
print("  (Please, Give your answer correctly.)")
print()
f = input("Enter Your Option: ")
print()
print()

if f=="1":
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="game_detail")
    mycursor = mydb.cursor()
    sqlFormula = "INSERT INTO players_result( name , Total_Questions , Correct_Questions , Percentage ) VALUES(%s,%s,%s,%s)"
else:
    # create database
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE game_detail")
    
    # Create table
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="game_detail")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE players_result (name VARCHAR(20),Total_Questions INT(255),Correct_Questions INT(255),Percentage VARCHAR(10))")

# Print game menu
menuu.menu()
