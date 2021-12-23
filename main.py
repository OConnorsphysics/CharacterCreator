"""
Created on Mon Nov 15 14:28:18 2021

@author: Liam O'Connor

DnD character random generator
"""
import random

name = input('What is your character\'s name?')


Dra = ["Black Scale Dragonborn", "Blue Scale Dragonborn", "Brass Scale Dragonborn", "Bronze Scale Dragonborn", "Copper Scale Dragonborn", "Gold Scale Dragonborn", "Green Scale Dragonborn", "Red Scale Dragonborn", "Silver Scale Dragonborn", "White Scale Dragonborn"]
Drag = random.choice(Dra)
Dwf = ["Mountain Dwarf", "Hill Dwarf"]
Dwar = random.choice(Dwf)
El = ["Dark Elf", "Ground Elf", "High Elf", "Wood Elf"]
Elf = random.choice(El)
Ge = ["Air Genasi", "Earth Genasi", "Fire Genasi", "Water Genasi"]
Genasi = random.choice(Ge)
Gn = ["Desert Gnome", "Forest Gnome", "Rock Gnome", "Svirfneblin Gnome"]
Gnome = random.choice(Gn)
Hal = ["Lightfoot Halfling", "Stout Halfling"]
Half = random.choice(Hal)
Hum = ["Human", "Variant Human"]
Human = random.choice(Hum)
rac = ["Aarakocra", Drag, Dwar, Elf, Genasi, Gnome, "Goliath", "Half-Elf", Half, "Half-Orc", Human, "Tiefling"]

raceChoice = input('Do you want a random race? [Y/N]')
if raceChoice == 'N' or raceChoice == 'n':
    race = input(
        'Enter your character\'s race from the list. (Aarakocra, Drag, Dwar, Elf, Genasi, Gnome, Goliath, Half-Elf, Half, Half-Orc, Human, Tiefling) ')
else:
    race = random.choice(rac)
    print('Your character is a ', race, ".")


Arti = ["Alchemist Speciliast Artificer", "Armorist Speciliast Artificer", "Artilierist Speciliast Artificer", "Battle Smith Speciliast Artificer"]
Artificer = random.choice (Arti)
Barb = ["Path of the Ancestral Guardian Barbarian", "Path of the Battleranger Barbarian", "Path of the Berserker Barbarian", "Path of the Storm Herold Barbarian", "Path of the Totem Warrior Barbarian", "Path of the Zelot Barbarian"]
Barbarian = random.choice(Barb)
Bar = ["College of Glamor Bard", "College of Lore Bard", "College of Satire Bard", "College of Sword Bard", "College of Valor Bard", "College of Whispers Bards"]
Bard = random.choice(Bar)
Cle = ["Death Domain Cleric", 'Forge Domain Cleric', "Grave Domain Cleric", "Knowledge Domain Cleric", "Life Domain Cleric", "Light Domain Cleric", "Nature Domain Cleric", "Order Domain Cleric", "Tempest Domain Cleric", "Trickery Domain Cleric", "War Domain Cleric", "Zeal Domain Cleric"]
Cleric = random.choice(Cle)
Dru = ["Circle of Dreams Druid", "Circle of Land Druid", "Circle of the Moon Druid", "Circle of the Sheppard Druid"]
Druid = random.choice(Dru)
Fig = ["Arcane Archer Archetype Fighter", "Battle Master Archetype Fighter", "Cavalier Archetype Fighter", "Champion Archetype Fighter", "Eldrich Knight Archetype Fighter", "Samurai Archetype Fighter"]
Fighter = random.choice(Fig)
Mon = ["Way of the Drunken Warrior Monk", "Way of the Four Elements Monk", "Way of the Kensei Monk", "Way of the Open Hand Monk", "Way of the Shadow Monk", "Way of the Sun Soul Monk"]
Monk = random.choice(Mon)
Pal= ["Oath of the Ancients Paladin", "Oath of Conquest Paladin", "Oath of the Crown Paladin", "Oath of Devotion Paladin", "Oath of Redemption Paladin", "Oath of Vengeance Paladin"]
Paladin = random.choice(Pal)
Ran = ["Beast Master Archetype Ranger", "Gloom Stalker Archetype Ranger", "Horizon Walker Archetype Ranger", "Hunter Archetype Ranger", "Monster Slayer Archetype Ranger", "Shooting Star Archetype Ranger"]
Ranger = random.choice(Ran)
Rog = ["Arcane Trickster Archetype Rogue", "Assassin Archetype Rogue", "Inquisitive Archetype Rogue", "Mastermind Archetype Rogue", "Mountebank Archetype Rogue", "Scout Archetype Rogue", "Swashbuckler Archetype Rogue", "Thief Archetype Rogue"]
Rogue = random.choice(Rog)
Sor = ["Draconic Bloodline Origin Sorcerer", "Divine Soul Origin Sorcerer", "Phoenix Origin Sorcerer", "Sea Origin Sorcerer", "Shadow Origin Sorcerer", "Stone Origin Sorcerer", "Storm Origin Sorcerer", "Wild Magic Origin Sorcerer"]
Sorcerer = random.choice(Sor)
War = ["Ancient Dragon Patron Warlock", "Archfey Patron Warlock", "Celestial Patron Warlock", "Fiend Patron Warlock", "Mysterious Feline Patron Warlock", "Great Old One Patron Warlock", "Hexblade Patron Warlock", "Queen of Spiders Patron Warlock", "Raven Queen Patron Warlock", "Serpent Patron Warlock"]
Warlock = random.choice(War)
Wiz = ["Abjuration Arcane Tradition Wizard", "Conjuration Arcane Tradition Wizard", "Divination Arcane Tradition Wizard", "Evocation Arcane Tradition Wizard", "Illusion Arcane Tradition Wizard", "Necromancy Arcane Tradition Wizard", "Transmutation Arcane Tradition Wizard", "War Arcane Tradition Wizard"]
Wizard = random.choice(Wiz)
clas = [Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard]

