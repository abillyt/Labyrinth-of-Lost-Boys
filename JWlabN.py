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
player_hp_dmg = 11	# current hit points
player_name = "Unknown"
player_class = "Unknown"
satchel_contents = []
gold = 0
fight_count = 0
fight_count_most = 51
battle_cave_furthest = 18
battle_cave_there_and_back = 36
high_scorer_fcm = "WFTIV"
high_scorer_bcf = "WFTIV"
high_scorer_bctb = "WFTIV"
attack_mod = 0
defense_mod = 0
current_weapon = "blank"

prompt = "-> "

came_from = "Unknown"
first_time_first_room = True
first_time_secret_room = True
first_time_chamber_one = True
first_time_second_room = True
first_time_third_room = True
first_time_2nd_secret_room = True
defeat_goblin_king = False
high_scorer = False
high_scorer_furthest = False
high_scorer_cave = False

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
weapon = False

loot_dict = {'Sturdy Walking Stick': '+1 attack for Ninja or Hybrid', 'Cloth Cap': '+1 int for Wizard', 
'Short Stick': '+1 attack for Wizard or Hybrid', 'Basic Gloves': '+1 dex for all classes', 
'Spade': 'a small, handheld digging instrument', 'Paper and Pen': 'Good for explaining stuff!',
'Thick Shirt': '+1 defense for all classes', 'Roll of String': 'about 100 feet of string',
'Small Medallion': 'a unique pattern is displayed on the face',
'Three Foot Pipe': '+2 attack for Ninja or Hybrid', 'Sturdy Hat': '+2 int for Wizard',
'Madrona Wand': '+2 attack for Wizard or Hybrid', 'Fingerless Gloves': '+2 dexterity for all classes',
'Shovel': 'a tool you could dig a hole with', 'Jagged Rocks': 'a few rocks, sharp as hell', 
'Leather T-Shirt': '+2 defense for all classes', 'Short Rope': 'about 12 feet of good rope',
'Big Medallion': 'a unique pattern is displayed on the face', 'Sword': '+3 attack for Ninja or Hybrid',
'Wide Brim Hat': '+3 int for Wizard', 'Oak Staff': '+3 attack for Wizard or Hybrid', 
'Power Mitts': '+3 dex for all classes', 'Balanced Pickaxe': 'a well weighted tool for digging or breaking stone',
'Book of Knots': 'Learn all sorts of knots!', 'Leather Jacket': '+3 defense for all classes',
'Long Rope': 'a 30 foot coil of good rope', 'Intricate Medallion': 'a craft of wonder and brilliance'}

loot_lvl_1_3 = ['Sturdy Walking Stick', 'Cloth Cap', 'Short Stick', 'Basic Gloves', 
'Spade', 'Paper and Pen', 'Thick Shirt', 'Roll of String', 'Small Medallion']

loot_lvl_4_6 = ['Three Foot Pipe', 'Sturdy Hat', 'Madrona Wand', 'Fingerless Gloves',
'Shovel', 'Jagged Rocks', 'Leather T-Shirt', 'Short Rope', 'Big Medallion']

loot_lvl_7_9 = ['Sword', 'Wide Brim Hat', 'Oak Staff', 'Power Mitts',
'Balanced Pickaxe', 'Book of Knots', 'Leather Jacket', 'Long Rope',
'Intricate Medallion'] 

enemies_lvl_1_3 = ['Slime', 'Gnoll', 'Wolf', 'Bat', 'Goblin', 'Cat', 'Flannel Bag',
'Glowing Top Hat', 'Pair of Round Spectacles']

enemies_lvl_4_6 = ['Large Slime', 'Pack of Gnolls', 'Alpha Wolf', 'Ancient Bat', 
'Desperate Goblin', 'Mountain Cat', 'Self Closing Flannel Bag',
'Glowing Top Hat w/ Cane', 'Jagged Contacts']

enemies_lvl_7_9 = ['Shiny Mist', 'Floor of Marbles', 'Shrieking Box', 'Wall of Bats',
'Competetive Eater', 'Donald Trump', 'Mary Poppin\'s Bag of Horrors', 
'Badass Three Piece Suit w/ Hat & Cane', 'Eye Candy']

fathers_wisdom = ['If it\'s the easy way, it\'s the wrong way.', 
'Make soup, not war.', 'The fastest way to the end of any journey is forward.',
'Life isn\'t fair.', 'When the going gets tough, stop and think about things.',
'Give it a little shake and see what falls out.',
'Talking is to first be done silently.', 'When talking is silent, silence is golden.',
'Don\'t forget to drink water.', 'Enunciated vowels produce healthy bowels!', 
'Club once in awhile, don\'t be a constant clubber.']

mothers_wisdom = ['Take garlic, son. And raw honey.',
'If you take ill, take raw honey.', 'Don\'t shake hands with a troll',
'Raw garlic. Feel the burn.', 'Soak your bunions.',
'Never trust a woman with one eye.', 'Always trust a bearded wizard.',
'Can I look at your blackheads?', 'Let\'s go wash your face.', 'Eucalyptus oil.',
'Always use protection.', 'Milk baths are healing.']


def print_wisdom(parent):
	
	if parent == "Dad":
		chance = randint(0, 10)
		print "\nFrom your Father:\n"
		print '"' + fathers_wisdom[chance] + '"'
		print " "
		
	else: 
		chance = randint(0, 11)
		print "\nFrom your Mother:\n"
		print '"' + mothers_wisdom[chance] + '"'
		print " "

def player_check():

	print "Would you like to see your stats or your inventory or best scores?"
	choice = raw_input(prompt)
	print " "
	
	if "tats" in choice:
		print """Here are your current stats:\n
		Name: %s Class: %s
		Strength: %d
		Dexterity: %d
		Intelligence: %d
		Max Hit Points: %d
		Current Hit Points: %d\n""" % (player_name, player_class, player_str,
		player_dex, player_int, player_hp, player_hp_dmg)
		print " "
	
	elif "nvent" in choice:
	
		if satchel_contents == []:
			print "Your satchel is empty!\n"
		
		else:
			print "Here are the current contents of your Satchel: "
			satchel_contents.sort()
			for item in satchel_contents: 
				print "\t--" + item + "--"
			print " "
			
			print "Would you like to equip something?"
			choice2 = raw_input(prompt)
			
			if "ye" in choice2:
				
				equip()
	
	elif "scores" in choice: 
		
		print """
		Most fights won before death: %d by %s
		Most fights won walking into the Battle Cave at one go: %d by %s
		Most fights won in the Battle Cave and survive: %d by %s
		\n""" % (fight_count_most, high_scorer_fcm, battle_cave_furthest, high_scorer_bcf,
		       battle_cave_there_and_back, high_scorer_bctb)
	
	else:
		print "I'm not sure what you're looking for.\n"
	
	print "Would you like to remember some advice from one of your parents?" 
	
	answer = raw_input(prompt)
	
	if "ye" in answer:
			
		chance = randint(1, 100)
		if chance <= 50: 
			print_wisdom("Dad")
			print "He was a good man.\n"
		else: 
			print_wisdom("Mom")
			print "She was an excellent woman.\n" 
		
	else: 
		print "I'm sure you know your way.\n"
		
