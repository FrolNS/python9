import telebot
from random import randint
from random import choice

bot = telebot.TeleBot("")

candys = 117


@bot.message_handler(commands="start")
def send_welcome(message):
    global turn, candys
    turn = choice(['Bot', 'User'])
    bot.send_message(message.chat.id, f'Первым начинает {turn}')
    if turn == 'Bot':
        take = randint(1, candys % 29)
        candys -= take
        bot.send_message(message.chat.id, f"Bot взял {take} конфет, осталось {str(candys)}")
        turn = 'User'



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global candys, turn
    if turn == 'User':
        if candys > 28:
            if 1 <= int(message.text) <= 28:
                candys -= int(message.text)
                bot.send_message(message.chat.id, f"Вы забрали {message.text} конфет, осталось {str(candys)}")
                turn = 'Bot'
            else:
                bot.send_message(message.chat.id, "Столько взять нельзя!")
        else:
            bot.send_message(message.chat.id, "Выиграл User")
        if turn == 'Bot':
            if candys > 28:
                take = randint(1, candys % 29)
                candys -= take
                bot.send_message(message.chat.id, f"Bot взял {take} конфет, осталось {str(candys)}")
                turn = 'User'
            else:
                bot.send_message(message.chat.id, "Выиграл Bot")


bot.infinity_polling()
