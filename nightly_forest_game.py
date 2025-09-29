# Nightly Forest Visitor — finished version

def choose_from(prompt, options):
    """Ask until the player gives a valid choice from options."""
    opts = {opt.lower(): opt for opt in options}
    while True:
        choice = input(prompt).strip().lower()
        if choice in opts:
            return choice
        print(f"Invalid choice. Options: {', '.join(options)}")

def level_weapon():
    weapon = choose_from(
        "You see on a table a SHOVEL, AXE, SWORD. Type your weapon: ",
        ["shovel", "axe", "sword"],
    )
    if weapon == "shovel":
        print("Decent choice on your weapon selection.")
    elif weapon == "axe":
        print("I like your choice! The axe is a good option!")
    else:
        print("Excellent! You will do well!")
    return weapon

def level1(weapon):
    print(f"\nYou have a {weapon}. You reach a fork in the trail.")
    side = choose_from("Do you go LEFT or RIGHT? ", ["left", "right"])

    if side == "left":
        bear = choose_from(
            f"You encounter a bear. FIGHT or RUN? ",
            ["fight", "run"],
        )
        if bear == "fight":
            print(f"You stand your ground and strike with your {weapon}. The bear flees. You live.")
            return "alive"
        else:
            print(f"You drop your {weapon}. The bear catches you. You died.")
            return "dead"

    # side == "right"
    tired = choose_from(
        f"You keep walking, arm tired from holding your {weapon}. BREAK or CONTINUE? ",
        ["break", "continue"],
    )
    if tired == "break":
        print("You doze off. Cold steel at your neck. Fade to black. You died.")
        return "dead"
    else:
        print("You swap arms and press on. Trails merge ahead. You live.")
        return "alive"

def level2():
    print("\nLevel 2 begins. Dusk falls.")
    need = choose_from(
        "Bladder full. LEAK off the trail or CONTINUE forward? ",
        ["leak", "continue"],
    )

    if need == "leak":
        creature = choose_from(
            "You trip, black out, and wake to something wet poking you. Is it DEER, HIKER, or BIGFOOT? ",
            ["deer", "hiker", "bigfoot"],
        )
        print("You end up in a cave with two shapes arguing in the dark.")
        stayrun = choose_from("Do you RUN or STAY? ", ["run", "stay"])
        if stayrun == "run":
            print("You creep toward the exit. The beasts shriek behind you. You sprint into the dawn.")
            return "escaped_cave"
        else:
            print("You lie still, listening. They argue about eating you, then wander deeper. You slip out.")
            return "escaped_cave"

    # need == "continue"
    print("You push on. A towering shape watches from the trees. Crack. Darkness. You wake in a cave.")
    return "cave_taken"

def level3(weapon):
    print("\nLevel 3. Final stretch.")
    path = choose_from(
        "Outside the cave mouth you spot two routes: RIVER path or RIDGE path? ",
        ["river", "ridge"],
    )

    if path == "river":
        action = choose_from(
            "The current is fast. Do you BUILD a raft or FORD the water? ",
            ["build", "ford"],
        )
        if action == "build":
            print(f"You lash branches with vines, paddle with your {weapon}. The river carries you safely to basecamp. You win.")
            return "win"
        else:
            print("You step in and the current slams you into rocks. You black out. You died.")
            return "dead"

    # path == "ridge"
    hazard = choose_from(
        "Loose shale underfoot. Do you CRAWL carefully or SPRINT for the top? ",
        ["crawl", "sprint"],
    )
    if hazard == "crawl":
        print("Slow and steady. You crest the ridge, spot smoke, and reach basecamp by noon. You win.")
        return "win"
    else:
        print("You sprint. The ridge gives way. You tumble into the ravine. You died.")
        return "dead"

def play_once():
    print("Welcome to the nightly forest visitor. Three levels, choose carefully.")
    weapon = level_weapon()
    if level1(weapon) == "dead":
        return "dead"
    cave_state = level2()
    if cave_state in ("escaped_cave", "cave_taken"):
        return level3(weapon)
    return "dead"

def main():
    while True:
        result = play_once()
        print("\n=== Game Over ===")
        if result == "win":
            print("You survived the forest and made it to basecamp.")
        else:
            print("Your story ends here.")
        again = choose_from("\nPlay again? YES or NO: ", ["yes", "no"])
        if again == "no":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
