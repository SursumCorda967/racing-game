import random
import os
import time

def get_user_name():
    return input("Enter your name: ")

def display_track(player_pos, opponent_pos, race_distance, player_name):
    track = f'Player: {player_name}\n'
    track += '-' * player_pos + 'P' + '-' * (race_distance - player_pos)
    track += '\n' + '-' * opponent_pos + 'O' + '-' * (race_distance - opponent_pos)
    return track

def get_user_input():
    return input("Press 'Enter' to accelerate or 'q' to quit: ").strip().lower()

def countdown():
    for i in range(3, 0, -1):
        print(f"Race starting in {i}...")
        time.sleep(1)

def main():
    race_distance = 50
    player_position = 0
    opponent_position = 0
    max_acceleration = 5
    opponent_speed_range = (1, 3)

    print("Welcome to the Racing Game!")

    difficulty = input("Select difficulty (easy, medium, hard): ").strip().lower()
    if difficulty == "easy":
        max_acceleration = 3
        opponent_speed_range = (1, 2)
    elif difficulty == "hard":
        max_acceleration = 7
        opponent_speed_range = (2, 4)

    player_name = get_user_name()
    os.system('clear')

    countdown()

    tracks = [
        "Track 1: A winding road through the mountains.",
        "Track 2: A fast and furious race through the city.",
        "Track 3: A challenging off-road course through the desert."
    ]

    cars = [
        "Car 1: A powerful sports car.",
        "Car 2: A sleek and stylish sports car.",
        "Car 3: A rugged and durable off-road vehicle."
    ]

    power_ups = [
        "Speed boost",
        "Invulnerability",
        "Oil slick"
    ]

    while player_position < race_distance and opponent_position < race_distance:
        print(display_track(player_position, opponent_position, race_distance, player_name))
        user_input = get_user_input()
        
        if user_input == 'q':
            print("Quitting the game...")
            break
        
        # Choose a random track
        track = random.choice(tracks)
        print(f"You're racing on {track}!")

        # Choose a random car
        car = random.choice(cars)
        print(f"You're driving a {car}!")

        # Choose a random power-up
        power_up = random.choice(power_ups)
        print(f"You found a {power_up}!")

        # Add some randomness to the player's acceleration
        player_acceleration = random.randint(1, max_acceleration)
        # Make the opponent's speed increase with difficulty
        opponent_speed = random.randint(*opponent_speed_range) + difficulty
        
        player_position += player_acceleration
        opponent_position += opponent_speed
        
        # Add a delay to make the game more realistic
        time.sleep(0.5)

    if player_position >= race_distance:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost. Better luck next time!")

if __name__ == "__main__":
    main()
