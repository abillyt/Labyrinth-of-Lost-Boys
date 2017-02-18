#starting Feb 17th, after 'round 80 commits on GitHub ~ 1500 lines written b4 GH

# overall game stats
overall_games_played = 0 
most_used_char_name = ""
least_used_char_name = ""
most_used_char_class = ""
least_used_char_class = ""
highest_lvl_attained = 1
highest_satchel_quan = 0

# battle stats
battle_win_avg = 0
bwa_name = "" # 4 char max
bwa_char_name = ""
bwa_char_class = ""
bwa_char_lvl = 1
bwa_char_str = 1
bwa_char_dex = 1
bwa_char_int = 1
bwa_satchel_quantity = 1

battle_loss_avg = 0
bla_name = "" # 4 char max
bla_char_name = ""
bla_char_class = ""
bla_char_lvl = 1
bla_char_str = 1
bla_char_dex = 1
bla_char_int = 1
bla_satchel_quantity = 1

battle_least = 0
bl_name = "" # 4 char max
bl_char_name = ""
bl_char_class = ""
bla_char_lvl = 1
bla_char_str = 1
bla_char_dex = 1
bla_char_int = 1
bla_satchel_quantity = 1

battle_count_most = 0
bwm_name = "" # 4 char max
bwm_char_name = ""
bwm_char_class = ""
bwm_char_lvl = 1
bwm_char_str = 1
bwm_char_dex = 1
bwm_char_int = 1
bwm_satchel_quantity = 1

battle_cave_furthest = 0
bcf_name = "" # 4 char max
bcf_char_name = ""
bcf_char_class = ""
bcf_char_lvl = 1
bcf_char_str = 1
bcf_char_dex = 1
bcf_char_int = 1
bcf_satchel_quantity = 1

battle_cave_there_and_back = 0
bctb_name = "" # 4 char max
bctb_char_name = ""
bctb_char_class = ""
bctb_char_lvl = 1
bctb_char_str = 1
bctb_char_dex = 1
bctb_char_int = 1
bctb_satchel_quantity = 1

user_names = []
user_name_count = []

def addNamesAndCount(name):
  spot = 0

  if name in user_name:

	  for x in range(len(user_name)):
		
		  if name == user_name[x]:
		  	spot = user_name_count[x]
		  	spot += 1
		  	user_name_count[x] = spot			


  else: 
  	user_name.append(name)
  	user_name_count.append(1)


    
print "\t\t-=Character Names Used=-"
for x in range(len(user_names)):

	print "\tName:   %s   |      Spawns:   %s" % (user_names[x], user_name_count[x])
