# this is a labyrinth text based adventure game. 

from random import randint
import time

player_lvl = 1
player_xp = 10 # current experience points
player_xp_cap = 10 # experience points - to next level
player_str = 3
player_dex = 4
player_int = 2
player_hp = 11 # hit point capacity
player_hp_dmg = 11 # current hit points
player_name = "Unknown"
player_class = "Unknown"
satchel_contents = [] # to be populated with loot
gold = 0
fight_count = 0
fight_count_most = 51
battle_cave_furthest = 18
battle_cave_there_and_back = 36
high_scorer_fcm = "WFTIV"
high_scorer_bcf = "WFTIV"
high_scorer_bctb = "WFTIV"
attack_mod = 0 # modification based on equipped item
defense_mod = 0 # modification based on equipped item
current_weapon = "blank"

prompt = "-> "

came_from = "Unknown"
first_time_first_room = True # implemented
first_time_secret_room = True # implemented
first_time_chamber_one = True # implemented
first_time_third_room = True
first_time_2nd_secret_room = True 
defeat_goblin_king = False # implemented
defeat_darkness_troll = False # implemented
rope_ready = False # 5th intersection, once rope swing is ready
high_scorer = False
high_scorer_furthest = False
high_scorer_cave = False 
boys_saved = 0 # number will increase until 12, which will be the final boy found
boys_rescued = [] # list will populate with boys as they are found
found_treasure1 = False # South of intersection 8

walking_stick = False
cloth_cap = False
short_stick = False
basic_gloves = False
thick_shirt = False
three_ft_pipe = False
sturdy_hat = False
madrona_wand = False
fingerless_gloves = False
leather_t = False
sword = False
wide_brim_hat = False
oak_staff = False
power_mitts = False
leather_jacket = False
small_medallion = False
big_medallion = False
intricate_medallion = False
wizard_robes = False
imbued_eye_mask = False
armored_tweed_vest = False
wizard_hat = False
stealth_slippers = False
knickers = False
wizard_staff = False
katana = False
scepter = False
weapon = False
book_of_knots = False

yes_list = ["yep", "yeppers", "yeah", "uh huh", "well, sure", "absolutely",
            "amen", "affirmative", "true", "yea", "decent", "beyond a doubt",
            "certainly", "good enough", "naturally", "of course", "undoubtedly",
            "unquestionably", "definitely", "you bet", "you betcha",
            "hell yea i am", "heck ya", "heck yah", "hell ya", "hell yeah",
            "hell yah", "without a doubt", "i am", "i am!", "yes", "y", "sure",
            "okay", "yes!", "yes!!", "yesss", "yesssss", "yesssssssss"]

no_list = ["nope", "no way", "negative", "absolutely not", "not at all",
           "not by any means", "never", "by no means", "nix", "not", "no", "n"] 

maybe_list = ["perchance", "perhaps", "mayhaps", "can be", "feasible",
              "imaginably", "i might be", "may be", "m", "i could be", "possibly",
              "god willing", "god willing", "could be", "maybe", "mby", "mabe"]

north_list = ["north", "go north", "head north", "nrth", "nroth", "nrt", "n",
              "no", "how about north", "how bout north", "north, i guess"]

south_list = ["south", "go south", "head south", "soth", "suoth", "sth", "s",
              "so", "how about south", "how bout south", "south, i guess"]

west_list = ["west", "go west", "head west", "wst", "w", "we", "how about west",
             "how bout west", "west, i guess"]
        
east_list = ["east", "go east", "head east", "est", "e", "ea", "how about east",
             "how bout east", "east, i guess"]

fight_list = ["fight", "fiht", "f", "fght", "fite", "figth", "fihtg", "fight!",
              "figh"]

flee_list = ["flee", "fle", "fleee", "fleeee", "fleeeee!", "flee!", "fleee!",
             "run away!", "run away", "get out of there", "hit the road",
             "run like hell"]

undecided_list = ["not sure", "which way should i go?", "dunno",
                  "i don't know"]

door_list = ['enter door', 'open door', 'open', 'door', 'enter room', 'room',
             'go into the room']
        
loot_dict = {'Sturdy Walking Stick': 'provides +1 attack bonus',
             'Cloth Cap': 'provides +1 intelligence', 'Short Stick': 'provides +1 attack bonus',
             'Basic Gloves': 'provides +1 dexterity for all classes',
             'Spade': 'a small, handheld digging instrument',
             'Paper and Pen': 'Good for explaining stuff!',
             'Thick Shirt': 'provides +1 defense bonus',
             'Roll of String': 'a roll of fairly sturdy string',
             'Small Medallion': 'a unique pattern is displayed on the face, and it is warm!',
             'Three Foot Pipe': 'provides +2 attack bonus',
             'Sturdy Hat': 'provides +2 intelligence to the wearer',
             'Madrona Wand': 'provies +2 attack bonus',
             'Fingerless Gloves': 'provides +2 dexterity for all classes',
             'Shovel': 'a tool you could dig a hole with',
             'Jagged Rocks': 'a few rocks, sharp as hell',
             'Leather T-Shirt': 'provides +2 defense for all classes',
             'Short Rope': 'about 15 feet of good rope',
             'Big Medallion': 'a unique pattern is displayed on the face and it is warm!',
             'Sword': 'provides +3 attack bonus', 'Wide Brim Hat': 'provides +3 intelligence',
             'Oak Staff': 'provides +3 attack bonus',
             'Power Mitts': 'provies +3 dexterity for all classes',
             'Balanced Pickaxe': 'a well weighted tool for digging or breaking stone',
             'Book of Knots': 'Learn all sorts of knots!',
             'Leather Jacket': 'provides +3 defense for all classes',
             'Long Rope': 'a 30 foot coil of good rope',
             'Intricate Medallion': 'a craft of wonder and brilliance, quite warm!',
             'Nothing Equipped': 'no bonus cause no loot'}

loot_lvl_1_3 = ['Sturdy Walking Stick', 'Cloth Cap', 'Short Stick', 'Basic Gloves',
                'Spade', 'Paper and Pen', 'Thick Shirt', 'Roll of String', 'Small Medallion']

loot_lvl_4_6 = ['Three Foot Pipe', 'Sturdy Hat', 'Madrona Wand', 'Fingerless Gloves',
                'Shovel', 'Jagged Rocks', 'Leather T-Shirt', 'Short Rope', 'Big Medallion']

loot_lvl_7_9 = ['Sword', 'Wide Brim Hat', 'Oak Staff', 'Power Mitts', 'Balanced Pickaxe',
                'Book of Knots', 'Leather Jacket', 'Long Rope', 'Intricate Medallion'] 

equippable_loot = ['Sturdy Walking Stick', 'Cloth Cap', 'Short Stick', 'Basic Gloves',
                   'Thick Shirt', 'Small Medallion', 'Three Foot Pipe', 'Sturdy Hat',
                   'Madrona Wand', 'Fingerless Gloves', 'Leather T-Shirt', 'Big Medallion',
                   'Sword', 'Wide Brim Hat', 'Oak Staff', 'Power Mitts', 'Leather Jacket',
                   'Intricate Medallion']

non_equippable_loot = ['Paper and Pen', 'Spade', 'Roll of String', 'Shovel', 'Jagged Rocks',
                       'Short Rope', 'Balanced Pickaxe', 'Book of Knots', 'Long Rope']

equipped_loot = {'Head': 'Nothing Equipped', 'Hands': 'Nothing Equipped',
                 'Body': 'Nothing Equipped', 'Neck': 'Nothing Equipped',
                 'Weapon': 'Nothing Equipped'}

enemies_lvl_1_2 = ['Slime', 'Gnoll', 'Wolf', 'Bat', 'Goblin', 'Cat', 'Flannel Bag',
                   'Glowing Top Hat', 'Pair of Round Spectacles']

enemies_lvl_3_4 = ['Large Slime', 'Pack of Gnolls', 'Alpha Wolf', 'Ancient Bat',
                   'Desperate Goblin', 'Mountain Cat', 'Self Closing Flannel Bag',
                   'Glowing Top Hat w/ Cane', 'Jagged Contacts']

enemies_lvl_5_6 = ['Shiny Mist', 'Floor of Marbles', 'Ancient Wolf', 'Wall of Bats',
                   'Competitive Eater', 'Donald Trump', 'Mary Poppin\'s Bag of Horrors',
                   'Badass Three Piece Suit w/ Hat & Cane', 'Eye Candy']

enemies_lvl_7_8 = ['Wall of Goo', 'Marble Maniac', 'Wolf Pack', 'Giant Bat',
                   'Jaws of Doom', 'Enraged Lion', 'Automated Sack of Death',
                   'Thrift Store Monster', 'Ball of Vipers']

fathers_wisdom = ['If it is the easy way, it is the wrong way.', 'Make soup, not war.',
                  'The fastest way to the end of any journey is forward.',
                  'Life is fair. Not fair, I mean!',
                  'When the going gets tough, stop and think about things.',
                  'Give it a little shake and see what falls out.',
                  'Talking is to first be done silently.',
                  'When talking is silent, silence is golden.',
                  'Do not forget to drink water.', 'Enunciated vowels produce healthy bowels!',
                  'Club once in awhile, do not be a constant clubber.']

mothers_wisdom = ['Take garlic, son. And raw honey.', 'If you take ill, take raw honey.',
                  'Never shake hands with a troll', 'Raw garlic. Feel the burn.',
                  'Soak your bunions.', 'Never trust a woman with one eye.',
                  'Always trust a bearded wizard.', 'Can I look at your blackheads?',
                  'Go wash your face.', 'Eucalyptus oil.', 'Always use protection.',
                  'Milk baths are healing.']


def determine_intent(question): # this is the user input gateway

    global player_hp, player_hp_dmg, player_lvl

    prompt2 = question + "\n-> "
    
    answer = input(prompt2)
    
    # cheating for playtest
    if answer == "cheat": 

        answer2 = input("Do you want to cheat?\n")

        while answer2 == "y":
    
            answer3 = input("Which item would you like to add to your inventory?\n")
            satchel_contents.append(answer3)
            answer2 = input("Add another item?\n")
        
            player_hp = 999
            player_hp_dmg = player_hp
        
            answer = input(prompt2)
    
    if answer in loot_lvl_1_3 or answer in loot_lvl_4_6 or answer in loot_lvl_7_9:

        return answer
    
    answer = answer.lower()
    print("\n\n")
    
    while len(answer) == 0 or answer in maybe_list or answer in undecided_list:

        if len(answer) == 0:

            print("Nothin aint no answer I ever heard of.\n")
            answer = input(prompt2)
            answer = answer.lower()
            print("\n\n")
        
        elif answer in maybe_list: 

            print("Perhaps you better decide definitely.\n")
            answer = input(prompt2)
            answer = answer.lower()
            print("\n\n")
        
        else: 

            print("Be decisive.\n")
            answer = input(prompt2)
            answer = answer.lower()
            print("\n\n")
        
    while answer == "stats" or answer == "options" or answer == "inventory" or answer == "scoreboard" or answer == "equip" or answer == "advice":
        
        if answer == "stats":

            print("Here are your current stats:\n")
            print(f"Name: {player_name!s}  |  Class: {player_class!s}")
            print(f"Level: {player_lvl}")
            print(f"Strength: {player_str}")
            print(f"Dexterity: {player_dex}")
            print(f"Intelligence: {player_int}")
            print(f"Max Hit Points: {player_hp}")
            print(f"Current Hit Points: {player_hp_dmg}\n\n")
            
            answer = input(prompt2)
            answer = answer.lower()
            print("\n\n")
        
        elif answer == "options":

            print("Each of these commands will do something if typed in when prompted for an answer.\n")
            print("\toptions       <--- That is this list!")
            print("\tstats         <--- Player Stats!")
            print("\tinventory     <--- Contents of your satchel!")
            print("\tscoreboard    <--- Best scores!")
            print("\tequip         <--- Equip an item!")
            print("\tadvice        <--- Remember advice from one of your parents!\n\n")
            
            answer = input(prompt2)
            answer = answer.lower()
            print("\n\n")
            
        elif answer == "inventory":
        
            if satchel_contents == []:

                print("Your satchel is empty!\n\n")

            else:

                print("Here are the current contents of your Satchel: \n")
                
                satchel_contents.sort()

                for item in satchel_contents: 

                    print("\t--" + item + "--")
                    print("\n\n")

                print("These are the equippable items in your possession: \n")

                for item in satchel_contents:

                    if item in equippable_loot:

                        print("\t<-> " + item)
                        print("\n\n")
                        
                print("Here is what you have equipped: \n")

                for key, value in equipped_loot.items():

                    print("\t" + key + " : " + value + "   ...   " + loot_dict[value])
                    print("\n\n")
                    
            answer = input(prompt2)
            answer = answer.lower()
            print("\n\n")
        
        elif answer == "scoreboard": 
        
            print(f"\t\tMost fights won before death: {fight_count_most} by {high_scorer_fcm}.")
            print(f"\t\tMost fights won walking into the Battle Cave at one go: {battle_cave_furthest} by {high_scorer_bcf}.")
            print(f"\t\tMost fights won in the Battle Cave and survive: {battle_cave_there_and_back} by {high_scorer_bctb}.")
            
            answer = input(prompt2)
            answer = answer.lower()
            print("\n\n")
            
        elif answer == "equip":
        
            equip()
            
            answer = input(prompt2)
            answer = answer.lower()
            print("\n\n")
        
        elif answer == "advice":
            
            chance = randint(1, 100)

            if chance <= 50: 

                print_wisdom("Dad")
                print("He was a good man.\n\n\n")

            else: 

                print_wisdom("Mom")
                print("She was an excellent woman.\n\n\n")
            
            answer = input(prompt2)
            answer = answer.lower()
            print("\n\n")

    if answer in yes_list:          

        answer = "y"

    elif answer in no_list:     

        answer = "n"
    
    elif answer in door_list:

        answer = "door"

    elif answer in north_list:          

        answer = "n"

    elif answer in south_list:      

        answer = "s"
        
    elif answer in west_list:       

        answer = "w"
        
    elif answer in east_list:       

        answer = "e"
        
    elif answer in fight_list:

        answer = "fight"
    
    elif answer in flee_list:

        answer = "flee"

    elif answer == "quit":

        dead("You have quit.") 
    
    elif answer in (1, 2, 3, 4, 5, 6, 7, 8): 
    
        return answer

    return answer
        

def print_wisdom(parent):
    
    if parent == "Dad":

        chance = randint(0, 10)
        print("\nYou remember your Father once said,\n")
        print('"' + fathers_wisdom[chance] + '"')
        print("\n\n")
        
    else: 

        chance = randint(0, 11)
        print("\nA memory comes to you quite clearly, of your Mother saying,\n")
        print('"' + mothers_wisdom[chance] + '"')
        print("\n\n")
        
        
