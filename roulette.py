import random 
import time
import pyinputplus

colors = ["red", "black"]
wallet = 0


def bet_coins(color_list, wallet):
    # Chooses random color from given list
    random_color = color_list[random.randint(0,len(color_list))]
    
    
    try:
        bet = int(input("How much do you want to bet: "))
        if bet < 0:
            print("Bets can't be negative!")
        elif bet > wallet:
            print("You can't bet more thean you have!")
    except:
        print("Please enter a valid amount!")
        
    while True:
        color_guess = input("Enter a color (red or black): ").lower()
        if color_guess in colors:
            continue
        else: 
            print("Please enter (red or black)!")
            print()
            
    # Game loop
        if color_guess == random_color:
            bet*2
        else:
            print("You guessed wrong!")
            print("Try again another time!")

def check_wallet(wallet):
    print(wallet)
    


def beg():
    min = 5
    max = 50
    beg_profet =  random.randint(min,max)
    print(f"You have recived {beg_profet} coins!")
    return beg_profet

# TUTORIAL -------------------------------------------------------------
print("This is a game called Roulette!")
print("You bet an amount and then you have to guess a color. Red or Black!")
print("If you guess it right then your bet you put in doubles and you can keep going till you want to back out")
print("But if you lose, then you lose all of what you bet!")
print("Good luck!")
    
    
print("Did you bring any money?")
print("Looks like your going to have to beg...")
while True:
    beg_command = input("Enter command (beg): ").lower()
    if beg_command == "beg":
        break
    else: 
        print("Please enter the command (beg)")

wallet = beg()


print("Looks like you can bet now!")
while True:
    bet_command = input("Enter command (bet): ").lower()
    if bet_command == "bet":
        break
    else: 
        print("Please enter the command (bet)")

bet_coins(colors, wallet)
        
print("Lets see how much you have in your wallet!")

while True:
    wallet_command = ("Enter command (wallet): ").lower()
    if wallet_command == "wallet":
        break
    else: 
        print("Please enter the command (wallet)")
        
check_wallet(wallet)

print("Looks like you can do it yourself.")
print("If you even need any help just type (help)!")


while True:
    command = input("Enter a command: ").lower()
    if command == "help":
        print("The commands you can use are (beg, )")

