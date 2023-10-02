import sys
import time
import topic
import game_style
print()
user_n = input("insert your name: ")
print(f"{user_n} do you really wanna play this game?")
user_choice = input(": ")
if user_choice == "yes": 
 print()
 import loading_game
 print()
 import game_bd
else:
  print()
  sys.exit("bye...\nYou would have said 'yes' ")
sys.exit("please rate our game...")