def equip():
    
    global player_str, player_dex, player_int, player_hp, attack_mod, defense_mod, walking_stick
    global cloth_cap, short_stick, basic_gloves, thick_shirt, three_ft_pipe, sturdy_hat, madrona_wand
    global fingerless_gloves, leather_t, sword, wide_brim_hat, oak_staff, power_mitts, leather_jacket
    global small_medallion, big_medallion, intricate_medallion, weapon, current_weapon
    
    equip_again = True

    answer = determine_intent("What would you like to equip?\n")
    
    while answer in satchel_contents and equip_again:
        
        print("\n\n")
        
        if answer in non_equippable_loot:
            
            print("That item cannot be equipped!\n\n")
        
        elif answer == "Cloth Cap" and not cloth_cap:
            
            if sturdy_hat or wide_brim_hat:

                print("Why would you do that? You'd lose intelligence!\n")
                time.sleep(2)
                print("I mean, if you're willing to make this decision with")
                print("this level of intelligence, what kind of decisions are")
                print("you going to make with less intelligence?\n")
                time.sleep(4)
                print("We'll hold off for now.\n")
                
            else: 

                print("You equip the Cloth Cap! Your intelligence is increased by 1!\n")
                player_int += 1
                cloth_cap = True
                equipped_loot['Head'] = "Cloth Cap"
            
        elif answer == "Cloth Cap" and cloth_cap:
            
            print("You are already wearing the Cloth Cap!\n")
            
        elif answer == "Short Stick" and not short_stick:
            
            if weapon:

                print(f"The Short Stick is replacing your {current_weapon!s}!\n")
                print("Your bonus attack is 1!\n")

                attack_mod = 1
                short_stick = True
                equipped_loot['Weapon'] = "Short Stick"

                if current_weapon == "Madrona Wand":

                    madrona_wand = False
                    
                elif current_weapon == "Oak Staff":

                    oak_staff = False
                    
                elif current_weapon == "Sturdy Walking Stick":

                    walking_stick = False
                    
                elif current_weapon == "Three Foot Pipe":

                    three_ft_pipe = False
                    
                else:

                    sword = False

                current_weapon = "Short Stick"
            
            else:

                print("Alright, you equip the Short Stick! Your bonus attack is 1!\n")
                attack_mod = 1
                short_stick = True
                weapon = True
                current_weapon = "Short Stick"
                equipped_loot['Weapon'] = "Short Stick"
            
        elif answer == "Short Stick" and short_stick:
            
            print("You already have the Short Stick equipped!\n")
            
        elif answer == "Basic Gloves" and not basic_gloves:
            
            if fingerless_gloves or power_mitts:

                print("Why would you do that? You'd lose dexterity!\n")
                time.sleep(2)
                print("It can't be for the looks...")
                time.sleep(1)
                print("We'll hold off for now.")
                
            else: 

                print("Yes, you equip the Basic Gloves! Your dexterity is increased by 1!\n")
                player_dex += 1
                basic_gloves = True
                equipped_loot['Hands'] = "Basic Gloves"
            
        elif answer == "Basic Gloves" and basic_gloves:
            
            print("You are already wearing the Basic Gloves!\n")
            
        elif answer == "Thick Shirt" and not thick_shirt:
                
            if leather_t or leather_jacket:

                print("Why would you do that? You'd become less defensive!\n")
                print("Plus, the Thick Shirt just doesn't look cool.")
                time.sleep(2)
                print("We'll just hold off for now.")
                
            else: 

                print("Alright, you equip the Thick Shirt! Your defense bonus is 1!\n")
                defense_mod = 1
                thick_shirt = True
                equipped_loot['Body'] = "Thick Shirt"
            
        elif answer == "Thick Shirt" and thick_shirt:
            
            print("You are already wearing the Thick Shirt!\n")
            
        elif answer == "Sturdy Hat" and not sturdy_hat:
            
            if cloth_cap == True:

                print("You have removed the Cloth Cap and equipped the Sturdy Hat!\n")
                print("Your intelligence is increased by 1!\n")
                player_int += 1
                sturdy_hat = True
                cloth_cap = False
                equipped_loot['Head'] = "Sturdy Hat"
                
            elif wide_brim_hat:

                print(f"Up to you, {player_name!s}...")
                print("Your intelligence is decreased by 1.\n")
                player_int -= 1
                wide_brim_hat = False
                sturdy_hat = True
                equipped_loot['Head'] = "Sturdy Hat"
            
            else:

                print("Cool, you equip the Sturdy Hat! Your intelligence is increased by 2!\n")
                player_int += 2
                sturdy_hat = True
                equipped_loot['Head'] = "Sturdy Hat"
                
        elif answer == "Sturdy Hat" and sturdy_hat:
            
            print("You're already wearing the Sturdy Hat!\n")
        
        elif answer == "Madrona Wand" and not madrona_wand:
            
            if weapon:

                print(f"Okay, {player_name!s}, the Madrona Wand is replacing your {current_weapon!s}!\n")
                print("Your bonus attack is 2!\n")
                attack_mod = 2
                madrona_wand = True
                equipped_loot['Weapon'] = "Madrona Wand"

                if current_weapon == "Short Stick":

                    short_stick = False
                
                elif current_weapon == "Oak Staff":

                    oak_staff = False
                    
                elif current_weapon == "Sturdy Walking Stick":

                    walking_stick = False
                    
                elif current_weapon == "Three Foot Pipe":

                    three_ft_pipe = False
                    
                else:

                    sword = False
                
                current_weapon = "Madrona Wand"
                
            else: 

                print("Nice! You equip the Madrona Wand. Your bonus attack is 2!\n")
                attack_mod = 2
                madrona_wand = True
                weapon = True
                current_weapon = "Madrona Wand"
                equipped_loot['Weapon'] = "Madrona Wand"
                
        elif answer == "Madrona Wand" and madrona_wand:
            
            print("You've already got the Madrona Wand equipped!\n")
            
        elif answer == "Fingerless Gloves" and not fingerless_gloves:
            
            if basic_gloves == True:

                print("You have removed the Basic Gloves and equipped the Fingerless Gloves!\n")
                print("You're dexterity is increased by 1!\n")
                player_dex += 1
                fingerless_gloves = True
                basic_gloves = False
                equipped_loot['Hands'] = "Fingerless Gloves"
                
            elif power_mitts:

                print(f"Up to you, {player_name!s}...")
                print("Your dexterity is decreased by 1.\n")
                player_dex -= 1
                power_mitts = False
                fingerless_gloves = True
                equipped_loot['Hands'] = "Fingerless Gloves"
            
            else:

                print("You equip the Fingerless Gloves! Your dexterity is increased by 2!\n")
                time.sleep(1)
                print("And you look cool.")
                player_dex += 2
                fingerless_gloves = True
                equipped_loot['Hands'] = "Fingerless Gloves"
                
        elif answer == "Fingerless Gloves" and fingerless_gloves:
            
            print("You're already wearing the Fingerless Gloves!\n")
            
        elif answer == "Leather T-Shirt" and not leather_t:
            
            if thick_shirt == True:

                print("You have removed the Thick Shirt and equipped the Leather T-Shirt!\n")
                print("You're defense bonus is 2!\n")
                defense_mod = 2
                leather_t = True
                thick_shirt = False
                equipped_loot['Body'] = "Leather T-Shirt"
                
            elif leather_jacket:

                print(f"Up to you, {player_name!s}...")
                print("Your defense bonus goes down by 1, and is now 2!\n")
                defense_mod = 2
                leather_jacket = False
                leather_t = True
                equipped_loot['Body'] = "Leather T-Shirt"
            
            else:

                print("You equip the Leather T-Shirt! Your defense bonus is 2!\n")
                defense_mod = 2
                leather_t = True
                equipped_loot['Body'] = "Leather T-Shirt"
                
        elif answer == "Leather T-Shirt" and leather_t:
            
            print("You're already wearing the Leather T-Shirt, and I must say it looks dashing!\n")
            
        elif answer == "Wide Brim Hat" and not wide_brim_hat:
            
            if cloth_cap:

                print("You have removed the Cloth Cap and equipped the Wide Brim Hat!\n")
                print("Your intelligence is increased by 2!\n")
                player_int += 2
                wide_brim_hat = True
                cloth_cap = False
                equipped_loot['Head'] = "Wide Brim Hat"
            
            elif sturdy_hat:

                print("You have removed the Sturdy Hat and equipped the Wide Brim Hat!\n")
                print("Your intelligence is increased by 1!\n")
                player_int += 1
                wide_brim_hat = True
                sturdy_hat = False
                equipped_loot['Head'] = "Wide Brim Hat"
                
            else: 

                print("Wow, nice! You equip the Wide Brim Hat. Your intelligence is increased by 3!\n")
                player_int += 3
                wide_brim_hat = True
                equipped_loot['Head'] = "Wide Brim Hat"
                
        elif answer == "Wide Brim Hat" and wide_brim_hat:
            
            print("You're already wearing the Wide Brim Hat - and you look really good!\n")
        
        elif answer == "Oak Staff" and not oak_staff:
            
            if weapon:

                print(f"The Oak Staff is replacing your {current_weapon!s}!\n")
                print("Your bonus attack is 3!\n")
                attack_mod = 3
                oak_staff = True
                equipped_loot['Weapon'] = "Oak Staff"

                if current_weapon == "Short Stick":

                    short_stick = False
                
                elif current_weapon == "Madrona Wand":

                    madrona_wand = False
                    
                elif current_weapon == "Sturdy Walking Stick":

                    walking_stick = False
                    
                elif current_weapon == "Three Foot Pipe":

                    three_ft_pipe = False
                    
                else:

                    sword = False
                
                current_weapon = "Oak Staff"
                
            else: 

                print("You equip the Oak Staff! Your bonus attack is 3!\n")
                attack_mod = 3
                oak_staff = True
                weapon = True
                current_weapon = "Oak Staff"
                equipped_loot['Weapon'] = "Oak Staff"
                
        elif answer == "Oak Staff" and oak_staff:
            
            print("You've already got the Oak Staff equipped!\n")
            
        elif answer == "Power Mitts" and not power_mitts:
            
            if basic_gloves:

                print("You have removed the Basic Gloves and equipped the Power Mitts!\n")
                print("You're dexterity is increased by 2!\n")
                player_dex += 2
                power_mitts = True
                basic_gloves = False
                equipped_loot['Hands'] = "Power Mitts"
                
            elif fingerless_gloves:

                print("You have removed the Fingerless Gloves and equipped the Power Mitts!\n")
                print("You're dexterity is increased by 1!\n")
                player_dex += 1
                power_mitts = True
                fingerless_gloves = False
                equipped_loot['Hands'] = "Power Mitts"
            
            else:

                print("YES!! You equip the Power Mitts! Your dexterity is increased by 3!\n")
                player_dex += 3
                power_mitts = True
                equipped_loot['Hands'] = "Power Mitts"
                
        elif answer == "Power Mitts" and power_mitts:
            
            print("Look at your hands, you're already wearing the Power Mitts!\n")
            
        elif answer == "Leather Jacket" and not leather_jacket:
            
            if thick_shirt:

                print("You have removed the Thick Shirt and equipped the Leather Jacket!\n")
                print("You're defense bonus is now 3!\n")
                defense_mod = 3
                leather_jacket = True
                thick_shirt = False
                equipped_loot['Body'] = "Leather Jacket"
                
            elif leather_t:

                print("You have removed the Leather T-Shirt and equipped the Leather Jacket!\n")
                print("You're defense bonus is now 3!\n")
                defense_mod = 3
                leather_jacket = True
                leather_t = False
                equipped_loot['Body'] = "Leather Jacket"
            
            else:

                print("Okay, you equip the Leather Jacket! Your defense is increased by 3!\n")
                defense_mod = 3
                leather_jacket = True
                equipped_loot['Body'] = "Leather Jacket"
                
        elif answer == "Leather Jacket" and leather_jacket:
            
            print("You're already wearing the Leather Jacket!\n")
        
        elif answer == "Sturdy Walking Stick" and not walking_stick:
            
            if weapon:

                print(f"Well, {player_name!s}, the Sturdy Walking Stick is replacing your {current_weapon!s}!\n")
                print("Your bonus attack is 1!\n")
                time.sleep(1)
                print("At least now you can walk around with more confidence in your footing.")
                attack_mod = 1
                walking_stick = True
                equipped_loot['Weapon'] = "Sturdy Walking Stick"

                if current_weapon == "Short Stick":

                    short_stick = False
                
                elif current_weapon == "Oak Staff":

                    oak_staff = False
                    
                elif current_weapon == "Madrona Wand":

                    madrona_wand = False
                    
                elif current_weapon == "Three Foot Pipe":

                    three_ft_pipe = False
                    
                else:

                    sword = False
                
                current_weapon = "Sturdy Walking Stick"
                
            else: 

                print("You equip the Sturdy Walking Stick! Your bonus attack is 1!\n")
                attack_mod = 1
                walking_stick = True
                weapon = True
                current_weapon = "Sturdy Walking Stick"
                equipped_loot['Weapon'] = "Sturdy Walking Stick"
            
        elif answer == "Sturdy Walking Stick" and walking_stick:
            
            print("You have the Sturdy Walking Stick equipped!\n")

        elif answer == "Three Foot Pipe" and not three_ft_pipe:
            
            if weapon:

                print(f"Nice, {player_name!s}, the Three Foot Pipe is replacing your {current_weapon!s}!\n")
                print("Your bonus attack is 2!\n")
                attack_mod = 2
                three_ft_pipe = True
                equipped_loot['Weapon'] = "Three Foot Pipe"

                if current_weapon == "Short Stick":

                    short_stick = False
                
                elif current_weapon == "Oak Staff":

                    oak_staff = False
                    
                elif current_weapon == "Sturdy Walking Stick":

                    walking_stick = False
                    
                elif current_weapon == "Madrona Wand":

                    madrona_wand = False
                    
                else:

                    sword = False
                
                current_weapon = "Three Foot Pipe"
                
            else: 

                print("You equip the Three Foot Pipe! Your bonus attack is 2!\n")
                attack_mod = 2
                three_ft_pipe = True
                weapon = True
                current_weapon = "Three Foot Pipe"
                equipped_loot['Weapon'] = "Three Foot Pipe"
                
        elif answer == "Three Foot Pipe" and three_ft_pipe:
            
            print("You are already holding the Three Foot Pipe!\n")
        
        elif answer == "Sword" and sword == False:
            
            if weapon:

                print(f"Very cool, {player_name!s}, the Sword is replacing your {current_weapon!s}!\n")
                print("Your bonus attack is 3!\n")
                attack_mod = 3
                madrona_want = True
                equipped_loot['Weapon'] = "Sword"

                if current_weapon == "Short Stick":

                    short_stick = False
                
                elif current_weapon == "Oak Staff":

                    oak_staff = False
                    
                elif current_weapon == "Sturdy Walking Stick":

                    walking_stick = False
                    
                elif current_weapon == "Three Foot Pipe":

                    three_ft_pipe = False
                    
                else:

                    madrona_wand = False
                
                current_weapon = "Sword"
                
            else: 

                print("Wow, you equip the Sword! Your bonus attack is 3!\n")
                attack_mod = 3
                sword = True
                weapon = True
                current_weapon = "Sword"
                equipped_loot['Weapon'] = "Sword"
                
        elif answer == "Sword" and sword:
            
            print(f"Look down at your hip, {player_name!s}, you've got the Sword equipped!\n")
            
        elif answer == "Small Medallion" and not small_medallion:
                
            print("You put the Small Medallion around your neck.\n")
            small_medallion = True
            big_medallion = False
            intricate_medallion = False
            equipped_loot['Neck'] = "Small Medallion"
            
        elif answer == "Small Medallion" and small_medallion:
            
            print("You're already wearing the Small Medallion!\n")
            
        elif answer == "Big Medallion" and not big_medallion:
                
            print("You put the Big Medallion around your neck.\n")
            big_medallion = True
            small_medallion = False
            intricate_medallion = False
            equipped_loot['Neck'] = "Big Medallion"
            
        elif answer == "Big Medallion" and big_medallion:
            
            print("You're already wearing the Big Medallion, and you look sexy!\n")
            
        elif answer == "Intricate Medallion" and not intricate_medallion:
            
            print("You put the Intricate Medallion around your neck.\n")
            intricate_medallion = True
            big_medallion = False
            small_medallion = False
            equipped_loot['Neck'] = "Intricate Medallion"
            
        elif answer == "Intricate Medallion" and intricate_medallion:
            
            print("You're already wearing the intricate medallion!\n")
        
        else: 

            print("YOU DO NOT HAVE THAT ITEM!\n")
        
        another_equip = determine_intent("Would you like to equip something else?\n")
        
        if another_equip == "y":
            
            answer = determine_intent("What would you like to equip?")
        
        else:

            equip_again = False
            print("\n\nOkay, good luck on your journey!")       
    
    if not equip_again:
        
        print("\n")
    
    else: 

        print("You do not have that item!\n")


def print_enemies_full():
    
    print("\nEnemies for Adventurers, Level 1 - 2: ")

    for i in range(len(enemies_lvl_1_2)):

        print(enemies_lvl_1_2[i])

        print('\n')
    
    print("Enemies for Adventurers, Level 3 - 4: ")

    for i in range(len(enemies_lvl_3_4)):

        print(enemies_lvl_3_4[i])

        print('\n')

    print("Enemies for Adventurers, Level 5 - 6: ")

    for i in range(len(enemies_lvl_5_6)):

        print(enemies_lvl_5_6[i])

        print('\n')
    
    print("Enemies for Adventurers, Level 7 - 8: ")

    for i in range(len(enemies_lvl_7_8)):

        print(enemies_lvl_7_8[i])

        
def print_items_full():
    
    print("\nItems for Adventurers, Level 1 - 3: ")

    for i in range(len(loot_lvl_1_3)):

        print(loot_lvl_1_3[i])

        print('\n')
    
    print("Items for Adventurers, Level 4 - 6: ")

    for i in range(len(loot_lvl_4_6)):

        print(loot_lvl_4_6[i])

        print('\n')
    
    print("Items for Adventurers, Level 7 - 9: ")

    for i in range(len(loot_lvl_7_9)):

        print(loot_lvl_7_9[i])


