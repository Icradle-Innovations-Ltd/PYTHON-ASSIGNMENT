import random
import tkinter as tk
from tkinter import messagebox

class CowHerdGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("🐄 Cow Herd Game 🐄")
        self.master.geometry("700x600")
        self.master.resizable(False, False)
        self.herds = [0, 0, 0]
        self.current_player = "Player"
        self.setup_ui()

    def setup_ui(self):
        # Instructions Frame
        self.instructions_frame = tk.Frame(self.master, bg="#F0E68C", pady=10)
        self.instructions_frame.pack(fill=tk.X)

        self.instructions_label = tk.Label(
            self.instructions_frame,
            text="🌟 Welcome to the Cow Herd Showdown! 🌟\n\nEnter the number of cows for each herd to begin the game.",
            font=("Arial", 14),
            bg="#F0E68C"
        )
        self.instructions_label.pack()

        # Herd Setup Frame
        self.setup_frame = tk.Frame(self.master, bg="#F0E68C", pady=10)
        self.setup_frame.pack(fill=tk.X)

        self.herd_entries = []
        for i in range(3):
            frame = tk.Frame(self.setup_frame, bg="#F0E68C")
            frame.pack(pady=5)
            label = tk.Label(frame, text=f"🐄 Herd {i + 1} Cows:", font=("Arial", 12), bg="#F0E68C")
            label.pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, width=5, font=("Arial", 12))
            entry.pack(side=tk.LEFT)
            self.herd_entries.append(entry)

        self.start_button = tk.Button(
            self.setup_frame,
            text="🎉 Start Game 🎉",
            command=self.start_game,
            bg="#32CD32",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.start_button.pack(pady=10)

        # Game Frame
        self.game_frame = tk.Frame(self.master, bg="#FFFACD", pady=10)

        # Herd Status
        self.herd_status_label = tk.Label(
            self.game_frame,
            text="📊 Current Herd Status:",
            font=("Arial", 14, "bold"),
            bg="#FFFACD"
        )
        self.herd_status_label.pack(pady=5)

        self.herd_labels = []
        for i in range(3):
            label = tk.Label(
                self.game_frame,
                text=f"  Herd {i + 1}: 0 cow(s) 🐄",
                font=("Arial", 12),
                bg="#FFFACD"
            )
            label.pack()
            self.herd_labels.append(label)

        # Player Action Frame
        self.action_frame = tk.Frame(self.game_frame, bg="#FFFACD", pady=10)
        self.action_frame.pack(pady=10)

        # Select Herd
        self.select_herd_label = tk.Label(
            self.action_frame,
            text="🔢 Select a herd:",
            font=("Arial", 12),
            bg="#FFFACD"
        )
        self.select_herd_label.grid(row=0, column=0, padx=5, pady=5)

        self.selected_herd = tk.IntVar()
        self.selected_herd.set(1)
        for i in range(1, 4):
            rb = tk.Radiobutton(
                self.action_frame,
                text=f"Herd {i}",
                variable=self.selected_herd,
                value=i,
                font=("Arial", 12),
                bg="#FFFACD"
            )
            rb.grid(row=0, column=i, padx=5, pady=5)

        # Enter Number of Cows to Remove
        self.remove_label = tk.Label(
            self.action_frame,
            text="🧮 Enter number of cows to remove:",
            font=("Arial", 12),
            bg="#FFFACD"
        )
        self.remove_label.grid(row=1, column=0, padx=5, pady=5)

        self.remove_entry = tk.Entry(self.action_frame, width=5, font=("Arial", 12))
        self.remove_entry.grid(row=1, column=1, padx=5, pady=5)

        # Remove Button
        self.remove_button = tk.Button(
            self.action_frame,
            text="✅ Remove Cows",
            command=self.player_move,
            bg="#1E90FF",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.remove_button.grid(row=1, column=2, padx=5, pady=5)

        # Message Display
        self.message_label = tk.Label(
            self.game_frame,
            text="🤠 Your turn!",
            font=("Arial", 12, "italic"),
            bg="#FFFACD",
            fg="#FF8C00"
        )
        self.message_label.pack(pady=10)

        # Replay Button (Hidden Initially)
        self.replay_button = tk.Button(
            self.game_frame,
            text="🔄 Play Again",
            command=self.reset_game,
            bg="#FF4500",
            fg="white",
            font=("Arial", 12, "bold")
        )

        # Pack the game frame but keep it hidden until the game starts
        # self.game_frame.pack() will be called in start_game()

    def start_game(self):
        # Validate and initialize herds
        try:
            for i, entry in enumerate(self.herd_entries):
                cows = int(entry.get())
                if cows < 0:
                    raise ValueError(f"Herd {i + 1} cannot have negative cows.")
                self.herds[i] = cows
                self.herd_labels[i].config(text=f"  Herd {i + 1}: {cows} cow(s) 🐄" + "🐄" * cows)
            if all(cow == 0 for cow in self.herds):
                messagebox.showerror("Error", "❌ At least one herd must have cows to start the game.")
                return
            # Hide setup frame and show game frame
            self.setup_frame.pack_forget()
            self.game_frame.pack(fill=tk.BOTH, expand=True)
            self.update_herd_status()
            self.message_label.config(text="🤠 Your turn!", fg="#FF8C00")
        except ValueError as ve:
            messagebox.showerror("Invalid Input", f"❌ {ve}")

    def update_herd_status(self):
        for i in range(3):
            self.herd_labels[i].config(
                text=f"  Herd {i + 1}: {self.herds[i]} cow(s) " + "🐄" * self.herds[i]
            )

    def player_move(self):
        if self.current_player != "Player":
            messagebox.showinfo("Not Your Turn", "❌ It's not your turn yet!")
            return
        try:
            herd = self.selected_herd.get() - 1
            cows_to_remove = int(self.remove_entry.get())
            if cows_to_remove <= 0:
                raise ValueError("Number of cows to remove must be positive.")
            if cows_to_remove > self.herds[herd]:
                raise ValueError(f"Herd {herd + 1} does not have {cows_to_remove} cow(s).")
            # Perform the move
            self.herds[herd] -= cows_to_remove
            self.update_herd_status()
            self.message_label.config(
                text=f"✅ You removed {cows_to_remove} cow(s) from Herd {herd + 1}. 🐄",
                fg="#32CD32"
            )
            self.remove_entry.delete(0, tk.END)
            if all(cow == 0 for cow in self.herds):
                self.end_game("Player")
                return
            # Switch to Computer's turn
            self.current_player = "Computer"
            self.master.after(1000, self.computer_move)  # Delay for better UX
        except ValueError as ve:
            messagebox.showerror("Invalid Move", f"❌ {ve}")

    def computer_move(self):
        if all(cow == 0 for cow in self.herds):
            return
        # Calculate nim-sum
        nim_sum = 0
        for cow in self.herds:
            nim_sum ^= cow
        if nim_sum == 0:
            # No winning move; remove one cow randomly
            non_empty_herds = [i for i, cows in enumerate(self.herds) if cows > 0]
            herd_index = random.choice(non_empty_herds)
            cows_to_remove = 1
            move_message = "The computer is in a tough spot and decides to remove 1 cow randomly."
        else:
            # Find a move to make nim-sum zero
            herd_index = -1
            cows_to_remove = 0
            for i in range(3):
                target = self.herds[i] ^ nim_sum
                if target < self.herds[i]:
                    herd_index = i
                    cows_to_remove = self.herds[i] - target
                    break
            if herd_index == -1:
                # Fallback to random move
                non_empty_herds = [i for i, cows in enumerate(self.herds) if cows > 0]
                herd_index = random.choice(non_empty_herds)
                cows_to_remove = 1
                move_message = "The computer couldn't find an optimal move and decides to remove 1 cow randomly."
            else:
                move_message = f"The computer has strategically removed {cows_to_remove} cow(s) from Herd {herd_index + 1}."
        # Perform the move
        self.herds[herd_index] -= cows_to_remove
        self.update_herd_status()
        # Display computer's move
        if self.herds[herd_index] < 0:
            self.herds[herd_index] = 0  # Prevent negative cows
        self.message_label.config(
            text=f"🤖 {move_message}\n✅ Computer removed {cows_to_remove} cow(s) from Herd {herd_index + 1}. 🐄",
            fg="#FF4500"
        )
        if all(cow == 0 for cow in self.herds):
            self.end_game("Computer")
            return
        # Switch back to Player's turn
        self.current_player = "Player"
        self.message_label.config(text="🤠 Your turn!", fg="#FF8C00")

    def end_game(self, winner):
        if winner == "Player":
            message = "🏆 Congratulations! You win the game! 🎉"
        else:
            message = "🤖 The computer wins the game! Better luck next time! 🏆"
        messagebox.showinfo("Game Over", message)
        self.message_label.config(text=message, fg="#8B0000")
        self.replay_button.pack(pady=10)

    def reset_game(self):
        # Reset all game variables and UI elements
        self.herds = [0, 0, 0]
        self.current_player = "Player"
        self.game_frame.pack_forget()
        for entry in self.herd_entries:
            entry.delete(0, tk.END)
        self.setup_frame.pack(fill=tk.X)
        self.replay_button.pack_forget()
        self.message_label.config(text="🤠 Your turn!", fg="#FF8C00")

if __name__ == "__main__":
    root = tk.Tk()
    game = CowHerdGameGUI(root)
    root.mainloop()
