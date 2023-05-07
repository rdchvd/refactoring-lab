from random import randint

NUM_TRIALS = 10000
SWITCH_WINS = 0
STAY_WINS = 0

for x in range(0, NUM_TRIALS):
    # Start the game with 3 doors, 1 car, 2 goats
    doors = ["goat", "goat", "car"]
    randint(0, 2)

    # Player makes a choice
    player_choice = randint(0, 2)
    print(f"Player chose door {player_choice}")

    # Host reveals one goat
    for i in range(len(doors)):
        if i != player_choice and doors[i] == "goat":
            host_choice = i
    # doors.pop(host_choice)
    print(f"Host reveals door {host_choice}")

    # Player chooses whether to switch or stay
    switch = randint(0, 1)
    if switch == 1:
        for i in range(len(doors)):
            if i != player_choice:
                player_choice = i

    # Check if the player won
    print(f"{player_choice=}, {len(doors)=}")
    if doors[player_choice] == "car":
        SWITCH_WINS += 1
    else:
        STAY_WINS += 1

# Print the results
print("Percentage of times player won by switching:", SWITCH_WINS/NUM_TRIALS*100)
print("Percentage of times player won by sticking with original choice:", STAY_WINS/NUM_TRIALS*100)