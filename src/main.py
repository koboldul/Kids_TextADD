from random import randint

classes = ['fighter', 'warlock', 'ranger']
races = ['human', 'daemon', 'elf']
weapons = ['maul', 'longsword', 'longbow']
#0: class 1:race_idx 2:weapon_idx 3:hp_idx 

class_idx = 0
race_idx = 1
weapon_idx = 2
hp_idx = 3

player = [0] * 4   

# def collect_info(feature_list, feature, feature_idx):
#     global player

#     print('(choose a ' + feature + ' )')

#     for i in range(0, len(feature_list)):
#         print (str(i+1) + '. ' + feature_list[i])

#     player[feature_idx] = int(input()) - 1

# print('Hello hero! You are in a sordid tavern when a stranger walk up to you and asks:')
# print('My name is armir and Im a great warrior but Im in need of help my job to you is ')

# collect_info(classes, 'class', class_idx)
# print ('I rarely see a')

# collect_info(races, 'race_idx', race_idx)
# print ('around this parts.')

# collect_info(weapons, 'weapon_idx', weapon_idx)
# print('you have there')

# hit_pnt = randint(20, 100)
# player[hp_idx] = hit_pnt

# print('Class: ' + classes[player[class_idx]] + ' Race: ' + races[player[race_idx]] + ' Weapon: ' + weapons[player[weapon_idx]] + ' HP: ' +  str(player[hp_idx]))

mob_races_lvl_1 = ['goblin', 'orc', 'giant rat']
mob_weapons_lvl_1 = ['dagger', 'rusty sword']
mob_classes_lvl_1 = ['fighter', 'warlock', 'ranger']

mob_class_idx = 0
mob_race_idx = 1
mob_weapon_idx = 2
mob_hp_idx = 3

mob_weapon_idx = randint(1, len(mob_weapon_lvl_1)

mob_class_idx = randint(0, len(mob_classes_lvl_1))

mob_race_idx = randint(0, len(mob_races_lvl_1))

mob_hp = randint(1, 7)
mob[mob_hp_idx] = 

print('mob race: ' +  mob_races_lvl_1[mob_race]  +' mob weapon: ' + mob_weapon + ' mob class: ' + classes[mob_class] + ' mob hp ' + str(mob_hp ))





    
    
    
