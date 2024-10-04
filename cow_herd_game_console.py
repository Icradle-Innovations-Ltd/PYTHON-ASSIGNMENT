import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class CowHerdGame:
    def __init__(self):
        self.herds = [0, 0, 0]
        self.current_player = "Player"
        self.instructions = {
            "start": "🌟 **Welcome to the Cow Herd Game!** 🌟\n\nEnter the number of cows for each herd to begin the game.",
            "choose": "🤠 **Your Mission:** Choose a herd and remove some cows. Be strategic to outwit your opponent and be the last one to remove cows!",
            "end": "🏁 **Your turn is over.**"
        }

    def start_game(self):
        # Initialize herds with player input
        print(Fore.CYAN + self.instructions["start"])
        for i in range(3):
            while True:
                try:
                    cows = int(input(Fore.YELLOW + f"🐄 Enter the number of cows for Herd {i + 1}: "))
                    if cows < 0:
                        raise ValueError
                    self.herds[i] = cows
                    break
                except ValueError:
                    print(Fore.RED + "❌ Please enter a valid non-negative integer for cows.")

        if all(cow == 0 for cow in self.herds):
            print(Fore.RED + "❌ At least one herd must have cows to start the game.")
            return

        print(Fore.GREEN + "\n🎉 **Game started!** 🎉")
        self.show_instructions("choose")
        self.play_game()

    def play_game(self):
        while not all(cows == 0 for cows in self.herds):
            self.show_herd_status()
            if self.current_player == "Player":
                self.player_move()
            else:
                self.computer_move()

        print(Fore.MAGENTA + f"\n🏆 **{self.current_player} wins the game!** 🏆")
        self.ask_replay()

    def player_move(self):
        print(Fore.BLUE + "\n" + self.instructions["choose"])
        try:
            herd = int(input(Fore.YELLOW + "🔢 Select a herd (1-3): ")) - 1
            cows = int(input(Fore.YELLOW + "🧮 Enter the number of cows to remove: "))

            if herd not in range(3):
                raise ValueError("Invalid herd selection. Please choose a herd between 1 and 3.")

            if cows <= 0:
                raise ValueError("Number of cows to remove must be positive.")

            if cows > self.herds[herd]:
                raise ValueError(f"Herd {herd + 1} does not have {cows} cow(s). Current cows: {self.herds[herd]}.")

            # Perform the move
            self.herds[herd] -= cows
            print(Fore.GREEN + f"✅ You removed {cows} cow(s) from Herd {herd + 1}. 🐄")

            if all(h == 0 for h in self.herds):
                return

            # Switch to Computer's turn
            self.current_player = "Computer"
            print(Fore.MAGENTA + "\n🤖 **Computer's turn...** 🤖")
        except ValueError as ve:
            print(Fore.RED + f"❌ Error: {ve}")

    def computer_move(self):
        if all(cows == 0 for cows in self.herds):
            return

        # Calculate the nim-sum (XOR of all herd sizes)
        nim_sum = 0
        for cows in self.herds:
            nim_sum ^= cows

        if nim_sum == 0:
            # If the nim-sum is zero, no winning move is possible; remove one cow from a random non-empty herd
            non_empty_herds = [i for i, cows in enumerate(self.herds) if cows > 0]
            herd_index = random.choice(non_empty_herds)
            cows_to_remove = 1
            print(Fore.YELLOW + "🤖 The computer is in a tough spot and decides to remove 1 cow randomly.")
        else:
            # Find a herd to make the nim-sum zero after the move
            herd_index = -1
            cows_to_remove = 0
            for i in range(3):
                target = self.herds[i] ^ nim_sum
                if target < self.herds[i]:
                    herd_index = i
                    cows_to_remove = self.herds[i] - target
                    break

            if herd_index == -1:
                # Fallback to random move if no optimal move is found
                non_empty_herds = [i for i, cows in enumerate(self.herds) if cows > 0]
                herd_index = random.choice(non_empty_herds)
                cows_to_remove = 1
                print(Fore.YELLOW + "🤖 The computer couldn't find an optimal move and decides to remove 1 cow randomly.")
            else:
                print(Fore.YELLOW + f"🤖 The computer has strategically removed {cows_to_remove} cow(s) from Herd {herd_index + 1}.")

        # Perform the move
        self.herds[herd_index] -= cows_to_remove
        print(Fore.GREEN + f"✅ Computer removed {cows_to_remove} cow(s) from Herd {herd_index + 1}. 🐄")

        if all(h == 0 for h in self.herds):
            return

        # Switch back to Player's turn
        self.current_player = "Player"
        print(Fore.BLUE + "\n🤠 **Your turn!** 🤠")

    def show_herd_status(self):
        print(Fore.CYAN + "\n📊 **Current Herd Status:**")
        for i, herd_count in enumerate(self.herds):
            cow_emoji = "🐄" * herd_count
            print(Fore.GREEN + f"  Herd {i + 1}: {herd_count} cow(s) {cow_emoji}")
        print("")  # Add an empty line for better readability

    def show_instructions(self, instruction_key):
        print(Fore.MAGENTA + self.instructions[instruction_key])

    def ask_replay(self):
        while True:
            replay = input(Fore.BLUE + "\n🔄 Do you want to play again? (y/n): ").strip().lower()
            if replay == 'y':
                print(Fore.GREEN + "\n🔁 Restarting the game...\n")
                self.herds = [0, 0, 0]
                self.current_player = "Player"
                self.start_game()
                break
            elif replay == 'n':
                print(Fore.MAGENTA + "\n👋 Thanks for playing the Cow Herd Showdown! Goodbye! 🐮\n")
                break
            else:
                print(Fore.RED + "❌ Invalid input. Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    game = CowHerdGame()
    game.start_game()