classChoice = input('Do you want a random Class? [Y/N]')
if classChoice == 'N' or classChoice == 'n':
    Class = input(
        'Enter your character\'s class from the following list. (Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard) ')
else:
    Class = random.choice(clas)
    print('Your character is a ', Class)


def character_description():
    hair = input('What does your players hair look like?')
    clothing = input('What does your character wear?')
    build = input('What is your character\'s build? (Strong, thin, fat)')

    print(name, 'is a', race, Class, '.')
    print('They have ', hair, ' hair, and are wearing ' , clothing, ' on their ', build, ' build.')
    description = str(name) + ' is a ' + str(race) + ' ' + str(Class) + '. ' + 'They have ' + str(hair) + ' hair, and are wearing ' + str(clothing) + ' on their ' + str(build) + ' build.\n'
    return description

def roll4d6minussmallest():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1, 6)
    roll3 = random.randint(1, 6)
    roll4 = random.randint(1, 6)
    print('The rolls are ', roll1, roll2, roll3, roll4)
    rolls = [roll1, roll2, roll3, roll4]
    rolls.sort()
    total = rolls[1] + rolls[2] + rolls[3]
    return total


def writefile():
    with open(str(name) + '.txt', 'w') as f:
        f.write(str(character_description()))
        abscores = ['Your Strength score is', str(strength),
                    'Your Dexterity score is', str(dex),
                    'Your Constitution score is', str(con),
                    'Your Intelligence score is', str(intel),
                    'Your Wisdom score is', str(wis),
                    'Your Charisma score is', str(charis)]
        f.write('\n'.join(abscores))
        f.write('\n')
        #TODO add initative, HP, Hit dice
        f.write(backstory)
        f.write(weapon_description)
    f.close()

abscoreroll = input('Do you want to roll your own ability scores? (Y/N)')
if abscoreroll == 'Y' or abscoreroll == 'y':
    print("Roll 4d6 and remove the lowest, write this number down on scrap paper. Repeat this 6 times.")
    print('Withouth adding any class or race modifiers please assign your ability scores.')
    strength = input('What is your strength score?')
    dex = input('What is your dexterity score?')
    con = input('What  is your constitution score?')
    intel = input('What is you intelligence score?')
    wis = input('What  is your wisdom score?')
    charis = input('What is you charisma score?')
else:
    print('Your characters ability scores are generated by rolling 4d6 and taking the 3 highest, given below.')
    strength = roll4d6minussmallest()
    print('Your base Strength score is', strength)
    dex = roll4d6minussmallest()
    print('Your base Dexterity score is', dex)
    con = roll4d6minussmallest()
    print('Your base Strength score is', con)
    intel = roll4d6minussmallest()
    print('Your base Strength score is', intel)
    wis = roll4d6minussmallest()
    print('Your base Strength score is', wis)
    charis = roll4d6minussmallest()
    print('Your base Strength score is', charis)

#checks for racial ability score modifiers and adds them
if race == "Mountain Dwarf" or race == "mountain dwarf" or race == "Mountain dwarf":
    con +=2
    strength +=2
if race in Dra:
    strength +=2
    charis +=2
if race == "Half-Orc" or race == "half-orc" or race == "Half-orc" or race == "Half Orc" or race == "half orc":
    con +=1
    strength +=2
if race == "Human" or race == "human":
    strength +=1
    dex +=1
    con +=1
    intel +=1
    wis +=1
    charis +=1
if race in El:
    dex +=2
if race == "Dark Elf" or race == "drow" or race == "Drow" or race == "dark elf":
    charis+=1
if race ==  "High Elf" or race == "high elf":
    intel +=1
if race == "Wood Elf" or race == 'wood elf':
    wis+=1
#TODO add all racial score modifier
#TODO add class score modifiers
#TODO add weapon stats with attack options

#allows user to  create backstory and other character flavor aspects
backstory = input('What is your character\'s backstory? Do they have a family? Why did they leave their home for adventure?')
weapon_description = input('What does your character\'s weapons and armour look like.')

writefile()        #writes the character to a new text file with the file name as the character name




