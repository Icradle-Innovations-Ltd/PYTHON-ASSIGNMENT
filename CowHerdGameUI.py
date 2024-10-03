import random
import tkinter as tk
from tkinter import messagebox

class CowHerdGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Cow Herd Game")
        self.herds = [0, 0, 0]
        self.current_player = "Player"
        self.instructions = {
            "start": "Enter the number of cows for each herd and click 'Start Game'.",
            "choose": "Choose a herd and enter the number of cows to remove.",
            "end": "Your turn is over."
        }

        self.setup_ui()
        self.show_instructions("start")

    def setup_ui(self):
        # Heading
        heading_label = tk.Label(
            self.master,
            text="Welcome to the Cow Herd Game",
            font=("Arial", 16, "bold")
        )
        heading_label.pack(pady=10)

        # Instructions
        self.instruction_label = tk.Label(
            self.master,
            text="",
            wraplength=400,
            justify="left",
            font=("Arial", 12)
        )
        self.instruction_label.pack(pady=10)

        # Herd setup frame
        self.setup_frame = tk.Frame(self.master)
        self.setup_frame.pack(pady=10)

        for i in range(3):
            tk.Label(
                self.setup_frame,
                text=f"Herd {i+1}:",
                font=("Arial", 12)
            ).grid(row=i, column=0, padx=5, pady=5, sticky='e')
            entry = tk.Entry(self.setup_frame, width=20, fg='grey')
            entry.grid(row=i, column=1, padx=5, pady=5)
            entry.insert(0, "Enter number of cows")
            entry.bind("<FocusIn>", lambda e, idx=i: self.clear_placeholder(e, idx))
            entry.bind("<FocusOut>", lambda e, idx=i: self.add_placeholder(e, idx))
            setattr(self, f"herd_{i+1}_entry", entry)

        tk.Button(
            self.setup_frame,
            text="Start Game",
            command=self.start_game,
            width=20,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold")
        ).grid(row=3, column=0, columnspan=2, pady=10)

        # Game frame
        self.game_frame = tk.Frame(self.master)

        # Herd display
        self.herd_labels = []
        for i in range(3):
            label = tk.Label(
                self.game_frame,
                text=f"Herd {i+1}: 0",
                font=("Arial", 12)
            )
            label.pack(pady=5)
            self.herd_labels.append(label)

        # Status label
        self.status_label = tk.Label(
            self.game_frame,
            text="",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=10)

        # Move controls
        move_frame = tk.Frame(self.game_frame)
        move_frame.pack(pady=10)

        # Herd selection
        tk.Label(move_frame, text="Select Herd:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.herd_choice = tk.StringVar()
        self.herd_choice.set("1")  # Default value
        self.herd_optionmenu = tk.OptionMenu(move_frame, self.herd_choice, "1", "2", "3")
        self.herd_optionmenu.config(width=10, font=("Arial", 12))
        self.herd_optionmenu.grid(row=0, column=1, padx=5, pady=5)

        # Cows to remove
        tk.Label(move_frame, text="Cows to Remove:", font=("Arial", 12)).grid(row=0, column=2, padx=5, pady=5, sticky='e')
        self.cows_entry = tk.Entry(move_frame, width=20, fg='grey')
        self.cows_entry.grid(row=0, column=3, padx=5, pady=5)
        self.cows_entry.insert(0, "Enter number of cows")
        self.cows_entry.bind("<FocusIn>", self.clear_cows_placeholder)
        self.cows_entry.bind("<FocusOut>", self.add_cows_placeholder)

        # Make Move button
        self.move_button = tk.Button(
            move_frame,
            text="Make Move",
            command=self.player_move,
            width=15,
            bg="#008CBA",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.move_button.grid(row=0, column=4, padx=5, pady=5)

        # Reset Game button
        self.reset_button = tk.Button(
            self.game_frame,
            text="Reset Game",
            command=self.reset_game,
            width=20,
            bg="#f44336",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.reset_button.pack(pady=5)
        self.reset_button.config(state="disabled")  # Disabled until game starts

    def clear_placeholder(self, event, idx):
        entry = getattr(self, f"herd_{idx+1}_entry")
        if entry.get() == "Enter number of cows":
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def add_placeholder(self, event, idx):
        entry = getattr(self, f"herd_{idx+1}_entry")
        if not entry.get():
            entry.insert(0, "Enter number of cows")
            entry.config(fg='grey')

    def clear_cows_placeholder(self, event):
        if self.cows_entry.get() == "Enter number of cows":
            self.cows_entry.delete(0, tk.END)
            self.cows_entry.config(fg='black')

    def add_cows_placeholder(self, event):
        if not self.cows_entry.get():
            self.cows_entry.insert(0, "Enter number of cows")
            self.cows_entry.config(fg='grey')

    def start_game(self):
        # Initialize herds
        for i in range(3):
            entry = getattr(self, f"herd_{i+1}_entry")
            value = entry.get().strip()
            if value == "Enter number of cows" or not value:
                messagebox.showerror("Invalid Input", f"Please enter the number of cows for Herd {i+1}.")
                return
            try:
                cows = int(value)
                if cows < 0:
                    raise ValueError
                self.herds[i] = cows
            except ValueError:
                messagebox.showerror("Invalid Input", f"Please enter a valid non-negative integer for Herd {i+1}.")
                return

        if all(cow == 0 for cow in self.herds):
            messagebox.showerror("Invalid Setup", "At least one herd must have cows to start the game.")
            return

        self.update_herd_display()
        self.setup_frame.pack_forget()
        self.game_frame.pack()
        self.reset_button.config(state="normal")
        self.show_instructions("choose")
        self.enable_move()

    def reset_game(self):
        self.herds = [0, 0, 0]
        self.current_player = "Player"
        self.update_herd_display()
        self.status_label.config(text="")
        self.game_frame.pack_forget()
        self.setup_frame.pack()
        self.show_instructions("start")
        self.reset_button.config(state="disabled")
        # Reset herd setup entries
        for i in range(3):
            entry = getattr(self, f"herd_{i+1}_entry")
            entry.delete(0, tk.END)
            entry.insert(0, "Enter number of cows")
            entry.config(fg='grey')

    def update_herd_display(self):
        for i, label in enumerate(self.herd_labels):
            label.config(text=f"Herd {i+1}: {self.herds[i]}")

    def player_move(self):
        if self.current_player != "Player":
            return

        try:
            herd = int(self.herd_choice.get()) - 1
            cows = self.cows_entry.get().strip()

            if cows == "Enter number of cows" or not cows:
                raise ValueError("Please enter the number of cows to remove.")

            cows = int(cows)

            if herd not in range(3):
                raise ValueError("Invalid herd selection.")

            if cows <= 0:
                raise ValueError("Number of cows to remove must be positive.")

            if cows > self.herds[herd]:
                raise ValueError(f"Herd {herd + 1} does not have {cows} cows.")

            # Perform the move
            self.herds[herd] -= cows
            self.update_herd_display()
            self.status_label.config(text=f"Player removed {cows} cow(s) from Herd {herd + 1}.")

            if all(h == 0 for h in self.herds):
                messagebox.showinfo("Game Over", "Player wins!")
                self.master.quit()
                return

            # Switch to Computer's turn
            self.current_player = "Computer"
            self.disable_move()
            self.master.after(1000, self.computer_move)

        except ValueError as ve:
            messagebox.showerror("Invalid Move", str(ve))

    def computer_move(self):
        if all(cows == 0 for cows in self.herds):
            messagebox.showinfo("Game Over", "Computer wins!")
            self.master.quit()
            return

        # Smart Strategy: Remove all cows from a randomly selected non-empty herd
        non_empty_herds = [i for i, cows in enumerate(self.herds) if cows > 0]
        if not non_empty_herds:
            messagebox.showinfo("Game Over", "Computer wins!")
            self.master.quit()
            return

        herd_index = random.choice(non_empty_herds)
        cows_to_remove = random.randint(1, self.herds[herd_index])

        self.herds[herd_index] -= cows_to_remove
        self.update_herd_display()
        self.status_label.config(text=f"Computer removed {cows_to_remove} cow(s) from Herd {herd_index + 1}.")

        if all(h == 0 for h in self.herds):
            messagebox.showinfo("Game Over", "Computer wins!")
            self.master.quit()
            return

        # Switch back to Player's turn
        self.current_player = "Player"
        self.enable_move()
        self.show_instructions("choose")

    def show_instructions(self, instruction_key):
        self.instruction_label.config(text=self.instructions[instruction_key])

    def disable_move(self):
        self.move_button.config(state="disabled")
        self.herd_optionmenu.config(state="disabled")  # OptionMenu doesn't support 'state', but included for consistency
        self.cows_entry.config(state="disabled")

    def enable_move(self):
        self.move_button.config(state="normal")
        self.herd_optionmenu.config(state="normal")  # OptionMenu doesn't support 'state', but included for consistency
        self.cows_entry.config(state="normal")
        self.cows_entry.delete(0, tk.END)
        self.cows_entry.insert(0, "Enter number of cows")
        self.cows_entry.config(fg='grey')

if __name__ == "__main__":
    root = tk.Tk()
    game = CowHerdGame(root)
    root.mainloop()
