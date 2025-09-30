import sys

#Opening
print("Welcome to the nightly forest visitor! There are three levels. Choose carefully.")
print("You see three items on a desk. Please pick one by typing the name of the item.")

#Visitor picks his weapon
while True:
    visitor_weapon = input("You see on a table a SHOVEL, AXE, SWORD. Type out what weapon you want. ").lower()
    if visitor_weapon == "shovel":
        print("Decent choice on your weapon selection.")
        break
    elif visitor_weapon == "axe":
        print("I like your choice! The axe is a good option!")
        break
    elif visitor_weapon == "sword":
        print("Excellent! You will do well!")
        break
    else:
        print("Wrong. Pick again.")

#Level 1 starts
visitor_choice = input(f"You have a {visitor_weapon}. You now walk onto a trail and encounter a fork in the trail. Do you go LEFT or RIGHT? ").lower()

if visitor_choice == "left":
    visitor_bear = input(f"You encounter a bear! You have a {visitor_weapon}. Do you stand your ground and FIGHT or RUN away? ").lower()
    if visitor_bear == "fight":
        print(f"The bear runs towards you but you have strong courage! You take your {visitor_weapon} and stab the bear! The animal falls down in defeat and you continue on your way! You notice that the trail combines but you continue forward.")
    elif visitor_bear == "run":
        print(f"You turn and drop your {visitor_weapon} and the bear stops to sniff the {visitor_weapon}. You continue to run away but dropping your {visitor_weapon} only delayed the bear shortly. You hear the bear start chasing you again! But since you dropped your {visitor_weapon}, you have no way to defend yourself. The bear eventually catches up and eats you alive!!! The end!")
        sys.exit()
    else:
        print("Invalid choice! You must type FIGHT or RUN.")
        sys.exit()

elif visitor_choice == "right":
    visitor_tired = input(f"You continue to walk this trail. With your arm getting tired holding your {visitor_weapon}. Do you decide to take a BREAK or CONTINUE? ").lower()
    if visitor_tired == "break":
        print(f"You take a break and fall asleep for a couple of hours. You wake up with your {visitor_weapon} missing. You look around for it. Then notice it's right against your neck. Then the world is dark. YOU DIED!!!")
        sys.exit()
    elif visitor_tired == "continue":
        print(f"You continue with your hike and hold your {visitor_weapon} with your other arm. You notice that the trail combines but you continue forward.")
    else:
        print("Invalid choice! You must type BREAK or CONTINUE.")
        sys.exit()
else:
    print("Invalid choice! You must type LEFT or RIGHT.")
    sys.exit()

#level 2 starts
print("You have completed level 1. Good job! Onto level 2.")

visitor_choice1 = input("You've been walking on the trail for sometime now. It's dusk and you feel your bladder full. Do you go off the trail and take a LEAK or CONTINUE forward? ").lower()

if visitor_choice1 == "leak":
    visitor_challenge = input("You decide to walk off the trail and you trip! You hit your head on a rock. You don't wake up for several hours. Then all of a sudden you start to feel something poke you. It's wet. You open your eyes and see an animal. But you don't know what you're looking at. Is it a DEER, HIKER, BIGFOOT? ").lower()
    
    if visitor_challenge == "deer":
        print("Your head is pounding and you make out the animal. It's a deer! You get startled and pee yourself. This scares off the deer. It's currently still dark out but the sun is slowing coming up. You clean yourself and decide to continue forward. Basecamp should only be a few more miles... Then you hear something behind you and feel a sharp pain in your head and you fall to the ground...")
        visitor_deer = input("You wake up inside of a cave. You can't believe your eyes! You see bigfoot and a Skin walker... Do you try to RUN or STAY? ").lower()
        if visitor_deer == "run":
            print("You slowly get up and slowly walk away out of the cave. As soon as you exit the cave. You hear the beasts start screaming! You start running as fast as you can!")
        elif visitor_deer == "stay":
            print("You hear them talking. But you can't make out what they're saying. You lay there for several minutes. You start to make out what they're talking about. They're talking about EATING YOU!!! You start to slowly get up and get out of the cave. As soon as you exit the cave, you hear them start screaming! You start running as fast as you can!")
        else:
            print("Invalid choice! You must type RUN or STAY.")
            sys.exit()
            
    elif visitor_challenge == "hiker":
        print("Your head is pounding and you try to make out the animal. But you look closer and its another hiker! Except this hiker isn't quite what they seem to be. You look closer and see rotting flesh on his face. You think to yourself, no way this is a Skinwalker. They don't exist. But the it speaks to you. The sharp voice it speaks in is painful. You cover your ears quickly but you knock yourself out from the force. You wake up in a cave with the Skinwalker and... Bigfoot??")
        visitor_hiker = input("You can't believe what you're seeing! You're in shock and have two ideas in your head. Do you RUN or STAY? ").lower()
        if visitor_hiker == "run":
            print("You slowly get up and slowly walk away out of the cave. As soon as you exit the cave. You hear the beasts start screaming! You start running as fast as you can!")
        elif visitor_hiker == "stay":
            print("You hear them talking. But you can't make out what they're saying. You lay there for several minutes. You start to make out what they're talking about. They're talking about EATING YOU!!! You start to slowly get up and get out of the cave. As soon as you exit the cave, you hear them start screaming! You start running as fast as you can!")
        else:
            print("Invalid choice! You must type RUN or STAY.")
            sys.exit()
            
    elif visitor_challenge == "bigfoot":
        print("Your head is pounding and you try to make out the animal. But it's huge! It's hairy! As your eyes clear up and you get a clearer look at the animal. You realize it looks like a Gorilla! But this one is tall. It speaks to you in a weird tone. You can barely make out what it's saying. It grabs you and you pass out again. You wake up in a cave and you see the Gorilla that grabbed you. It's bigfoot! It's talking to another aniaml...")
        visitor_bigfoot = input("You can't make out what they're talking about. Decide if you want to RUN or STAY? ").lower()
        if visitor_bigfoot == "run":
            print("You slowly get up and slowly walk away out of the cave. As soon as you exit the cave. You hear the beasts start screaming! You start running as fast as you can!")
        elif visitor_bigfoot == "stay":
            print("You hear them talking. But you can't make out what they're saying. You lay there for several minutes. You start to make out what they're talking about. They're talking about EATING YOU!!! You start to slowly get up and get out of the cave. As soon as you exit the cave, you hear them start screaming! You start running as fast as you can!")
        else:
            print("Invalid choice! You must type RUN or STAY.")
            sys.exit()
    else:
        print("Invalid choice! You must type DEER, HIKER, or BIGFOOT.")
        sys.exit()
        
