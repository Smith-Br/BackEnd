# Ex. 3 --- --- --- --- --- ---
from random import randrange


def Ex3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for num in a:
        if num < 5:
            print(num)
    ins = int(input("Your Number: "))
    for num in a:
        if num < ins:
            print(num)
Ex3()#

# Ex. 4 --- --- --- --- --- ---
def Ex4():
    input_from_user = int(input("Your Number: "))
    for value_of_input_from_user in range(1, input_from_user):
        if (input_from_user % value_of_input_from_user == 0):
            print(value_of_input_from_user)
Ex4()#

# Ex. 5 --- --- --- --- --- ---
print('--- --- --- --- --- ---')
def Ex5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for i in a and b:
        if i in a and b:
            print(i)
Ex5()#

# Ex. 6 --- --- --- --- --- ---
def Ex6():
    input_from_user = input("Your Word: ")
    palindrome = input_from_user[::-1]
    print(palindrome)
    if palindrome == input_from_user:
        print("This is a palindrome")
    else:
        print("This isn't a palindrom")
Ex6()#

# Ex. 7 --- --- --- --- --- ---
def Ex7():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print([i for i in a if i % 2 == 0])
Ex7()

# Ex. 8 --- --- --- --- --- ---
def Ex8():
    player_1 = input("Your Choose (Player 1): ")
    player_2 = input("Your Choose (Player 2): ")
    if player_1.lower() == "rock":
        if player_2.lower() == "scissors":
            print("Player 1: You win!\nPlayer 2: You lose!")
        elif player_2.lower() == "paper":
            print("Player 1: You lose!\nPlayer 2: You win!")
        elif player_2.lower() == "rock":
            print("Draw!")
        else:
            print("Your choose unavaiable!")
    elif player_1.lower() == "scissors":
        if player_2.lower() == "paper":
            print("Player 1: You win!\nPlayer 2: You lose!")
        elif player_2.lower() == "rock":
            print("Player 1: You lose!\nPlayer 2: You win!")
        elif player_2.lower() == "scissors":
            print("Draw!")
        else:
            print("Your choose unavaiable!")
    elif player_1.lower() == "paper":
        if player_2.lower() == "rock":
            print("Player 1: You win!\nPlayer 2: You lose!")
        elif player_2.lower() == "scissors":
            print("Player 1: You lose!\nPlayer 2: You win!")
        elif player_2.lower() == "paper":
            print("Draw!")
        else:
            print("Your choose unavaiable!")
    else:
        print("Your choose unavaiable!")
Ex8()

# Ex. 9 --- --- --- --- --- ---
def Ex9():
    from random import Random
    count_time = 0
    while 1:
        count_time = count_time + 1
        import random
        input_from_user = input("Input your number: ")
        if input_from_user == "exit":
            if count_time <= 1 :
                print("You guessed: " + str(count_time) + " Time")
            else:
                print("You guessed: " + str(count_time) + " Times")
            break
        input_from_user=int(input_from_user)
        if input_from_user == random.randrange(1, 9):
            print("Correct! You're very lucky!")
        if input_from_user < 1:
            print("Sorry! Your number is too low!")
        elif input_from_user > 9:
            print("Sorry! Your number is too high!")
Ex9()