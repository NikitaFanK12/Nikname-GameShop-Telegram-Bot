import telebot

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def start(message):
    text = str()
    markup = telebot.types.ReplyKeyboardMarkup()
    if message.text == "/start":
        text = "Hello, I am a bot"
        markup.add(telebot.types.KeyboardButton("Магазин"),
        telebot.types.KeyboardButton("Акції"),
        telebot.types.KeyboardButton("Новинки"),
        telebot.types.KeyboardButton("Відгуки"),
        telebot.types.KeyboardButton("Правила"),
        telebot.types.KeyboardButton("Тех підтримка"))

        #for i in range(2):
        #    bot.delete_message(message.chat.id, message.message_id-i)
    elif message.text == "Магазин":
        text = "Hello, I am a bot"
        markup.add(telebot.types.KeyboardButton("Steam"),
        telebot.types.KeyboardButton("Epic games"),
        telebot.types.KeyboardButton("Origin"),
        telebot.types.KeyboardButton("PlayStore"),
        telebot.types.KeyboardButton("X Box"),
        telebot.types.KeyboardButton("Black market"),
        telebot.types.KeyboardButton("Назад"))

        #for i in range(2):
        #    bot.delete_message(message.chat.id, message.message_id-i)
    elif message.text == "Назад":
        text = "Hello, I am a bot"
        markup.add(telebot.types.KeyboardButton("Магазин"),
        telebot.types.KeyboardButton("Акції"),
        telebot.types.KeyboardButton("Новинки"),
        telebot.types.KeyboardButton("Відгуки"),
        telebot.types.KeyboardButton("Правила"),
        telebot.types.KeyboardButton("Тех підтримка"))

        #for i in range(2):
        #    bot.delete_message(message.chat.id, message.message_id-i)
    bot.send_message(message.chat.id, text, reply_markup=markup)

bot.infinity_polling()