def battle(enemy, enemy_name):
    
    #player list order: Hp, Str, Dex, Int, xp
    #enemy list order: Hp, MaxAttack, xp given, dex   ------- want to add a defense modifier
        
    global player_xp, player_hp_dmg, fight_count, fight_count_most
    global high_scorer, high_scorer_fcm
    
    result = "No Hit."
    enemy_hp = enemy[0]
    enemy_attack = 0
    player_attack = 0
    round_count = 0
        
    if enemy[3] > player_dex:
        
        while player_hp_dmg > 0 and enemy_hp > 0:
            
            round_count += 1
            
            print(f"\t###      ROUND {round_count}      ###\n\n\n")
            
            print(f"\nThe {enemy_name!s} attacks!\n")
            time.sleep(2)
            
            enemy_attack = randint(1, enemy[1])
            precision = randint(1, 100)
        
            if precision >= 90:
        
                if precision == 100:

                    result = "Unreal Critical Precision!\n\n" 
                    enemy_attack += 4
                
                else: 

                    result = "Critical Precision!\n\n" 
                    enemy_attack += 3
            
            elif 75 < precision < 90:

                result = "Precision hit!\n\n" 
                enemy_attack += 2
            
            elif 50 < precision < 76:
                
                result = "Good hit!\n\n"
                enemy_attack += 1
            
            elif 30 < precision < 51:

                result = "Hit!\n\n"
            
            elif 10 < precision < 31:

                result = "Weak hit!\n\n"
                enemy_attack -= 1
                
            elif 1 <= precision <= 10:
            
                if precision == 3 or precision == 4:

                    result = "Glancing blow.\n\n" 
                    enemy_attack -= 3
                
                elif precision == 1 or precision == 2:

                    result = "Missed!\n\n"
                    enemy_attack = 0
                
                else:

                    result = "Made Contact.\n\n"
                    enemy_attack -= 2
                
            print(result)
            
            if defense_mod > 0:

                enemy_attack -= defense_mod

            print(f"\n -- Defense Modifier is {defense_mod} -- \n")
            
            if enemy_attack < 0:
            
                enemy_attack = 0
            
            print(f"The {enemy_name!s} strikes you for: {enemy_attack} damage!\n")
            time.sleep(2)
            
            player_hp_dmg -= enemy_attack
            
            if player_hp_dmg <= 0:
                
                determine_player_death(player_hp_dmg, enemy_name)

            print(f"You now have {player_hp_dmg} hit points.\n")
            print("  -------------********-------------  \n\n")
            time.sleep(2)
            
            print("Now it's your turn to attack!\n")

            time.sleep(2)
            
            # First attack algorithm:
            # player_attack = x + y + j
            
            # Second attack algorithm:
            # modifier = randint(1, 3)
            # player_attack = (x + y + j) // modifier
    
            # updated attack algorithm:

            x = player_str
            y = player_dex 
            j = player_int
            order = [x, y, j]
            order.sort()
            a = order[0] // 3
            b = order[1] // 2
            c = order[2] 
            player_attack = a + b + c
            
            balance = randint(1, 3)
            
            if balance == 1:

                print("Perfectly balanced attack!\n")
            
            elif balance == 2:

                print("Well balanced attack!\n")
                player_attack //= 2
            
            elif balance == 3:

                print("Off balance attack.\n")
                player_attack //= 3
            
            else:

                print("This should not ever print. Ever.")
            
            precision = randint(1, 100)
            
            if precision >= 90:
            
                if precision == 99 or precision == 100:

                    result = "Unreal Critical Precision!\n\n" 
                    player_attack += 4
                
                else: 

                    result = "Critical Precision!\n\n" 
                    player_attack += 3
            
            elif 75 < precision < 90:

                result = "Precision hit!\n\n" 
                player_attack += 2
            
            elif 50 < precision < 76:

                result = "Good Hit!\n\n"
                player_attack += 1
                
            elif 30 < precision < 51:
                
                result = "Hit!\n\n"
            
            elif 10 < precision < 31:

                result = "Weak hit!\n\n"
                player_attack -= 1
            
            elif 1 <= precision <= 10:
            
                if precision == 3 or precision == 4:

                    result = "Glancing blow.\n\n" 
                    player_attack -= 3
                
                elif precision == 1 or precision == 2:

                    result = "Miss!\n\n"
                    player_attack = 0
                
                else:

                    result = "Made Contact.\n\n"
                    player_attack -= 2
                
            print(result)
            
            if attack_mod > 0:

                player_attack += attack_mod
                print(f"\n -- Attack Modifier is {attack_mod} -- \n")
            
            if player_attack < 0:
                
                player_attack = 0
            
            elif result == "Miss!\n\n":
                
                player_attack = 0
            
            print(f"You strike the {enemy_name!s} for: {player_attack} damage!\n")
            time.sleep(2)
            
            enemy_hp -= player_attack
            
            if enemy_hp <= 0:
                
                determine_enemy_death(enemy_hp, enemy_name)
                continue
            
            print(f"The {enemy_name!s} now has {enemy_hp} hit points.\n")
            print("  -------------********-------------  \n\n")
            time.sleep(1)
                
            if small_medallion and round_count % 2 == 1:

                print("Warmth radiates from the medallion,")
                print("suddenly you heal a little bit.")
                time.sleep(1)
                print("You gain 1 hit point!\n\n")
                player_hp_dmg += 1
    
                if player_hp_dmg > player_hp:

                    player_hp_dmg = player_hp
            
            elif big_medallion and round_count % 2 == 1:

                print("The medallion's heat radiates through your body,")
                print("and suddenly you see a wound close up.")
                time.sleep(1)
                print("You gain 2 hit points!\n\n")
                player_hp_dmg += 2

                if player_hp_dmg > player_hp:

                    player_hp_dmg = player_hp

            elif intricate_medallion and round_count % 2 == 1:

                print("The medallion's heat radiates through your body,")
                print("and suddenly you see a wound close up.")
                time.sleep(1)
                print("You gain 2 hit points!\n\n")
                player_hp_dmg += 2

                if player_hp_dmg > player_hp:

                    player_hp_dmg = player_hp
    
    else:
        
        while player_hp_dmg > 0 and enemy_hp > 0:
            
            round_count += 1
            
            print(f"\t###      ROUND {round_count}      ###\n\n\n")
            
            print("You attack!\n")
            
            time.sleep(1)
        
            x = player_str
            y = player_dex 
            j = player_int
            order = [x, y, j]
            order.sort()
            a = order[0] // 3
            b = order[1] // 2
            c = order[2] 
            player_attack = a + b + c
            
            balance = randint(1, 3)
            
            if balance == 1:

                print("Perfectly balanced attack!\n")
            
            elif balance == 2:

                print("Well balanced attack!\n")
                player_attack //= 2
            
            elif balance == 3:

                print("Off balance attack.\n")
                player_attack //= 3
            
            else:

                print("This should not ever print. Ever.")
            
            precision = randint(1, 100)
            
            if precision >= 90:
            
                if precision == 99 or precision == 100:

                    result = "Unreal Critical Precision!\n\n" 
                    player_attack += 4
                
                else: 

                    result = "Critical Precision!\n\n" 
                    player_attack += 3
            
            elif 75 < precision < 90:

                result = "Precision hit!\n\n" 
                player_attack += 2
            
            elif 50 < precision < 76:

                result = "Good Hit!\n\n"
                player_attack += 1
                
            elif 30 < precision < 51:
                
                result = "Hit!\n\n"
            
            elif 10 < precision < 31:

                result = "Weak hit!\n\n"
                player_attack -= 1
            
            elif 1 <= precision <= 10:
            
                if precision == 3 or precision == 4:

                    result = "Glancing blow.\n\n" 
                    player_attack -= 3
                
                elif precision == 1 or precision == 2:

                    result = "Miss!\n\n"
                    player_attack = 0
                
                else:

                    result = "Made Contact.\n\n"
                    player_attack -= 2
                
            print(result)
            
            if attack_mod > 0:

                player_attack += attack_mod
                print(f"\n -- Attack Modifier is {attack_mod} -- \n")
            
            if player_attack < 0:
                
                player_attack = 0
            
            elif result == "Miss!\n\n":
                
                player_attack = 0
            
            print(f"You strike the {enemy_name!s} for: {player_attack} damage!\n")
            time.sleep(2)
            
            enemy_hp -= player_attack
            
            if enemy_hp <= 0:
                
                determine_enemy_death(enemy_hp, enemy_name)
                continue
            
            print(f"The {enemy_name!s} now has {enemy_hp} hit points.\n")
            print("  -------------********-------------  \n\n")
            time.sleep(2)
                
            print(f"Now it's the {enemy_name!s}\'s turn!\n")            

            time.sleep(2)
            
            enemy_attack = randint(1, enemy[1])
            precision = randint(1, 100)
        
            if precision >= 90:
        
                if precision == 99 or precision == 100:

                    result = "Unreal Critical Precision!\n\n" 
                    enemy_attack += 4
                
                else: 

                    result = "Critical Precision!\n\n" 
                    enemy_attack += 3
            
            elif 75 < precision < 90:

                result = "Precision hit!\n\n" 
                enemy_attack += 2
                
            elif 50 < precision < 76:
                
                result = "Good hit!\n\n"
                enemy_attack += 1
            
            elif 30 < precision < 51:

                result = "Hit!\n\n"
            
            elif 10 < precision < 31:

                result = "Weak hit!\n\n"
                enemy_attack -= 1
                
            elif 1 <= precision <= 10:
            
                if precision == 3 or precision == 4:

                    result = "Glancing blow.\n\n" 
                    enemy_attack -= 3
                
                elif precision == 1 or precision == 2:

                    result = "Missed!\n\n"
                    enemy_attack = 0
                
                else:

                    result = "Made Contact.\n\n"
                    enemy_attack -= 2
                
            print(result)
            
            if defense_mod > 0:

                enemy_attack -= defense_mod

            print(f"\n -- Defense Modifier is {defense_mod} -- \n")
            
            if enemy_attack < 0:
            
                enemy_attack = 0
            
            print(f"The {enemy_name!s} strikes you for: {enemy_attack} damage!\n")
            time.sleep(2)
            
            player_hp_dmg -= enemy_attack
            
            if player_hp_dmg <= 0:
                
                determine_player_death(player_hp_dmg, enemy_name)

            print(f"You now have {player_hp_dmg} hit points.\n")
            print("  -------------********-------------  \n\n")
            time.sleep(2)
                
            if small_medallion and round_count % 2 == 1:

                print("Warmth radiates from the medallion,")
                print("suddenly you heal a little bit.")
                time.sleep(1)
                print("You gain 1 hit point!\n\n")
                player_hp_dmg += 1
    
                if player_hp_dmg > player_hp:

                    player_hp_dmg = player_hp
            
            elif big_medallion and round_count % 2 == 1:

                print("The medallion's heat radiates through your body,")
                print("and suddenly you see a wound close up.")
                time.sleep(1)
                print("You gain 2 hit points!\n\n")
                player_hp_dmg += 2

                if player_hp_dmg > player_hp:

                    player_hp_dmg = player_hp

            elif intricate_medallion and round_count % 2 == 1:

                print("The medallion's heat radiates through your body,")
                print("and suddenly you see a wound close up.")
                time.sleep(1)
                print("You gain 2 hit points!\n\n")
                player_hp_dmg += 2

                if player_hp_dmg > player_hp:

                    player_hp_dmg = player_hp
    
        print("You win!\n")
        time.sleep(2)
    
    #LOOT CODE
    chance = randint(1, 100)
    if chance > 40: 
        
        print(f"The {enemy_name!s} dropped loot!\n")
        j = randint(0, 8)

        if player_lvl <= 3:
            
            loot = loot_lvl_1_3[j]
        
            print(f"It's a {loot!s}!\n\n")
            time.sleep(1)
            
            if loot in satchel_contents:

                print(f"You've already got a {loot!s}...\n")
                time.sleep(1)
            
            else: 

                satchel_contents.append(loot)
                print(f"You've looted {loot!s} from the {enemy_name!s}!\n")
                time.sleep(3)
        
        elif player_lvl <= 6:
            
            chance = randint(1, 50)

            if chance < 20:

                loot = loot_lvl_1_3[j]

                print(f"It's a {loot!s}!\n\n")
                time.sleep(1)
            
                if loot in satchel_contents:

                    print(f"You've already got a {loot!s}...\n")
                    time.sleep(1)
            
                else: 

                    satchel_contents.append(loot)
                    print(f"You've looted {loot!s} from the {enemy_name!s}!\n")
                    time.sleep(3)

        else: 

            loot = loot_lvl_4_6[j]
            
            print(f"It's a {loot!s}!\n\n")
            time.sleep(1)
            
            if loot in satchel_contents:

                print(f"You've already got the {loot!s}...\n")
                time.sleep(1)
            
            else: 

                satchel_contents.append(loot)
                print(f"You've looted the {loot!s} from the {enemy_name!s}!\n")
                time.sleep(3)
                
    else:
            
        chance = randint(1, 60)
        j = randint(0, 8)

        if chance < 30:

            loot = loot_lvl_1_3[j]

            print(f"It's a {loot!s}!\n\n")
            time.sleep(1)
            
            if loot in satchel_contents:

                print(f"You've already got the {loot!s}...\n")
                time.sleep(1)
            
            else: 

                satchel_contents.append(loot)
                print(f"You've looted the {loot!s} from the {enemy_name!s}!\n")
                time.sleep(3)

        elif chance < 47:

            loot = loot_lvl_4_6[j]

            print(f"It's a {loot!s}!\n\n")
            time.sleep(1)
            
            if loot in satchel_contents:

                print(f"You've already got the {loot!s}...\n")
                time.sleep(1)
            
            else: 

                satchel_contents.append(loot)
                print(f"You've looted the {loot!s} from the {enemy_name!s}!\n")
                time.sleep(3)

        else:

            loot = loot_lvl_7_9[j]
            
            print(f"It's a {loot!s}!\n\n")
            time.sleep(1)
            
            if loot in satchel_contents:

                print(f"You've already got the {loot!s}...\n")
                time.sleep(1)
            
            else: 

                satchel_contents.append(loot)
                print(f"You've looted the {loot!s} from the {enemy_name!s}!\n")
                time.sleep(3)
        
    fight_count += 1  #to tabulate fights won while alive
    
    if high_scorer == False:
        
        if fight_count > fight_count_most: 
            
            high_scorer = True
            print("You've just taken 1st place on the fight count list!\n")
            time.sleep(1)
            high_scorer_fcm = input("Enter your name to go on the scoreboard: ")
    
    if fight_count > fight_count_most:

        fight_count_most = fight_count
    
    print(f"You've gained {enemy[2]} experience points!\n")
    
    time.sleep(1)
    
    player_xp -= enemy[2]
    
    if player_xp <= 0:

        level_up()
        player_xp = player_xp_cap
    
    print(f"You have {player_xp} experience points to gain before you level up.\n")


def determine_enemy_death(num, enemy_name):

    if num == 0:

        print(f"You barely defeated the {enemy_name!s}!\n")
        
    elif num == -1:

        print(f"The {enemy_name!s} juuuuust rolls over!\n")
        
    elif num == -2:

        print(f"The {enemy_name!s} falls with little glory.\n")
        
    elif num == -3:

        print(f"You thumped the {enemy_name!s}.\n")
        
    elif num == -4:

        print("Solidly dead. Nice work.\n")
    
    elif num == -5:

        print("Clearly dead. No brainer.\n")
        
    elif num == -6:

        print("Were you making that personal? (hypothetical)\n")
    
    elif num == -7:

        print("Holy Moly, you freaking crushed it. freaking. crushed. it.\n")
    
    elif num == -8:

        print(f"Wow, that {enemy_name!s} died a lot.\n")
    
    elif num == -9:

        print("Yikes. Not too often I need to look away at a death.\n")
        
    elif num == -10:

        print("You might need to change your clothes after that shelacking!\n")
        
    elif num == -11:

        print("Foooooeey! Cosmic strike!\n")
        
    elif num == -12:

        print(f"The {enemy_name!s} explodes!\n")
    
    elif num == -13:

        print(f"The {enemy_name!s} basically died 5 minutes ago from that hit.\n")
    
    elif num == -14:

        print("-14, really? Holy Fuggin Heckfire!\n")
        
    elif num == -15:

        print("Hit so hard it's been forgotten.\n")
    
    elif num == -16:

        print("I'm not sure it could get any more dead.\n")
        
    elif num == -17:

        print("Flat out destroyed!\n")
    
    elif num == -18:

        print("Undeniably, inarguably, destroyed!\n")
        
    elif num == -19:

        print(f"That blow may have killed three {enemy_name!s}s.\n")
    
    elif num == -20:

        print("A strike like that should not be possible.\n")
    
    elif num <= -21:

        print("Bravo! Hall of Fame Death!\n")
    
    else:

        print("This should never ever ever print.\n\n")
        

def determine_player_death(num, enemy_name):

    if num == 0:

        dead(f"The {enemy_name!s} has barely defeated you!\n")
        
    elif num == -1:

        dead(f"The {enemy_name!s} juuuuust defeated you!\n")
        
    elif num == -2:

        dead(f"You got beaten by the {enemy_name!s}.\n")
        
    elif num == -3:

        dead(f"You got thwumped by the {enemy_name!s}.\n")
        
    elif num == -4:

        dead("Well, you are solidly dead, I'd say.\n")
    
    elif num == -5:

        dead("Clearly dead. No doubter.\n") 
        
    elif num == -6:

        dead("That was not nice and frankly, it looked a little personal.\n")
    
    elif num == -7:

        dead("Holy Maolly, you got freaking crushed. freaking. crushed.\n")
    
    elif num == -8:

        dead("Having a bad day? (don't answer that)\n") 
    
    elif num == -9:

        dead("Yikes. Not too often a monster looks away at a death.\n")
        
    elif num == -10:

        dead("May need to check the corners for limbs because you got torn apart!\n")
        
    elif num == -11:

        dead("I was not sure someone could get this dead.\n")
        
    elif num <= -12:

        dead("Bravo! Hall of Fame Death!\n")
    
    else:

        dead("this should never print\n")


def boss_encounter(room, modifier):
    
    if room == "room2":

        enemy_name = "Goblin King"
        
        if modifier == "Spade":

            enemy = (99, 9, 32, 12)

            print("You have cleanly re-potted the plant!\n")
            time.sleep(1)
            print(f"Suddenly, you hear a grumble in the hallway, and in walks the {enemy_name!s}!")
            time.sleep(2)
            print("Even though he's appreciative of you doing the chore he'd been")
            print(f"neglecting, the {enemy_name!s} is still going to fight you.\n\n")
            time.sleep(3)
        
        elif modifier == "Shovel" or modifier == "Hands":

            enemy = (99, 12, 32, 12)

            print("You have messily re-potted the plant!\n")
            time.sleep(1)
            print(f"Suddenly, you hear an angry grunt from the hallway, and in walks the {enemy_name!s}!")
            time.sleep(2)
            print("Apparently, he's particular about keeping his soil from hitting the stone,")
            print("and so he's frustrated and disappointed with you, and is ready to fight.\n")
            time.sleep(3)
        
        elif modifier == "Balanced Pickaxe":

            enemy = (99, 15, 32, 12)

            print("Your pickaxe breaks the empty pot and you hear an enraged roar!\n")
            time.sleep(2)
            print(f"The {enemy_name!s} bursts into the room and throws his arms above his head, howling")
            print("with rage as he sees his broken pot.\n")
            print("Obviously, you appear to be in trouble.\n\n")
            time.sleep(3)
        
        elif modifier == "Thief":

            enemy = (99, 15, 32, 12)

            print("The moment you touch the pot, you hear a deep scream of anguish!\n")
            time.sleep(2)
            print(f"Charging through the door is the {enemy_name!s}! He sees you trying to take his pot")
            print("and he becomes enraged!\n")
            time.sleep(3)
        
        else:

            enemy = (99, 12, 32, 12)
            print("Your bumbling has made a mess and caused a ruckus in the hallway!\n")
            time.sleep(2)
            print(f"The {enemy_name!s} appears at the door and he's ready to fight!\n")
            time.sleep(3)
            print("You and the {enemy_name!s} fight!\n\n\n")

        battle(enemy, enemy_name)
        
    elif room == "hiddenChamber":
        
        enemy_name = "Darkness Troll"
        enemy = (148, 13, 45, 18)
        battle(enemy, enemy_name)
        
    #elif room == "hidden2":
        #enemy_name = "Deranged Duke"
    
    #elif room == "hidden3":
        #enemy_name = "Venomous Queen"

        
