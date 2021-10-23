import random
import time

running = True
my_bead = 10
computer_bead = 10
attack_turn = True

print("Let's start the playing marbles ")
print()
print("________________________________________________")
print("I'll explain the rules of playing marbles.")

print()
print(""" 
Each player starts with 10 beads.
Decide how many beads the first-man player will grab.
And a junior player bets on his marble. Next, it refers to whether the number of beads is a hole or a pair.
If you get it right, the player who made the opponent's marble as many times as the number of bets will get it, and if it's wrong, the player who made the first gets it.
If one person loses all the beads, the game is over.
    """)

print("Before we start, we will decide the order by rock-paper-scissors.")
print()
time.sleep(2)


# Rock,Scissors,Paper

while running:

    rsp = input("What would you like to release? (Choose between scissors, rock, paper): ")
    Rsp = ['rock','scissors','paper']
    Rsp_choice = random.sample(Rsp,1)
    F_L = ['first' , 'later']
    computer_choice = random.sample(F_L,1)
    print()

    if rsp != 'scissors' and rsp != 'rock' and rsp != 'paper':
        print("Enter only one of rock, paper, scissors.")
        continue

    if rsp == Rsp_choice[0]:
        print("It's a tie, so please release it again.")
        continue

    if rsp == 'scissors' and Rsp_choice[0] == 'paper':
        my_choice = input("You won. Please choose between first and later: ")
        print()
        if my_choice != 'first' and my_choice != 'later':
            print("Please enter only first or later!")
            continue
        print()
        print(f"You are the {my_choice}.")
    

    if rsp == 'scissors' and Rsp_choice[0] == 'rock':
        print("You lost. The computer decides first and later.")
        print()
        time.sleep(2)
        print(f" Computer is the {computer_choice[0]}.")
        print()
        
    if rsp == 'rock' and Rsp_choice[0] == 'scissors':
        my_choice = input("You won. Please choose between first and later: ")
        print()
        if my_choice != 'first' and my_choice != 'later':
            print("Please enter only first or later!")
            continue
        print()
        print(f"You are the {my_choice}.")
       
    if rsp == 'rock' and Rsp_choice[0] == 'paper':
        print("You lost. The computer decides first and later.")
        print()
        time.sleep(2)
        print(f" Computer is the {computer_choice[0]}.")
        print()

    if rsp == 'paper' and Rsp_choice[0] == 'rock':
        my_choice = input("You won. Please choose between first and later: ")
        print()
        if my_choice != 'first' and my_choice != 'later':
            print("Please enter only first or later!")
            continue
        print()
        print(f"You are the {my_choice}.")
        

    if rsp == 'paper' and Rsp_choice[0] == 'scissors':
        print("You lost. The computer decides first or later.")
        print()
        time.sleep(2)
        print(f" Computer is the {computer_choice[0]}.")
        print()
       
    break    


# Playing marbles.