elif visitor_choice1 == "continue":
    print("You continue forward and you see off in the distance some really tall animal. It looks like bigfoot... But that's not true... It can't be... You continue forward on the trail and you step on a twig. It makes a loud sound and you look where you saw bigfoot. But it's not there anymore. Then all of a sudden you wake up in a cave.")
    visitor_challenge1 = input(f"You must try to escape before they notice anything! Do you grab your {visitor_weapon.capitalize()} and FIGHT? Or quietly RUN away? ").lower()
    
    if visitor_challenge1 == visitor_weapon or visitor_challenge1 == "fight":
        no_weapon = input("You quietly go to grab your weapon but it's missing. Type RUN to run away! ").lower()
        if no_weapon == "run":
            print("You sneak out of the cave but the beasts noticed and give chase!")
        else:
            print("Invalid choice! You must type RUN.")
            sys.exit()
    elif visitor_challenge1 == "run":
        visitor_run = input("You decide to run quickly out of the cave! But the beasts notice and give chase! YELL at them while you run away! ").lower()
        if visitor_run == "yell":
            print("YOUR BREATH SMELLS LIKE A WEEK OLD EGG ROLL THAT WAS MADE AT TACO BELL!")
        else:
            print("Invalid choice! You must type YELL.")
            sys.exit()
    else:
        print(f"Invalid choice! You must type {visitor_weapon.upper()}, FIGHT, or RUN.")
        sys.exit()
else:
    print("Invalid choice! You must type LEAK or CONTINUE.")
    sys.exit()

#Level 3
print("Level 3...")
print("You have escape the cave but the beasts are right behind you!")
visitor_last_chance = input(f"You run for several miles and somehow find the trail. Do you decide to run back to your CAR, or try to find your {visitor_weapon.upper()}? ").lower()

if visitor_last_chance == "car":
    visitor_last_chance1 = input("You eventually see your car in view with the DNR nearby. Do you stay SILENT and drive away? Or ask for HELP from the DNR? ").lower()
    if visitor_last_chance1 == "silent":
        visitor_car = input("You hop into your vehicle and find a rifle. Do you choose to FIGHT or DRIVE away? ").lower()
        if visitor_car == "fight":
            print("You choose to fight the beasts with your rifle. You go in and search for 10 minutes with no luck. You return back and the DNR is actively searching for you. They find you and arrest you for DUI. You wake up in the hospital and you find out you were in a car wreck and been in a coma for 3 years.")
        elif visitor_car == "drive":
            print("You hop into your car and drive away. Then you get into an car accident and wake up in the hospital. The beasts are your doctors...")
        else:
            print("Invalid choice! You must type FIGHT or DRIVE.")
            sys.exit()
    elif visitor_last_chance1 == "help":
        print("You ask the DNR for help. They look at you strangely and ask if you're okay. You look behind you and the beasts are gone... You tell them what happened but they think you're crazy. They escort you to your car and you drive home, forever wondering if it was real...")
    else:
        print("Invalid choice! You must type SILENT or HELP.")
        sys.exit()
        
elif visitor_last_chance == visitor_weapon:
    print(f"You keep running and eventually find your {visitor_weapon}! You return to find them and attack them! You quickly get overwhelmed and the beasts get ahold of your weapon and slay you. RIP")
    sys.exit()
else:
    print(f"Invalid choice! You must type CAR or {visitor_weapon.upper()}.")
    sys.exit()

print("\nThanks for playing!")