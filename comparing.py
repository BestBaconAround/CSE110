animal = input("What is your favorite animal? ").lower()
sound = ""

if animal == "cat":
    sound = "meow"
elif animal == "dog":
    sound = "ruff"
else:
    sound = "unknown"
    
print(f"The {animal} makes the sound: {sound}.")