def enemy_encounter():
    
    global player_hp_dmg
    
    x = randint(0, 8)
    
    if 0 < player_lvl <= 2:
        
        enemy = enemies_lvl_1_2[x]

        enemy_name = enemy

        #Enemy form: (hp, max_attack, gives_xp, dex)

        if x == 0:

            enemy = (6, 3, 4, 1) #slime 14
        
        elif x == 1:

            enemy = (7, 4, 4, 5) #gnoll 18
        
        elif x == 2:

            enemy = (8, 5, 5, 6) #wolf 21
        
        elif x == 3: 

            enemy = (5, 3, 5, 10) #bat 23
        
        elif x == 4:

            enemy = (7, 3, 4, 6) #goblin 19
        
        elif x == 5:

            enemy = (4, 3, 3, 8) #cat 16
        
        elif x == 6:

            enemy = (6, 3, 3, 2) #flannel_bag 12
        
        elif x == 7:

            enemy = (10, 3, 5, 2) #glowing_top_hat 19
        
        else:

            enemy = (4, 3, 2, 2) #round_spectacles() 11

    elif 2 < player_lvl <= 4:
        
        enemy = enemies_lvl_3_4[x]

        enemy_name = enemy
        
        if x == 0:

            enemy = (12, 5, 7, 2) #lg_slime 22
        
        elif x == 1:
    
            enemy = (14, 10, 10, 12) #gnoll_pack 37
        
        elif x == 2:

            enemy = (11, 7, 8, 7) #alpha_wolf 31
        
        elif x == 3: 

            enemy = (8, 8, 9, 12) #ancient_bat 35
        
        elif x == 4:

            enemy = (7, 10, 7, 6) #desperate_goblin 27
        
        elif x == 5:

            enemy = (10, 7, 7, 10) #mountain_cat 31
        
        elif x == 6:

            enemy = (7, 10, 7, 3) #self_closing_flannel_bag 25
        
        elif x == 7:

            enemy = (12, 8, 9, 2) #glowing_top_hat_w_cane 29
            
        else:

            enemy = (8, 8, 6, 3) #jagged_contacts 23
    
    elif 4 < player_lvl <= 6:
        
        enemy = enemies_lvl_5_6[x]

        enemy_name = enemy
    
        if x == 0:

            enemy = (16, 15, 12, 8) #shiny_mist 47
        
        elif x == 1:

            enemy = (17, 2, 9, 18) #floor_of_marbles 43
        
        elif x == 2:

            enemy = (14, 14, 10, 5) #ancient_wolf 36
        
        elif x == 3: 

            enemy = (18, 12, 12, 5) #wall_of_bats 41
        
        elif x == 4:

            enemy = (28, 5, 9, 3) #competitive_eater 35
        
        elif x == 5:

            enemy = (19, 15, 14, 1) #donald_trump 40
        
        elif x == 6:

            enemy = (25, 18, 14, 4) #mary_poppins_bag_of_horrors 51
        
        elif x == 7:

            enemy = (19, 13, 14, 11) #badass_3_suit_hat_cane 50
        
        else:

            enemy = (1, 20, 15, 20) #eye_candy 56

    elif 6 < player_lvl:
        
        enemy = enemies_lvl_4_6[x]

        enemy_name = enemy
        
        if x == 0:

            enemy = (31, 19, 15, 5) #wall_of_goo
        
        elif x == 1:
    
            enemy = (25, 21, 14, 16) #marble_maniac
        
        elif x == 2:

            enemy = (45, 24, 20, 20) #wolf_pack
        
        elif x == 3: 

            enemy = (29, 18, 14, 24) #giant_bat
        
        elif x == 4:

            enemy = (40, 21, 17, 6) #jaws_of_doom
        
        elif x == 5:

            enemy = (38, 25, 18, 14) #enraged_lion
        
        elif x == 6:

            enemy = (50, 14, 14, 8) #automated_sack_of_death
        
        elif x == 7:

            enemy = (43, 16, 16, 12) #thrift_store_monster
            
        else:

            enemy = (31, 26, 16, 19) #ball_of_vipers
    
    else:

        return("Did not work!\n")
    
    print("You've run into an enemy!\n")
    time.sleep(1)
    print(f"It's a {enemy_name!s}.\n\n")
    
    choice = determine_intent("Are you going to fight or flee?\n")
    
    if choice == "fight": 
    
        print(f"You and the {enemy_name!s} fight!\n\n\n")
        time.sleep(1)
        battle(enemy, enemy_name)
    
    else: 
    
        if enemy[3] > player_dex:
            
            diff = (enemy[3] - player_dex) * 10
            chance = randint(1, 100)

            if chance >= 50 + diff:
                
                print("Somehow you escape!\n\n")
            
            else: 

                print(f"You fail to escape, and the {enemy_name!s} makes you pay!\n")
                print("You take 4 damage!\n\n")
                time.sleep(2)
                player_hp_dmg -= 4

                if player_hp_dmg <= 0:

                    dead("That was enough to kill ya, sadly enough.")

                battle(enemy, enemy_name)
        
        else:
            
            diff = (player_dex - enemy[3]) * 10

            if diff > 40:

                diff = 40
                chance = randint(1, 100)

            if chance <= 50 + diff:
                
                print("Because of your superior quickness, you escape.\n\n")
                time.sleep(2)
            
            else: 

                print(f"You fail to escape, and the {enemy_name!s} makes you pay!\n")
                print("You take 4 damage!\n\n")
                time.sleep(2)
                player_hp_dmg -= 4

                if player_hp_dmg <= 0:

                    dead("That was enough to kill ya, sadly enough.")

                battle(enemy, enemy_name)


def level_up():
    
    global player_lvl, player_xp_cap, player_str, player_dex, player_int, player_hp
    global player_hp_dmg, player_xp
    
    print("You've leveled up! Congrats, that's awesome!\n\n")
    time.sleep(2)
    
    print(f"""These are your old stats:
        Level: {player_lvl}
        Strength: {player_str}
        Dexterity: {player_dex}
        Intelligence: {player_int}
        Hit Points: {player_hp}\n""")
    print("_____________\n")
    
    player_lvl += 1
    player_xp_cap *= 2
    player_xp = player_xp_cap
    
    if player_class == "Wizard":
        
        player_str += randint(0, 1)
        player_dex += randint(0, 1)
        player_int += randint(2, 4)
    
    elif player_class == "Ninja":
        
        player_str += randint(0, 1)
        player_dex += randint(2, 4)
        player_int += randint(0, 1)
    
    else:

        player_str += randint(0, 3)
        player_dex += randint(0, 3)
        player_int += randint(0, 3)
    
    player_hp += randint(2, 5)
    player_hp_dmg = player_hp
    time.sleep(2)
    
    print(f"""These are your new stats: 
        Level: {player_lvl}
        Strength: {player_str}
        Dexterity: {player_dex}
        Intelligence: {player_int}
        Hit Points: {player_hp}\n\n""")
    print("___________\n")
    
    time.sleep(2)


def start():
    
    global first_time_secret_room, first_time_first_room, came_from, player_hp_dmg, defense_mod
    global player_name, player_class, player_lvl, player_xp, satchel_contents, attack_mod
    global defeat_darkness_troll, defeat_goblin_king, boys_saved, boys_rescued, walking_stick
    global cloth_cap, short_stick, basic_gloves, thick_shirt, three_ft_pipe, sturdy_hat, madrona_wand
    global fingerless_gloves, leather_t, sword, wide_brim_hat, oak_staff, power_mitts, leather_jacket
    global small_medallion, big_medallion, intricate_medallion, wizard_robes, wizard_hat, wizard_staff
    global imbued_eye_mask, stealth_slippers, katana, armored_tweed_vest, knickers, scepter, weapon
    
    player_name = ""
    player_class = ""
    player_lvl = 1
    first_time_secret_room = True
    first_time_first_room = True
    high_scorer_cave = False
    high_scorer_furthest = False
    high_scorer = False
    satchel_contents = []
    attack_mod = 0
    defense_mod = 0
    defeat_darkness_troll = False
    defeat_goblin_king = False
    boys_saved = 0
    boys_rescued = []
    walking_stick = False
    cloth_cap = False
    short_stick = False
    basic_gloves = False
    thick_shirt = False
    three_ft_pipe = False
    sturdy_hat = False
    madrona_wand = False
    fingerless_gloves = False
    leather_t = False
    sword = False
    wide_brim_hat = False
    oak_staff = False
    power_mitts = False
    leather_jacket = False
    small_medallion = False
    big_medallion = False
    intricate_medallion = False
    wizard_robes = False
    imbued_eye_mask = False
    armored_tweed_vest = False
    wizard_hat = False
    stealth_slippers = False
    knickers = False
    wizard_staff = False
    katana = False
    scepter = False
    weapon = False
    book_of_knots = False
    found_treasure_1 = False
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\t\tLabyrinth of the Lost Sons\n\n\n")
    
    time.sleep(2)
    print("Thanks for playing.\n")
    print("At any time type 'options' to view your in-game commands.")
    print("\n\n\n")
    time.sleep(2)
    
    print("""
    You awaken. It's cold but you're insulated by a thin layer of fat. It feels 
    like you shouldn't be here or you're lost. It's a strange feeling.\n""")
    time.sleep(3)
    
    print("""
    You get up and look around you. You see snow covered fields and a grey sky. 
    A light snow falls. You look down and see that you're only wearing
    unders.\n""")
    time.sleep(3)
    
    print("""
    You turn around and there is a high concrete wall stretching far 
    in both directions extensively, going on and on for, at most, forever.\n""")
    time.sleep(3)
    
    print("""
    An old woman sits next to a thin rectangular opening in the concrete. You 
    approach the woman and she sees you and speaks.\n\n\n""")
    time.sleep(3)
    
    print("\n\t I see you're awake. You came out of nowhere it seems.\n")
    
    build_character()
    
    answer = determine_intent("Are you on a quest? Or just hanging out? Or What?\n")
    
    if "quest" in answer: 
        
        print("Oh, a quest, eh?" )
        time.sleep(2)
        print("This labyrinth holds great treasure. And danger. Did I mention danger?\n")
        
        decision = determine_intent("Are you willing to proceed?\n\n")
        
        if decision == "y": 

            print("Best luck in there!\n")
            came_from = "South"
            
            first_intersection()
        
        else:

            dead("The old woman rises up in a fury and one-punch kills you.")
    
    elif "hang" in answer:
        
        print("You're so cool. I wish any one of my twelve sons were as cool")
        print("as you are. Are you single?\n")
        time.sleep(1)
        
        print("Just kidding. It's fine. I didn't mean it anyway.\n")
        
        time.sleep(2)
        print("Speaking of my kids... I lost them. They're in the labyrinth")
        print("and I'm certain they're being held prisoner or lost somewhere...\n\n")
        time.sleep(1)
        print("Woe is me!! I have the gout.\n")
        
        decision = determine_intent("Will you help me?\n")
        
        if decision == "y":

            print("Oh, thank you! Send them back to me when you've found them.\n\n")
            time.sleep(2)
            print("You might need to draw them a map, if you have the materials for it...")
            print("Just so they know how to get back to me.\n")
            time.sleep(2)
            print("Good luck!")
            came_from = "South"

            first_intersection()
        
        else: 

            print("I curse you then! May death be upon your door!\n\n\n.\n..\n...")
            print("You walk awkwardly past the woman and into the labyrinth.")
            print("The wall of the labyrinth breaks for no apparent reason.\n")
            time.sleep(1)

            dead("The wall falls on you and the woman laughs as you perish.")
    
    else: 

        print("That doesn't suprise me.\n")
        time.sleep(1)
        print("I think whatever you're looking for is in this labyrinth.\n\n")
        print("There's some pretty sweet loot and basically no danger.\n")
        time.sleep(1)
        
        decision = determine_intent("Are you going to enter the labyrinth?\n")
        
        if decision == "y": 

            print(f"'Best luck in there, you mysterious {player_class}'\n\n")
            came_from = "South"
            
            first_intersection()
        
        else:

            dead("The old woman starts to sing and suddenly your head explodes.")


def build_character():

    global player_name, player_class, player_str, player_dex, player_int, player_hp
    global player_hp_dmg, player_lvl, player_xp, player_xp_cap
                                
    player_name = input("What, may I ask, is your name, sweet traveler?\n\n->")
    
    choice = determine_intent(f"""\nAnd what type of a hero are you, {player_name!s}?\n
                    \t 1. Pro Wizard
                    \t 2. Master Ninja
                    \t 3. Amatuer Wizard, decent Ninja\n""")
    
    if choice == "1":
        
        player_class = "Wizard"
        player_lvl = 1
        player_str = 1
        player_dex = 2
        player_int = 6
        player_hp = 11
        player_hp_dmg = player_hp
        player_xp_cap = 10
        player_xp = player_xp_cap
    
    elif choice == "2":
        
        player_class = "Ninja"
        player_lvl = 1
        player_str = 3
        player_dex = 4
        player_int = 2
        player_hp = 13
        player_hp_dmg = player_hp
        player_xp_cap = 10
        player_xp = player_xp_cap
    
    else:

        player_class = "Wizard/Ninja"
        player_lvl = 1
        player_str = 3
        player_dex = 3
        player_int = 3
        player_hp = 12
        player_hp_dmg = player_hp
        player_xp_cap = 10
        player_xp = player_xp_cap
    
    print(f"Ahh, {player_name!s} the {player_class!s}! Exciting!\n")
    print(f"Jeez. I haven't seen a {player_class!s} in ages...")
    time.sleep(2)
    
    print("\nActually, I haven't seen anyone in ages.\n")
    print("You look really good. Seriously, have you looked at yourself lately?\n\n")
    time.sleep(2)
    
    choice2 = determine_intent("Type 'stats' to check yourself out or type 'okay' to continue.\n")
    
    if choice2 == "n":

        print("I am not your mother, so I'm not going to force you.\n")


def first_intersection():

    global came_from
    
    print("\nThe hallway is dark but enough light is present to see around.\n") 
    time.sleep(1)
    print("You may choose to travel North, West, or East.")
    print(f"You came from the {came_from!s}.\n")
    
    choice = determine_intent("Which direction do you choose?\n")
    
    if choice == "w":
        
        print("You go West and come to an elbow leading North.\n")
        time.sleep(2)
        
        print("You follow the elbow and are in a corridor that smells like dust")
        print("and decay.\n")

        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()

        time.sleep(2)
        print("As you walk you see a 6 inch bookcase on your left.")
        print("There is a Red Book, a Green Book, and a Blue Book.\n")
        time.sleep(1)
        
        choice2 = determine_intent("Do you move on or do you inspect a book?\n")
        
        if choice2 == "move":
            
            print("You go around the corner and come to another intersection.\n")
            came_from = "West"

            chance = randint(1, 100)
            
            if chance <= 60:

                enemy_encounter()

            second_intersection()
        
        elif choice2 == "inspect":
            
            secret_room_1()
        
        else: 

            print("I wish I was human! Then I could understand you!")
            dead("A wave of sound comes and crushes your skull.")
                            
    elif choice == "e":
        
        print("You follow the path East, which comes to an elbow that heads")
        print("North. You follow that path and come to another intersection.\n")
        came_from = "South"

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()

        third_intersection()
        
    elif choice == "n": 

        print("You head North and come to a T intersection, branching West and East.\n")
        came_from = "South"
        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()

        second_intersection()
    
    else: 

        print("You've entered something I do not understand.")

        first_intersection()
        