def equip():
	
	global player_str, player_dex, player_int, player_hp, attack_mod, defense_mod, walking_stick
	global cloth_cap, short_stick, basic_gloves, thick_shirt, three_ft_pipe, sturdy_hat, madrona_wand
	global fingerless_gloves, leather_t, sword, wide_brim_hat, oak_staff, power_mitts, leather_jacket
	global small_medallion, big_medallion, intricate_medalion, weapon, current_weapon
	
	
	print "What would you like to equip, good %s, the %s?\n" % (player_name, player_class)
	answer = raw_input(prompt)
	while answer == "player":
		player_check()
		
		print "What would you like to equip, good %s, the %s?\n" % (player_name, player_class)
		answer = raw_input(prompt)
	
	if answer in satchel_contents:
		if answer == "Cloth Cap" and cloth_cap == False:
			
			if sturdy_hat or wide_brim_hat:
				print "Why would you do that? You'd lose intelligence!\n"
				time.sleep(2)
				print "I mean, if you're willing to make this decision with"
				print "this level of intelligence, what kind of decisions are"
				print "you going to make with less intelligence?\n"
				time.sleep(9)
				print "We'll hold off for now.\n"
				
			print "Okay, you equip the Cloth Cap! Your intelligence has increased by 1!\n"
			player_int += 1
			cloth_cap = True
			
		elif answer == "Cloth Cap" and cloth_cap == True:
			
			print "You are already wearing the Cloth Cap!\n"
			
		elif answer == "Short Stick" and short_stick == False:
			
			if weapon:
				print "Okay, %s, the Short Stick is replacing your %s!\n" % (player_name, current_weapon)
				print "Your bonus attack is 1!\n"
				attack_mod = 1
				short_stick = True
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
				print "Okay, you equip the Short Stick! Your attack has increased by 1!\n"
				attack_mod = 1
				short_stick = True
				weapon = True
				current_weapon = "Short Stick"
			
		elif answer == "Short Stick" and short_stick == True:
			
			print "You already have the Short Stick equipped!\n"
			
		elif answer == "Basic Gloves" and basic_gloves == False:
			
			if fingerless_gloves or power_mitts:
				print "Why would you do that? You'd lose dexterity!\n"
				
			print "Okay, you equip the Basic Gloves! Your dexterity has increased by 1!\n"
			player_dex += 1
			basic_gloves = True
			
		elif answer == "Basic Gloves" and basic_gloves == True:
			
			print "You are already wearing the Basic Gloves!\n"
			
		elif answer == "Thick Shirt" and thick_shirt == False:
				
			if leather_t or leather_jacket:
				print "Why would you do that? You'd become more defenseless!\n"
				
			print "Okay, you equip the Thick Shirt! Your defense has increased by 1!\n"
			defense_mod += 1
			thick_shirt = True
			
		elif answer == "Thick Shirt" and thick_shirt == True:
			
			print "You are already wearing the Thick Shirt!\n"
			
		elif answer == "Sturdy Hat" and sturdy_hat == False:
			
			if cloth_cap == True:
				print "You have removed the Cloth Cap and equipped the Sturdy Hat!\n"
				print "Your intelligence has increased by 2!\n"
				player_int += 1
				sturdy_hat = True
				cloth_cap = False
				
			elif wide_brim_hat:
				print "Up to you, %s." % player_name
				print "Your intelligence is decreased by 1.\n"
				player_int -= 1
				wide_brim_hat = False
				sturdy_hat = True
			
			else:
				print "Okay, you equip the Sturdy Hat! Your intelligence has increased by 2!\n"
				player_int += 2
				sturdy_hat = True
				
		elif answer == "Sturdy Hat" and sturdy_hat == True:
			
			print "You're already wearing the Sturdy Hat!\n"
		
		elif answer == "Madrona Wand" and madrona_wand == False:
			
			if weapon:
				print "Okay, %s, the Madrona Wand is replacing your %s!\n" % (player_name, current_weapon)
				print "Your bonus attack is 2!\n"
				attack_mod = 2
				madrona_want = True
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
				print "Okay, you equip the Madrona Wand! Your attack has increased by 2!\n"
				attack_mod = 2
				madrona_wand = True
				weapon = True
				current_weapon = "Madrona Wand"
				
		elif answer == "Madrona Wand" and madrona_wand == True:
			
			print "You've already got the Madrona Wand equipped!\n"
			
		elif answer == "Fingerless Gloves" and fingerless_gloves == False:
			
			if basic_gloves == True:
				print "You have removed the Basic Gloves and equipped the Fingerless Gloves!\n"
				print "You're dexterity has increased by 2!\n"
				player_dex += 1
				fingerless_gloves = True
				basic_gloves = False
				
			elif power_mitts:
				print "Up to you, %s." % player_name
				print "Your dexterity is decreased by 1.\n"
				player_dex -= 1
				power_mitts = False
				fingerless_gloves = True
			
			else:
				print "Okay, you equip the Fingerless Gloves! Your dexterity is increased by 2!\n"
				player_dex += 2
				fingerless_gloves = True
				
		elif answer == "Fingerless Gloves" and fingerless_gloves == True:
			
			print "You're already wearing the Fingerless Gloves!\n"
			
		elif answer == "Leather T-Shirt" and leather_t == False:
			
			if thick_shirt == True:
				print "You have removed the Thick Shirt and equipped the Leather T-Shirt!\n"
				print "You're defense has increased by 1!\n"
				defense_mod += 1
				leather_t = True
				thick_shirt = False
				
			elif leather_jacket:
				print "Up to you, %s." % player_name
				print "Your defense is decreased by 1.\n"
				defense_mod -= 1
				leather_jacket = False
				leather_t = True
			
			else:
				print "Okay, you equip the Leather T-Shirt! Your defense has increased by 2!\n"
				defense_mod += 2
				leather_t = True
				
		elif answer == "Leather T-Shirt" and leather_t == True:
			
			print "You're already wearing the Leather T-Shirt, and I must say it looks dashing!\n"
			
		elif answer == "Wide Brim Hat" and wide_brim_hat == False:
			
			if cloth_cap == True:
				print "You have removed the Cloth Cap and equipped the Wide Brim Hat!\n"
				print "Your intelligence has increased by 2!\n"
				player_int += 2
				wide_brim_hat = True
				cloth_cap = False
			
			elif sturdy_hat == True:
				print "You have removed the Sturdy Hat and equipped the Wide Brim Hat!\n"
				print "Your intelligence has increased by 1!\n"
				player_int += 1
				wide_brim_hat = True
				sturdy_hat = False
				
			else: 
				print "Okay, you equip the Wide Brim Hat! Your intelligence has increased by 3!\n"
				player_int += 3
				wide_brim_hat = True
				
		elif answer == "Wide Brim Hat" and wide_brim_hat == True:
			
			print "You're already wearing the Wide Brim Hat!\n"
		
		elif answer == "Oak Staff" and oak_staff == False:
			
			if weapon:
				print "Okay, %s, the Oak Staff is replacing your %s!\n" % (player_name, current_weapon)
				print "Your bonus attack is 3!\n"
				attack_mod = 3
				oak_staff = True
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
				print "Okay, you equip the Oak Staff! Your attack has increased by 3!\n"
				attack_mod = 3
				oak_staff = True
				weapon = True
				current_weapon = "Oak Staff"
				
		elif answer == "Oak Staff" and oak_staff == True:
			
			print "You've already got the Oak Staff equipped!\n"
			
		elif answer == "Power Mitts" and power_mitts == False:
			
			if basic_gloves == True:
				print "You have removed the Basic Gloves and equipped the Power Mitts!\n"
				print "You're dexterity has increased by 2!\n"
				player_dex += 2
				power_mitts = True
				basic_gloves = False
				
			elif fingerless_gloves == True:
				print "You have removed the Fingerless Gloves and equipped the Power Mitts!\n"
				print "You're dexterity has increased by 1!\n"
				player_dex += 1
				power_mitts = True
				fingerless_gloves = False
			
			else:
				print "Okay, you equip the Power Mitts! Your dexterity is increased by 3!\n"
				player_dex += 3
				fingerless_gloves = True
				
		elif answer == "Power Mitts" and power_mitts == True:
			
			print "You're already wearing the Power Mitts!\n"
			
		elif answer == "Leather Jacket" and leather_jacket == False:
			
			if thick_shirt == True:
				print "You have removed the Thick Shirt and equipped the Leather Jacket!\n"
				print "You're defense has increased by 2!\n"
				defense_mod += 2
				leather_jacket = True
				thick_shirt = False
				
			elif leather_t == True:
				print "You have removed the Leather T-Shirt and equipped the Leather Jacket!\n"
				print "You're defense has increased by 1!\n"
				defense_mod += 1
				leather_jacket = True
				leather_t = False
			
			else:
				print "Okay, you equip the Leather Jacket! Your defense has increased by 3!\n"
				defense_mod += 3
				leather_jacket = True
				
		elif answer == "Leather Jacket" and leather_jacket == True:
			
			print "You're already wearing the Leather Jacket!\n"
		
		elif answer == "Sturdy Walking Stick" and walking_stick == False:
			
			if weapon:
				print "Okay, %s, the Sturdy Walking Stick is replacing your %s!\n" % (player_name, current_weapon)
				print "Your bonus attack is 1!\n"
				attack_mod = 1
				walking_stick = True
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
				print "Okay, you equip the Sturdy Walking Stick! Your attack has increased by 1!\n"
				attack_mod = 1
				walking_stick = True
				weapon = True
				current_weapon = "Sturdy Walking Stick"
			
		elif answer == "Sturdy Walking Stick" and walking_stick == True:
			
			print "You've already got the Sturdy Walking Stick equipped!\n"

		elif answer == "Three Foot Pipe" and three_ft_pipe == False:
			
			if weapon:
				print "Okay, %s, the Three Foot Pipe is replacing your %s!\n" % (player_name, current_weapon)
				print "Your bonus attack is 2!\n"
				attack_mod = 2
				three_ft_pipe = True
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
				print "Okay, you equip the Three Foot Pipe! Your attack has increased by 2!\n"
				attack_mod += 2
				three_ft_pipe = True
				weapon = True
				current_weapon = "Three Foot Pipe"
				
		elif answer == "Three Foot Pipe" and three_ft_pipe == True:
			
			print "You've already got the Three Foot Pipe equipped!\n"
		
		elif answer == "Sword" and sword == False:
			
			if weapon:
				print "Okay, %s, the Sword is replacing your %s!\n" % (player_name, current_weapon)
				print "Your bonus attack is 3!\n"
				attack_mod = 3
				madrona_want = True
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
				print "Okay, you equip the Sword! Your attack has increased by 3!\n"
				attack_mod = 3
				sword = True
				weapon = True
				current_weapon = "Sword"
				
		elif answer == "Sword" and sword == True:
			
			print "You've already got the Sword equipped!\n"
			
		elif answer == "Small Medallion" and small_medallion == False:
				
			print "You put the Small Medallion around your neck.\n"
			small_medallion = True
			big_medallion = False
			intricate_medallion = False
			
		elif answer == "Small Medallion" and small_medallion == True:
			
			print "You're already wearing the Small Medallion!\n"
			
		elif answer == "Big Medallion" and big_medallion == False:
				
			print "You put the Big Medallion around your neck.\n"
			big_medallion = True
			small_medallion = False
			intricate_medallion = False
			
		elif answer == "Big Medallion" and big_medallion == True:
			
			print "You're already wearing the Big Medallion, and you look sexy!\n"
			
		elif answer == "Intricate Medallion" and intricate_medallion == False:
			
			print "You put the intricate medallion around your neck.\n"
			intricate_medallion = True
			big_medallion = False
			small_medallion = False
			
		elif answer == "Intricate Medallion" and intricate_medallion == True:
			
			print "You're already wearing the intricate medallion!\n"
			
		else: 
			print "You do not have that item!\n"
				
	else: 
		print "You do not have that item!\n"
	
	#if player_class == "Wizard":

	#elif player_class == "Ninja":
	
	#else:

# def use(): 

def print_enemies_full():
	
	print "\nEnemies for Adventurers, Level 1 - 3: "
	for i in range(len(enemies_lvl_1_3)):
		print enemies_lvl_1_3[i]
	print '\n'
	
	print "Enemies for Adventurers, Level 4 - 6: "
	for i in range(len(enemies_lvl_4_6)):
		print enemies_lvl_4_6[i]
	print '\n'
	
	print "Enemies for Adventurers, Level 7 - 9: "
	for i in range(len(enemies_lvl_7_9)):
		print enemies_lvl_7_9[i]
		
def print_items_full():
	
	print "\nItems for Adventurers, Level 1 - 3: "
	for i in range(len(loot_lvl_1_3)):
		print loot_lvl_1_3[i]
	print '\n'
	
	print "Items for Adventurers, Level 4 - 6: "
	for i in range(len(loot_lvl_4_6)):
		print loot_lvl_4_6[i]
	print '\n'
	
	print "Items for Adventurers, Level 7 - 9: "
	for i in range(len(loot_lvl_7_9)):
		print loot_lvl_7_9[i]

