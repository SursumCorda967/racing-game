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

    while player_position < race_distance and opponent_position < race_distance:
        print(display_track(player_position, opponent_position, race_distance, player_name))
        user_input = get_user_input()
        
        if user_input == 'q':
            print("Quitting the game...")
            break
        
        player_acceleration = random.randint(1, max_acceleration)
        opponent_speed = random.randint(*opponent_speed_range)
        
        player_position += player_acceleration
        opponent_position += opponent_speed
        
        os.system('clear')

    if player_position >= race_distance:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost. Better luck next time!")

if __name__ == "__main__":
    main()
