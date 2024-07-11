import random
def generate_number(length):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])
def provide_hints(actual, guess):
    hints = []
    for i in range(len(actual)):
        if guess[i] == actual[i]:
            hints.append(guess[i])
        else:
            hints.append('_')
    return ''.join(hints)
def player_guessing(actual, player_name):
    attempts = 0
    while True:
        guess = input(f"{player_name}, enter your guess: ")
        attempts += 1
        if guess == actual:
            print(f"Correct! {player_name} guessed the number in {attempts} attempts.")
            return attempts
        else:
            hints = provide_hints(actual, guess)
            print(f"Hints: {hints}")
def play_mastermind():
    print("Welcome to Mastermind!")
    length = int(input("Enter the length of the number: "))
    
    print("Player 1, set the number (Player 2, close your eyes):")
    actual_number_player1 = input("Player 1, enter the number: ").strip()
    
    print("\nPlayer 2's turn to guess.")
    attempts_player2 = player_guessing(actual_number_player1, "Player 2")
    
    print("\nPlayer 2, set the number (Player 1, close your eyes):")
    actual_number_player2 = input("Player 2, enter the number: ").strip()
    
    print("\nPlayer 1's turn to guess.")
    attempts_player1 = player_guessing(actual_number_player2, "Player 1")
    
    if attempts_player1 < attempts_player2:
        print("Player 1 wins and is crowned Mastermind!")
    else:
        print("Player 2 wins and is crowned Mastermind!")

if __name__ == "__main__":
    play_mastermind()

