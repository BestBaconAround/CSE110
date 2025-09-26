#Greeting
player_name = input("Welcome to Bacon's Resturant! What is your name? ")
player_response1 = input(f"Hello {player_name}! I should warn you. There are dangers waiting inside. You must prepare youself for the untold mysteries. Are you ready? Reply YES or NO. ").upper()

if player_response1 == "YES":
    player_agrees = True
    print("Great! Start walking inside now.")
else:
    print("I'm sorry to hear that. Good day")


while True:
    player_challenge1 = int(input("You encounter Joe at the entrance. He asks you if you know what 2 * 2 equals. Type your response. "))
    if player_challenge1 == 4:
        print("-Joe That's correct! You may move forward.")
        break
    else:
        print("That is not correct! Please try again!")

player_food = input("You walk into the resturant and the waiter asks if you would like Mexican, American, or Asian. Type in what food you want")
if player_food == "mexican":
    print("Great! You'll be having Mexican food!")
elif player_food == "american":
    
        