def secret_room_1():

    global came_from, player_int, player_dex, first_time_secret_room
        
    print("Interesting. You're curious. I like that.\n")
        
    choice3 = determine_intent("""Which one book would you like to inspect?\n
        1. Red Book
        2. Green Book   
        3. Blue Book\n""")
            
    if choice3 == "1" or choice3 == "Red Book":
        
        print("""
        You take the Red Book off the shelf and read the title;\n
        'Making Friends with Blood Pacts' 
        by 'Glungoral the Witty' \n
        You flip through the book, finding it boorish. You put the book back and
        can now decide to go North or South in the corridor.\n\n""")
        came_from = "West"
        
        choice = determine_intent("Would you like to go North or South in the corridor?\n")
        
        if choice == "n":

            print("You go North.\n")

            second_intersection()
        
        elif choice == "s":

            print("You go South.\n")

            first_intersection()
            
        else: 

            print("You stay put.")

            secret_room_1()
                        
    elif choice3 == "2" or choice3 == "Green Book":

        print("""
        You take the Green book off the shelf and read the title; \n
        'Pushing Past Your Own Insecurities for Fun and Profit!' 
        by 'Mungorak the Pleasant'\n
        You flip through the book and it quickly becomes your favorite, but you've
        got no time to read, so you put the book back and can now decide to go North 
        or South in the corridor.\n\n""")
        came_from = "West"
        
        choice = determine_intent("Would you like to go North or South in the corridor?\n")
            
        if choice == "n":

            print("You go North.\n")

            second_intersection()
        
        elif choice == "s":

            print("You go South.\n")

            first_intersection()
            
        else:

            print("I DO NOT UNDERSTAND.\n\n")

            secret_room_1()
            
    elif choice3 == "3" or choice3 == "Blue Book":

        print("""
        As you attempt to take the Blue Book off the shelf, you feel it
        stick and then click mechanically into place as it comes forward. The book 
        gets sucked back onto the shelf and a panel in the wall moves aside,
        revealing a passageway.\n""")
        time.sleep(3)
                
        choice4 = determine_intent("Do you enter the passageway?\n")
                
        if choice4 == "y":

            came_from = "West"
            
            print("The passageway is short and leads to a secret room!\n")
            
            if not first_time_secret_room:

                print("You're standing in the secret room you hung out in earlier.\n")
                time.sleep(2)
                print("You remember the good times you had, then you turn around")
                print("and leave the room because there's nothing in there anymore.\n") 
                
                choice1 = determine_intent("Do you go North or South?\n")
                        
                if choice1 == "n":

                    print("North you go!\n")

                    second_intersection()
                
                elif choice1 == "s": 

                    print("South it is!\n")

                    first_intersection()
                
            else:
                
                first_time_secret_room = False

                enemy_encounter()
                
                print("Now that you stand victorious, you notice there is a shaft")
                print("of light highlighting a sweet looking chocolate danish on a")
                print("narrow pedestal.\n\n")
                time.sleep(2)
                
                print("\nYou examine it closely.\n\n")
                time.sleep(2)
                
                print("You don't want to put it in your satchel (messy!).\n")
                time.sleep(2)
                
                print("And it smells so good! You must eat it or leave it.\n")
                time.sleep(2)
                
                choice5 = determine_intent("Do you eat the danish or leave it?\n")
                    
                if "eat" in choice5:

                    print("You've never tasted anything so delicious and fresh!\n")
                    time.sleep(1)
                    
                    if player_class == "Wizard":
                        
                        player_int += 1
                        print("The danish expands your brain by approximately five percent.")
                        print(f"Your intelligence has grown by one. It is now {player_int}.\n")
                        time.sleep(3)
                        print("You leave the secret room.")
                        
                        choice1 = determine_intent("Do you go North or South?\n")
                            
                        if choice1 == "n":

                            print("North you go!\n\n")

                            second_intersection()
                        
                        else: 

                            print("South it is!\n\n")

                            first_intersection()
                            
                    else:
                            
                        player_dex += 1
                        print("The danish hones your muscles and heightens your quickness.")
                        print(f"Your dexterity has grown by one. It is now {player_dex}.\n")
                        time.sleep(3)
                        print("You leave the secret room.")
                        
                        choice1 = determine_intent("Do you go North or South?\n")
                            
                        if choice1 == "n":

                            print("North you go!\n\n")

                            second_intersection()
                        
                        else: 

                            print("South it is!\n\n")

                            first_intersection()    
                            
                else:

                    print("You back away from the danish... slowly back away.\n")
                    time.sleep(3)
                    print("Phew! That thing looked too delicious to be of any use!\n")  
                    
                    choice1 = determine_intent("Do you go North or South?\n")
                        
                    if choice1 == "n":

                        print("North you go!\n\n")

                        second_intersection()
                    
                    elif choice1 == "s":

                        print("South it is!\n\n")

                        first_intersection()
                        
                    else: 

                        print("I DO NOT KNOW WHY I PRINT.")

                        first_intersection()
                
        elif choice4 == "n":
                    
            print("""
                Yeah, who in their right mind would go in there!? It's probably 
                haunted or something. Definitely worth avoiding. You leave the panel and
                can now decide to go North or South in the corridor.\n""")
            came_from = "West"
            
            choice2 = determine_intent("Would you like to go North or South in the corridor?\n")
            
            if choice2 == "n":

                print("You go North.\n")

                second_intersection()
            
            elif choice2 == "s":

                print("You go South.\n")
    
                first_intersection()
            
            else:

                print("DO NOT KNOW.")

                first_intersection()
                
        else: 

            dead("Standing. Waiting. The floor opens and you fall into eternity.")
            
    else: 

        print("I wish I knew what you chose, but... you cryptic!")
        time.sleep(2)

        dead("Standing and waiting, suddenly the floor opens up and you fall onto some well made spikes.")


def second_intersection():

    global came_from, player_hp_dmg

    print("You are at an intersection that has passageways to the South, West, and East.")
    print("There is a dripping sound.\n")
    print(f"You came from the {came_from!s}.\n")
    time.sleep(1)
    
    choice = determine_intent("Which way do you go?\n")
    
    if choice == "s":

        print("You move South.\n")
        came_from = "North"

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()

        first_intersection()
    
    elif choice == "e":

        print("You move East\n")

        came_from = "West"

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()

        third_intersection()
    
    elif choice == "w":

        print("You go West and come to an elbow leading South.\n")
        time.sleep(2)
        print("You follow the elbow and are in a corridor that smells like dust and decay.\n")
        time.sleep(2)
        print("As you walk you see a 6 inch bookcase on your right.")
        print("There is a Red Book, a Green Book, and a Blue Book.\n")
        
        choice2 = determine_intent("Do you move on or do you inspect a book?\n")
        
        if choice2 == "move":

            print("You go around the corner and come to another intersection.\n")
            came_from = "West"
            chance = randint(1, 100)
            
            if chance <= 50:

                enemy_encounter()

            first_intersection()
        
        elif choice2 == "inspect":
            
            secret_room_1()
    
    elif choice == "n":

        print("You try to head North, but run into the concrete wall.\n")
        player_hp_dmg -= 1
        print(f"You lost a hit point! you now have {player_hp_dmg} hit points.\n")

        if player_hp_dmg <= 0:

                dead("You died on impact.")

        chance = randint(1, 100)
    
        if chance <= 50:

            enemy_encounter()

        second_intersection()
    
    else:

        print("NO DIRECTION. You head South.")

        first_intersection()


def third_intersection():

    global came_from, player_hp_dmg
    
    print("You are at an intersection with passageways to the South, West, and East.\n")
    print("There is a door along the cleft wall to the South/West.\n")
    print(f"You came from {came_from!s}.\n")
    
    choice = determine_intent("Which way do you go?\n")
            
    if choice == "door":
    
        first_room()
    
    elif choice == "s":

        print("You head South and hang a right, heading West, and")
        print("come to another intersection.\n")
        came_from = "East"

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        first_intersection()
    
    elif choice == "w":

        print("You head West and shortly come to another intersection.\n")
        came_from = "East"

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        second_intersection()
    
    elif choice == "e":

        print("You head East... and the hallway turns slightly.\n")
        time.sleep(1)
        print("Following the turn you head up stone stairs.\n")
        time.sleep(1)
        
        chance = randint(1, 100)
        
        if chance <= 70:

            enemy_encounter()
            
        print("Upon reaching the top of the stairs, a great chamber comes into view!\n\n")
        came_from = "Southwest"
        
        first_chamber()
    
    elif choice == "n":
        
        print("You try to head North, but run into the concrete wall.\n")
        player_hp_dmg -= 1
        print(f"You lost a hit point! you now have {player_hp_dmg} hit points.\n")

        if player_hp_dmg <= 0:

            dead("You died on impact. Impact with the wall.")

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        third_intersection()
    
    else:
        
        print("no thAnks. BLRGH.")

        third_intersection()

    
def first_room():
    
    global satchel_contents, came_from, first_time_first_room, player_hp_dmg
    came_from = "The Room"
    
    print("You open the door and step into a stark, dark room!\n\n")
    time.sleep(1)
    
    chance = randint(1, 100)

    if chance <= 70:

        enemy_encounter()
        
    if first_time_first_room:
    
        print("You notice a cube of stone in the center of the room and sitting")
        print("atop the stone are three precious gems.\n")
        time.sleep(1)
        print("There is an Emerald, a Ruby, and a Sapphire.\n\n")
    
        choice = determine_intent("""What do you do?\n
            \t1. Take the Emerald.
            \t2. Take the Ruby.
            \t3. Take the Sapphire.
            \t4. Take the Emerald & Ruby.
            \t5. Take the Emerald & Sapphire.
            \t6. Take the Ruby & Sapphire.
            \t7. Take all 3 stones.
            \t8. Take nothing and leave the room.\n""")
                
        if choice == "1":
            
            print("You grab the Emerald.\n")
            time.sleep(2)
            print("You feel intense burning that travels up your arm to your chest!\n\n")
            print("You lose 5 hit points!\n")
            player_hp_dmg -= 5

            if player_hp_dmg <= 0:

                dead("Looks like grabbing that Emerald kilt ya.")

            else:

                print("That sucked.\n")

                third_intersection()
            
        elif choice == "2":
            
            print("You pick up the Ruby and put it in your bag.\n")
            satchel_contents.append("Ruby")

            first_time_first_room = False
            
            choice2 = determine_intent("""Now what do you do?
                \t1. Take the Emerald.
                \t2. Take the Sapphire.
                \t3. Take the Emerald & Sapphire.
                \t4. Take nothing more and leave the room.\n""")
        
            if choice2 == "1":
                
                print("You grab the Emerald.\n")
                time.sleep(2)
                print("You feel intense burning that travels up your arm to your chest!\n\n")
                print("You lose 5 hit points!\n")
                player_hp_dmg -= 5

                if player_hp_dmg <= 0:

                    dead("Looks like grabbing that Emerald kilt ya.")

                else:

                    print("That wasn't cool.\n")

                    third_intersection()
                
            elif choice2 == "2":
                
                print("You pick up the Sapphire and put it in your bag.\n")
                satchel_contents.append("Sapphire")

                first_time_first_room = False
                
                choice3 = determine_intent("""Now what do you do?
                    \t1. Take the Emerald.
                    \t2. Take nothing more and leave the room.\n""")
                    
                if choice3 == "1":
                    
                    print("You grab the Emerald.\n")
                    time.sleep(2)
                    print("You feel intense burning that travels up your arm to your chest!\n\n")
                    print("You lose 5 hit points!\n")
                    player_hp_dmg -= 5

                    if player_hp_dmg <= 0:

                        dead("Looks like grabbing that Emerald kilt ya.")
        
                    else:

                        print("That hurt.\n")

                        third_intersection()

                else:

                    print("You are finished in this room.\n")

                    third_intersection()
                    
            elif choice2 == "3":
                
                print("You grab the Sapphire & Emerald.\n")
                time.sleep(2)
                print("You feel intense burning that travels up your arm to your chest!\n\n")
                print("You lose 5 hit points!\n")
                player_hp_dmg -= 5

                if player_hp_dmg <= 0:

                    dead("Looks like grabbing that Sapphire or that Emerald kilt ya.")

                else:

                    print("Ouch.\n")

                    third_intersection()

            else:

                print("You are finished in this room.\n")

                third_intersection()
                
        elif choice == "3":
            
            print("You pick up the Sapphire and put it in your bag.\n")
            satchel_contents.append("Sapphire")

            first_time_first_room = False
            
            choice2 = determine_intent("""Now what do you do?
                \t1. Take the Emerald.
                \t2. Take the Ruby.
                \t3. Take the Emerald & Ruby.
                \t4. Take nothing more and leave the room.\n""")
                
            if choice2 == "1":
                
                print("You grab the Emerald.\n")
                time.sleep(2)
                print("You feel intense burning that travels up your arm to your chest!\n\n")
                print("You lose 5 hit points!\n")
                player_hp_dmg -= 5

                if player_hp_dmg <= 0:

                    dead("Looks like grabbing that Emerald kilt ya.")

                else: 

                    print("That hurts bad!\n")

                    third_intersection()
                
            elif choice2 == "2":
                
                print("You pick up the Ruby and put it in your bag.\n")
                satchel_contents.append("Ruby")

                first_time_first_room = False
                
                choice3 = determine_intent("""Now what do you do?
                    \t1. Take the Emerald.
                    \t2. Take nothing more and leave the room.\n""")
                    
                if choice3 == "1":
                    
                    print("You grab the Emerald.\n")
                    time.sleep(2)
                    print("You feel intense burning that travels up your arm to your chest!\n\n")
                    print("You lose 5 hit points!\n")
                    player_hp_dmg -= 5

                    if player_hp_dmg <= 0:

                        dead("Looks like grabbing that Emerald kilt ya.")

                    else:

                        print("Geez. Hurt much?\n")

                        third_intersection()
                    
                else:

                    print("You are finished in this room.\n")

                    third_intersection()
                    
            elif choice2 == "3":
                
                print("You grab the Ruby & Emerald.\n")
                time.sleep(2)
                print("You feel intense burning that travels up your arm to your chest!\n\n")
                print("You lose 5 hit points!\n")
                player_hp_dmg -= 5

                if player_hp_dmg <= 0:

                    dead("Looks like grabbing that Emerald kilt ya.")

                else: 

                    print("Painful to say the least.\n")

                    third_intersection()
                
            else: 

                print("You're finished in this room.\n")

                third_intersection()
                
        elif choice == "4":
            
            print("You grab the Ruby and the Emerald.\n")
            time.sleep(2)
            print("You feel intense burning that travels up your arm to your chest!\n\n")
            print("You lose 5 hit points!\n")
            player_hp_dmg -= 5
            if player_hp_dmg <= 0:

                dead("Looks like grabbing that Emerald kilt ya.")

            else: 

                print("Owie zowie.\n")

                third_intersection()
            
        elif choice == "5":
            
            print("You grab the Sapphire and the Emerald.\n")
            time.sleep(2)
            print("You feel intense burning that travels up your arm to your chest!\n\n")
            print("You lose 5 hit points!\n")
            player_hp_dmg -= 5

            if player_hp_dmg <= 0:

                dead("Looks like grabbing that Emerald kilt ya.")

            else: 

                print("Gall darn, that hurt!\n")

                third_intersection()
            
        elif choice == "6":
            
            print("You grab the Ruby and the Sapphire and put them in your bag.\n")
            satchel_contents.append("Ruby")
            satchel_contents.append("Sapphire")

            first_time_first_room = False
            
            choice2 = determine_intent("""What do you do now?\n
                \t1. Take the Emerald.
                \t2. Take nothing more and leave the room.\n""")
            
            if choice2 == "1":
                
                print("You grab the Emerald.\n")
                time.sleep(2)
                print("You feel intense burning that travels up your arm to your chest!\n\n")
                print("You lose 5 hit points!\n")
                player_hp_dmg -= 5

                if player_hp_dmg <= 0:

                    dead("Looks like grabbing that Emerald kilt ya.")

                else: 

                    print("You cry a little bit to yourself because of the pain.\n")

                    third_intersection()
                
            else: 

                print("You're totally done in this room. Booyah!\n")

                third_intersection()
        
        elif choice == "7":
            
            print("You take the stones: Sapphire, Ruby, and Emerald.\n")
            time.sleep(2)
            first_time_first_room = False
        
            dead("Was it your greed?! Something seared into you and you disintigrate on the spot.")
            
        else: 

            print("Yeah, who needs those stones anyway? I'm sure they're worthless in this labyrinth...\n")

            third_intersection()
                    
    else:

        print("You stand in the familiar doorway. All of the gems have vanished.\n")
        time.sleep(3)
        print("You sniff and cry a little, then you get over it and get back to the hallway.\n")
    
        third_intersection()