def battle(enemy, enemy_name):
	
	#player list order: Hp, Str, Dex, Int, xp
	#enemy list order: Hp, MaxAttack, xp given, dex
		
	global player_xp, player_hp_dmg, fight_count, fight_count_most
	global high_scorer, high_scorer_fcm
	
	result = "No Hit."
	enemy_hp = enemy[0]
	enemy_attack = 0
	player_attack = 0
	v = time.sleep(0.25)
		
	if enemy[3] > player_dex:
		
		while player_hp_dmg > 0 and enemy_hp > 0:
			
			print "\nThe %s attacks!\n" % enemy_name
			time.sleep(1)
			
			enemy_attack = randint(0, enemy[1])
			precision = randint(1, 100)
		
			if precision >= 90:
		
				if precision == 100:
					result = "Unreal Critical Precision!\n\n" 
					enemy_attack += 3
					v
				
				else: 
					result = "Critical Precision!\n\n" 
					enemy_attack += 2
					v
			
			elif 75 < precision < 90:
				result = "Precision hit!\n\n" 
				enemy_attack += 1
				v
			
			elif 30 < precision < 76:
				result = "Hit!\n\n"
				v
			
			elif 10 < precision < 31:
				result = "Weak hit!\n\n"
				enemy_attack -+ 1
				v
			
			elif 1 <= precision <= 10:
			
				if precision == 2:
					result = "Glancing blow.\n\n" 
					enemy_attack -= 3
					v
				
				elif precision == 1:
					result = "Missed!\n\n"
					enemy_attack = 0
					v
				
				else:
					result = "Contact.\n\n"
					enemy_attack -= 2
					v
			
			else:
				result = "This shouldn't ever print."
				
			print result
			
			if defense_mod > 0:
				enemy_attack -= defense_mod
				print "\n -- Defense Modifier is %d -- \n" % defense_mod
			
			if enemy_attack < 0:
			
				enemy_attack = 0
			
			print "The %s strikes you for: %d damage!\n" % (enemy_name, enemy_attack)
			time.sleep(1)
			
			player_hp_dmg -= enemy_attack
			
			print "You now have %s hit points.\n" % player_hp_dmg
			print "--------------------********--------------------\n\n"
			time.sleep(1)
			
			if player_hp_dmg <= 0:
				
				determine_player_death(player_hp_dmg, enemy_name)
			
			print "Now it's your turn to attack!\n"
			time.sleep(1)
			
			# First attack algorithm:
			# player_attack = x + y + j
			
			# Second attack algorithm:
			# modifier = randint(1, 3)
			# player_attack = (x + y + j) / modifier
	
			# updated attack algorithm:
			x = player_str
			y = player_dex 
			j = player_int
			order = [x, y, j]
			order.sort()
			a = order[1] / 3
			b = order[2]
			player_attack = a + b
			
			balance = randint(1, 3)
			
			if balance == 1:
				print "Perfectly balanced attack!\n"
			
			elif balance == 2:
				print "Well balanced attack!\n"
				player_attack /= 2
			
			elif balance == 3:
				print "Off balance attack.\n"
				player_attack /= 3
			
			else:
				print "This should not ever print. Ever."
			
			precision = randint(1, 100)
			
			if precision >= 90:
			
				if precision == 100:
					result = "Unreal Critical Precision!\n\n" 
					player_attack += 3
					v
				
				else: 
					result = "Critical Precision!\n\n" 
					player_attack += 2
					v
			
			elif 75 < precision < 90:
				result = "Precision hit!\n\n" 
				player_attack += 1
				v
			
			elif 30 < precision < 76:
				result = "Hit!\n\n"
				v
			
			elif 10 < precision < 31:
				result = "Weak hit!\n\n"
				player_attack -+ 1
				v
			
			elif 1 <= precision <= 10:
			
				if precision == 2:
					result = "Glancing blow.\n\n" 
					player_attack -= 3
					v
				
				elif precision == 1:
					result = "Miss!\n\n"
					player_attack = 0
					v
				
				else:
					result = "Contact.\n\n"
					player_attack -= 2
					v
			
			else:
				result = "This shouldn't ever print."
				
			print result
			
			if attack_mod > 0:
				player_attack += attack_mod
				print "\n -- Attack Modifier is %d -- \n" % attack_mod
			
			if player_attack < 0:
				
				player_attack = 0
			
			elif result == "Miss!\n\n":
				
				player_attack = 0
			
			print "You strike the %s for: %d damage!\n" % (enemy_name, player_attack)
			time.sleep(1)
			
			enemy_hp -= player_attack
			
			print "The %s now has %d hit points.\n" % (enemy_name, enemy_hp)
			print "--------------------********--------------------\n\n"
			time.sleep(1)
			
			if enemy_hp <= 0:
				
				determine_enemy_death(enemy_hp, enemy_name)
				print "---------------------------"
				break
				
			if small_medallion:
				print "You feel warmth on your chest, and suddenly become a little healthier."
				player_hp_dmg += 1
				if player_hp_dmg > player_hp:
					player_hp_dmg = player_hp
			
			elif big_medallion or intricate_medallion:
				print "You feel heat all over your body, and suddenly become much healthier."
				player_hp_dmg += 2
				if player_hp_dmg > player_hp:
					player_hp_dmg = player_hp
			
		if player_hp_dmg <= 0:
			
			determine_player_death(player_hp_dmg, enemy_name)
	
	else:
		
		while player_hp_dmg > 0 and enemy_hp > 0:
			
			print "You attack!\n"
			
			time.sleep(1)
		
			x = player_str
			y = player_dex 
			j = player_int
			order = [x, y, j]
			order.sort()
			a = order[1] / 3
			b = order[2]
			player_attack = a + b
			
			balance = randint(1, 3)
			
			if balance == 1:
				print "Perfectly balanced attack!\n"
			
			elif balance == 2:
				print "Well balanced attack!\n"
				player_attack /= 2
			
			elif balance == 3:
				print "Off balance attack.\n"
				player_attack /= 3
			
			else:
				print "This should not ever print. Ever."
			
			precision = randint(1, 100)
			
			if precision >= 90:
			
				if precision == 100:
					result = "Unreal Critical Precision!\n\n" 
					player_attack += 3
					v
			
				else: 
					result = "Critical Precision!\n\n" 
					player_attack += 2
					v
			
			elif 75 < precision < 90:
				result = "Precision hit!\n\n" 
				player_attack += 1
				v
			
			elif 30 < precision < 76:
				result = "Hit!\n\n"
				v
			
			elif 10 < precision < 31:
				result = "Weak hit!\n\n"
				player_attack -+ 1
				v
			
			elif 1 <= precision <= 10:
			
				if precision == 2:
					result = "Glancing blow.\n\n" 
					player_attack -= 3
					v
			
				elif precision == 1:
					result = "Miss!\n\n"
					player_attack = 0
					v
			
				else:
					result = "Contact.\n\n"
					player_attack -= 2
					v
			
			else:
				result = "This shouldn't ever print."
				
			print result
			
			if attack_mod > 0:
				player_attack += attack_mod
				print "\n -- Attack Modifier is %d -- \n" % attack_mod
			
			if player_attack < 0:
				
				player_attack = 0
			
			elif result == "Miss!\n\n":
				
				player_attack = 0
				
			print "You strike the %s for: %d damage!\n" % (enemy_name, player_attack)
			time.sleep(1)
			
			enemy_hp -= player_attack
			
			print "The %s now has %d hit points.\n" % (enemy_name, enemy_hp)
			print "--------------------********--------------------\n\n"
			
			time.sleep(1)
			
			if enemy_hp <= 0:
			
				determine_enemy_death(enemy_hp, enemy_name)
				print "---------------------------"
				break 
				
			print "Now it's the %s\'s turn!\n" % enemy_name			
			time.sleep(1)
			
			enemy_attack = randint(0, enemy[1])
			precision = randint(1, 100)
		
			if precision >= 90:
		
				if precision == 100:
					result = "Unreal Critical Precision!\n\n" 
					enemy_attack += 3
					v
		
				else: 
					result = "Critical Precision!\n\n" 
					enemy_attack += 2
					v
		
			elif 75 < precision < 90:
				result = "Precision hit!\n\n" 
				enemy_attack += 1
				v
		
			elif 30 < precision < 76:
				result = "Hit!\n\n"
				v
		
			elif 10 < precision < 31:
				result = "Weak hit!\n\n"
				enemy_attack -+ 1
				v
		
			elif 1 <= precision <= 10:
			
				if precision == 2:
					result = "Glancing blow.\n\n" 
					enemy_attack -= 3
					v
			
				elif precision == 1:
					result = "Miss!\n\n"
					enemy_attack = 0
					v
			
				else:
					result = "Contact.\n\n"
					enemy_attack -= 2
					v
			
			else:
			
				result = "This shouldn't ever print."
				
			print result
			
			if defense_mod > 0:
				enemy_attack -= defense_mod
				print "\n -- Defense Modifier is %d -- \n" % defense_mod
			
			if enemy_attack < 0:
			
				enemy_attack = 0
			
			print "The %s strikes you for: %d damage!\n" % (enemy_name, enemy_attack)
			time.sleep(1)
			
			player_hp_dmg -= enemy_attack
			
			print "You now have %s hit points.\n" % player_hp_dmg
			print "--------------------********--------------------\n\n"
			
			time.sleep(1)		
			
			if player_hp_dmg <= 0:
				
				determine_player_death(player_hp_dmg, enemy_name)
				
			if small_medallion:
				print "You feel warmth on your chest, and suddenly become a little healthier."
				player_hp_dmg += 1
				if player_hp_dmg > player_hp:
					player_hp_dmg = player_hp
			
			elif big_medallion or intricate_medallion:
				print "You feel heat all over your body, and suddenly become much healthier."
				player_hp_dmg += 2
				if player_hp_dmg > player_hp:
					player_hp_dmg = player_hp
			
		if player_hp_dmg <= 0:
			
			determine_player_death(player_hp_dmg, enemy_name)
			
	
	print "You win!\n"
	
	#LOOT CODE
	chance = randint(1, 100)
	if chance > 40: 
		
		print "The %s dropped loot!\n" % enemy_name
		j = randint(0, 8)
		if player_lvl <= 3:
			
			loot = loot_lvl_1_3[j]
			#loot_lvl_1_3.pop(j)
		
			print "It's a %s!" % loot
			
			if loot in satchel_contents:
				print "You've already got a %s...\n" % loot
			
			else: 
				satchel_contents.append(loot)
				print "You've looted %s from the %s!\n" % (loot, enemy_name)
		
		elif player_lvl <= 6:
			
			chance = randint(1, 50)
			if chance < 20:
				loot = loot_lvl_1_3[j]
			else: 
				loot = loot_lvl_4_6[j]
			
			print "It's a %s!\n" % loot
			
			if loot in satchel_contents:
				print "You've already got a %s...\n" % loot
			
			else: 
				satchel_contents.append(loot)
				print "You've looted %s from the %s!\n" % (loot, enemy_name)
				
		else:
			
			chance = randint(1, 60)
			if chance < 10:
				loot = loot_lvl_1_3[j]
			elif chance < 25:
				loot = loot_lvl_4_6[j]
			else:
				loot = loot_lvl_7_9[j]
			
			print "It's a %s!\n" % loot
			
			if loot in satchel_contents:
				print "You've already got a %s...\n" % loot
			
			else: 
				satchel_contents.append(loot)
				print "You've looted %s from the %s!\n" % (loot, enemy_name)
		
	fight_count += 1  #to tabulate fights won while alive
	
	if high_scorer == False:
		
		if fight_count > fight_count_most: 
			
			high_scorer = True
			print "You've just taken 1st place on the fight count list!\n" 
			time.sleep(1)
			high_scorer_fcm = raw_input("Enter your name to go on the scoreboard: ")
	
	if fight_count > fight_count_most:
		fight_count_most = fight_count
	
	print "You've gained %d experience points!\n" % enemy[2]
	
	time.sleep(1)
	
	player_xp -= enemy[2]
	
	if player_xp <= 0:
		level_up()
		player_xp = player_xp_cap
	
	print "You have %d experience points to gain before you level up.\n" % player_xp

def determine_enemy_death(num, enemy_name):

	if num == 0:
		print "You barely defeated the %s!\n" % enemy_name
		
	elif num == -1:
		print "The %s juuuuust rolls over!\n" % enemy_name
		
	elif num == -2:
		print "The %s falls with little glory.\n" % enemy_name
		
	elif num == -3:
		print "You thwacked the %s.\n" % enemy_name
		
	elif num == -4:
		print "Solidly dead. Nice work.\n"
	
	elif num == -5:
		print "Clearly dead. No brainer.\n"
		
	elif num == -6:
		print "Were you making that personal?\n"
	
	elif num == -7:
		print "Holy Maloly, you freaking crushed it. freaking. crushed. it.\n"
	
	elif num == -8:
		print "Having a good day?\n"
	
	elif num == -9:
		print "Yikes. Not too often I need to look away at a death.\n"
		
	elif num == -10:
		print "You might need to change your clothes after that shelacking!\n"
		
	elif num == -11:
		print "Foooooeey! Cosmic strike!\n"
		
	elif num == -12:
		print "The %s explodes!\n" % enemy_name
	
	elif num == -13:
		print "The %s basically died 5 minutes ago from that hit.\n" % enemy_name
	
	elif num == -14:
		print "-14, really? Holy Fuggin Heckfire!\n"
		
	elif num == -15:
		print "Hit so hard it's been forgotten.\n"
	
	elif num == -16:
		print "I'm not sure it could get any more dead.\n"
		
	elif num == -17:
		print "Flat out flattened!\n"
	
	elif num == -18:
		print "Undeniably destroyed!\n"
		
	elif num == -19:
		print "It's like three of them died with that blow.\n"
	
	elif num == -20:
		print "A strike like that should not be possible.\n"
	
	elif num <= -21:
		print "Bravo! Hall of Fame Death!\n"
	
	else:
		print "This should never ever ever print.\n\n"
		