while running:
    nums = [1,2,3,4,5,6,7,8,9,10]
    computer_nums = random.sample(nums,1)
    choice = ['odd','even']
    computer_choice_hz = random.sample(choice,1)
    computer_num_refresh = []
    
    try :
        if my_choice == 'first':
            if attack_turn :

                try:
                    my_choices = int(input("Please decide the number of beads (input only the number): "))
                    print()
                except ValueError:
                    print("Just enter the number.")
                    continue
                
                if my_choices > my_bead:
                    print("You can't bet more than the number of beads you own.")
                    continue
                print()
                
                if my_choices <= 0 :
                    print("Zero and negative numbers cannot be entered.")
                    continue
                print()

                if computer_nums[0] >= computer_bead:
                        for i in range(1,computer_bead):
                            computer_num_refresh.append(i)
                            number = random.sample(computer_num_refresh,1)
                        computer_nums[0] = number[0]

                
                print(f"""
You have chosen {my_choices}.
Please wait for the computer to choose!
                """)
                time.sleep(2)

                print(f"""
The choice of computer is {computer_choice_hz[0]}.                
                """)

                # Make sure it's odd or even.
                if my_choices % 2 == 0:
                    answer = 'even'
                else:
                    answer = 'odd'
                

                if answer == computer_choice_hz[0]:
                    my_bead -= computer_nums[0]
                    computer_bead += computer_nums[0]
            

                    # Initialize if the number of beads is negative or more than 20.

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                        
                    print(f"""
The computer got it right. There are {computer_nums[0]} beads bet by the computer.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                

                else:
                    my_bead += computer_nums[0]
                    computer_bead -= computer_nums[0]

                    # Initialize if the number of beads is negative or more than 20.

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
The computer is wrong. There are {computer_nums[0]} beads bet by the computer.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                attack_turn = False
 
            else:
                my_selection = input("Choose odd or even: ")
                print()
                
                if my_selection != 'odd' and my_selection != 'even':
                    print("Please enter only odd or even.")
                    continue
                print()

                try:
                    my_choice_2 = int(input("Please decide the number of beads (input only the number): "))
                    print()
                except ValueError:
                    print("Just enter the number.")
                    continue

                
                if my_choice_2 > my_bead:
                    print("You can't bet more than the number of beads you own.")
                    continue
                print()

                if my_choice_2 <= 0 :
                    print("Zero and negative numbers cannot be entered.")
                    continue
                print()

                print("The computer is determining the number of beads. Please wait.")
                time.sleep(2)

                if computer_nums[0] >= computer_bead:
                        for i in range(1,computer_bead):
                            computer_num_refresh.append(i)
                            number = random.sample(computer_num_refresh,1)
                        computer_nums[0] = number[0]


                if int(computer_nums[0]) % 2 == 0:
                    answer = 'even'
                
                else:
                    answer = 'odd'


                print(f"The computer made {computer_nums[0]} beads.")
                time.sleep(2)


                if answer == my_selection:
                    my_bead += my_choice_2
                    computer_bead -= my_choice_2


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20


                    print(f"""
You got it right. You bet {my_choice_2} beads.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                
                
                else:
                    my_bead -= my_choice_2
                    computer_bead += my_choice_2


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
You're wrong. You bet {my_choice_2} beads.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                attack_turn = True


        if my_choice == 'later':
            if attack_turn:
                my_selection = input("Choose odd or even: ")
                print()
                
                if my_selection != 'odd' and my_selection != 'even':
                    print("Please enter only odd or even.")
                    continue
                print()

                try:
                    my_choice_2 = int(input("Please decide the number of beads (input only the number): "))
                    print()
                except ValueError:
                    print("Just enter the number.")
                    continue

                
                if my_choice_2 > my_bead:
                    print("You can't bet more than the number of beads you own.")
                    continue
                print()

                if my_choice_2 <= 0 :
                    print("Zero and negative numbers cannot be entered.")
                    continue
                print()

                print("The computer is determining the number of beads. Please wait.")
                time.sleep(2)

                if computer_nums[0] >= computer_bead:
                        for i in range(1,computer_bead):
                            computer_num_refresh.append(i)
                            number = random.sample(computer_num_refresh,1)
                        computer_nums[0] = number[0]


                if int(computer_nums[0]) % 2 == 0:
                    answer = 'even'
                
                else:
                    answer = 'odd'


                print(f"The computer made {computer_nums[0]} beads.")
                time.sleep(2)


                if answer == my_selection:
                    my_bead += my_choice_2
                    computer_bead -= my_choice_2


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20


                    print(f"""
You got it right. You bet {my_choice_2} beads.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                
                
                else:
                    my_bead -= my_choice_2
                    computer_bead += my_choice_2


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
You're wrong. You bet {my_choice_2} beads.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                attack_turn = False
            
            else:
                try:
                    my_choices = int(input("Please decide the number of beads (input only the number): "))
                    print()
                except ValueError:
                    print("Just enter the number.")
                    continue
                
                if my_choices > my_bead:
                    print("You can't bet more than the number of beads you own.")
                    continue
                print()
                
                if my_choices <= 0 :
                    print("Zero and negative numbers cannot be entered.")
                    continue
                print()

                if computer_nums[0] >= computer_bead:
                        for i in range(1,computer_bead):
                            computer_num_refresh.append(i)
                            number = random.sample(computer_num_refresh,1)
                        computer_nums[0] = number[0]

                
                print(f"""
You have chosen {my_choices}.
Please wait for the computer to choose!
                """)
                time.sleep(2)

                print(f"""
The choice of computer is {computer_choice_hz[0]}.                
                """)

                if my_choices % 2 == 0:
                    answer = 'even'
                else:
                    answer = 'odd'
                

                if answer == computer_choice_hz[0]:
                    my_bead -= computer_nums[0]
                    computer_bead += computer_nums[0]
            


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                        
                    print(f"""
The computer got it right. There are {computer_nums[0]} beads bet by the computer.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                

                else:
                    my_bead += computer_nums[0]
                    computer_bead -= computer_nums[0]


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
The computer is wrong. There are {computer_nums[0]} beads bet by the computer.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                attack_turn = True

                

    except NameError:
        if computer_choice[0] == 'first':
            if attack_turn:
                my_selection = input("Choose odd or even: ")
                print()
                
                if my_selection != 'odd' and my_selection != 'even':
                    print("Please enter only odd or even.")
                    continue
                print()

                try:
                    my_choice_2 = int(input("Please decide the number of beads (input only the number): "))
                    print()
                except ValueError:
                    print("Just enter the number.")
                    continue

                
                if my_choice_2 > my_bead:
                    print("You can't bet more than the number of beads you own.")
                    continue
                print()

                if my_choice_2 <= 0 :
                    print("Zero and negative numbers cannot be entered.")
                    continue
                print()

                print("The computer is determining the number of beads. Please wait.")
                time.sleep(2)

                if computer_nums[0] >= computer_bead:
                        for i in range(1,computer_bead):
                            computer_num_refresh.append(i)
                            number = random.sample(computer_num_refresh,1)
                        computer_nums[0] = number[0]


                if int(computer_nums[0]) % 2 == 0:
                    answer = 'even'
                
                else:
                    answer = 'odd'


                print(f"The computer made {computer_nums[0]} beads.")
                time.sleep(2)


                if answer == my_selection:
                    my_bead += my_choice_2
                    computer_bead -= my_choice_2


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20


                    print(f"""
You got it right. You bet {my_choice_2} beads.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                
                
                else:
                    my_bead -= my_choice_2
                    computer_bead += my_choice_2


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
You're wrong. You bet {my_choice_2} beads.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                attack_turn = False


            else:
                try:
                    my_choices = int(input("Please decide the number of beads (input only the number): "))
                    print()
                except ValueError:
                    print("Just enter the number.")
                    continue
                
                if my_choices > my_bead:
                    print("You can't bet more than the number of beads you own.")
                    continue
                print()
                
                if my_choices <= 0 :
                    print("Zero and negative numbers cannot be entered.")
                    continue
                print()

                if computer_nums[0] >= computer_bead:
                        for i in range(1,computer_bead):
                            computer_num_refresh.append(i)
                            number = random.sample(computer_num_refresh,1)
                        computer_nums[0] = number[0]

                
                print(f"""
You have chosen {my_choices}.
Please wait for the computer to choose!
                """)
                time.sleep(2)

                print(f"""
The choice of computer is {computer_choice_hz[0]}.                
                """)

                if my_choices % 2 == 0:
                    answer = 'even'
                else:
                    answer = 'odd'
                

                if answer == computer_choice_hz[0]:
                    my_bead -= computer_nums[0]
                    computer_bead += computer_nums[0]
            

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                        
                    print(f"""
The computer got it right. There are {computer_nums[0]} beads bet by the computer.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                

                else:
                    my_bead += computer_nums[0]
                    computer_bead -= computer_nums[0]


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
The computer is wrong. There are {computer_nums[0]} beads bet by the computer.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                attack_turn = True


                
        if computer_choice[0] == 'later':
            if attack_turn:
                
                try:
                    my_choices = int(input("Please decide the number of beads (input only the number): "))
                    print()
                except ValueError:
                    print("Just enter the number.")
                    continue
                
                if my_choices > my_bead:
                    print("You can't bet more than the number of beads you own.")
                    continue
                print()
                
                if my_choices <= 0 :
                    print("Zero and negative numbers cannot be entered.")
                    continue
                print()

                if computer_nums[0] >= computer_bead:
                        for i in range(1,computer_bead):
                            computer_num_refresh.append(i)
                            number = random.sample(computer_num_refresh,1)
                        computer_nums[0] = number[0]

                
                print(f"""
You have chosen {my_choices}.
Please wait for the computer to choose!
                """)
                time.sleep(2)

                print(f"""
The choice of computer is {computer_choice_hz[0]}.                
                """)

                if my_choices % 2 == 0:
                    answer = 'even'
                else:
                    answer = 'odd'
                

                if answer == computer_choice_hz[0]:
                    my_bead -= computer_nums[0]
                    computer_bead += computer_nums[0]
            

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                        
                    print(f"""
The computer got it right. There are {computer_nums[0]} beads bet by the computer.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                

                else:
                    my_bead += computer_nums[0]
                    computer_bead -= computer_nums[0]


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
The computer is wrong. There are {computer_nums[0]} beads bet by the computer.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                attack_turn = False

            else:
                my_selection = input("Choose odd or even: ")
                print()
                
                if my_selection != 'odd' and my_selection != 'even':
                    print("Please enter only odd or even.")
                    continue
                print()

                try:
                    my_choice_2 = int(input("Please decide the number of beads (input only the number): "))
                    print()
                except ValueError:
                    print("Just enter the number.")
                    continue

                
                if my_choice_2 > my_bead:
                    print("You can't bet more than the number of beads you own.")
                    continue
                print()

                if my_choice_2 <= 0 :
                    print("Zero and negative numbers cannot be entered.")
                    continue
                print()

                print("The computer is determining the number of beads. Please wait.")
                time.sleep(2)

                if computer_nums[0] >= computer_bead:
                        for i in range(1,computer_bead):
                            computer_num_refresh.append(i)
                            number = random.sample(computer_num_refresh,1)
                        computer_nums[0] = number[0]


                if int(computer_nums[0]) % 2 == 0:
                    answer = 'even'
                
                else:
                    answer = 'odd'


                print(f"The computer made {computer_nums[0]} beads.")
                time.sleep(2)


                if answer == my_selection:
                    my_bead += my_choice_2
                    computer_bead -= my_choice_2


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20


                    print(f"""
You got it right. You bet {my_choice_2} beads.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                
                
                else:
                    my_bead -= my_choice_2
                    computer_bead += my_choice_2


                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
You're wrong. You bet {my_choice_2} beads.
The number of your beads is {my_bead}. The number of beads on the computer is {computer_bead}.
                    """)
                attack_turn = True

                            
    # Game Over
    if my_bead <= 0:

        print("You are loses!")
        time.sleep(3)
        running = False
    
    if computer_bead <=0:
        print("You are win!")
        time.sleep(3)
        running = False

    
