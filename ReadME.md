🐄 Cow Herd Game 🐄
Welcome to the Cow Herd Game, where you face off against the computer to strategically remove cows from herds. The last one to remove the cows wins!

This repository contains two versions of the game:

Console Version: A text-based version that runs in your terminal.
Tkinter GUI Version: A graphical version with a fun, interactive interface using Tkinter.
Table of Contents
About the Game
Console Version
How to Run
How to Play
Tkinter GUI Version
How to Run
How to Play
Strategy
License
About the Game
In the Cow Herd Game, there are 3 herds of cows. Each player takes turns removing cows from a selected herd. The objective is to make the other player remove the last cow(s).

Console Version
How to Run (Console Version)
Clone or Download the repository.

Open a terminal and navigate to the directory where the file cow_herd_game_console.py is located.

Run the script using Python:

python cow_herd_game_console.py
The game will start in your terminal.

How to Play (Console Version)
You will be prompted to enter the number of cows in each of the 3 herds to start the game.

On your turn:

Select which herd you want to remove cows from.
Enter how many cows you want to remove.
The computer will make its move after you.

The game continues until all cows are removed from the herds. The player forced to remove the last cow(s) loses.

Replay: After the game ends, you will be asked if you want to play again or exit.

Tkinter GUI Version
How to Run (Tkinter Version)
Clone or Download the repository.

Open a terminal and navigate to the directory where the file cow_herd_game_gui.py is located.

Run the script using Python:

python cow_herd_game_gui.py
The graphical game window will appear.

How to Play (Tkinter Version)
Start the Game:

Enter the number of cows in each herd in the provided entry fields.
Press the "Start Game" button to initialize the game.
Your Turn:

Select a herd using the radio buttons.
Enter the number of cows you want to remove from the selected herd.
Click the "Remove Cows" button to make your move.
Computer’s Turn:

The computer will automatically make its move after yours.
Messages will display the computer’s actions.
The game continues until all cows are removed from the herds. The player forced to remove the last cow(s) loses.

Replay: After the game ends, click "Play Again" to reset the game and start over, or close the window to exit.

Strategy
The Cow Herd Game is based on the concept of Nim-Sum, a game theory strategy:

If the Nim-Sum (XOR of all herd sizes) is 0, the current player is at a disadvantage.
A winning strategy involves making the Nim-Sum 0 after your move, forcing the opponent into a losing position.
The computer uses this strategy to make smart moves.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Happy gaming! 🐄🎉