def determine_player_death(num, enemy_name):

	if num == 0:
		dead("The %s has barely defeated you!\n" % enemy_name)
		
	elif num == -1:
		dead("The %s juuuuust defeated you!\n" % enemy_name)
		
	elif num == -2:
		dead("You got beaten by the %s.\n" % enemy_name)
		
	elif num == -3:
		dead("You got thwacked by the %s.\n" % enemy_name)
		
	elif num == -4:
		dead("Well, solidly dead, I'd say.\n")
	
	elif num == -5:
		dead("Clearly dead. No doubter.\n") 
		
	elif num == -6:
		dead("That was not nice and frankly, I think it was personal.\n")
	
	elif num == -7:
		dead("Holy Maloly, you got freaking crushed. freaking. crushed.\n")
	
	elif num == -8:
		dead("Having a bad day?\n") 
	
	elif num == -9:
		dead("Yikes. Not too often I need to look away at a death.\n")
		
	elif num == -10:
		dead("May need to check the corners for limbs because you got torn apart!\n")
		
	elif num == -11:
		dead("I'm not sure you can get this dead.\n")
		
	elif num <= -12:
		dead("Bravo! Hall of Fame Death!\n")
	
	else:
		dead("this should never print\n")

def boss_encounter(room, modifier):
	
	if room == "room2":
		enemy_name = "The Goblin King"
		
		if modifier == "Spade":
			enemy = (80, 9, 32, 12)
			print "You have cleanly re-potted the plant!\n" 
			print "Suddenly, you hear a grumble in the hallway, and in walks in %s!" % enemy_name
			print "Even though he\'s appreciative of you doing the chore he\'d been"
			print "neglecting, %s is still going to fight you.\n" % enemy_name
		
		elif modifier == "Shovel" or modifier == "Hands":
			enemy = (80, 12, 32, 12)
			print "You have messily re-potted the plant!\n" 
			print "Suddenly, you hear an angry grunt from the hallway, and in walks in %s!" % enemy_name
			print "Apparently, he\'s particular about keeping his soil from hitting the stone,"
			print "and so he\'s frustrated and disappointed with you, and is ready to fight.\n"
		
		elif modifier == "Balanced Pickaxe":
			enemy = (80, 15, 32, 12)
			print "Your pickaxe breaks the empty pot and you hear an enraged roar!\n"
			print "%s bursts into the room and throws his arms above his head, howling"
			print "with rage as he sees his broken pot.\n"
		
		elif modifier == "Thief":
			enemy = (80, 15, 32, 12)
			print "The moment you touch the pot, you hear a deep scream of anguish!\n"
			print "Charging through the door is %s! He sees you trying to take his pot"
			print "and he becomes enraged!\n"
		
		else:
			enemy = (80, 12, 32, 12)
			print "Your bumbling has made a mess. %s appears at the door and he's ready to fight!\n" % enemy_name
	
	
		print "You and the %s fight!\n\n\n" % enemy_name
		battle(enemy, enemy_name)
		
def enemy_encounter():
	
	x = randint(0, 8)
	loot = ""
	
	if 0 < player_lvl <= 3:
		
		enemy = enemies_lvl_1_3[x]
		enemy_name = enemy
		#Enemy form: (hp, max_attack, gives_xp, dex)
		if x == 0:
			enemy = (6, 3, 4, 1) #slime 14
		
		elif x == 1:
			enemy = (6, 3, 4, 5) #gnoll 18
		
		elif x == 2:
			enemy = (6, 4, 5, 6) #wolf 21
		
		elif x == 3: 
			enemy = (5, 3, 5, 10) #bat 23
		
		elif x == 4:
			enemy = (6, 3, 4, 6) #goblin 19
		
		elif x == 5:
			enemy = (3, 2, 3, 8) #cat 16
		
		elif x == 6:
			enemy = (6, 2, 3, 1) #flannel_bag 12
		
		elif x == 7:
			enemy = (10, 2, 5, 2) #glowing_top_hat 19
		
		else:
			enemy = (5, 2, 2, 2) #round_spectacles() 11
	
	elif 3 < player_lvl <= 6:
		
		enemy = enemies_lvl_4_6[x]
		enemy_name = enemy
		
		if x == 0:
			enemy = (9, 5, 6, 2) #lg_slime 22
		
		elif x == 1:
			enemy = (10, 10, 9, 8) #gnoll_pack 37
		
		elif x == 2:
			enemy = (9, 7, 8, 7) #alpha_wolf 31
		
		elif x == 3: 
			enemy = (6, 8, 9, 12) #ancient_bat 35
		
		elif x == 4:
			enemy = (4, 10, 7, 6) #desperate_goblin 27
		
		elif x == 5:
			enemy = (8, 6, 7, 10) #mountain_cat 31
		
		elif x == 6:
			enemy = (5, 10, 7, 3) #self_closing_flannel_bag 25
		
		elif x == 7:
			enemy = (10, 8, 9, 2) #glowing_top_hat_w_cane 29
		
		else:
			enemy = (6, 8, 6, 3) #jagged_contacts 23
	
	elif 6 < player_lvl <= 9:
		
		enemy = enemies_lvl_7_9[x]
		enemy_name = enemy
	
		if x == 0:
			enemy = (12, 15, 12, 8) #shiny_mist 47
		
		elif x == 1:
			enemy = (13, 2, 6, 18) #floor_of_marbles 43
		
		elif x == 2:
			enemy = (8, 14, 10, 5) #shrieking_box 36
		
		elif x == 3: 
			enemy = (12, 12, 12, 5) #wall_of_bats 41
		
		elif x == 4:
			enemy = (18, 5, 9, 3) #competetive_eater 35
		
		elif x == 5:
			enemy = (10, 15, 14, 1) #donald_trump 40
		
		elif x == 6:
			enemy = (15, 18, 14, 4) #mary_poppins_bag_of_horrors 51
		
		elif x == 7:
			enemy = (12, 13, 14, 11) #badass_3_suit_hat_cane 50
		
		else:
			enemy = (1, 20, 15, 20) #eye_candy 56
	
	else:
		return "Did not work!\n"
	
	print "You've run into an enemy!" 
	print "It's a %s\n" % enemy_name
	
	print "Are you going to fight or flee?"
	
	choice = raw_input(prompt)
	print " "
	
	while choice == "player":
		player_check()
		
		print "Are you going to fight or flee?"
		choice = raw_input(prompt)
		print " "
	
	if "ight" in choice: 
	
		print "You and the %s fight!\n\n\n" % enemy_name
		battle(enemy, enemy_name)
	
	else: 
	
		if enemy[3] > player_dex:
			
			diff = (enemy[3] - player_dex) * 10
			chance = randint(1, 100)
			if chance >= 50 + diff:
				
				print "Somehow you escape!\n\n"
			
			else: 
				dead("""Wow, you're slow. As you turn around and expose your neck,
				the %s attacks and it kills ya.""" % enemy_name) 
		
		else:
			
			diff = (player_dex - enemy[3]) * 10
			if diff > 40:
				diff = 40
			chance = randint(1, 100)
			if chance <= 50 + diff:
				
				print "Because of your superior quickness, you escape.\n\n" 
			
			else: 
				dead("Just because you SHOULD BE faster than your enemy, you weren't.")

def level_up():
	
	global player_lvl, player_xp_cap, player_str, player_dex, player_int, player_hp
	global player_hp_dmg, player_xp
	
	print "You've leveled up! Congrats, that's awesome!\n\n" 
	time.sleep(2)
	
	print """These are your old stats:
	Level: %d
	Strength: %d
	Dexterity: %d
	Intelligence: %d
	Hit Points: %d\n""" % (player_lvl, player_str, player_dex, player_int, player_hp)
	print "_____________\n"
	
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
	
	print """These are your new stats: 
	Level: %d
	Strength: %d
	Dexterity: %d
	Intelligence: %d
	Hit Points: %d\n\n""" % (player_lvl, player_str, player_dex, player_int, player_hp)
	print "___________\n"

def start():
	
	global first_time_secret_room, first_time_first_room, came_from, player_hp_dmg
	global player_name, player_class, player_lvl, player_xp, satchel_contents
	
	player_name = ""
	player_class = ""
	player_lvl = 1
	first_time_secret_room = True
	first_time_first_room = True
	high_scorer_cave = False
	high_scorer_furthest = False
	high_scorer = False
	satchel_contents = []
	
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
	print "\n\n\t\tLabyrinth of the Lost Sons\n\n\n"
	
	time.sleep(2)
	print "Thanks for playing.\n"
	print "At any time type 'player' to see your stats or inventory."
	print "\n\n\n"
	time.sleep(2)
	
	print """
	You awaken. It's cold but you're insulated by layers. It feels like you 
	shouldn't be here or you're lost. It's a strange feeling.\n"""
	time.sleep(3)
	
	print """
	You get up and look around you. You see snow covered fields and a grey sky. 
	A light snow falls.\n"""
	time.sleep(3)
	
	print """
	You turn around and there is a high concrete wall stretching far 
	in both directions extensively, going on and on for, at most, forever.\n"""
	time.sleep(3)
	
	print """
	An old woman sits next to a thin rectangular opening in the concrete. You 
	approach the woman and she sees you.\n\n\n"""
	time.sleep(3)
	
	print "\n\t Old Woman: 'I see you're awake. You came out of nowhere it seems.'\n"
	
	build_character()
	
	print "Old Woman: 'Are you on a quest? Or just hanging out? Or What?'"
	
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Old Woman: 'Are you on a quest? Or just hanging out?'"
		answer = raw_input(prompt)
		print " "
	
	if "uest" in answer: 
		
		print "'Oh, a quest, eh?" 
		time.sleep(2)
		print "This labyrinth holds great treasure. And danger. Did I mention danger?"
		print "Are you willing to proceed?'"
		
		decision = raw_input(prompt)
		print " "
		
		while decision == "player":
			player_check()
			
			print "Are you willing to proceed?'"
			decision = raw_input(prompt)
			print " "
		
		if "ye" in decision: 
			print "'Best luck in there!'"
			came_from = "South"
			
			first_intersection()
		
		else:
			dead("The old woman rises up in a fury and one-punch kills you.")
	
	elif "ang" in answer:
		
		print "You're so cool. I wish any one of my twelve sons were as cool"
		print "as you are. Are you single?'\n"
		time.sleep(1)
		
		print "'Just kidding. It's fine. I didn't mean it anyway.'\n"
		
		time.sleep(2)
		print "Speaking of my kids... I lost them. They're in the labyrinth"
		print "and I'm certain they're being held prisoner or lost somewhere...\n\n"
		time.sleep(1)
		print "Woe is me!! I have the gout.\n"
		
		print "Will you help me?'\n"
		
		decision = raw_input(prompt)
		print " "
		
		while decision == "player":
			
			player_check()
			
			print "Will you help me?'\n"
			decision = raw_input(prompt)
			print " "
		
		if "ye" in decision:
			print "'Oh, thank you! Send them back to me when you've found them.\n\n"
			print "You might need to draw them a map, if you have the materials for it..."
			print "Just so they know how to get back to me.\n"
			print "Good luck!'"
			came_from = "South"
			first_intersection()
		
		elif "Ye" in decision:
			print "Oh, I knew I could trust you.\n\n"
			print "Send them back safely!"
			came_from = "South"
			first_intersection()
		
		elif "YE" in decision:
			print "My hero!! Oh, I love a man that does what's right.\n"
			print "I look forward to seeing you all real soon.\n\n"
			print "Good luck now, ya hear?" 
			came_from = "South"
			first_intersection()
		
		else: 
			print "'I curse you then! May death be upon your door!'\n\n\n.\n..\n..."
			print "You walk awkwardly past the woman and into the labyrinth."
			print "The wall of the labyrinth breaks for no apparent reason.\n"
			time.sleep(1)
			dead("The wall falls on you and the woman laughs as you perish.")
	
	else: 
		print "'That doesn't suprise me.\n"
		time.sleep(1)
		print "I think whatever you're looking for is in this labyrinth.\n\n"
		print "There's some pretty sweet loot and basically no danger.\n"
		time.sleep(1)
		print "Are you going to enter the labyrinth?'"
		
		decision = raw_input(prompt)
		print " "
		
		while decision == "player":
			
			player_check()
			
			print "Are you going to enter the labyrinth?'"
			decision = raw_input(prompt)
			print " "
		
		if "ye" in decision: 
			print "'Best luck in there, you mysterious %s'\n\n" % player_class
			came_from = "South"
			
			first_intersection()
		
		else:
			dead("The old woman starts to sing and suddenly your head explodes.")

