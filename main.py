import random

num_trials = 10000
switch_wins = 0
stay_wins = 0

for i in range(num_trials):
    # Set up the game
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)

    # Player chooses a door
    player_choice = random.randint(0, 2)

    # Host opens a door with a goat
    if doors[player_choice] == 'car':
        goat_doors = [i for i in range(3) if i != player_choice]
        host_choice = random.choice(goat_doors)
    else:
        host_choice = [i for i in range(3) if doors[i] != 'car' and i != player_choice][0]

    # Switch doors
    switch_choice = [i for i in range(3) if i not in [player_choice, host_choice]][0]

    # Determine the outcome
    if doors[player_choice] == 'car':
        stay_wins += 1
    elif doors[switch_choice] == 'car':
        switch_wins += 1

# Print the results
print(f"Switching doors won {switch_wins} out of {num_trials} times ({switch_wins/num_trials*100:.2f}%).")
print(f"Sticking with the original choice won {stay_wins} out of {num_trials} times ({stay_wins/num_trials*100:.2f}%).")
