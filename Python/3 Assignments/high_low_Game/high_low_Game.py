def high_low_game():
    import random
    round:int=1
    score:int=0
    print('Welcome to the High-Low Game!\n')
    while round <= 5:   
        user_number=random.randint(1,100)
        sys_number=random.randint(1,100)
        print(f"Round: {round}")
        print(f"Your number is {user_number}")
        user_guse=input("Do you think your number is higher or lower than the computer's?:").lower().strip()
        if user_guse == "higher" and user_number > sys_number:  
            print(f"You were right! The computer's number was {sys_number}")
            score+=1
            print(f"Your score is now {score}\n")
        elif user_guse  == "higher" and user_number < sys_number:
            print(f"Aww, that's incorrect. The computer's number was {sys_number}")
            print(f"Your score is now {score}\n")
        elif user_guse == "lower" and  user_number < sys_number:
            print(f"You were right! The computer's number was {sys_number}")
            score+=1
            print(f"Your score is now {score}\n")
        elif user_guse == "lower" and  user_number > sys_number:
            print(f"Aww, that's incorrect. The computer's number was {sys_number}")
            print(f"Your score is now {score}\n")
        else:
            print("Error! Invalid Input: \t Please Enter Only 'Higher' or 'Lower' \n")

        round+=1
    print("Thanks for playing!")
    print("Good job, you played really well!")

high_low_game()