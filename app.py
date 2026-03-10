import random

attacker = ["Slag", "Spark", "Eldklot", "Heal"]
skador = [5, 10, 20]
heal = 10

hp_spelare = 100
hp_monster = 100

print("--- FIGHT START ---")

while hp_spelare > 0 and hp_monster > 0:
    val_attack = input(f"Välg attack [ {" | ".join(attacker)} ]: ").lower()
    val = random.choice([0, 1, 2])

    if val_attack.capitalize() not in attacker:
        print("Välj någon av attackerna!\n")
        continue

    if val_attack.lower() != "heal":
        skada = skador[val]
        hp_monster -= skada
        print(f"Du använder {val_attack.capitalize()}! Monstern tar {skada} skada.")
    else:
        hp_spelare += heal
        print(f"Du använder {val_attack.capitalize()}! Du healas {heal} hp.")

    if hp_monster > 0:
        val = random.choice([0, 1, 2])
        skada = skador[val]
        hp_spelare -= skada
        print(f"Monstret använder {attacker[val]}! Du tar {skada} skada.")
    
    print(f"Din HP: {hp_spelare} | Monster HP: {hp_monster}\n")

if hp_spelare > 0:
    print("Du vann!")
else:
    print("Du dog...")