import random

#attacker = ["Slag", "Spark", "Eldklot", "Heal"]
attacker = [
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
        "skada": 20, 
    },
    {
        "name": "Heal",
        "heal": 10,
    }
]
monster_attacker = [
    {
        "name": "Slag",
        "skada": 5, #monstrets skada på spelaren
    },
    {
        "name": "Spark",
        "skada": 10, #monstrets skada på spelaren
    },
    {
        "name": "Eldklot",
        "skada": 20, #monstrets skada på spelaren
    },
]
skador = [5, 10, 20]

hp_spelare = 100
hp_monster = 100

print("--- FIGHT START ---")

print_list = []
for attack in attacker:
    print_list.append(attack["name"]) 

heal_index = print_list.index("Heal")

while hp_spelare > 0 and hp_monster > 0:
    
    val_attack = input(f"Välg attack [ {" | ".join(print_list)} ]: ").lower()
    skada = random.choice(skador)

    if val_attack.capitalize() not in print_list:
        print("Välj någon av attackerna!\n")
        continue

    if val_attack.lower() != "heal":
        hp_monster -= skada
        print(f"Du använder {val_attack.capitalize()}! Monstret tar {skada} skada.")
    else:
        hp_spelare += attacker[heal_index]["heal"]
        print(f"Du använder {val_attack.capitalize()}! Du healas {attacker[heal_index]["heal"]} hp.")

    if hp_monster > 0:
       monster_attack = random.choice(monster_attacker)
       hp_spelare -= monster_attack["skada"]
       print(f"Monstret använder {monster_attack["name"]}! Du tar {monster_attack["skada"]} skada.")
    
#     #print(f"Din HP: {hp_spelare} | Monster HP: {hp_monster}\n")

# if hp_spelare > 0:
#     print("Du vann!")
# else:
#     print("Du dog...")