def build_character():

	global player_name, player_class, player_str, player_dex, player_int, player_hp
	global player_hp_dmg, player_lvl, player_xp, player_xp_cap
								
	print "'What, may I ask, is your name sweet traveler?'"
	player_name = raw_input(prompt)
	print " "
	
	while player_name == "player":
		
		player_check()
		
		print "'What, may I ask, is your name sweet traveler?'"
		player_name = raw_input(prompt)
		print " "
	
	print "'And what type of a hero are you, %s?'" % player_name
	print "\t 1. Pro Wizard"
	print "\t 2. Master Ninja"
	print "\t 3. Amatuer Wizard, decent Ninja"
	
	choice = raw_input(prompt)
	print " "
	
	while choice == "player":
		
		player_check()
		
		print "'And what type of a hero are you, %s?'" % player_name
		print "\t 1. Pro Wizard"
		print "\t 2. Master Ninja"
		print "\t 3. Amatuer Wizard, decent Ninja"
		choice = raw_input(prompt)
		print " "
	
	if "1" in choice:
		
		player_class = "Wizard"
		player_lvl = 1
		player_str = 1
		player_dex = 2
		player_int = 6
		player_hp = 11
		player_hp_dmg = player_hp
		player_xp_cap = 10
		player_xp = player_xp_cap
	
	elif "2" in choice:
		
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
	
	print "'Ahh, %s the %s! Exciting!'" % (player_name, player_class)
	print "'Jeez. I haven't seen a %s in ages...'" % player_class
	time.sleep(2)
	
	print "\n'Actually, I haven't seen anyone in ages."
	print "You look really good. Seriously, have you looked at yourself lately?'"
	print " "
	time.sleep(2)
	
	print "Type 'player' to check yourself out." 
	choice2 = raw_input(prompt)
	print " "
	
	if "player" in choice2: 
		
		player_check()
	
	else:
		
		print "I guess I'm not your mother so I can't force you to...\n\n"

def first_intersection():

	global came_from
	
	print "\nThe hallway is dark but enough light is present to see around.\n" 
	time.sleep(1)
	print "You may choose to travel North, West, or East."
	print "You came from the %s.\n" % came_from
	print "Which direction do you choose?" 
	
	choice = raw_input(prompt)
	print " "
	
	while choice == "player":
		
		player_check()
		
		print "Which direction do you choose?" 
		choice = raw_input(prompt)
		print " "
	
	if "est" in choice:
		
		print "You go West and come to an elbow leading North.\n"
		time.sleep(2)
		
		print "You follow the elbow and are in a corridor that smells like dust"
		print "and decay.\n"
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		time.sleep(2)
		print "As you walk you see a 6 inch bookcase on your left."
		print "There is a Red Book, a Green Book, and a Blue Book.\n"
		time.sleep(1)
		print "Do you move on or do you inspect a book?"
		
		choice2 = raw_input(prompt)
		print " "
		
		while choice2 == "player":
			
			player_check()
			
			print "Do you move on or do you inspect a book?"
			choice2 = raw_input(prompt)
			print " "
		
		if "move" in choice2:
			
			print "You go around the corner and come to another intersection.\n"
			came_from = "West"
			chance = randint(1, 100)
			
			if chance <= 60:
				enemy_encounter()
			second_intersection()
		
		elif "nsp" in choice2:
			secret_room_1()
		
		else: 
			print "I wish I was human! Then I could understand you!"
			dead("A wave of sound comes and crushes your skull.")
							
	elif "ast" in choice:
		
		print "You follow the path East, which comes to an elbow that heads"
		print "North. You follow that path and come to another intersection.\n"
		came_from = "South"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		third_intersection()
		
	else: 
		print "You head North and come to a T intersection, branching West and East.\n"
		came_from = "South"
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		second_intersection()

def secret_room_1():

	global came_from, player_int, player_dex, player_str, first_time_secret_room
		
	print "Interesting. You're curious. I like that.\n"
	print "Which one book would you like to inspect?\n"
	print "1. Red Book"
	print "2. Green Book"
	print "3. Blue Book"
			
	choice3 = raw_input(prompt)
	print " "
	
	while choice3 == "player":
		
		player_check()
		
		print "Which one book would you like to inspect?\n"
		print "1. Red Book"
		print "2. Green Book"	
		print "3. Blue Book"
		choice3 = raw_input(prompt)
		print " "
			
	if "1" in choice3:
		
		print """
		You take the Red Book off the shelf and read the title;\n
		'Making Friends with Blood Pacts' 
		by 'Glungoral the Witty' \n
		You flip through the book, finding it boorish. You put the book back and
		can now decide to go North or South in the corridor."""
		came_from = "West"
		
		choice = raw_input(prompt)
		print " "
		
		while choice == "player":
			
			player_check()
			
			print "Would you like to go North or South in the corridor?"
			choice = raw_input(prompt)
			print " "
		
		if "orth" in choice:
			second_intersection()
		
		else:
			first_intersection()
						
	elif "2" in choice3:
		print """
		You take the Green book off the shelf and read the title; \n
		'Pushing Past Your Own Insecurities for Fun and Profit!' 
		by 'Mungorak the Pleasant'\n
		You flip through the book and it quickly becomes your favorite, but you've
		got no time to read, so you put the book back and can now decide to go North 
		or South in the corridor."""
		came_from = "West"
		
		choice = raw_input(prompt)
		print " "
		
		while choice == "player":
			player_check()
			
			print "Would you like to go North or South in the corridor?"
			choice = raw_input(prompt)
			print " "
		
		if "orth" in choice:
			print "You go North."
			second_intersection()
		
		else:
			print "You go South."
			first_intersection()
			
	elif "3" in choice3:
		print """
		As you attempt to take the Blue Book off the shelf, you feel it
		stick and then click mechanically into place as it comes forward. The book 
		gets sucked back onto the shelf and a panel in the wall moves aside,
		revealing a passageway.\n"""
		time.sleep(3)
		print "Do you enter the passageway?" 
				
		choice4 = raw_input(prompt)
		print " "
		
		while choice4 == "player":
			
			player_check()
			
			print "Do you enter the passageway?"
			choice4 = raw_input(prompt)
			print " "
				
		if "ye" in choice4:
			came_from = "West"
			
			print "The passageway is short and leads to a secret room!\n"
			
			if not first_time_secret_room:
				print "You're standing in the secret room you hung out in earlier.\n"
				time.sleep(2)
				print "You remember the good times you had, then you turn around"
				print "and leave the room because there's nothing in there anymore.\n" 
				print "Do you go North or South?"
				choice1 = raw_input(prompt)
				print " "
				
				while choice1 == "player":
					
					player_check()
					
					print "Do you go North or South?"
					choice1 = raw_input(prompt)
					print " "
						
				if "orth" in choice1:
					print "North you go!"
					second_intersection()
				
				else: 
					print "South it is!"
					first_intersection()
			
			while first_time_secret_room:
				
				first_time_secret_room = False
				enemy_encounter()
				
				print "Now that you stand victorious, you notice there is a shaft"
				print "of light highlighting a sweet looking chocolate danish on a"
				print "narrow pedestal.\n\n"
				time.sleep(2)
				
				print "\nYou examine it closely.\n\n"
				time.sleep(2)
				
				print "You don't want to put it in your satchel (messy!).\n"
				time.sleep(2)
				
				print "And it smells so good! You must eat it or leave it."
				time.sleep(2)
				
				print "\nEat it or leave it?"
				choice5 = raw_input(prompt)
				print " "
		
				while choice5 == "player":
					
					player_check()
			
					print "Do you eat the danish?"
					choice5 = raw_input(prompt)
					print " "
					
				if "eat" in choice5:
					print "You've never tasted anything so delicious and fresh!\n"
					time.sleep(1)
					
					if player_class == "Wizard":
						
						player_int += 1
						print "The danish expands your brain by five percent."
						print "Your intelligence has grown by one. It is now %d.\n" % player_int
						time.sleep(3)
						print "You leave the secret room."
						print "Do you go North or South?"
						choice1 = raw_input(prompt)
						print " "
						
						while choice1 == "player":
							player_check()
							print "Do you go North or South?"
							choice1 = raw_input(prompt)
							print " "
							
						if "orth" in choice1:
							print "North you go!"
							second_intersection()
						
						else: 
							print "South it is!"
							first_intersection()
							
					else:
						
						player_dex += 1
						print "The danish hones your muscles and heightens your quickness."
						print "Your dexterity has grown by one. It is now %d.\n" % player_dex
						time.sleep(3)
						print "You leave the secret room."
						print "Do you go North or South?"
						choice1 = raw_input(prompt)
						print " "
						
						while choice1 == "player":
							
							player_check()
							
							print "Do you go North or South?"
							choice1 = raw_input(prompt)
							print " "
							
						if "orth" in choice1:
							print "North you go!"
							second_intersection()
						
						else: 
							print "South it is!"
							first_intersection()	
							
				else:
					print "You back away from the danish... slowly back away.\n"
					time.sleep(3)
					print "Phew! That thing looked too delicious to be of any use!\n"	
					print "Do you go North or South?"
					choice1 = raw_input(prompt)
					print " "
					
					while choice1 == "player":
						
						player_check()
						
						print "Do you go North or South?"
						choice1 = raw_input(prompt)
						print " "
						
					if "orth" in choice1:
						print "North you go!"
						second_intersection()
					
					else: 
						print "South it is!"
						first_intersection()
			 	
		elif "no" in choice4:
			print """
			Yeah, who in their right mind would go in there!? It's probably 
			haunted or something. Definitely worth avoiding. You leave the panel and
			can now decide to go North or South in the corridor.\n"""
			came_from = "West"
			
			choice2 = raw_input(prompt)
			print " "
			
			while choice2 == "player":
				
				player_check()
				
				print "Would you like to go North or South in the corridor?"
				choice2 = raw_input(prompt)
				print " "
			
			if "orth" in choice2:
				print "You go North.\n"
				second_intersection()
			
			else:
				print "You go South.\n"
				first_intersection()
				
		else: 
			dead("Standing. Waiting. The floor opens and you fall into eternity.")
			
	else: 
		print "I wish I knew what you chose, but... you cryptic!"
		time.sleep(3)
		dead("""
		Standing and waiting, suddenly the floor 
		opens up and you fall onto some well made spikes.""")

