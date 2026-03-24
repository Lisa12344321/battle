import random
import os

attacker = [
    {
        "name": "Slag",
        "critical_hit": "*Slagträ*"
    },
    {
        "name": "Spark",
        "critical_hit": "*Spikskor*"
    },
    {
        "name": "Eldklot",
        "critical_hit": "*Sol*"
    },
    {
        "name": "Heal",
        "heal": 10,
    }
]
monster_attacker = [
    {
        "name": "Slag",
        "skada": 5,
    },
    {
        "name": "Spark",
        "skada": 10,
    },
    {
        "name": "Eldklot",
        "skada": 20
    },
]
skador = [5, 10, 20]
critical_hit_skada = 20
critical_chans = ["sant", "falskt", "falskt", "falskt"] # 25%

hp_spelare = 100
hp_monster = 100

print("--- FIGHT START ---")

print_list = []
for attack in attacker:
    print_list.append(attack["name"]) 

while hp_spelare > 0 and hp_monster > 0:

    critical_hit = random.choice(critical_chans)
    if critical_hit == "sant":
        skada = random.choice(skador) + critical_hit_skada
    else:
        skada = random.choice(skador)


    val_attack = input(f"Välg attack [ {" | ".join(print_list)} ]: ").lower()
    
    
    if val_attack.capitalize() not in print_list:
        print("Välj någon av attackerna!\n")
        continue
    
    os.system("cls")

    index = print_list.index(val_attack.capitalize())

    if val_attack.lower() != "heal":
        hp_monster -= skada
        if critical_hit == "sant":
            print(f"Du använder {attacker[index]["critical_hit"]} *CRITICAL HIT*! Monstret tar {skada} skada!")
        else:
            print(f"Du använder {attacker[index]["name"]}! Monstret tar {skada} skada.")
    else:
        hp_spelare += attacker[index]["heal"]
        print(f"Du använder {attacker[index]["name"]}! Du healas {attacker[index]["heal"]} hp.")

    if hp_monster > 0:
       monster_attack = random.choice(monster_attacker)
       hp_spelare -= monster_attack["skada"]
       print(f"Monstret använder {monster_attack["name"]}! Du tar {monster_attack["skada"]} skada.\n")
    
    print(f"Din HP: {hp_spelare} | Monster HP: {hp_monster}\n")

if hp_spelare > 0:
    print("Du vann!")
else:
    print("Du dog...")