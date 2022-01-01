# Ex. 3 --- --- --- --- --- ---
import random


def Ex3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for num in a:
        if num < 5:
            print(num)
    ins = int(input("Your Number: "))
    for num in a:
        if num < ins:
            print(num)


Ex3()

# Ex. 4 --- --- --- --- --- ---


def Ex4():
    input_from_user = int(input("Your Number: "))
    for value_of_input_from_user in range(1, input_from_user):
        if (input_from_user % value_of_input_from_user == 0):
            print(value_of_input_from_user)


Ex4()

# Ex. 5 --- --- --- --- --- ---
print('--- --- --- --- --- ---')


def Ex5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for i in a and b:
        if i in a and b:
            print(i)


Ex5()

# Ex. 6 --- --- --- --- --- ---


def Ex6():
    input_from_user = input("Your Word: ")
    palindrome = input_from_user[::-1]
    print(palindrome)
    if palindrome == input_from_user:
        print("This is a palindrome")
    else:
        print("This isn't a palindrom")


Ex6()

# Ex. 7 --- --- --- --- --- ---


def Ex7():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print([i for i in a if i % 2 == 0])


Ex7()

# Ex. 8 --- --- --- --- --- ---


def Ex8():
    player_1 = input("Your Choose (Player 1): ")
    player_2 = input("Your Choose (Player 2): ")
    player_1 = player_1.lower()
    player_2 = player_2.lower()
    if player_1 == "rock":
        if player_2 == "scissors":
            print("Player 1: You win!\nPlayer 2: You lose!")
        elif player_2 == "paper":
            print("Player 1: You lose!\nPlayer 2: You win!")
        elif player_2 == "rock":
            print("Draw!")
        else:
            print("Your choose unavaiable!")
    elif player_1 == "scissors":
        if player_2 == "paper":
            print("Player 1: You win!\nPlayer 2: You lose!")
        elif player_2 == "rock":
            print("Player 1: You lose!\nPlayer 2: You win!")
        elif player_2 == "scissors":
            print("Draw!")
        else:
            print("Your choose unavaiable!")
    elif player_1 == "paper":
        if player_2 == "rock":
            print("Player 1: You win!\nPlayer 2: You lose!")
        elif player_2 == "scissors":
            print("Player 1: You lose!\nPlayer 2: You win!")
        elif player_2 == "paper":
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
            if count_time <= 1:
                print("You guessed: " + str(count_time) + " Time")
            else:
                print("You guessed: " + str(count_time) + " Times")
            break
        input_from_user = int(input_from_user)
        if input_from_user == random.randrange(1, 9):
            print("Correct! You're very lucky!")
        if input_from_user < 1:
            print("Sorry! Your number is too low!")
        elif input_from_user > 9:
            print("Sorry! Your number is too high!")


Ex9()

# Ex. 10 --- --- --- --- --- ---


def Ex10():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # write this in one line.
    # use at least one list comprehension.
    print([i for i in a and b if i in a and b])  # List comprehension.


Ex10()

# Ex. 11 --- --- --- --- --- ---


def Ex11():
    import sys
    # import sys lib.
    prime = int(input("Your number: "))
    if prime > 1:
        for i in range(2, prime - 1):
            if prime % i != 0:
                continue
            elif prime % i == 0:
                sys.exit("The number isn't prime")
        sys.exit("The number is prime")
    else:
        print("The number is prime")


Ex11()

# Ex. 12 --- --- --- --- --- ---


def Ex12():
    a = [5, 10, 15, 20, 25]
    print(a[0], a[-1])


Ex12()

# Ex. 13 --- --- --- --- --- ---


def Ex13():
    num = int(input("Times: "))
    fibonacci = [1, 1]
    i = 1
    while i < (num - 1):
        fibonacci.append(fibonacci[i] + fibonacci[i-1])
        i = i + 1
    print(fibonacci)


Ex13()

# Ex. 14 --- --- --- --- --- ---


def Ex14():
    a = [1, 2, 3, 3, 4, 2, 1, 5, 2, 3, 1]
    a = set(a)
    print(a)


Ex14()
# Extra:


def Extra_Ex14():
    a = {1, 2, 3}
    b = {3, 4, 5}
    print(a | b, a & b)


Extra_Ex14()

# Ex. 15 --- --- --- --- --- ---


def Ex15():
    input_from_user = input("Input your command: ")
    print(" ".join(input_from_user.split()[::-1]))


Ex15()

# Ex. 16 --- --- --- --- --- ---


def Ex16():
    import random
    Stringinpass = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=_+:!@#$%^&*()"
    passlength = int(input("Length of password you want: "))
    print("".join(random.sample(Stringinpass, passlength)))


Ex16()

# Ex. 17 --- --- --- --- --- ---


def Ex17():
    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            print(story_heading.a.text.replace("\n", " ").strip())
        else:
            print(story_heading.contents[0].strip())


Ex17()

# Ex. 18 --- --- --- --- --- ---


def Ex18(number, user_guess):
    cowbull = [0, 0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1] += 1
        else:
            cowbull[0] = +1
    return cowbull


if __name__ == "__main__":
    playing = True
    number = str(random.randint(0, 9999))
    guesses = 0

    print("Let's play a game of Cowbull!")  # explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input("Give me your best guess!")
        if user_guess == "exit":
            break
        cowbullcount = Ex18(number, user_guess)
        guesses += 1
        print("You have " + str(cowbullcount[0]) +
              " cows, and " + str(cowbullcount[1]) + " bulls.")
        if cowbullcount[1] == 4:
            playing = False
            print("You win the game after " + str(guesses) +
                  "! The number was " + str(number))
            break  # redundant exit
        else:
            print("Your guess isn't quite right, try again.")
Ex18()
# Ex. 20 --- --- --- --- --- ---
