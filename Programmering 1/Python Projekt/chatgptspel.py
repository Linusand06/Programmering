import random

# Funktion för att validera spelarens namn
def get_player_name():
    while True:
        name = input("Ange namn på slagskämpe A (mellan 3 och 10 tecken): ")
        if 3 <= len(name) <= 10:
            return name
        print("Namnet måste vara mellan 3 och 10 tecken.")

# ASCII-art för slagskämpar (kan modifieras efter smak)
fighter_a_ascii = """
   O
  /|\\
  / \\
"""
fighter_b_ascii = """
   O
  /|\\
  / \\
"""

# Slumpa namn för slagskämpe B
fighter_b_names = ["Bulldozer", "Tiger", "Phoenix"]

# Funktion för att satsa pengar
def place_bet():
    while True:
        try:
            bet = int(input("Hur mycket vill du satsa? (minst 10 och max 100): "))
            if 10 <= bet <= 100:
                return bet
        except ValueError:
            print("Ange ett giltigt belopp.")
        print("Satsningen måste vara mellan 10 och 100.")

# Funktion för att välja antal rundor
def choose_rounds():
    while True:
        try:
            rounds = int(input("Välj antal rundor (3-10): "))
            if 3 <= rounds <= 10:
                return rounds
        except ValueError:
            print("Ange ett giltigt antal.")
        print("Antal rundor måste vara mellan 3 och 10.")

# Funktion för att utföra en attack
def attack(hit_chance, min_damage, max_damage):
    if random.random() <= hit_chance:  # Bestäm om slaget träffar
        return random.randint(min_damage, max_damage)  # Slumpa skadan
    else:
        return 0  # Missar slaget

# Huvudspel-funktion
def fight_game():
    player_a_name = get_player_name()
    player_b_name = random.choice(fighter_b_names)

    player_a_hp = 100
    player_b_hp = 100

    # Låt spelaren satsa pengar
    player_money = 100
    bet = place_bet()

    rounds = choose_rounds()

    print(f"\nSlagskämpe A ({player_a_name}):\n{fighter_a_ascii}")
    print(f"Slagskämpe B ({player_b_name}):\n{fighter_b_ascii}")

    for round_num in range(1, rounds + 1):
        print(f"\nRunda {round_num}:")
        
        # Spelarens val av attack
        print("Välj din attack:")
        print("1. Hög risk (20% chans, 20-30 skada)")
        print("2. Låg risk (70% chans, 5-10 skada)")
        attack_choice = input("Ange 1 eller 2: ")

        if attack_choice == "1":
            damage = attack(0.2, 20, 30)  # Hög risk, stor skada
        else:
            damage = attack(0.7, 5, 10)  # Låg risk, liten skada

        player_b_hp -= damage
        if damage > 0:
            print(f"{player_a_name} träffade {player_b_name} med {damage} skada!")
        else:
            print(f"{player_a_name} missade!")

        # Kolla om spelare B är nere
        if player_b_hp <= 0:
            print(f"\n{player_b_name} har 0 HP kvar! {player_a_name} vinner!")
            player_money += bet
            break

        # Slagskämpe B:s slumpmässiga attack
        if random.random() > 0.5:
            damage = attack(0.2, 20, 30)  # B väljer hög risk
        else:
            damage = attack(0.7, 5, 10)  # B väljer låg risk

        player_a_hp -= damage
        if damage > 0:
            print(f"{player_b_name} träffade {player_a_name} med {damage} skada!")
        else:
            print(f"{player_b_name} missade!")

        # Kolla om spelare A är nere
        if player_a_hp <= 0:
            print(f"\n{player_a_name} har 0 HP kvar! {player_b_name} vinner!")
            player_money -= bet
            break

        # Visa HP kvar
        print(f"{player_a_name}: {player_a_hp} HP kvar.")
        print(f"{player_b_name}: {player_b_hp} HP kvar.")

    # Om ingen har förlorat efter alla rundor
    if player_a_hp > 0 and player_b_hp > 0:
        if player_a_hp > player_b_hp:
            print(f"\n{player_a_name} vinner med mer HP!")
            player_money += bet
        else:
            print(f"\n{player_b_name} vinner med mer HP!")
            player_money -= bet

    # Visa slutresultat och fråga om spelaren vill spela igen
    print(f"\nDu har nu {player_money} pengar kvar.")
    play_again = input("Vill du spela igen? (ja/nej): ")
    if play_again.lower() == "ja":
        fight_game()
    else:
        print("Tack för att du spelade!")

# Starta spelet
fight_game()
