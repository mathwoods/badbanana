#!/usr/bin/env python3
'''
********************************************************************************
Mathwoods - Bad Banana Redux
A text-based game in which a player mentally multiplies two whole numbers as
many times as possible.
Tested on Python 3.4.1
Created by Mathwoods, June-July 2017
Last modified: July 7, 2017
********************************************************************************
'''
from badbanana.cli.cligame import CliGame
from badbanana.player import Player

if __name__ == '__main__':
    player = Player()
    game = CliGame(player=player)
    game.play()