def first_chamber():

    global came_from, first_time_chamber_one, player_hp_dmg, boys_saved, boys_rescued
    
    print("The chamber before you is a grand open chamber.\n")
    time.sleep(1)
    print("There are doors exiting the chamber in all directions,")
    print("and the grass floor has a slight covering of snow.\n")
    time.sleep(2)
    print("Great slabs of concrete act as a sort of Stonehenge")
    print("circling the chamber.\n\n" )
    print(f"You came from the {came_from!s}.\n")
    
    if first_time_chamber_one:

        print("You see an older boy chained to a chair in the middle of the chamber.")
        time.sleep(1)
        print("He is shivering yet not looking weak.\n")
        time.sleep(1)
        
        answer = determine_intent("What would you like to do? Approach the boy or take a door?\n")
    
        if "boy" in answer or "approach" in answer:
        
            print("You approach the boy.")
            time.sleep(1)
            print("He looks up at hearing your footsteps.\n")
            time.sleep(1)
            print("Hello there! I haven't seen anyone in so long, I don't even")
            print("know how I'm still alive.\n")
            time.sleep(2)
        
            answer1 = determine_intent("Are you here to help me?\n")
        
            if answer1 == "y":

                print("'Wonderful! My chains are secured to the ground by stone.'")
                answer2 = determine_intent("Are you able to free me?\n")
                
                if answer2 == "y":

                    choice = determine_intent("Excellent! What item will you use?\n")

                    if choice == "Balanced Pickaxe" and "Balanced Pickaxe" in satchel_contents:
    
                        print("You bring the Pickaxe sharply down on the first chain at the floor")
                        print("and it breaks.\n")
                        time.sleep(2)
                        print("You follow it up with the remaining three chains and the boy becomes")
                        print("free and stands looking at you.\n")
                        print("How do I get out of here? I'm sure I'll get chained up again if I can't leave now./n")
                        
                        choice2 = determine_intent("What item do you use?\n")
                        
                        if choice2 == "Paper and Pen" and "Paper and Pen" in satchel_contents:

                            print("You draw him a map and send him on his way.\n")
                            boys_saved += 1
                            print(f"You have saved {boys_saved} boys from the Labyrinth!\n\n")
                            boys_rescued.append("Boy 1")

                            first_time_chamber_one = False

                            first_chamber()
                    
                        else:

                            print("Oh well, maybe next time.\n")
    
                            first_chamber()
                    
                            
                elif choice == "Jagged Rocks" and "Jagged Rocks" in satchel_contents: 

                    print("You bring the Jagged Rock sharply down on the first chain at the floor.\n\n")
                    time.sleep(2)
                    print("The rock works well but you hurt yourself in the process.\n")
                    print("You lose 1 hit point.\n\n")
                    player_hp_dmg -= 1
                        
                    if player_hp_dmg <= 0:

                        dead("You died trying to save that boy. How noble!")

                    print("You manage to break the other three chains with the other Jagged Rocks")
                    print("without too much more pain. But you still take 1 more hit point of damage.\n\n")
                    player_hp_dmg -= 1
                        
                    if player_hp_dmg <= 0:

                        dead("You died freeing that boy. You are a noble person.")
                        
                    print("The boy stands free, looking at you.\n")
                    print("How do I get out of here? I'm sure I'll get chained up again if I can't leave now.\n")
                    
                    choice2 = determine_intent("What item do you use?\n")
                        
                    if choice2 == "Paper and Pen" and "Paper and Pen" in satchel_contents:

                        print("You draw him a map and send him on his way.\n")
                        boys_saved += 1
                        print(f"You have rescued {boys_saved} boys from the Labyrinth!\n\n")
                        boys_rescued.append("Boy 1")

                        first_time_chamber_one = False

                        first_chamber()
                        
                    else:

                        print("Oh well, perhaps next time.\n")

                        first_chamber()
                
                else: 

                    print("Oh well, come back when you can think of something that works.\n")
    
                    first_chamber()
        
            else: 

                print("That's okay. I kind of like this chair anyway. I do miss")
                print("the freedom though. I got used to that before I was tied here.\n")
                time.sleep(2)
                print("It's fine. I'll be fine. Have fun out there.\n")

                first_chamber()

        elif "door" in answer:
        
            came_from = "Chamber"
    
            answer3 = determine_intent("""Which door would you like to take?\n
            
            1. West
            2. Northwest
            3. North
            4. Northeast
            5. East
            6. Southeast
            7. South
            8. Southwest\n""")
        
            if answer3 == "1" or answer3 =="w":

                print("You go through the west leading door and arrive shortly")
                print("at a T-intersection.\n")
            
                sixth_intersection()
        
            elif answer3 == "2" or answer3 == "northwest":

                print("You go through the northwest leading door.")
                print("It leads you down a stone stairway.\n")
            
                seventh_intersection()
        
            elif answer3 == "3" or answer3 == "n":

                print("You go through the north leading door.\n")
            
                twelfth_intersection()
        
            elif answer3 == "4" or answer3 == "northeast":

                print("You go through the northeast leading door.\n")
            
                vendor_room()
        
            elif answer3 == "5" or answer3 == "e":
    
                print("You go through the east leading door and arrive at a four way")
                print("intersection.\n")
            
                eighth_intersection()
        
            elif answer3 == "6" or answer3 == "southeast":

                print("You go through the southeast leading door.\n")
            
                third_room()
        
            elif answer3 == "7" or answer3 == "s":

                print("You go through the south leading door and come to a")
                print("T-intersection.\n")
            
                fourth_intersection()
        
            elif answer3 == "8" or answer3 == "southwest":

                print("You go through the southwest leading door and walk down some")
                print("stone steps.\n")
            
                third_intersection()
        
        else: 

            print("You're still in the chamber.\n")
            
            first_chamber()


def fourth_intersection():

    global came_from, player_hp_dmg
    
    print("You are at a mossy intersection that branches West, East, and North.\n")
    print(f"You came from the {came_from!s}.\n")
    
    answer = determine_intent("Which way do you choose to go?\n")
    
    if answer == "w":

        print("You head west and...\n")
        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        came_from = "East"
        
        second_room()
    
    elif answer == "e":

        print("You head east and...\n")
        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        came_from = "West"
        
        fifth_intersection()
    
    elif answer == "n": 

        print("You head north and...\n")
        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        came_from = "South"
        
        first_chamber()
        
    elif answer == "s":

        print("You run into the southern wall and hurt your head.\n")
        player_hp_dmg -= 1

        if player_hp_dmg <= 0:

            dead("You died on impact. When you impacted the wall, you died.")
                
        print(f"You lose 1 hit point. You now have {player_hp_dmg} hit points.")
        
    else: 

        print("i d o n o t k n o w")

        first_chamber()


def fifth_intersection():
    
    global came_from, player_hp_dmg, boys_saved, boys_rescued, rope_ready, satchel_contents, book_of_knots
    
    print("You are at an intersection that branches West and East.")
    print("There is a branch to the South whose end is visible.\n")
    print("Do you go East or West or South?\n")
    print(f"You came from the {came_from!s}.\n")
    
    answer = determine_intent("Which way do you choose to go?\n")
        
    if answer == "s":

        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()

        print("You walk to the small dead end. In the floor, centered a few feet")
        print("from the back wall, stands a small pedestal with a circular, indented top.\n")
        time.sleep(2)
        choice = determine_intent("What item do you use?")
        
        if choice == "Big Medallion" and "Big Medallion" in satchel_contents:

            if "Boy 5" in boys_rescued:

                print("You insert your Big Medallion into the top of the pedestal,")
                print("and the whole unit raises up a couple inches.\n\n")
                time.sleep(2)
                print("A panel of wall to the West opens up, revealing an empty")
                print("chamber.\n\n")

                time.sleep(2)
                print("Done here, you head back to the intersection.\n\n")
                
                came_from = "South"

                fifth_intersection()
                
            else: 

                print("You insert your Big Medallion into the top of the pedestal,")
                print("and the whole unit raises up a couple inches.\n\n")
                time.sleep(2)
                print("A panel of wall to the West opens up, revealing a chamber.\n")
                time.sleep(2)
                print("Inside the chamber is a boy, who is tracing his finger along")
                print("the stone wall and humming a sweet tune to himself.\n")
                time.sleep(1)
                print("He notices you, and seems to be oddly disinterested.\n")
                print("You mention his Mom and he comes to his senses.\n")
                print("You know my Mom? Well, I can't find my way out of here anyway, so whatever.\n")
                choice2 = determine_intent("What item do you use?")
                
                if choice2 == "Paper and Pen" and "Paper and Pen" in satchel_contents:

                    print("You take out your Paper and Pen and draw the lad a map.\n\n")
                    print("He's thrilled that he has something new to look at and")
                    print("takes the map and leaves.\n")
                    boys_saved += 1
                    print("You have saved {boys_saved} boys!\n\n")
                    boys_rescued.append("Boy 5")
                    print("Done here, you head back to the intersection.\n")
                    
                    came_from = "South"

                    fifth_intersection()
                
                else:

                    print("He's just going to hang out here until you figure something out.\n\n")
                    
                    came_from = "South"

                    fifth_intersection()
        
        else: 

            print("That didn't do anything.\n")
            print("At a loss for what to do, you move back to the intersection.\n\n")
            
            came_from = "South"
        
            fifth_intersection()
    
    elif answer == "e": 

        print("You go east and abruptly come upon the edge of a pit.\n") 
        time.sleep(2)
        print("You can see the other side, though it is quite a distance.") 
        print("There is tree trunk punched through the labryinth wall,")
        print("extending up into the darkness, between the path you stand on")
        print("and the path across the pit.\n")
        time.sleep(2)
        came_from = "East"

        to_do = determine_intent("What item do you use?\n")
        
        if to_do == "Long Rope" and "Long Rope" in satchel_contents:

            print("You pull out your Long Rope and set it at your feet.")
            time.sleep(1)
            
            to_do_2 = determine_intent("Now what item do you use?\n")
            
            if to_do_2 == "Book of Knots" and "Book of Knots" in satchel_contents:

                print("You pull out your Book of Knots and read.\n\n")
                time.sleep(2)
                print("You learn a knot that can tie the end of your rope to an object")
                print("to create a sort of small grappling hook.\n\n")
                book_of_knots = True
                
                to_do_3 = determine_intent("What item do you use?\n")
                
                if to_do_3 == "Spade" and "Spade" in satchel_contents:

                    print("You attach the Spade to the end of the Long Rope")
                    print("using your newfound knowledge of knots.\n\n")
                    time.sleep(2)
                    print("Using the makeshift grappling hook, you whip it around")
                    print("several times and fling it over the trunk of the fallen")
                    print("tree.\n\n")
                    time.sleep(2)
                    print("It wraps around the trunk and the rope luckily pins the")
                    print("Spade head.\n")
                    print("Your rope is secure around the trunk of the tree.")
                    
                    choice = determine_intent("Do you swing across the pit?\n")
                    
                    if choice == "y":

                        print("You swing across the gaping pit like an awkward Tarzan.\n\n")
                        time.sleep(2)
                        print("You land safely on the other side and are able to secure")
                        print("the rope end to a rare sconce on the wall.\n\n")
                        print("ahead of you, the passageway opens up to a room.\n")

                        satchel_contents.remove("Spade")
                        satchel_contents.remove("Long Rope")

                        treasure_room()
                    
                    elif choice == "n":

                        print("All that work and not gonna jump, eh?\n\n")
                        print("Well, to each their own.\n")
                        time.sleep(1)
                        print("You secure the end of the rope to a jut in the wall")
                        print("as to not disrupt the rope's lucky attachment.\n\n")

                        satchel_contents.remove("Spade")
                        satchel_contents.remove("Long Rope")

                        rope_ready = True
                    
                    else: 

                        print("You secure the end of the rope to a jut in the wall")
                        print("as to not disrupt the rope's lucky attachment.\n\n") 

                        satchel_contents.remove("Spade")
                        satchel_contents.remove("Long Rope")    

                        rope_ready = True   
                        
                else:

                    print("Certainly you will think of something to attach to the")
                    print("end of the rope.\n\n")

                    fifth_intersection()
            
            else: 
                
                print("It may be difficult to use another item without further")
                print("understanding what you are capable of...\n\n")
                time.sleep(2)
                print("ABL. Always be learning.\n")

                came_from = "South"

                fifth_intersection()
        
        else: 

            print("Come back when you can think of something that may be useful.\n")        

            came_from = "South"

            fifth_intersection()
            
    elif answer == "w":

        print("You head West and...\n")
        came_from = "West"

        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()

        print("...you come to another intersection.\n")

        fourth_intersection()
        
    elif answer == "n":
        
        print("You ran yo head into the concrete wall.\n")
        player_hp_dmg -= 1
        print(f"You lost a hit point! you now have {player_hp_dmg} hit points.\n")

        if player_hp_dmg <= 0:

                dead("You died on impact. When you bumped the wall, you died.")

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        fifth_intersection()
    
    else: 

        print("should    no     printing")

        fifth_intersection()


def sixth_intersection():

    global came_from
    
    print("You can see that both the North and the South paths turn a")
    print("corner heading in the same direction. You can go North, South, or East.\n")
    print(f"You came from {came_from!s}.\n")
    
    answer = determine_intent("Which way do you choose to go?\n")
    
    if answer == "s":

        print("You head South, turning the corner to the West.\n" )
        time.sleep(2)
        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()

        print("You walk along a narrow corridor until you reach an elbow heading")
        print("North. Now you walk and stop between two walls.\n")
        time.sleep(2)
        print("On your left the wall is blank. On the right there are three")
        print("protruding circles.\n")
            
        answer1 = determine_intent("You can go North or South or examine the wall.\n")
        
        if answer1 == "examine":

            print("Looking more closely, you see that the circles move.")
            answer2 = determine_intent("Which item would you like to use?\n")
                
            if answer2 == "Roll of String" and "Roll of String" in satchel_contents:
                
                hidden_chamber_one()
                
            elif answer2 in satchel_contents: 
                    
                print("That items has no effect here.\n\n")

                sixth_intersection()
                
            else: 

                print("You find yourself dumbfounded, and move on.\n\n")

                sixth_intersection()
        
        elif answer1 == "s": 

            print("You go South.\n")
            
            sixth_intersection()
        
        elif answer1 == "n":

            print("You go North.\n")
            
            sixth_intersection()
            
        else: 

            print("DO not KNOW.")

            sixth_intersection()
            
    elif answer == "n": 
        
        print("You head North, turning the corner to the West.\n" )
        time.sleep(2)

        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()

        print("You walk along a narrow corridor until you reach an elbow heading")
        print("South. Now you walk and stop between two walls.\n")
        time.sleep(2)
        print("On your right the wall is blank. On the left there are three")
        print("protruding circles.\n")

        answer1 = determine_intent("You can go North or South or examine the wall.\n")
        
        if answer1 == "examine":

            print("Looking more closely, you see that the circles move.\n")

            answer2 = determine_intent("Which item would you like to use?\n")
                
            if answer2 == "Roll of String" and "Roll of String" in satchel_contents:
                
                hidden_chamber_one()
                
            elif answer2 in satchel_contents: 
                    
                print("That items has no effect here.\n\n")

                sixth_intersection()
                
            else: 

                print("You find yourself dumbfounded, and move on.\n\n")

                sixth_intersection()
                
        elif answer1 == "s": 

            print("You go South.\n")
            came_from = "South"

            chance = randint(1, 100)

            if chance <= 50:

                enemy_encounter()
                
            sixth_intersection()
        
        elif answer1 == "n":

            print("You go North.\n")
            came_from = "North"

            chance = randint(1, 100)

            if chance <= 50:

                enemy_encounter()
                
            sixth_intersection()
        
        elif answer1 == "e" or answer1 == "w":

            print("Instead, you walk into the wall. Ouch!\n")
            player_hp_dmg -= 1

            if player_hp_dmg <= 0:

                dead("Oof. What a way to die. Running into a wall... Darwin award for sure.")
        
            print(f"You lost a hit point! you now have {player_hp_dmg} hit points.\n")

            chance = randint(1, 100)
        
            if chance <= 50:

                enemy_encounter()
                
            print("You walk back to the South and reach a familiar intersection.\n")

            sixth_intersection()
        
        else: 

            print("dunno why printing")

            sixth_intersection()
            
    else: 

        first_chamber()


def seventh_intersection():

    global came_from, book_of_knots
    
    print("You come to a three-way intersection.")
    print("The paths go West or North or Southeast up the stairs.\n")
    print(f"You came from the {came_from!s}.\n")
    
    answer = determine_intent("Which way do you go? West, North, or South?\n")
    
    if answer == "w": 

        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()

        print("You head West and shortly come to a dead end. It's different than")
        print("a normal dead end, because the top of the wall at this dead end")
        print("is much shorter than the walls surrounding it.\n")
        time.sleep(3)
        
        to_do = determine_intent("What do you use?\n")
        
        if to_do == "Short Rope" and "Short Rope" in satchel_contents:

            print("You swing one end of the short rope over the wall")
            print("and it slips back to you.\n\n")
            print("If only the end of the rope had something attached to it.\n")
            
            to_do_2 = determine_intent("What do you use now?\n")
            
            if to_do_2 == "Book of Knots" and "Book of Knots" in satchel_contents:

                print("You pull out your Book of Knots and read.\n\n")
                time.sleep(2)
                print("You learn a knot that can tie the end of your rope to an object")
                print("to create a sort of large grappling hook.\n\n")
                book_of_knots = True
                
                to_do_3 = determine_intent("What item would you like to attach to the rope?\n")
                
                if to_do_3 == "Shovel" and "Shovel" in satchel_contents:

                    print("You attach your shovel to the end of the Short Rope")
                    print("and heave it over the top of the wall.\n\n")
                    time.sleep(2)
                    print("You feel it hold on the other side of the wall and you")
                    print("test the weight of it.\n")
                    time.sleep(2)
                    print("It seems secure.\n")
                    print("You climb up and over the short wall, making sure to")
                    print("bring your rope with you to the other side.\n\n")

                    secret_room_2()
                    
                elif to_do_3 == "Balanced Pickaxe" and "Balanced Pickaxe" in satchel_contents:

                    print("You attach your Balanced Pickaxe to the end of the Short Rope")
                    print("and heave it over the top of the wall.\n\n")
                    time.sleep(2)
                    print("You feel it hold on the other side of the wall and you")
                    print("test the weight of it.\n")
                    time.sleep(2)
                    print("It is definitely secure.\n")
                    print("You climb up and over the short wall, making sure to")
                    print("bring your rope with you to the other side.\n\n")

                    secret_room_2()
                
                else: 

                    print("Perhaps one day you will think of something that could be used.\n\n")
                    came_from = "West"

                    seventh_intersection()
                
            elif book_of_knots:

                if to_do_2 == "Shovel" and "Shovel" in satchel_contents:

                    print("You attach your shovel to the end of the Short Rope")
                    print("and heave it over the top of the wall.\n\n")
                    time.sleep(2)
                    print("You feel it hold on the other side of the wall and you")
                    print("test the weight of it.\n")
                    time.sleep(2)
                    print("It seems secure.\n")
                    print("You climb up and over the short wall, making sure to")
                    print("bring your rope with you to the other side.\n\n")

                    secret_room_2()
                
                elif to_do_2 == "Balanced Pickaxe" and "Balanced Pickaxe" in satchel_contents:

                    print("You attach your Balanced Pickaxe to the end of the Short Rope")
                    print("and heave it over the top of the wall.\n\n")
                    time.sleep(2)
                    print("You feel it hold on the other side of the wall and you")
                    print("test the weight of it.\n")
                    time.sleep(2)
                    print("It is definitely secure.\n")
                    print("You climb up and over the short wall, making sure to")
                    print("bring your rope with you to the other side.\n\n")

                    secret_room_2()

                else:

                    print("Perhaps you will have an idea of what to use later.")

                    seventh_intersection()
                
            else: 

                print("Perhaps one day you will think of something that could be used.\n\n")
                came_from = "West"

                seventh_intersection()
                
        else:

            print("Maybe some other idea will come to you in the future.\n\n")
            came_from = "West"

            seventh_intersection()
    
    elif answer == "n":

        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()

        print("You head North and come to another intersection.\n")
        came_from = "South"

        eleventh_intersection()
    
    elif answer == "s" or answer == "e":

        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()

        print("You head up the stairs to the Southeast.\n")
        came_from = "Northwest"

        first_chamber()
        
    else:

        print("Shouldn't see me, ever.")

        first_chamber()


