import random
import os
import time

# ... (Previous code remains the same)

def show_power_up_effect(power_up):
    if power_up == "Speed boost":
        return "Your speed has increased!"
    elif power_up == "Invulnerability":
        return "You are invulnerable for a short time!"
    elif power_up == "Oil slick":
        return "You dropped an oil slick on the track!"
    else:
        return "Unknown power-up effect"

def apply_power_up(player_position, opponent_position, power_up):
    if power_up == "Speed boost":
        player_position += random.randint(2, 5)
    elif power_up == "Invulnerability":
        opponent_position -= random.randint(1, 3)
    elif power_up == "Oil slick":
        opponent_position -= random.randint(2, 4)
    return player_position, opponent_position

def display_stats(player_position, opponent_position, race_distance):
    player_progress = (player_position / race_distance) * 100
    opponent_progress = (opponent_position / race_distance) * 100

    print("\nRace Progress:")
    print(f"Player: {'=' * int(player_progress)} ({player_position}/{race_distance})")
    print(f"Opponent: {'=' * int(opponent_progress)} ({opponent_position}/{race_distance})")

def main():
    # ... (Previous code remains the same)

    while player_position < race_distance and opponent_position < race_distance:
        os.system('clear')
        display_stats(player_position, opponent_position, race_distance)
        print(display_track(player_position, opponent_position, race_distance, player_name))
        user_input = get_user_input()

        if user_input == 'q':
            print("Quitting the game...")
            break

        # Choose a random track, car, and power-up
        track = random.choice(tracks)
        car = random.choice(cars)
        power_up = random.choice(power_ups)

        print(f"You're racing on {track}!")
        print(f"You're driving a {car}!")
        print(f"You found a {power_up}!")
        print(show_power_up_effect(power_up))

        player_acceleration = random.randint(1, max_acceleration)
        opponent_speed = random.randint(*opponent_speed_range) + difficulty

        player_position += player_acceleration
        opponent_position += opponent_speed

        if random.random() < 0.2:
            player_position, opponent_position = apply_power_up(player_position, opponent_position, power_up)

        time.sleep(1)  # Add a delay to make the game more realistic

    os.system('clear')
    display_stats(player_position, opponent_position, race_distance)

    if player_position >= race_distance:
        print("\nCongratulations! You won the race!")
    else:
        print("\nSorry, you lost. Better luck next time!")

if __name__ == "__main__":
    main()
