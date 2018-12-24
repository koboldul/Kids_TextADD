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

def collect_info(feature_list, feature, feature_idx):
    global player

    print('(choose a ' + feature + ' )')

    for i in range(0, len(feature_list)):
        print (str(i+1) + '. ' + feature_list[i])

    player[feature_idx] = int(input()) - 1

def print_stats(stats, class_list, race_list, weapon_list):
    print('Class: ' + class_list[stats[class_idx]] + ' Race: ' + race_list[stats[race_idx]] + ' Weapon: ' + weapon_list[stats[weapon_idx]] + ' HP: ' +  str(stats[hp_idx]))


print('Hello hero! You are in a sordid tavern when a stranger walk up to you and asks:')
print('My name is armir and Im a great warrior but Im in need of help my job to you is ')

collect_info(classes, 'class', class_idx)
print ('I rarely see a')

collect_info(races, 'race_idx', race_idx)
print ('around this parts.')

collect_info(weapons, 'weapon_idx', weapon_idx)
print('you have there')

hit_pnt = randint(20, 100)
player[hp_idx] = hit_pnt

print_stats(player, classes, races, weapons)

mob_races_lvl_1 = ['goblin', 'orc', 'giant rat']
mob_weapons_lvl_1 = ['dagger', 'rusty sword']
mob_classes_lvl_1 = ['fighter', 'warlock', 'ranger']

widx = randint(0, len(mob_weapons_lvl_1)-1)
cidx = randint(0, len(mob_classes_lvl_1)-1)
ridx = randint(0, len(mob_races_lvl_1)-1)

mob = [0] * 4 

mob_hp = randint(1, 7)
mob[hp_idx] = mob_hp
mob[class_idx]=cidx
mob[race_idx]=ridx
mob[weapon_idx]=widx
print ('idx c ' + str(cidx) + ' w: ' + str(widx) +  '  r ' + str(ridx))

print_stats(mob, mob_classes_lvl_1, mob_races_lvl_1, mob_weapons_lvl_1)




    
    
    