def eighth_intersection():

    global came_from, gold, found_treasure1
    
    print("You stand in a four-way intersection.")
    print("You can go North, South, East, or West.\n")
    print(f"You came from the {came_from!s}.\n")
    
    answer = determine_intent("Which way do you go?\n")
    
    if answer == "n":

        print("You head North.\n")
        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()

        print("You've come to another intersection.\n")

        came_from = "South"
        
        ninth_intersection()
    
    elif answer == "s":

        print("You head South.\n")

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        print("The corridor turns an elbow to the east.\n")
        time.sleep(2)

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        print("The corridor ends at an ornately carved wall.\n")
        time.sleep(1)
        print("Its intricacy is somehow familiar and your focus centers")
        print("on a circular form.\n")

        answer = determine_intent("Which item will you use?")
        
        if answer == "Intricate Medallion" and "Intricate Medallion" in satchel_contents: 
            
            time.sleep(2)
            print("A low rumble shakes the floor. The wall sucks in an inch and")
            print("abruptly splits at the horizontal center.\n\n")
            door_graphic(" ", 1)
            door_graphic("\n", 2)
            door_graphic("\n\n\n", 3)
            door_graphic("\n\n\n\n\n", 4)
            door_graphic("\n\n\n\n\n\n\n", 5)
            door_graphic("\n\n\n\n\n\n\n\n\n", 6)
            door_graphic("\n\n\n\n\n\n\n\n\n\n\n", 7)
            door_graphic("\n\n\n\n\n\n\n\n\n\n\n\n\n", 8)

            if not found_treasure1:

                print("You have found incredible treasure!!!\n\n")
                print("You receive 5000 gold!\n")
                gold += 5000
                print(f"You have {gold} gold in your satchel!\nWhat a satchel!!!\n\n")
                found_treasure1 = True
            
            else:

                print("You stand looking at the spot where sweet treasure used to be.\n")
                time.sleep(2)
                print("What memories!\n\n")
            
                came_from = "South"
                print("You head back.")
            
                chance = randint(1, 100)
        
                if chance <= 50:

                    enemy_encounter()
            
                eighth_intersection()

        print("You decide to head back the way you came.")      

        came_from = "South"
        
        eighth_intersection()
    
    elif answer == "e":

        print("You head East and enter a long room.\n")

        enemy_encounter()
        
        fourth_room()
    
    elif answer == "w":

        print("You head West.\n")
        
        first_chamber()
        
    else:

        print("should not be printing this.")

        first_chamber()

        
def door_graphic(openness, topbottom):
    
    dr_wid = 20
    sml_sym = 10
    md_sym = 6
    big_sym = 5
    
    print("\n\n")
    print(" " + "_" * dr_wid)
    print("|" + " " * dr_wid + "|")
    print("|" + "_" * dr_wid + "|")

    if topbottom <= 1: 

        print("|" + "<>" * sml_sym + "|")

    if topbottom <= 2:

        print("|" + "<>" * sml_sym + "|")

    if topbottom <= 3:

        print("|" + "-" + "<->" * md_sym + "-" + "|")

    if topbottom <= 4:

        print("|" + "-" + "<->" * md_sym + "-" + "|")

    if topbottom <= 5:

        print("|" + "~" * dr_wid + "|")

    if topbottom <= 6: 

        print("|" + "}{}{" * big_sym + "|")

    if topbottom <= 7:

        print("|" + "}{}{" * big_sym + "|")
    
    if topbottom <= 8:

        print("|" + "~" * dr_wid + "|")
        print("|" + "}{}{" * big_sym + "|")
        print("|" + "}{}{" * big_sym + "|")
        print("|" + "~" * dr_wid + "|")
        print("|" + "-" * 8 + "(" + "=" + ")" + "-" * 9 + "|")
        print("|" + "-" * 7 + "(" + "---" + ")" + "-" * 8 + "|")
        print("|" + "_" * dr_wid + "|")

    if openness != " ":

        print(openness)
        
    print(" " + "_" * dr_wid)
    print("|" + "-" * 7 + "(" + "---" + ")" + "-" * 8 + "|")
    print("|" + "-" * 8 + "(" + "=" + ")" + "-" * 9 + "|")
    print("|" + "~" * dr_wid + "|")
    print("|" + "}{}{" * big_sym + "|")
    print("|" + "}{}{" * big_sym + "|")

    if topbottom <= 8:

        print("|" + "~" * dr_wid + "|")

    if topbottom <= 7:

        print("|" + "}{}{" * big_sym + "|")

    if topbottom <= 6:

        print("|" + "}{}{" * big_sym + "|")

    if topbottom <= 5:

        print("|" + "~" * dr_wid + "|")

    if topbottom <= 4:

        print("|" + "-" + "<->" * md_sym + "-" + "|")

    if topbottom <= 3:

        print("|" + "-" + "<->" * md_sym + "-" + "|")

    if topbottom <= 2:

        print ("|" + "<>" * sml_sym + "|")

    if topbottom <= 1:

        print ("|" + "<>" * sml_sym + "|")
        print ("|" + "_" * dr_wid + "|")
        print ("|" + " " * dr_wid + "|")    
        print ("|" + "_" * dr_wid + "|")
    
        time.sleep(1)


def ninth_intersection():

    global came_from
    
    print("You stand at a three-way intersection.")
    print("You can go North, South, or East.\n")
    print(f"You came from the {came_from!s}.\n")
    
    answer = determine_intent("Which way do you go?\n")
    
    if answer == "e":

        print("You head East and immediately the corridor takes you South.\n")
        print("You come to a dead end with a portrait hanging on the wall.\n")
        time.sleep(2)
        print("The portrait is of the old woman you saw at the beginning of")
        print("the labryinth.\n")
        print("A quick search yields nothing of note, so you go back.\n")
        came_from = "East"
        
        ninth_intersection()
    
    elif answer == "n":

        print("You head North.\n")
        came_from = "South"
        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()

        print("You find yourself at the back entrance of a Grand Hallway.\n")
        
        grand_hallway()
    
    elif answer == "s":

        print("You head South.\n")
        came_from = "North"

        chance = randint(1, 100)

        if chance <= 50:

            enemy_encounter()
        
        eighth_intersection()
        
    else: 

        print("You put your head down and lunge forward into the western wall.\n")

        player_hp_dmg -= 1

        if player_hp_dmg <= 0:

            dead("Not a good idea! As it turns out, that was a killing blow.")

        print(f"You lost a hit point! you now have {player_hp_dmg} hit points.\n")

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
            
        ninth_intersection()
        
# incomplete def tenth_intersection():


def eleventh_intersection():
    
    global came_from, player_hp_dmg
    
    print("You stand at an intersection that leads North, East, or South.\n")
    print(f"You came from the {came_from!s}.\n")
    
    answer = determine_intent("Which way do you go?\n")
    
    if answer == "n":

        print("You approach the mouth of a cave!\n")

        answer1 = determine_intent("Do you go into the cave?\n")
        
        if answer1 == "y":

            came_from = "South"

            battle_cave()
        
        else: 

            print("Better not...")

            eleventh_intersection()
    
    elif answer == "e": 

        print("You head East along a long corridor.\n")
        time.sleep(2)
        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()

        print("You come to a large intersection.\n")
        came_from = "West"
        
        twelfth_intersection()
    
    elif answer == "s":

        print("You head South.\n")
        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()

        came_from = "North"
        
        seventh_intersection()
    
    else: 

        print("You walk directly into the western wall.\n")
        player_hp_dmg -= 1

        if player_hp_dmg <= 0:

            dead("Watch that first step. Turns out it was deadly for you.")

        print(f"You lost a hit point! you now have {player_hp_dmg} hit points.\n")

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
            
        seventh_intersection()

    
def twelfth_intersection():

    global came_from
    
    print("The large intersection holds an immense Grand Hallway to the East.\n")
    print("You may go East to the hallway or North or South or West.\n")
    print(f"You came from the {came_from!s}.")
    chance = randint(1, 100)
    
    if chance <= 50:

        enemy_encounter()
    
    answer = determine_intent("Which way do you go?\n")
    
    if answer == "e":

        print("You find yourself in the Grand Hallway.\n")
        chance = randint(1, 100)
        
        if chance <= 80:

            enemy_encounter()
        
        grand_hallway()
    
    elif answer == "s":

        print("You head South.\n")
        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()

        came_from = "North"
        
        first_chamber()
    
    elif answer == "w":

        print("You head West.\n")
        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()

        came_from = "East"
        
        eleventh_intersection()
    
    elif answer == "n":

        print("That part of the labryinth hasn't been coded yet.\n\n")
        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        twelfth_intersection()  
        
    else:

        print("investigate this printing.")

        twelfth_intersection()


def second_room():

    global came_from, defeat_goblin_king
    came_from = "East"
    
    print("You enter a large room, its walls covered in stone carved flowers.\n\n\n")
    print(f"You came from the {came_from!s}.\n")
    
    enemy_encounter()
    
    if defeat_goblin_king == False:

        print("\n\nAn eerie silence falls upon the room after your battle.\n")
        print("There is a plant in a pot on a stone slab in the middle of the room.")
        print("Beside this pot is another pot, though empty.\n")
        print("On the ground, there is a container of what looks like fresh potting soil.\n")
    
        answer = determine_intent("""What do you do?\n
            \t1. Use an item.
            \t2. Take the empty pot.
            \t3. Take the potted plant.
            \t4. Put the new soil in the empty pot with your hands and re-pot the plant.
            \t5. Do nothing and leave the room.\n""")
        
        if answer == "1":
        
            answer2 = determine_intent("Which item would you like to use?\n")
        
            if answer2 in satchel_contents:
            
                if answer2 == "Spade":

                    boss_encounter("room2", "Spade")
                    defeat_goblin_king = True
            
                elif answer2 == "Shovel":

                    boss_encounter("room2", "Shovel")
                    defeat_goblin_king = True
            
                elif answer2 == "Balanced Pickaxe":

                    boss_encounter("room2", "Balanced Pickaxe")
                    defeat_goblin_king = True
                
                else: 

                    boss_encounter("room2", answer2)
                    defeat_goblin_king = True
    
        elif answer == "2" or answer == "3":
        
            boss_encounter("room2", "Thief")
            defeat_goblin_king = True
        
        elif answer == "4":
        
            boss_encounter("room2", "Hands")
            defeat_goblin_king = True
    
        else:
        
            print("You back away slowly, touching nothing.\n")
    
            print("You exit the room and come to an intersection.\n")
    
            came_from = "West"
    
            fourth_intersection()
    
    else: 

        print("The room looks just like you left it, and will forevermore...")
        print("since you've destroyed The Goblin King.\n\n")
        came_from = "West"
        
        fourth_intersection()


def third_room():
    
    global came_from, first_time_third_room
    
    print("The door you took leads directly into a small room.")
    print(f"You came from the {came_from!s}.\n")
    
    enemy_encounter()
    
    print("There is some sweet art in this room. Dang. Good stuff.\n")
    time.sleep(2)
    print("You head back to the chamber.")
    
    came_from = "Southeast"
    
    first_chamber()


def fourth_room():
    
    print("In the fourth room.\n")
    time.sleep(2)
    print("Now leaving. Room incomplete.\n")
    
    eighth_intersection()

    
def secret_room_2():
    
    global came_from, gold
    
    print("You drop down from the wall and are in a well lit parlour.\n\n")
    print("There is a lady with a clear green visor sitting at a table, shuffling cards.\n")
    print("As you approach her, she looks up and smiles.\n")

    answer = determine_input("Want to play a guessing game?\n")
    
    if answer == "y":

        print("Well, let's play, then!\n")
        guessGame()
        play = input("Want to play?  y/n?")

    
        while play == "y":

            print("Great, let's play!\n")
            guessGame()

            play = input("want to play again? y/n?\n")

        print("Thanks for playing! I'm sure I'll see you later.\n")
        print("You sling your makeshift grappling hook over the wall")
        print("and climb up and out.\n\n")

        came_from = "Secret Room"

        seventh_intersection()
        
    else:

        print("Oh well. That's okay. Gambling is probably not wise.\n")
        print("Best luck in your adventures.\n\n")
        print("You sling your makeshift grappling hook over the wall")
        print("and climb up and out.\n\n")

        came_from = "Secret Room"

        seventh_intersection()

    
def treasure_room():
    
    global came_from
    
    print("You have found your way to the TREASURE ROOM.\n\n")
    print("Unfortunately, it hasn't been coded yet.")
    came_from = "Treasure Room"
    print("You swing back over the pit and secure your rope again so you")
    print("can come back when the treasure room is programmed.\n\n")
    
    fifth_intersection()

        
def vendor_room():

    global came_from
    
    print("You enter a triangle shaped room.\n")
    print("You see an old man sitting behind a wooden shelf in the far corner of")
    print("the room. He's chiseling at a rock.\n")
    time.sleep(1)

    answer = determine_intent("Would you like to talk to him?")
    
    if answer == "y": 
    
        print("You step forward to talk to him.\n")
        vendor()

        came_from = "Northeast"

        first_chamber()
    
    else:

        print("You go back to the Chamber.\n")
        came_from = "Northeast"

        first_chamber()

    
def vendor():
    
    global satchel_contents, player_hp_dmg, gold
    
    trading_block = []
    use = "blank"
    loot = "blank"
    count = 0
    item_loc = 0
    
    print("The vendor looks up from his chiseling and looks you in the eye.\n")
    time.sleep(1)
    print("Vendor: It's been a long time since I've seen a stranger.")
    print("What can I help you with?\n")
    
    selection = determine_intent("1. Trade \t2. Sell \t3. Heal \t4. Enemies \t5. Items\n")
    
    if selection == "1" or selection == "trade":
        
        if satchel_contents == []:
            
            print("It looks like your satchel is empty. What are you trying to pull?\n")

            vendor_room()
        
        trade = determine_intent("What would you like to trade?\n")
        
        if trade in satchel_contents:

            for item in satchel_contents:

                if item == trade:

                    trading_block.append(satchel_contents[count])
                    item_loc = count
                    count += 1
            
                    print(f"Ahh, you have a {trading_block[0]}.")
                    print("I have this to trade:\n")

                    if 0 < player_lvl < 4:

                        print("***Thick Shirt***\n")
                        loot = "Thick Shirt"
                        use = "+1 Defense"

                    elif 3 < player_lvl < 7:

                        print("***Leather T-Shirt***\n")
                        loot = "Leather T-Shirt"
                        use = "+2 Defense"

                    elif 6 < player_lvl:

                        print("***Leather Jacket***\n")
                        loot = "Leather Jacket"
                        use = "+3 Defense"
                        time.sleep(2)
        
                    answer = determine_intent("Would you like to trade? Straight up? Mine for yours?\n")
            
                    if answer == "y":
            
                        print("Ok, good deal!")
                        satchel_contents.pop(item_loc)
                        satchel_contents.append(loot)
            
                        print("This is what is in your satchel now:")

                        for item in satchel_contents:

                            print(item + " ")

                    else:

                        print("I didn't really want to either. FINE. Now go away, I am busy.")

                        vendor_room()
            
                else: 

                    print("I do not think you know what you are referring to.\n") 
                    vendor_room()
    
    elif selection == "2":
        
        if satchel_contents == []:
            
            print("It looks like your satchel is empty. What are you trying to pull?\n")
            vendor_room()
        
        print("What would you like to sell?")

        trade = determine_intent("What would you like to sell?\n")
        
        if trade in satchel_contents:

            for item in satchel_contents:

                if item == trade:

                    trading_block.append(satchel_contents[count])
                    item_loc = count
                    count += 1
        
                    print(f"Ahh, you have a {trading_block[0]}.")

                    choice2 = determine_intent(f"I will give you 50 gold for the {trading_block[0]}, okay?\n")
        
                    if choice2 == "y":
            
                        print("Great!\n")

                        if trade in satchel_contents:
                    
                            satchel_contents.pop(item_loc)
                            print("You received 50 gold!\n")
                            gold += 50
                            print(f"You have {gold} gold now.")
        
                    else: 
            
                        print("Fine. I didn't want it anyway.\n")
                        vendor_room()
        
                else:

                    print("You do not have that item.\n")
        
    elif selection == "3": 
        
        print("You want me to heal yah, huh?")
        time.sleep(1)
        print("There was a time I was known as a healer.\n")
        print(f"I see that you currently have {player_hp_dmg} hit points.")
        print(f"That is {player_hp - player_hp_dmg} less than your maximum!\n")
        
        if player_hp_dmg <= 2:

            print("I can hardly believe you're still alive.\n")
        
        print("\nI s'pose I could do that. For a price.")
        time.sleep(2)
        print("It'll cost you a rare gem to heal yourself.\n\n")
        print("I know that's a valuable item, but they're probably just laying around somewhere to find.")

        if satchel_contents == []:
            
            print("It looks like you don't have any gems. See ya.\n")
            vendor_room()
        
            choice = determine_intent("Which gem do you want to give me in exchange for full health?\n")
        
            if "uby" in choice: 
                
                if "Ruby" in satchel_contents:
                
                    satchel_contents.remove("Ruby")
                    print("Okay, looks good. I took your Ruby.\n")
                    time.sleep(2)
                    print("I will now perform a miracle of healing!!")
                    time.sleep(4)
                    print("\n\nYou have been healed!")

                    player_hp_dmg = player_hp

                    print(f"You now have {player_hp_dmg} hit points.\n")
                    vendor_room()
                    
                else: 

                    print("You don't have a Ruby.\n")
                    vendor_room()
                
            elif "hire" in choice:
            
                if "Sapphire" in satchel_contents:
                
                    satchel_contents.remove("Sapphire")
                    print("Okay, looks good. I took your Sapphire.\n")
                    time.sleep(2)
                    print("I will now perform a miracle of healing!!")
                    time.sleep(4)
                    print("\n\nYou have been healed!")
                    player_hp_dmg = player_hp
                    print(f"You now have {player_hp_dmg} hit points.\n")
                    vendor_room()
                    
            else: 

                print("You don't have a Sapphire.\n")
                vendor_room()
            
        else: 

            print("I'm glad, tbh. It means I can conserve my energy.\n\n")
            vendor_room()   
            
    elif selection == "4":
        
        print("You want to learn about the enemies of this dungeon, do yah?\n")
        print("Well, because we're in a beta version, I can do that for you." )
        print_enemies_full()
        time.sleep(4)
        vendor_room()
        
    else: 
        
        answer = determine_intent("What item would you like to learn about?\n")
            
        if answer == "list all items":
            
            print_items_full()
            time.sleep(4)
            vendor_room()
        
        elif answer in satchel_contents:
            
            print(f"Ah, yes, the {answer!s}!\n")
            time.sleep(2)
            print(f"As far as I'm aware, this is what the {answer!s} does:\n")
            print(loot_dict[answer])

            vendor_room()
        
        else:
            
            print("I don't know what you're talking about.\n")

            vendor_room()

    
