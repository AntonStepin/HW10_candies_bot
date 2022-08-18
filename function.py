
from random import randint
from candies import*
from steps_of_game import*

global game
game = False
global step
global sweet
global sweet_round
global bot_on
global turn

def start(update, context):
    context.bot.send_message(update.effective_chat.id, f"Привет это игра в конфеты! "
                                                    f"Выберай сколько конфет будет в банке. "
                                                    f"Какое количество конфет можно взять за раунд. "
                                                    f"Кто забрал последнюю конфету тот и проиграл. /Lets_go ?")

def lets_go(update, context):
    context.bot.send_message(update.effective_chat.id, "Выбери количество конфет в банке")
    global game
    game = True
    global sweet
    sweet = 0
    global step
    step = 1
    global sweet_round
    sweet_round = 0
    global bot_on
    bot_on = False
    global turn
    turn = 0
    global friend_name
    friend_name = ""

def main(update, context):
    text = update.message.text
    global step
    global bot_on
    global turn
    global sweet
    global sweet_round
    global friend_name
    global game
    user_msg = str(text)
    if game: 
        if step == 1:
            blok = step_1(update, context, user_msg, sweet)
            sweet = blok[0]
            step = blok[1]
        elif step == 2:
            blok = step_2(update, context, user_msg, sweet_round)
            sweet_round = blok[0]
            step = blok[1]
        elif step == 3:
            blok = step_3(update, context, user_msg, bot_on, turn)
            bot_on = blok[0]
            turn = blok[1]
            step = blok[2]
            if bot_on == True and turn < 2:
                return main(update, context)
        elif step == 4:
            blok = step_4(update, context, user_msg,bot_on,sweet, sweet_round, turn, friend_name)
            sweet = blok[0]
            friend_name = blok[1]
            step = blok[2]
            turn = blok[3]
        elif step ==5:
            blok = step_5(update, context, user_msg,bot_on,sweet, sweet_round, friend_name, turn, game)
            sweet = blok[0]
            turn = blok[1]
            game = blok[2]
            if turn == 0 and bot_on == True:
                return main(update, context)
    else:
        context.bot.send_message(update.effective_chat.id, "Ну и ладно...если передумаешь /Lets_go")
                
                    
            
            
        