def second_intersection():

	global came_from, player_hp

	print "You are at an intersection that has passageways to the South, West, and East."
	print "There is a dripping sound.\n"
	print "You came from the %s." % came_from
	time.sleep(1)
	print "Which way do you go?"
	
	choice = raw_input(prompt)
	print " "
	
	while choice == "player":
		
		player_check()
		
		print "Which way do you go?"
		choice = raw_input(prompt)
		print " "
	
	if "outh" in choice:
		print "You move South.\n"
		came_from = "North"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		first_intersection()
	
	elif "ast" in choice:
		print "You move East\n"
		came_from = "West"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		third_intersection()
	
	elif "est" in choice:
		print "You go West and come to an elbow leading South.\n"
		time.sleep(2)
		print "You follow the elbow and are in a corridor that smells like dust and decay.\n"
		time.sleep(2)
		print "As you walk you see a 6 inch bookcase on your right."
		print "There is a Red Book, a Green Book, and a Blue Book.\n"
		print "Do you move on or do you inspect a book?"
		
		choice2 = raw_input(prompt)
		print " "
		
		while choice2 == "player":
			
			player_check()
			
			print "Do you move on or do you inspect a book?"
			choice2 = raw_input(prompt)
			print " "
		
		if "move" in choice2:
			print "You go around the corner and come to another intersection.\n"
			came_from = "West"
			chance = randint(1, 100)
			
			if chance <= 50:
				enemy_encounter()
			first_intersection()
		
		elif "inspect" in choice2:
			
			secret_room_1()
	
	elif "orth" in choice:
		print "You try to head North, but run into the concrete wall.\n"
		player_hp -= 1
		print "You lost a hit point! you now have %d hit points.\n" % player_hp
		chance = randint(1, 100)
	
		if chance <= 50:
			enemy_encounter()
		second_intersection()
	else:
		dead("triggering dead")

def third_intersection():

	global came_from, player_hp
	
	print "You are at an intersection with passageways to the South, West, and East.\n"
	print "There is a door along the cleft wall to the South/West.\n"
	print "You came from %s." % came_from
	print "Which way do you go?"
	
	choice = raw_input(prompt)
	print " "
	
	while choice == "player":
		
		player_check()
	
		print "Which way do you go?"
		choice = raw_input(prompt)
		print " "
			
	if "door" in choice:
	
		first_room()
	
	elif "outh" in choice:
		print "You head South and hang a right, heading West, and"
		print "come to another intersection.\n"
		came_from = "East"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		
		first_intersection()
	
	elif "est" in choice:
		print "You head West and shortly come to another intersection.\n"
		came_from = "East"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		
		second_intersection()
	
	elif "ast" in choice:
		print "You head East... and the hallway turns slightly.\n"
		time.sleep(1)
		print "Following the turn you head up stone stairs.\n"
		time.sleep(1)
		
		chance = randint(1, 100)
		
		if chance <= 70:
			enemy_encounter()
			
		print "Upon reaching the top of the stairs, a great chamber comes into view!\n\n"
		came_from = "Southwest"
		
		first_chamber()
	
	elif "orth" in choice:
		
		print "You try to head North, but run into the concrete wall.\n"
		player_hp -= 1
		print "You lost a hit point! you now have %d hit points.\n" % player_hp
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		
		third_intersection()
	
	else:
		dead("Triggering DEATH")
	
	third_intersection()

def first_room():
	
	global satchel_contents, came_from, first_time_first_room
	came_from = "The Room"
	
	print "You open the door and step into a stark, dark room!\n\n"
	time.sleep(1)
	
	chance = randint(1, 100)
	if chance <= 70:
		enemy_encounter()
	
	while first_time_first_room:
	
		first_time_first_room = False
	
		print "You notice a cube of stone in the center of the room and sitting"
		print "atop the stone are three precious gems.\n"
		time.sleep(1)
		print "There is an Emerald, a Ruby, and a Sapphire.\n\n"
		print "What do you do?\n"
		print "\t1. Take the Emerald."
		print "\t2. Take the Ruby."
		print "\t3. Take the Sapphire."
		print "\t4. Take the Emerald & Ruby."
		print "\t5. Take the Emerald & Sapphire."
		print "\t6. Take the Ruby & Sapphire."
		print "\t7. Take all 3 stones."
		print "\t8. Take nothing and leave the room.\n" 
	
		choice = raw_input(prompt)
		print " "
		
		while choice == "player":
			player_check()
			
			print "What do you do?\n"
			print "\t1. Take the Emerald."
			print "\t2. Take the Ruby."
			print "\t3. Take the Sapphire."
			print "\t4. Take the Emerald & Ruby."
			print "\t5. Take the Emerald & Sapphire."
			print "\t6. Take the Ruby & Sapphire."
			print "\t7. Take all 3 stones."
			print "\t8. Take nothing and leave the room.\n" 
			choice = raw_input(prompt)
			
				
		if choice == "1":
			
			print "You grab the Emerald.\n"
			time.sleep(2)
			dead("Although the pain was searing, it was brief. You dead.")
			
		elif choice == "2":
			
			print "You pick up the Ruby and put it in your bag.\n"
			satchel_contents.append("Ruby")
			print "Now what do you do?"
			print "\t1. Take the Emerald."
			print "\t2. Take the Sapphire."
			print "\t3. Take the Emerald & Sapphire."
			print "\t4. Take nothing more and leave the room.\n"
			
			choice2 = raw_input(prompt)
			
			while choice2 == "player":
				player_check()
				
				print "Now what do you do?"
				print "\t1. Take the Emerald."
				print "\t2. Take the Sapphire."
				print "\t3. Take the Emerald & Sapphire."
				print "\t4. Take nothing more and leave the room.\n"
				choice2 = raw_input(prompt)
				
			if choice2 == "1":
				
				print "You grab the Emerald.\n"
				time.sleep(2)
				dead("Although the pain was searing, it was brief. You dead.")
				
			elif choice2 == "2":
				
				print "You pick up the Sapphire and put it in your bag.\n"
				satchel_contents.append("Sapphire")
				print "Now what do you do?"
				print "\t1. Take the Emerald."
				print "\t2. Take nothing more and leave the room.\n"
				
				choice3 = raw_input(prompt)
				
				while choice3 == "player":
					player_check()
					
					print "Now what do you do?"
					print "\t1. Take the Emerald."
					print "\t2. Take nothing more and leave the room.\n"
					choice3 = raw_input(prompt)
					
				if choice3 == "1":
					
					print "You grab the Emerald.\n"
					time.sleep(2)
					dead("Although the pain was searing, it was brief. You dead.")
					
				else: 
					third_intersection()
					
			elif choice2 == "3":
				
				print "You grab the Sapphire & Emerald.\n"
				time.sleep(2)
				dead("Although the pain was searing, it was brief. You dead.")
				
			else: 
				print "You're finished in this room." 
				third_intersection()
		
		elif choice == "3":
			
			print "You pick up the Sapphire and put it in your bag.\n"
			satchel_contents.append("Sapphire")
			print "Now what do you do?"
			print "\t1. Take the Emerald."
			print "\t2. Take the Ruby."
			print "\t3. Take the Emerald & Ruby."
			print "\t4. Take nothing more and leave the room.\n"
			
			choice2 = raw_input(prompt)
			
			while choice2 == "player":
				player_check()
				
				print "Now what do you do?"
				print "\t1. Take the Emerald."
				print "\t2. Take the Ruby."
				print "\t3. Take the Emerald & Ruby."
				print "\t4. Take nothing more and leave the room.\n"
				choice2 = raw_input(prompt)
				
			if choice2 == "1":
				
				print "You grab the Emerald.\n"
				time.sleep(2)
				dead("Although the pain was searing, it was brief. You dead.")
				
			elif choice2 == "2":
				
				print "You pick up the Ruby and put it in your bag.\n"
				satchel_contents.append("Ruby")
				print "Now what do you do?"
				print "\t1. Take the Emerald."
				print "\t2. Take nothing more and leave the room.\n"
				
				choice3 = raw_input(prompt)
				
				while choice3 == "player":
					player_check()
					
					print "Now what do you do?"
					print "\t1. Take the Emerald."
					print "\t2. Take nothing more and leave the room.\n"
					choice3 = raw_input(prompt)
					
				if choice3 == "1":
					
					print "You grab the Emerald.\n"
					time.sleep(2)
					dead("Although the pain was searing, it was brief. You dead.")
					
				else: 
					third_intersection()
					
			elif choice2 == "3":
				
				print "You grab the Ruby & Emerald.\n"
				time.sleep(2)
				dead("Although the pain was searing, it was brief. You dead.")
				
			else: 
				print "You're finished in this room." 
				third_intersection()
				
		elif choice == "4":
			
			print "You grab the Ruby and the Emerald.\n"
			time.sleep(2)
			dead("Although the pain was searing, it was brief. You dead.")
			
		elif choice == "5":
			
			print "You grab the Sapphire and the Emerald.\n"
			time.sleep(2)
			dead("Although the pain was searing, it was brief. You dead.")
			
		elif choice == "6":
			
			print "You grab the Ruby and the Sapphire and put them in your bag.\n"
			satchel_contents.append("Ruby")
			satchel_contents.append("Sapphire")
			print "What do you do now?\n"
			print "\t1. Take the Emerald."
			print "\t2. Take nothing more and leave the room.\n"
			
			choice2 = raw_input(prompt)
			
			while choice2 == "player":
				player_check()
				
				print "What do you do now?\n"
				print "\t1. Take the Emerald."
				print "\t2. Take nothing more and leave the room.\n"
				choice2 = raw_input(prompt)
				
			if choice2 == "1":
				
				print "You grab the Emerald.\n"
				time.sleep(2)
				dead("Although the pain was searing, it was brief. You dead.")
				
			else: 
				print "You're totally done in this room. Booyah!"
				third_intersection()
		
		elif choice == "7":
			
			print "You take the stones, Sapphire, Ruby, and Emerald.\n"
			time.sleep(2)
			dead("Was it your greed?! Something seared into you and you disintigrate on the spot.")
			
		else: 
			print "Yeah, who needs those stones anyway? I'm sure they're worthless in here...\n"
			third_intersection()
					
	print "You stand in the familiar doorway. All of the rubies have vanished.\n"
	time.sleep(3)
	print "You sniff and cry a little, then you get over it and get back to the hallway.\n"
	
	third_intersection()

