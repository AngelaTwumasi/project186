#This is the name of the project
print("WELCOME TO SPACE PIRATES")

charName=(input("what shall we call you?"))

print("Greetings "+charName + " you look dangerous. Let's roll for attributes.")

import random 
 #This rolls 2-six-sided dice and it's resulting numbers

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

 #calculating roll for Attributes

charStrength = dice1 + dice2
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

charIntelligence = dice1 + dice2
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

charCharisma = dice1 + dice2
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

charDexterity = dice1 + dice2
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

charHealth = dice1 + dice2
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
 
#Printing the roll Attribute
print(f"Strength: {charStrength}")
print(f"Intelligence: {charIntelligence}")
print(f"Charisma: {charCharisma}")
print(f"Dexterity: {charDexterity}")
print(f"Health: {charHealth}")


        # This code will define the race options
race_options = {
    1: "Human – no description required",
    2: "Slane – reptile humanoid – strong but slow",
    3: "Droid – no organic flesh – strong but poor on communication",
    4: "Krill – four arms, plenty of attitude, healing ability",
    5: "Cyborg – part man, part machine",
    6: "Mutant – strong, faster – uglier"
}
# This code will display the race options
print("Choose your race:")
for num, description in race_options.items():
    print(f"{num}. {description}")

# This code will Get user input
race_choice = int(input("Enter the number corresponding to your chosen race: "))

# This code will Validate input
if race_choice in race_options:
    print(f"Your chosen race: {race_options[race_choice]}")
else:
    print("Invalid choice. Please select a valid race number.")
if race_choice == 1:
    charHealth = charHealth + 1 
    print(charHealth)
if race_choice == 1:
    charCharisma = charCharisma + 1 
    print(charCharisma)
    
if race_choice == 2:
    charStrength = charStrength + 3 
    print(charStrength)
if race_choice == 2:
    charDexterity = charDexterity - 2
    print(charDexterity)
    
if race_choice == 3:
    charStrength = charStrength + 5
    print(charStrength)
if race_choice == 3:
    charCharisma = charCharisma - 3 
    print(charCharisma)
    
if race_choice == 4:
    charHealth = charHealth + 5 
    print(charHealth)
if race_choice == 4:
    charDexterity = charDexterity - 3
    print(charDexterity)
if race_choice == 4:
    charIntelligence = charIntelligence + 4
    print(charIntelligence)
    
if race_choice == 5:
    charStrength = charStrength - + 3
    print(charStrength)
if race_choice == 5:
    charCharisma = charCharisma - 2 
    print(charCharisma)

if race_choice == 6:
    charStrength = charStrength + 2
    print(charStrength)
if race_choice == 6:
    charDexterity = charDexterity + 2
    print(charDexterity)
if race_choice == 6:
    charCharisma = charCharisma - 3 
    print(charCharisma)
    
def get_profession():
    professions = {
        "Bounty Hunter": {"dexterity": 2},
        "Pirate": {"charisma": 3, "strength": 1, "health": 2},
        "Soldier": {"charisma": 3, "strength": 1, "health": 2},
        "Hacker": {"intelligence": 3}
    }

    while True:
        print("Choose a profession:")
        for i, prof in enumerate(professions.keys(), 1):
            print(f"{i}. {prof}")

        choice = input("Enter the number corresponding to your choice: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(professions):
                return list(professions.keys())[choice - 1]
            else:
                print("Invalid choice. Please choose again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    profession = get_profession()
    print(f"You work as a {profession}.")

    attributes = professions[profession]
    print("\nAttributes:")
    for attr, value in attributes.items():
        print(f"+{value} {attr}")
 

