import random
import os

attacker = [
    {
        "namn": "Slag",
        "critical_hit": "*Slagträ*"
    },
    {
        "namn": "Spark",
        "critical_hit": "*Spikskor*"
    },
    {
        "namn": "Eldklot",
        "critical_hit": "*Sol*"
    },
    {
        "namn": "Heal",
        "heal": 10,
    }
]
pokemons = [
    {
        "namn": "Pikachu",
        "typ": "Electric",
        "attacker": [
            {
                "namn": "Thunder Shock",
                "skada": 20
            },
            {
                "namn": "Wild Charge",
                "skada": 10
            },
            {
                "namn": "Thunderbolt",
                "skada": 5
            }
            ]
    },
    {
        "namn": "Charizard",
        "typ": "Fire och Flying",
        "attacker": [
            {
                "namn": "Fire Spin",
                "skada": 20
            },
            {
                "namn": "Flamethrower",
                "skada": 10
            },
            {
                "namn": "Blast Burn",
                "skada": 5
            }
            ]
    },
    {
        "namn": "Bulbasaur",
        "typ": "Grass och Poison",
        "attacker": [
            {
                "namn": "Power Whip",
                "skada": 20
            },
            {
                "namn": "Vine Whip",
                "skada": 10
            },
            {
                "namn": "Sludge Bomb",
                "skada": 5
            }
            ]
    },
    {
        "namn": "Wartortle",
        "typ": "Water",
        "attacker": [
            {
                "namn": "Water Gun",
                "skada": 20
            },
            {
                "namn": "Hydro Pump",
                "skada": 10
            },
            {
                "namn": "Aqua Jet",
                "skada": 5
            }
            ]
    }
]
skador = [5, 10, 20]
critical_hit_skada = 20
critical_chans = ["sant", "falskt", "falskt", "falskt"] # 25%

hp_spelare = 100
hp_pokemon = 100

print("--- FIGHT START ---")

print_list = []
for attack in attacker:
    print_list.append(attack["namn"])



run = True

while run:
    pokemon = random.choice(pokemons)
    print(f"Du möter en {pokemon["namn"]} som är av typen {pokemon["typ"]}.\n")

    while hp_spelare > 0 and hp_pokemon > 0:

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
            hp_pokemon -= skada
            if critical_hit == "sant":
                print(f"Du använder {attacker[index]["critical_hit"]} *CRITICAL HIT*! {pokemon["namn"]} tar {skada} skada!")
            else:
                print(f"Du använder {attacker[index]["namn"]}! {pokemon["namn"]} tar {skada} skada.")
        else:
            hp_spelare += attacker[index]["heal"]
            print(f"Du använder {attacker[index]["namn"]}! Du healas {attacker[index]["heal"]} hp.")

        if hp_pokemon > 0:
            pokemon_attack = random.choice(pokemon["attacker"])

            critical_hit = random.choice(critical_chans)
            if critical_hit == "sant":
                skada = (pokemon_attack["skada"] + critical_hit_skada)
                print(f"{pokemon["namn"]} använder {pokemon_attack["namn"]} *CRITICAL HIT*! Du tar {skada} skada.\n")
            else:
                skada = pokemon_attack["skada"]
                print(f"{pokemon["namn"]} använder {pokemon_attack["namn"]}! Du tar {skada} skada.\n")
                
            hp_spelare -= skada


        print(f"Din HP: {hp_spelare} | {pokemon["namn"]} HP: {hp_pokemon}\n")

    if hp_spelare > 0:
        print("Du vann!")
    else:
        print("Du dog...")

    spela_igen = input("Spela igen? ").lower()
    if spela_igen != "nej":
        hp_spelare = 100
        hp_pokemon = 100
        os.system("cls")
    else:
        run = False