def battle_cave():
    
    global came_from, battle_cave_furthest, battle_cave_there_and_back, high_scorer_bcf
    global high_scorer_bctb, high_scorer_cave, high_scorer_furthest, boys_rescued, boys_saved
    
    count = 0
    battle_cave_count = 0
    boy_three = False
    
    print("You enter the cave.\n")
    print("It stinks like death and you hear living sounds beyond the darkness.\n")
    print("You can only see about five feet in front of you.\n\n\n")
    
    answer = determine_intent("Do you go forward?\n")
    
    while answer == "y":

        print("You move forward.\n")
        enemy_encounter()
        count += 1
        battle_cave_count += 1
        
        if battle_cave_count > battle_cave_furthest and high_scorer_furthest == False:
                
            high_scorer_furthest = True
            print("You have gone the furthest of any Battle Cave Explorer!\n")
            battle_cave_furthest = battle_cave_count
            high_scorer_bcf = input("Enter your name so it can rest atop the leaderboard: ")


        if battle_cave_count > battle_cave_furthest:

            battle_cave_furthest = battle_cave_count
        
        if count == 20 and "Boy 3" not in boys_rescued:

            print("You have come across one of the Old Woman's Sons!\n")
            choice = determine_intent("Would you like to bring him back with you?\n")

            if choice == "y":

                boy_three = True
                print("Okay, he'll stick close, but won't jump into the fighting.\n\n")

            else:

                print("Oh, well. Maybe next time.\n\n")
        
        answer = determine_intent("Do you go forward?\n")
    
    while count > 0:

        print("You move back toward the entrance.\n")
        enemy_encounter()
        count -= 1
        battle_cave_count += 1
    
        if boy_three and count == 0:

            print("You've brought the boy back to the entrance of the cave.\n")
            print("He's tired of sticking with you and wants to get out.\n\n")
            time.sleep(2)
            choice = determine_intent("Which item do you use?\n")
        
            if choice == "Paper and Pen" and "Paper and Pen" in satchel_contents:

                print("You draw him a map and he heads home to the entrance.")
                boys_saved += 1
                print(f"You have saved {boys_saved} boys.\n\n")
                boys_rescued.append("Boy 3")

            else: 

                print("You tell him you'll be back for him.\n")
                print("You can tell he's listening, but there's something about his mannerisms")
                print("that let you know that he may go wandering back into the cave.\n\n")
        
    came_from = "The Cave"

    if battle_cave_count > battle_cave_there_and_back:
                
        print("You have survived the longest trip into the Battle Cave!\n")
        battle_cave_there_and_back = battle_cave_count  
        high_scorer_bctb = input("Enter your name so it can rest atop the leaderboard: ")
        print("\n\n")

    eleventh_intersection()



# incomplete ritual_room()



def grand_hallway():
    
    global came_from, player_hp_dmg
    
    print("There are stone carved pillars lining the North and South walls.\n")
    print("It looks like a room long past used for banquets and merriment.\n")
    time.sleep(2)
    print("Empty now, a breeze sweeps through the room coming from the South.\n")
    print("There is an exit to the Southeast beyond the farthest pillar.\n")
    print("You can walk to intersection on the Western end of the Hallway")
    print("Or exit the Hallway to the Southeast. So West or Southeast?")
    print(f"You came from the {came_from!s}.\n")
    
    answer = determine_intent("Which way do you go?\n")
    
    if answer == "w":

        print("You move to the Hallway's entrance.\n")
        came_from = "Hallway"
        
        twelfth_intersection()
        
    elif answer == "s" or answer == "southeast":

        print("You walk to the end of the Grand Hallway and exit to the South.\n")
        came_from = "North"
        
        ninth_intersection()
    
    elif answer == "e":

        print("You ran your head into the eastern wall.\n")
        player_hp_dmg -= 1

        if player_hp_dmg <= 0:

            dead("The head wound was serious. So serious... you DIED!")

        print(f"You lost a hit point! you now have {player_hp_dmg} hit points.\n")

        chance = randint(1, 100)
        
        if chance <= 50:

            enemy_encounter()
        
        grand_hallway()
    
    else:

        print("You check out the Northern wall and find nothing of note.\n")
        came_from = "Hallway"
        
        grand_hallway()

        
def hidden_chamber_one():
    
    global came_from, boys_rescued, satchel_contents, defense_mod, boys_saved, attack_mod 
    global defeat_darkness_troll, player_hp, player_hp_dmg
    
    came_from = "Hidden Chamber"
    
    if defeat_darkness_troll == True:

        print("\nYou unravel the string and wind it between the three wheels.\n\n")
        time.sleep(2)
        print("After some testing of the tension, you pull the string hard and the wheels spin.\n")
        time.sleep(1)
        print("The panel of wall in front of your falls away from you and down to the ground!\n\n")
        print("The sound is thunderous!!\n\n")
        
        if "Boy 4" in boys_rescued:

            print("The room is empty.\n")
            print("You turn go south and back to the intersection.\n")
        
        else:  

            print("You notice there is a boy huddled in the corner, who watched you dress.\n\n")
            print("He notices you noticing him and he sorta defers to you, in status.\n")
    
            answer = determine_intent("Do you want to talk to him?\n")
    
            if answer == "y":

                print("You say hello and he jumps up.\n")
                print("Boy: I bet you're here to save me?")
                print("I never thought anyone would come down here to save me.\n\n")

                answer1 = determine_intent("Are you going to save me?\n")
        
                if answer1 == "y":

                    print("How? I don't know the way out.\n")
                    answer2 = determine_intent("Which item would you like to use?\n\n")
            
                    if answer2 == "Paper and Pen" and "Paper and Pen" in satchel_contents:

                        print("You draw the boy a map to the entrance and he leaves, emboldened.\n\n")
                        boys_saved += 1
                        print(f"You have saved {boys_saved} boys!\n\n")
                        boys_rescued.append("Boy 4")
                        print("Finished here, you head back to the hallway, go south, and back to the intersection.\n\n")

                        sixth_intersection()
                        
                    else: 

                        print("Well, I'll wait here until you think of something that works.\n\n")
        
                else: 

                    print("Well, that sucks, but I understand. It's not so bad in here.\n\n")
    
            else: 

                print("That's disappointing. Okay, no worries, I'll be fine. I guess I'll eat this guy.\n\n")
    
        print("You exit the hidden chamber go north back to the intersection.\n")

        sixth_intersection()

    else: 
    
        print("\nYou unravel the string and wind it between the three wheels.\n\n")
        time.sleep(2)
        print("After some testing of the tension, you pull the string hard and the wheels spin.\n")
        time.sleep(1)
        print("The panel of wall in front of your falls away from you and down to the ground!\n\n")
        print("The sound is thunderous!!\n\n")
        print("In the split second you recognize a hulking beast in one corner and a boy in the other...")
        time.sleep(1)
        print("The beast snaps awake from the sound and sees you. The Darkness Troll charges.\n\n")
    
        boss_encounter("hiddenChamber", "none")
    
        defeat_darkness_troll = True

        print("You stand after your bloody battle and look at your foe!\n\n")
        time.sleep(1)
        print("You notice something poking out from his bag.\n\n")
        print("Upon closer inspection...\n")

        if player_class == "Wizard":

            print("It is Wizard Robes of the highest quality!\n")
            time.sleep(2)
            satchel_contents.append("Wizard Robes")
            equippable_loot.append("Wizard Robes")
            wizard_robes = True
            equipped_loot['Body'] = "Wizard Robes"
            print("You put on the Wizard Robes and feel the best you've ever felt.\n\n")

            if wizard_hat and wizard_staff:

                print("You've completed the set!!\n")
                print("Your Wizard Robes now give you a defense bonus of 5!")
                print("Your Wizard Hat adds 3 to your health, permanently!")
                print("Your Wizard Staff now gives you an attack bonus of 5!\n\n")
                defense_mod = 5
                attack_mod = 5
                player_hp += 3
                player_hp_dmg += 3
            
            else:

                print("Your defense bonus is 4!!!")
                defense_mod = 4
        
        elif player_class == "Ninja":

            print("It is an Imbued Eye Mask!\n\n")
            time.sleep(2)
            satchel_contents.append("Imbued Eye Mask")
            equippable_loot.append("Imbued Eye Mask")
            imbued_eye_mask = True
            print("You put on the Imbued Eye Mask and feel the best you've ever felt.\n\n")
            equipped_loot['Head'] = "Imbued Eye Mask"

            if katana and stealth_slippers: 

                print("You've completed the set!!\n")
                print("Your Imbued Eye Mask now gives you a defense of 5!")
                print("Your Stealth Slippers add 3 to your health, permanently!")
                print("Your Katana now gives you an attack bonus of 5!\n\n")
                defense_mod = 5
                attack_mod = 5
                player_hp += 3
                player_hp_dmg += 3
            
            else:

                print("Your defense bonus is 4!")
                defense_mod = 4
        
        else:

            print("It is an Armored Tweed Vest!\n\n")
            time.sleep(2)
            satchel_contents.append("Armored Tweed Vest.")
            equippable_loot.appand("Armored Tweed Vest.")
            armored_tweed_vest = True
            equipped_loot['Body'] = "Armored Tweed Vest"
            print("You put on the Armored Tweed Vest and feel the best you've ever felt.\n\n")

            if scepter and knickers:

                print("You've completed the set!!\n")
                print("Your Armored Tweed Vest now gives you a defense of 5!")
                print("Your Knickers add 3 to your health, permanently!")
                print("Your Scepter now gives you an attack bonus of 5!\n\n")
                defense_mod = 5
                attack_mod = 5
                player_hp += 3
                player_hp_dmg += 3
            
            else:

                print("Your defense bonus is 4!")
                defense_mod = 4             
        
        print("You notice there is a boy huddled in the corner, who watched you dress.\n\n")
        print("He notices you noticing him and he sorta defers to you, in status.\n")
        
        answer = determine_intent("Do you want to talk to him?\n")
        
        if answer == "y":

            print("You say hello and he jumps up.\n")
            print("I bet you're here to save me!?")
            print("I never thought anyone would come down here to save me.\n\n")

            answer1 = determine_intent("Are you going to save me?\n")
            
            if answer1 == "y":

                answer2 = determine_intent("How? I don't know the way out.\n")
                
                if answer2 == "use Paper and Pen" and "Paper and Pen" in satchel_contents:

                    print("You draw the boy a map to the entrance and he leaves, emboldened.\n\n")
                    boys_saved += 1
                    print(f"You have saved {boys_saved} boys!\n\n")
                    boys_rescued.append("Boy 4")
                    print("Finished here, you head back to the hallway, go south, and back to the intersection.\n\n")

                    sixth_intersection()
                
                else: 

                    print("Well, I'll wait here until you think of something that works.\n\n")
            
            else: 

                print("Well, that sucks, but I understand. It's not so bad in here.\n\n")
        
        else: 

            print("That's disappointing. Okay, no worries, I'll be fine. I guess I'll eat this guy.\n\n")

        
    print("You exit the hidden chamber and head back to the intersection.\n")

    sixth_intersection()


def guessGame():

    random_number = random.randrange(1, 50000)
    win = False

    print("This is a guessing game.\n")
    print("I'll think of a number between one and fifty thousand\n",
          "and you have 20 guesses to get it right!\n")
    print("Oh, and I'll let you know if you guess high or low.\n")
    print("Wait! Do you want more detailed hints or less detailed hints?\n")
    difficulty = input("Type \'more\' or \'less\'\n")
    difficulty = difficulty.lower()

    if difficulty != "more" and difficulty != "less":

        print("Well, I don't understand your preference...\n\n",
              "oh well, we'll play anyway, with the more detailed hints.\n")
        difficulty = "more"
        
    if difficulty == "more":

        print("This is the easier difficulty.\n")
        count = 0

        while count < 21 and not win:

            if count == 19:

                print("Last guess! Good luck... \n")

            user_guess = int(input("What's your guess?\n"))
            count += 1
            print("Guess", count)

            if user_guess < 1 or user_guess > 50000:
                print("Your guess is out of range, please play nicer next time.\n")

            if user_guess == 1022:
                print("Your name's not Vanessa is it? LOL.\n")

            if user_guess == random_number:
                print(f"Congratulations!! You win!!\n", "It took you {count} tries.\n")
                win = True

            elif user_guess > random_number:

                if user_guess - random_number < 9:
                    print("You guessed high, and you're SUPER close.\n")

                elif user_guess - random_number < 49:
                    print("You guessed high, and you're very close.\n")

                elif user_guess - random_number < 99:
                    print("You guessed high, and you're close.\n")

                elif user_guess - random_number < 249:
                    print("You guessed high, and you're getting closer.\n")

                elif user_guess - random_number < 499:
                    print("You guessed high, and you're closing in on it.\n")

                elif user_guess - random_number < 999:
                    print("You guessed high, and you're in the ballpark.\n")

                elif user_guess - random_number < 2499:
                    print("You guessed high, and you're in the same city.\n")

                elif user_guess - random_number < 4999:
                    print("You guessed high, and you're getting warmer.\n")

                elif user_guess - random_number < 9999:
                    print("You guessed high, and you're still a ways off.\n")

                elif user_guess - random_number < 14999:
                    print("You guessed high, and you're not close.\n")

                elif user_guess - random_number < 19999:
                    print("You guessed high, and yet you're super cold.\n")

                else:
                    print("You guessed high, and you're basically a million or more off.\n")

            elif user_guess < random_number:

                if random_number - user_guess < 9:
                    print("You guessed low, and you're SUPER close.\n")

                elif random_number - user_guess < 49:
                    print("You guessed low, and you're very close.\n")

                elif random_number - user_guess < 99:
                    print("You guessed low, and you're close.\n")

                elif random_number - user_guess < 249:
                    print("You guessed low, and you're getting closer.\n")

                elif random_number - user_guess < 499:
                    print("You guessed low, and you're closing in on it.\n")

                elif random_number - user_guess < 999:
                    print("You guessed low, and you're in the ballpark.\n")

                elif random_number - user_guess < 2499:
                    print("You guessed low, and you're in the same city.\n")

                elif random_number - user_guess < 4999:
                    print("You guessed low, and you're getting warmer.\n")

                elif random_number - user_guess < 9999:
                    print("You guessed low, and you're still a ways off.\n")

                elif random_number - user_guess < 14999:
                    print("You guessed low, and you're not close.\n")

                elif random_number - user_guess < 19999:
                    print("You guessed low, and you're super cold.\n")

                else:
                    print("You guessed low, and you're like, a million or more off.\n")

        if count == 21:
            print("Too bad, you lost, game over, man, game over.\n")

    else:
        print("Okay, this is the harder difficulty.\n")
        count = 0

        while count < 21 and not win:

            if count == 19:
                print("Last guess! Good luck... \n")

            user_guess = int(input("What's your guess?\n"))
            count += 1         
            print("Guess", count)

            if user_guess < 1 or user_guess > 50000:
                print("Your guess is out of range, please play nicer next time.\n")

            if user_guess == 1022:
                print("Your name's not Vanessa, is it? LOL!\n")

            if user_guess == random_number:
                print("Congratulations!!! You win!!\n")
                print(f"It took you {count} tries to get it.\n")
                win = True

            elif user_guess > random_number:
                print("You guessed high.\n")

            elif user_guess < random_number:
                print("You guessed low.\n")

        if count == 21:
            print("Game over. You lose.", "A loo hoo, ser.\n")

    print("Thanks for playing!\n\n")
    

                
def dead(why):
    
    global player_hp_dmg
    
    print(why)
    
    quandry = determine_intent("test version. Would you like to reload with all yo stats & lvl?\n")
    
    if quandry == "y":
    
        player_hp_dmg = player_hp

        first_intersection()
    
    answer = determine_intent("Would you like to play again?\n")
        
    if answer == "y":

        start()
    
    else: 

        print("Thank you for playing!\n")
        exit(0)

start()