def first_chamber():

	global came_from, first_time_chamber_one
	
	print "The chamber before you is a grand open chamber.\n"
	time.sleep(1)
	print "There are doors exiting the chamber in all directions,"
	print "and the grass floor has a slight covering of snow.\n"
	time.sleep(2)
	print "Great slabs of concrete act as a sort of Stonehenge"
	print "circling the chamber.\n\n" 
	print "You came from the %s.\n" % came_from
	
	if first_time_chamber_one:
		print "You see an older boy chained to a chair in the middle of the chamber."
		time.sleep(1)
		print "He is shivering yet not looking weak.\n"
		time.sleep(1)
	
	else: 
		print "You are alone in the chamber.\n"
	
	print "What would you like to do? Approach the boy or take a door?" 
	answer = raw_input(prompt)
	print " " 
	
	while answer == "player":
		player_check()
		
		print "So what'll it be? Approach the boy or take a door?"
		answer = raw_input(prompt)
		print " "
	
	if "boy" in answer:
		
		print "You approach the boy."
		time.sleep(1)
		print "He looks up at hearing your footsteps.\n"
		time.sleep(1)
		print "'Hello there! I haven't seen anyone in so long, I don't even"
		print "know how I'm still alive.'\n"
		time.sleep(2)
		print "'Are you here to help me?'\n"
		
		answer1 = raw_input(prompt)
		
		while answer1 == "player":
			
			player_check()
			
			print "'Are you here to help me?'"
			answer1 = raw_input(prompt)
			print " "
			
		if "ye" in answer1:
			print "'Wonderful! My chains are secured to the ground by stone.'"
			print "'Are you able to free me?'"
			answer2 = raw_input(prompt)
			print " " 
			
			while answer2 == "player":
				player_check()
				
				print "'Are you able to free me?'"
				answer2 = raw_input(prompt)
				print " "
				
			if "ye" in answer2:
				print "'Excellent! I'm waiting'"
				choice = raw_input(prompt)
			
			else:
				print "'Oh well, maybe later.'"
		
		else: 
			print "That's okay. I kind of like this chair anyway. I do miss"
			print "the freedom though. I got used to that before I was tied here.\n"
			time.sleep(2)
			print "It's fine. I'll be fine. Have fun out there.\n" 

	elif "door" in answer:
		
		print "Which door would you like to take?"
		
		came_from = "Chamber"
		
		print """
		1. West
		2. Northwest
		3. North
		4. Northeast
		5. East
		6. Southeast
		7. South
		8. Southwest"""
		
		answer3 = raw_input(prompt)
		
		while answer3 == "player":
			
			player_check()
			
			print "Which door would you like to take?"
			print """
			1. West
			2. Northwest
			3. North
			4. Northeast
			5. East
			6. Southeast
			7. South
			8. Southwest"""
			
			answer3 = raw_input(prompt)
		
		if answer3 == "1":
			print "You go through the west leading door and arrive shortly"
			print "at a T-intersection.\n"
			
			sixth_intersection()
		
		elif answer3 == "2":
			print "You go through the northwest leading door."
			print "It leads you down a stone stairway.\n"
			
			seventh_intersection()
		
		elif answer3 == "3":
			print "You go through the north leading door.\n"
			
			twelfth_intersection()
		
		elif answer3 == "4":
			print "You go through the northeast leading door.\n"
			
			vendor_room()
		
		elif answer3 == "5":
			print "You go through the east leading door and arrive at a four way"
			print "intersection.\n"
			
			eighth_intersection()
		
		elif answer3 == "6":
			print "You go through the southeast leading door.\n"
			
			third_room()
		
		elif answer3 == "7":
			print "You go through the south leading door and come to a"
			print "T-intersection.\n"
			
			fourth_intersection()
		
		elif answer3 == "8":
			print "You go through the southwest leading door and walk down some"
			print "stone steps.\n"
			
			third_intersection()
		
		else: 
			print "You're still in the chamber.\n" 
			
			first_chamber()
	
	else: 
		first_chamber()
		
def fourth_intersection():

	global came_from
	
	print "You are at a mossy intersection that branches West, East, and North.\n"
	print "You came from the %s." % came_from
	
	print "Which way do you go?"
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "est" in answer:
		print "You head west and...\n"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		
		print "...you come to a large room!\n" 
		came_from = "East"
		
		second_room()
	
	elif "ast" in answer:
		print "You head east and...\n"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		
		print "...you come to another intersection.\n"
		came_from = "West"
		
		fifth_intersection()
	
	else: 
		print "You head north and...\n"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		
		print "... you enter the chamber.\n" 
		came_from = "South"
		
		first_chamber()

def fifth_intersection():
	
	global came_from
	
	print "You are at an intersection that branches West and East."
	print "There is a branch to the South whose end is visible.\n"
	print "Do you go East or West or South?\n"
	print "You came from the %s." % came_from
	
	print "Which way do you go?"
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
		
	if "outh" in answer:
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You walk to the small dead end. In the floor, centered a few feet"
		print "from the back wall, stands a small pedestal with a circular top.\n"
		time.sleep(2)
		choice = raw_input(prompt)
		
		print "You cannot find any way to interact with the pedestal so you turn"
		print "back around.\n"
		came_from = "South"
		
		fifth_intersection()
	
	elif "ast" in answer: 
		print "You abruptly come upon the edge of a pit.\n" 
		time.sleep(2)
		print "You can see the other side, though it is quite a distance." 
		print "There is tree trunk punched through the labryinth walls.\n"
		time.sleep(2)
		print "The trunk is well above you and in between the path you stand on"
		print "and the path across the pit.\n"
		print "Do you do something or go back?"
		to_do = raw_input(prompt)
		
		if "back" in to_do:
			
			came_from = "East"
			
			fifth_intersection()
			
	else:
		print "You head West and...\n"
		came_from = "West"
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "...you come to another intersection.\n"
		fourth_intersection()

def sixth_intersection():

	global came_from
	
	print "You can see that both the North and the South paths turn a"
	print "corner heading in the same direction. You can go North, South, or East.\n"
	print "You came from %s.\n" % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "outh" in answer:
		print "You head South, turning the corner to the West.\n" 
		time.sleep(2)
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You walk along a narrow corridor until you reach an elbow heading"
		print "North. Now you walk and stop between two walls.\n" 
		time.sleep(2)
		print "On your left the wall is blank. On the right there are three"
		print "protruding circles.\n" 
		print "You can go North or South or examine the wall."
		answer1 = raw_input(prompt)
		while answer1 == "player":
			player_check()
			
			print "You can go North or South or examine the wall.\n"
			answer1 = raw_input(prompt)
		
		if "xamin" in answer1:
			print "Looking more closely, you see that the circles move, but you"
			print "you cannot make odds or ends of it.\n" 
		
			sixth_intersection()
		
		elif "outh" in answer1: 
			print "You go South.\n"
			
			sixth_intersection()
		
		else:
			print "You go North.\n"
			
			sixth_intersection()
			
	elif "orth" in answer: 
		
		print "You head North, turning the corner to the West.\n" 
		time.sleep(2)
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You walk along a narrow corridor until you reach an elbow heading"
		print "South. Now you walk and stop between two walls.\n" 
		time.sleep(2)
		print "On your right the wall is blank. On the left there are three"
		print "protruding circles.\n" 
		print "You can go North or South or examine the wall.\n"
		answer1 = raw_input(prompt)
		
		while answer1 == "player":
			player_check()
			
			print "You can go North or South or examine the wall.\n"
			answer1 = raw_input(prompt)
		
		if "xamin" in answer1:
			print "Looking more closely, you see that the circles move, but you"
			print "you cannot make odds or ends of it.\n"
			print "You keep walking."
			
			sixth_intersection()
		
		elif "outh" in answer1: 
			print "You go South.\n"
			chance = randint(1, 100)
			if chance <= 50:
				enemy_encounter()
				
			sixth_intersection()
		
		else:
			print "You go North.\n"
			chance = randint(1, 100)
			if chance <= 50:
				enemy_encounter()
				
			sixth_intersection()
	else: 
		first_chamber()

def seventh_intersection():

	global came_from
	
	print "You come to a three-way intersection." 
	print "The paths go West or North or Southeast up the stairs.\n"
	print "You came from the %s.\n" % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "est" in answer: 
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You head West and shortly come to a dead end. It's different than"
		print "a normal dead end, because the top of the wall at this dead end"
		print "is much shorter than the walls surrounding it.\n"
		time.sleep(3)
		print "You can't do anything at this time so you go back to the intersection.\n"
		came_from = "West"
		seventh_intersection()
	
	elif "orth" in answer:
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You head North and come to another intersection.\n"
		came_from = "South"
		eleventh_intersection()
	
	else:
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You head up the stairs to the Southeast.\n"
		came_from = "Northwest"
		first_chamber()

def eighth_intersection():

	global came_from
	
	print "You stand in a four-way intersection."
	print "You can go North, South, East, or West.\n"
	print "You came from the %s.\n" % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "orth" in answer:
		print "You head North.\n"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		print "You've come to another intersection.\n"
		came_from = "South"
		
		grand_hallway()
	
	elif "outh" in answer:
		print "You head South.\n"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		
		print "The corridor turns an elbow to the east.\n" 
		time.sleep(2)
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		print "The corridor turns into a dead end. The wall at the end has"
		print "an intricately carved inlay on the wall, centered by a hollow"
		print "circular form.\n" 
		print "You can't seem to do anything, so you turn around and go back.\n"
		came_from = "South"
		
		eighth_intersection()
	
	elif "ast" in answer:
		print "You head East and enter a long room.\n"
		enemy_encounter()
		
		fourth_room()
	
	else:
		print "You head West.\n"
		
		first_chamber()

def ninth_intersection():

	global came_from
	
	print "You stand at a three-way intersection."
	print "You can go North, South, or East.\n"
	print "You came from the %s.\n" % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "ast" in answer:
		print "You head East and immediately the corridor takes you South.\n"
		print "You come to a dead end with a portrait hanging on the wall.\n"
		time.sleep(2)
		print "The portrait is of the old woman you saw at the beginning of"
		print "the labryinth.\n"
		came_from = "East"
		
		ninth_intersection()
	
	elif "orth" in answer:
		print "You head North.\n"
		came_from = "South"
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You find yourself at the back of a Grand Hallway.\n"
		
		grand_hallway()
	
	else:
		print "You head South.\n"
		came_from = "North"
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		
		eighth_intersection()
		
# incomplete def tenth_intersection():

def eleventh_intersection():
	
	global came_from
	
	print "You stand at an intersection that leads North, East, or South.\n"
	print "You came from the %s.\n" % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "orth" in answer:
		print "You approach the mouth of a cave!\n" 
		print "Do you go into the cave?"

		answer1 = raw_input(prompt)
		print " "
		
		while answer1 == "player":
			player_check()
			
			print "Do you go into the cave?"
			answer1 = raw_input(prompt)
			print " "
		
		if "ye" in answer1:
			came_from = "South"
			battle_cave()
		
		else: 
			eleventh_intersection()
	
	elif "ast" in answer: 
		print "You head East along a long corridor.\n"
		time.sleep(2)
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		print "You come to a large intersection.\n"
		came_from = "West"
		
		twelfth_intersection()
	
	elif "outh" in answer:
		print "You head South.\n"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		came_from = "North"
		
		seventh_intersection()
	
	else: 
		print "Dunno why.\n"
		seventh_intersection()
	
def twelfth_intersection():

	global came_from
	
	print "The large intersection holds an immense Grand Hallway to the East.\n"
	print "You may go East to the hallway or North or South or West.\n"
	print "You came from the %s." % came_from
	chance = randint(1, 100)
	
	if chance <= 50:
		enemy_encounter()
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "ast" in answer:
		print "You find yourself in the Grand Hallway.\n"
		chance = randint(1, 100)
		
		if chance <= 80:
			enemy_encounter()
		
		grand_hallway()
	
	elif "outh" in answer:
		print "You head South.\n"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		came_from = "North"
		
		first_chamber()
	
	elif "est" in answer:
		print "You head West.\n"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		came_from = "East"
		
		eleventh_intersection()
	
	else:
		print "That part of the labryinth hasn't been coded yet.\n\n"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		
		twelfth_intersection()		

