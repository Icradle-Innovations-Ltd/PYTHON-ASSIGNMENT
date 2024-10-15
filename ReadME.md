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
Computer's Turn:

The computer will automatically make its move after yours.
Messages will display the computer's actions.
The game continues until all cows are removed from the herds. The player forced to remove the last cow(s) loses.

Replay: After the game ends, click "Play Again" to reset the game and start over, or close the window to exit.

Strategy
The Cow Herd Game is based on the concept of Nim-Sum, a game theory strategy:

The Nim-Sum is calculated by performing a bitwise XOR operation on all the herd sizes.
For example, if the herds have 3, 4, and 5 cows, the Nim-Sum would be 3 XOR 4 XOR 5 = 2.

If the Nim-Sum is 0, the current player is at a disadvantage.
This is because any move they make will result in a non-zero Nim-Sum, giving the opponent a winning position.

A winning strategy involves making the Nim-Sum 0 after your move, forcing the opponent into a losing position.
To do this, you need to remove cows from a herd in such a way that the XOR of the resulting herd sizes is 0.

The computer uses this strategy to make smart moves:
1. It calculates the current Nim-Sum.
2. If the Nim-Sum is not 0, it finds a move that will make it 0.
3. If the Nim-Sum is already 0, it makes a random move, as any move will give the advantage to the opponent.

By understanding and applying the Nim-Sum strategy, you can improve your chances of winning the game.
However, keep in mind that if both players play optimally, the player who starts with a non-zero Nim-Sum will always win.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Happy gaming! 🐄🎉