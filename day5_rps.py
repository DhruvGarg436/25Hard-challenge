# ROCK,PAPER AND SCISSORS
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("Rock,paper,scissors".center(35, "."))
player_ch = int(
    input("Enter.....\n 1 for 'Rock'\n 2 for 'Paper'\n 3 for'Scissors'\n"))
comp_ch = int(random.choice("123"))
print("You choose", str(RPS(player_ch)).replace("RPS.", ""))
print("computer choose", str(RPS(comp_ch)).replace("RPS.", ""))
if player_ch > 3 or player_ch < 1:
    print("Wrong choice,please enter again")
if player_ch == comp_ch:
    print("Tie game!, good try")
elif player_ch == 1 and comp_ch == 3:
    print("Hooray!,You win")
elif player_ch == 2 and comp_ch == 1:
    print("Hooray!,You win")
elif player_ch == 3 and comp_ch == 2:
    print("Hooray!,You win")
else:
    print("OH no! You lost,Better luck next time")