def second_room():

	global came_from, defeat_goblin_king
	came_from = "East"
	
	print "You enter a large room, its walls covered in stone carved flowers.\n\n\n" 
	print "You came from the %s.\n" % came_from
	
	enemy_encounter()
	
	print "\n\nAn eerie silence falls upon the room after your battle.\n"
	print "There is a plant in a pot on a stone slab in the middle of the room."
	print "Beside this pot is another pot, though empty.\n"
	print "On the ground, there is a container of what looks like fresh potting soil.\n"
	print "What do you do?\n"
	print "\t1. Use an item."
	print "\t2. Take the empty pot."
	print "\t3. Take the potted plant."
	print "\t4. Put the new soil in the empty pot with your hands and re-pot the plant."
	print "\t5. Do nothing and leave the room."
	answer = raw_input(prompt)
	
	while answer == "player":
		player_check()
		
		print "What do you do?\n"
		print "\t1. Use an item."
		print "\t2. Take the empty pot."
		print "\t3. Take the potted plant."
		print "\t4. Put the new soil in the empty pot with your hands and re-pot the plant."
		print "\t5. Do nothing and leave the room.\n"
		answer = raw_input(prompt)
	
	if answer == "1":
		
		print "Which item would you like to use?"
		answer2 = raw_input(prompt)
		
		while answer2 == "player":
			player_check()
			
			print "Which item would you like to use?"
			answer2 = raw_input(prompt)
		
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
		
		print "You back away slowly, touching nothing.\n"
				
	
	print "You exit the room and come to an intersection.\n"
	
	came_from = "West"
	
	fourth_intersection()

def third_room():
	
	global came_from
	
	print "The door you took leads directly into a small room."
	print "You came from the %s.\n" % came_from
	
	enemy_encounter()
	
	print "There is some sweet art in this room. Dang. Good stuff.\n"
	time.sleep(2)
	print "You head back to the chamber."
	
	came_from = "Southeast"
	
	first_chamber()
	
def fourth_room():
	
	print "In the fourth room.\n"
	time.sleep(2)
	print "Now leaving. Room incomplete.\n"
	
	eighth_intersection()
	
def vendor_room():

	global came_from
	
	print "You enter a triangle shaped room.\n"
	print "You see an old man sitting behind a wooden shelf in the far corner of"
	print "the room. He's crotcheting.\n" 
	time.sleep(1)
	print "\nWould you like to talk to him?"
	answer = raw_input(prompt)
	
	while answer == "player":
		
		player_check()
		
		print "Would you like to talk to him?\n"
		answer = raw_input(prompt)
	
	if "ye" in answer: 
	
		print "You step forward to talk to him.\n" 
		vendor()
	
	else:
		print "You go back to the Chamber.\n" 
		came_from = "Northeast"
		first_chamber()
	
def vendor():
	
	global satchel_contents, player_hp_dmg, gold
	
	trading_block = []
	use = "blank"
	loot = "blank"
	count = 0
	item_loc = 0
	
	print "The vendor looks up from his chiseling and looks you in the eye.\n"
	time.sleep(1)
	print "Vendor: It's been a long time since I've seen a stranger."
	print "What can I help you with?\n"
	print "1. Trade \t2. Sell \t3. Heal \t4. Enemies \t5. Items"
	selection = raw_input(prompt)
	
	while selection == "player":
		
		player_check()
		
		print "1. Trade \t2. Sell \t3. Heal \t4. Enemies \t5. Items"
		selection = raw_input(prompt)
	
	if selection == "1":
		
		if satchel_contents == []:
			
			print "It looks like your satchel is empty. What are you trying to pull?\n" 
			vendor_room()
		
		print "What would you like to trade?"
		trade = raw_input(prompt)
		while trade == "player":
			
			player_check()
			
			print "What would you like to trade?"
			trade = raw_input(prompt)
		
		for item in satchel_contents:
			if item == trade:
				trading_block.append(satchel_contents[count])
				item_loc = count
			count += 1
			
		print "Ahh, you have a %s." % trading_block[0]
		print "I have this to trade:\n"
		if 0 < player_lvl < 4:
			print "***Thick Shirt***\n"
			loot = "Thick Shirt"
			use = "+1 Defense"
		elif 3 < player_lvl < 7:
			print "***Leather T-Shirt***\n"
			loot = "Leather T-Shirt"
			use = "+2 Defense"
		elif 6 < player_lvl:
			print "***Leather Jacket***\n"
			loot = "Leather Jacket"
			use = "+3 Defense"
		time.sleep(2)
		print "Would you like to trade? Straight up? Mine for yours?" 
		answer = raw_input(prompt)
		
		while answer == "player":
			
			player_check()
			
			print "Would you like to trade? Straight up?"
			answer = raw_input(prompt)
		
		if "ye" in answer:
			
			print "Ok, good deal!"
			satchel_contents.pop(item_loc)
			satchel_contents.append(loot)
			
			print "This is what is in your satchel:"
			for item in satchel_contents:
				print item + " " 
			
		else: 
			print "Oh well.\n" 
			vendor_room()
	
	elif selection == "2":
		
		if satchel_contents == []:
			
			print "It looks like your satchel is empty. What are you trying to pull?\n" 
			vendor_room()
		
		print "What would you like to sell?"
		trade = raw_input(prompt)
		while trade == "player":
			
			player_check()
			
			print "What would you like to sell?"
			trade = raw_input(prompt)
		
		
		for item in satchel_contents:
			if item == trade:
				trading_block.append(satchel_contents[count])
				item_loc = count
			count += 1
		
		print "Ahh, you have a %s." % trading_block[0]
		print "I will give you 50 gold for the %s." % trading_block[0]
		print " "
		choice2 = raw_input(prompt)
		
		if "ye" in choice2:
			
			print "Great!\n"

			if trade in satchel_contents:
					
				satchel_contents.pop(item_loc)
				print "You received 50 gold!\n"
				gold += 50
				print "You have %d gold now." % gold
		
		else: 
			
			print "Fine. I didn't want it anyway.\n" 
			vendor_room()
		
	elif selection == "3": 
		
		print "You want me to heal yah, huh?"
		time.sleep(1)
		print "There was a time a was known as a healer.\n"
		print "I see that you currently have %d hit points." % player_hp_dmg
		print "That is %d less than your maximum!\n" % (player_hp - player_hp_dmg)
		
		if player_hp_dmg <= 2:
			print "I can hardly believe you're still alive.\n"
		
		print "\nI s'pose I could do that. For a price." 
		time.sleep(2)
		print "It'll cost you a rare gem to heal yourself.\n\n"
		print "I know that's a valuable item, but they're probably just laying around somewhere to find." 
		if satchel_contents == []:
			
			print "It looks like you don't have any gems. See ya.\n" 
			vendor_room()
		
		print "Which gem do you want to give me in exchange for full health?" 
		choice = raw_input(prompt)
		
		while choice == "player":
			
			player_check()
			
			print "Which gem do you want to give me in exchange for full health?"
			choice = raw_input(prompt)
		
		if "uby" in choice: 
				
			if "Ruby" in satchel_contents:
				
				satchel_contents.remove("Ruby")
				print "Okay, looks good. I took your Ruby.\n"
				time.sleep(2)
				print "I will now perform a miracle of healing!!"
				time.sleep(4)
				print "\n\nYou have been healed!" 
				player_hp_dmg = player_hp
				print "You now have %d hit points.\n" % player_hp_dmg
				vendor_room()
					
			else: 
				print "You don't have a Ruby.\n" 
				vendor_room()
				
		elif "hire" in choice:
			
			if "Sapphire" in satchel_contents:
				
				satchel_contents.remove("Sapphire")
				print "Okay, looks good. I took your Sapphire.\n"
				time.sleep(2)
				print "I will now perform a miracle of healing!!"
				time.sleep(4)
				print "\n\nYou have been healed!" 
				player_hp_dmg = player_hp
				print "You now have %d hit points.\n" % player_hp_dmg
				vendor_room()
					
			else: 
				print "You don't have a Sapphire.\n" 
				vendor_room()
			
		else: 
			print "I'm glad, tbh. It means I can conserve my energy.\n\n" 
			vendor_room()	
			
	elif selection == "4":
		
		print "You want to learn about the enemies of this dungeon, do yah?\n"
		print "Well, because we're in a beta version, I can do that for you." 
		print_enemies_full()
		time.sleep(4)
		vendor_room()
		
	else: 
		
		print "What item would you like to learn about?" 
		answer = raw_input(prompt)
		
		while answer == "player":
			player_check()
			
			print "What item would you like to learn about?"
			answer = raw_input(prompt)
			
		if answer == "list all items":
			
			print_items_full()
			time.sleep(4)
			vendor_room()
		
		elif answer in satchel_contents:
			
			print "Ah, yes, the %s!\n" % answer
			time.sleep(2)
			print "As far as I'm aware, this is what the %s does:\n" % answer
			print loot_dict[answer]
			vendor_room()
		
		else:
			
			print "I don't know what you're talking about.\n"
			vendor_room()
	
def battle_cave():
	
	global came_from, battle_cave_furthest, battle_cave_there_and_back, high_scorer_bcf
	global high_scorer_bctb, high_scorer_cave, high_scorer_furthest
	
	count = 0
	battle_cave_count = 0
	
	print "You enter the cave.\n" 
	print "It stinks like death and you hear living sounds beyond the darkness.\n"
	print "You can only see about five feet in front of you.\n\n\n"
	print "Do you go forward?"
	answer = raw_input(prompt)
	
	while answer == "player":
		player_check()
		
		print "Do you go forward?"
		answer = raw_input(prompt)
	
	while "ye" in answer:
		print "You move forward.\n"
		enemy_encounter()
		count += 1
		battle_cave_count += 1
		if high_scorer_furthest == False: 
			
			if battle_cave_count > battle_cave_furthest:
				
				high_scorer_furthest = True
				print "You have gone the furthest of any Battle Cave Explorer!\n" 
				battle_cave_furthest = battle_cave_count
				high_scorer_bcf = raw_input("Enter your name so it can rest atop the leaderboard: ")
		
		if battle_cave_count > battle_cave_furthest:
				
			battle_cave_furthest = battle_cave_count
		
		if count == 4:
			print "You have come across one of the Old Woman's Sons!\n"
			print "Would you like to bring him back with you?\n"
			# hero makes trips back with the sons, to deliver them to mama	
		
		print "Do you go forward?"
		answer = raw_input(prompt)
	
		while answer == "player":
			player_check()
			
			print "Do you go forward?"
			answer = raw_input(prompt)
	
	while count > 0:
		print "You move back toward the entrance.\n"
		enemy_encounter()
		count -= 1
		battle_cave_count += 1
			
	if battle_cave_count > battle_cave_there_and_back:
				
		print "You have survived the longest trip into the Battle Cave!\n" 
		battle_cave_there_and_back = battle_cave_count	
		high_scorer_bctb = raw_input("Enter your name so it can rest atop the leaderboard: ")

	else: 
		
		eleventh_intersection()
	
	came_from = "The Cave"
	eleventh_intersection()

# incomplete ritual_room()

def grand_hallway():
	
	global came_from
	
	print "There are ornately carved pillars lining the North and South walls"
	print "and you see an exit at the Southeast end of the Hallway.\n" 
	print "Do you go West down the corridor or South, or Southeast?"
	print "You came from the %s.\n" % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " " 
	
	if "est" in answer:
		print "Going West.\n"
		came_from = "East"
		
		eleventh_intersection()
		
	elif "outh" in answer:
		print "Going South.\n"
		came_from = "North"
		
		first_chamber()
	
	else:
		print "You walk to the end of the Grand Hallway and exit to the South.\n"
		came_from = "North"
		
		ninth_intersection()
			
def dead(why):
	
	global player_hp_dmg
	
	print why
	
	print "test version. Would you like to reload with all yo stats & lvl?"
	quandry = raw_input(prompt)
	
	if "y" in quandry:
	
		player_hp_dmg = player_hp
		battle_cave()
	
	print "Would you like to play again? y or n?"
	
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Would you like to play again? y or n?"
		answer = raw_input(prompt)
		print " "
		
	if "y" in answer:
		start()
	
	else: 
		exit(0)

start()

