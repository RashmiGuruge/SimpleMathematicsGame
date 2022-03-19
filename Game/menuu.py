# Main program

def menu():
    
    import quickgame
    import easy
    import medium
    import hard
    import db

    # Displaying game menu
    print("\n\t____________ Game Menu ____________")
    print()
    print("\t\t (1). Quick game")
    print("\t\t (2). Custom game")
    print("\t\t (3). Display the past game detail")
    print("\t\t (4). Exit")
    
    # Get user choice
    choice = int(input("\nEnter your option : "))
    
    # Selection
    if choice == 1:
        quickgame.quick()
    elif choice == 2:
        
        print()
        print("Select you defficulty level")
        print("\t1.Easy")
        print("\t2.Medium")
        print("\t3.Hard")
        print()
        
        l=int(input("Enter your option : "))
        if l == 1:
            easy.easylevel()
        elif l == 2:
            medium.mediumlevel()
        elif l == 3:
            hard.hardlevel()
            
    elif choice == 3:
        db.playersdb()
    else:
        choice == 4
        print("\t.....You have exited the game.....")
    
        quit()


    
