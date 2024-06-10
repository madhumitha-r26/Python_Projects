# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:52:35 2024

@author: Madhumitha
"""

import random

player = input("R for Rock, R for paper, S for scissor:")
choose = ["R","P","S"]
computer=random.choice(choose)
print(f'your choice {player} <=> opponent {computer}')
if(player==computer):
    print("GAME IS IN TIE!")
elif((player=='R' and computer=='S') or(player=='S' and computer=='P')or (player=='P' and computer=='R') ):
    print("YOU WON THE GAME!")
else:
    print("BETTER LUCK NEXT TIME!")
