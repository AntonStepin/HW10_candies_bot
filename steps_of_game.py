from random import randint
from candies import*

def step_1 (update, context, user_msg, sweet):
    if user_msg.isdigit():
        sweet = int(user_msg)
        step = 2
        context.bot.send_message(update.effective_chat.id, "Выбери сколько конфет можно брать за раунд")
        return [sweet, step]
    else: context.bot.send_message(update.effective_chat.id, "Не понял тебя что то, нужно ввести цифры")


def step_2(update, context, user_msg, sweet_round):
    if user_msg.isdigit():
        sweet_round = int(user_msg)
        step = 3
        context.bot.send_message(update.effective_chat.id, "Будешь играть со мной или с другом?")
        return [sweet_round, step]
    else: context.bot.send_message(update.effective_chat.id, "Не понял тебя что то, нужно ввести цифры")


def step_3(update, context, user_msg, bot_on, turn):
    if "друг" in user_msg or "втор" in user_msg:
        context.bot.send_message(update.effective_chat.id, "С другом так с другом... зачем тогда меня позвал...")
        bot_on = False
        turn = randint(0,1)
        context.bot.send_message(update.effective_chat.id, "Как зовут друга?")
        step = 4
        return [bot_on, turn, step]
    elif "тобо" in user_msg or "перв" in user_msg:
        bot_on = True
        context.bot.send_message(update.effective_chat.id, "Cо мной значит...ну давай сыграем")   
        turn = randint(0,1)
        step = 4
        # context.bot.send_message(update.effective_chat.id, "Ну что уверен....играем?")
        return [bot_on, turn, step]
    else: context.bot.send_message(update.effective_chat.id, "Ничего не понял... так с кем?")

def step_4(update, context, user_msg,bot_on,sweet, sweet_round, turn, friend_name):
    context.bot.send_message(update.effective_chat.id, f"Итого: {sweet} конфет в банке, максимальный ход {sweet_round} конфет")
    if bot_on == True:
        # if not "да" in user_msg: context.bot.send_message(update.effective_chat.id, "Мне все равно))")
        if turn == 0: 
            context.bot.send_message(update.effective_chat.id, "Первым хожу я)))")
            temp_bot_move = game_core_smart_bot(sweet,sweet_round)
            sweet-= temp_bot_move
            context.bot.send_message(update.effective_chat.id, f"Мой ход {temp_bot_move}")
            if sweet > 0:
                context.bot.send_message(update.effective_chat.id, f"Осталось {sweet} конфет")
                context.bot.send_message(update.effective_chat.id, f"Твой ход")
                turn = 1
        else: context.bot.send_message(update.effective_chat.id, "Ладно... ходи ты..")
    elif bot_on == False:
        friend_name = user_msg
        if turn == 0: context.bot.send_message(update.effective_chat.id, "Первым ты ходишь")
        else: context.bot.send_message(update.effective_chat.id, f"Первым ходит {friend_name}")
    step = 5
    return [sweet, friend_name, step, turn]

def step_5 (update, context, user_msg,bot_on,sweet:int, sweet_round, friend_name, turn, game):
    if user_msg.isdigit():
        if bot_on == True:
            if turn == 0:
                if sweet > 0:
                    # game = True
                    bot_move = game_core_smart_bot(sweet, sweet_round)
                    turn = 1
                    sweet -= bot_move
                    context.bot.send_message(update.effective_chat.id, f" Мой ход {bot_move}")
                    context.bot.send_message(update.effective_chat.id, f"Осталось {sweet} конфет")
                    if sweet<=0:
                        context.bot.send_message(update.effective_chat.id, "Ладно, я поддался...ты выиграл")
                        game = False
                        context.bot.send_message(update.effective_chat.id, f"Хочешь еще сыграть? /Lets_go ")
                    else: context.bot.send_message(update.effective_chat.id, f"Твой ход")
                    return [sweet, turn, game]
            elif turn == 1:
                if int(user_msg) < 1 or int(user_msg) > sweet_round:
                    context.bot.send_message(update.effective_chat.id, f"Так не честно, ход доджен быть от 0 до {sweet_round}")
                else: 
                    if sweet > 0:
                        sweet-=int(user_msg)
                        context.bot.send_message(update.effective_chat.id, f"Осталось {sweet} конфет")
                        turn = 0
                        if sweet <= 0:
                            if sweet == 0:
                                context.bot.send_message(update.effective_chat.id, "Поздравляю я выиграл")
                            elif sweet < 0:
                                context.bot.send_message(update.effective_chat.id, "Столько конфет конечно нет, бери все что осталось и ты проиграл")   
                            turn = 2
                            game = False
                            context.bot.send_message(update.effective_chat.id, f"Хочешь еще сыграть? /Lets_go ")
                        return [sweet, turn, game]      
        elif bot_on == False:
            bot = 0
            if int(user_msg) < 0 or int(user_msg) > sweet_round:
                 context.bot.send_message(update.effective_chat.id, f"Так не честно, ход доджен быть от 0 до {sweet_round}")
            else:
                move = int(user_msg)
                sweet -= move
                if turn == 0:
                    if sweet > 0:
                        turn = 1
                        # game = True
                        context.bot.send_message(update.effective_chat.id, f"Теперь ходит {friend_name}")
                        context.bot.send_message(update.effective_chat.id, f"Осталось {sweet} конфет")
                        return [sweet, turn, game]
                    if sweet<=0:
                        if sweet < 0:
                            context.bot.send_message(update.effective_chat.id, "Столько конфет конечно нет, бери все что осталось и ты проиграл") 
                        game = False
                        context.bot.send_message(update.effective_chat.id, f"Выиграл {friend_name}")
                        context.bot.send_message(update.effective_chat.id, f"Хочешь еще сыграть? /Lets_go ")
                        return [sweet, turn, game]
                elif turn == 1:
                    if sweet > 0:
                        turn = 0
                        context.bot.send_message(update.effective_chat.id, f"Теперь ты ходишь")
                        context.bot.send_message(update.effective_chat.id, f"Осталось {sweet} конфет")
                        # game = True
                        return [sweet, turn, game]
                    elif sweet <= 0:
                        if sweet < 0:
                            context.bot.send_message(update.effective_chat.id, f"Столько конфет конечно нет, {friend_name} бери все что осталось и ты проиграл")
                        game = False
                        context.bot.send_message(update.effective_chat.id, f"Выиграл хозяин аккаунта")
                        context.bot.send_message(update.effective_chat.id, f"Хочешь еще сыграть? /Lets_go ")
                        return [sweet, turn, game]
    else:context.bot.send_message(update.effective_chat.id, f"Тут только цифры")
            