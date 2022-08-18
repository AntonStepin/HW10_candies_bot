import random

def game_core_smart_bot(sweets_left, game_step):
    if sweets_left / game_step > 1:
        player = game_step
    elif sweets_left // game_step == 0 and sweets_left - 1 !=0:
        player = sweets_left - 1
    elif sweets_left // game_step == 1:
        player = game_step-1
    else:
        player = 1
    return player
