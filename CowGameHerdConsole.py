import random

class CowHerdGame:
    def __init__(self):
        self.herds = [0, 0, 0]
        self.current_player = "Player"
        self.instructions = {
            "start": "Enter the number of cows for each herd.",
            "choose": "Choose a herd and enter the number of cows to remove.",
            "end": "Your turn is over."
        }

    def start_game(self):
        # Initialize herds with player input
        for i in range(3):
            while True:
                try:
                    cows = int(input(f"Enter the number of cows for Herd {i + 1}: "))
                    if cows < 0:
                        raise ValueError
                    self.herds[i] = cows
                    break
                except ValueError:
                    print("Please enter a valid non-negative integer for cows.")

        if all(cow == 0 for cow in self.herds):
            print("At least one herd must have cows to start the game.")
            return

        print("Game started!")
        self.show_instructions("choose")
        self.play_game()

    def play_game(self):
        while not all(cows == 0 for cows in self.herds):
            self.show_herd_status()
            if self.current_player == "Player":
                self.player_move()
            else:
                self.computer_move()

        print(f"{self.current_player} wins!")

    def player_move(self):
        try:
            herd = int(input("Select a herd (1-3): ")) - 1
            cows = int(input("Enter the number of cows to remove: "))

            if herd not in range(3):
                raise ValueError("Invalid herd selection.")

            if cows <= 0:
                raise ValueError("Number of cows to remove must be positive.")

            if cows > self.herds[herd]:
                raise ValueError(f"Herd {herd + 1} does not have {cows} cows.")

            # Perform the move
            self.herds[herd] -= cows
            print(f"Player removed {cows} cow(s) from Herd {herd + 1}.")

            if all(h == 0 for h in self.herds):
                return

            # Switch to Computer's turn
            self.current_player = "Computer"
            print("Computer's turn...")
        except ValueError as ve:
            print(ve)

    def computer_move(self):
        if all(cows == 0 for cows in self.herds):
            return

        # Smart Strategy: Remove all cows from a randomly selected non-empty herd
        non_empty_herds = [i for i, cows in enumerate(self.herds) if cows > 0]
        herd_index = random.choice(non_empty_herds)
        cows_to_remove = random.randint(1, self.herds[herd_index])

        self.herds[herd_index] -= cows_to_remove
        print(f"Computer removed {cows_to_remove} cow(s) from Herd {herd_index + 1}.")

        if all(h == 0 for h in self.herds):
            return

        # Switch back to Player's turn
        self.current_player = "Player"
        print("Player's turn...")

    def show_herd_status(self):
        for i, herd_count in enumerate(self.herds):
            print(f"Herd {i + 1}: {herd_count} cows")

    def show_instructions(self, instruction_key):
        print(self.instructions[instruction_key])


if __name__ == "__main__":
    game = CowHerdGame()
    game.start_game()
