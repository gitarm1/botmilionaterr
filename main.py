import telebot
from telebot import types
import codecs
from config import token
import random

bot = telebot.TeleBot(token)


rand = 0

sum = 0
userlist = []
idlist = []

@bot.message_handler(commands=['start'])
def any_msg(message):

    global idik
    idik = message.from_user.id

    with open(str(message.from_user.id) + ".txt", "w+") as f:
        f.write("600")


    username = message.from_user.username
    if username not in userlist:
        userlist.append(username)

    if idik not in idlist:
        idlist.append(idik)


    name = message.from_user.first_name

    namak = message.text[7:]

    try:
        bot.send_message(namak, """1 человек зарегистрировался по вашей ссылке🎉
Вы заработали 270 тенге💸""")
        rand = rand + 1

    except:
        pass

    # print(username)
    keyboard = types.InlineKeyboardMarkup()
    okay = types.InlineKeyboardButton(text="✅Ознакомлен", callback_data="okay")

    keyboard.add(okay)
    bot.send_message(message.chat.id, """📸
Добро пожаловать в Угадай Страну,{}  Данная платформа платит тебе за угадывание различных стран мира.
🔥
Вывод средств в течении 2-3 рабочих дней.
✅
Жми "Ознакомлен", чтобы уже начать угадывать страны.""".format(name), reply_markup=keyboard)



@bot.message_handler(commands=['admin'])
def admin_msg(message):
    if message.from_user.id == 1076482828:

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        a1 = types.InlineKeyboardButton(text="Список пользователей", callback_data="userlist")
        a2 = types.InlineKeyboardButton(text="Рассылка", callback_data="sending")
        a4 = types.InlineKeyboardButton(text="Статистика", callback_data="stats")
        a3 = types.InlineKeyboardButton(text="Каналы", callback_data="channels")


        keyboard.add(a1, a2, a4, a3)
        bot.send_message(message.chat.id, "⬇️ Выбери интересующий тебя пункт меню!", reply_markup = keyboard)

    else:
        bot.send_message(message.chat.id, "Я вас не понимаю:(")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "okay":
            global attempts
            attempts = 3
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard = True)
            button = types.KeyboardButton(text='💸Заработать')
            button4 = types.KeyboardButton(text='💼Партнёрство')
            button2 = types.KeyboardButton(text='💰Вывод')
            button3 = types.KeyboardButton(text='🤑Больше денег')
            markup.add(button,button4, button2, button3)

            bot.send_message(call.message.chat.id, '⬇️ Выбери интересующий тебя пункт меню!', reply_markup=markup)

        if call.data[0] == "c":
            print("maladec")
            with open(str(idik) + ".txt", "w+") as f:
                f.write("1200")
            foto = open('paris.jpg', 'rb')
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            a1 = types.InlineKeyboardButton(text="1️⃣", callback_data="a1")
            a2 = types.InlineKeyboardButton(text="2️⃣", callback_data="v2")
            a3 = types.InlineKeyboardButton(text="3️⃣", callback_data="a3")
            a4 = types.InlineKeyboardButton(text="4️⃣", callback_data="a4")

            keyboard.add(a1, a2, a3, a4)
            bot.send_photo(call.message.chat.id, foto)
            bot.send_message(call.message.chat.id,"""✅Правильный ответ! Вы заработали 600 тенге
❓ Страна на 1200 тенге
1️⃣  Сингапур
2️⃣  Франция
3️⃣  Великобритания
4️⃣  США""", reply_markup=keyboard)


        if call.data[0] == "v":
            print("maladec")
            with open(str(idik) + ".txt", "w+") as f:
                f.write("2400")
            foto = open('brazil.jpg', 'rb')
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            a1 = types.InlineKeyboardButton(text="1️⃣", callback_data="a1")
            a2 = types.InlineKeyboardButton(text="2️⃣", callback_data="a2")
            a3 = types.InlineKeyboardButton(text="3️⃣", callback_data="a3")
            a4 = types.InlineKeyboardButton(text="4️⃣", callback_data="b4")

            keyboard.add(a1, a2, a3, a4)
            bot.send_photo(call.message.chat.id, foto)
            bot.send_message(call.message.chat.id,"""✅Правильный ответ! Вы заработали 1200 тенге
❓ Страна на 1800 тенге
1️⃣  Испания
2️⃣  Италия
3️⃣  Франция
4️⃣  Бразилия""", reply_markup=keyboard)

        if call.data[0] == "b":
            print("maladec")
            with open(str(idik) + ".txt", "w+") as f:
                f.write("4000")
            foto = open('china.jpg', 'rb')
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            a1 = types.InlineKeyboardButton(text="1️⃣", callback_data="a1")
            a2 = types.InlineKeyboardButton(text="2️⃣", callback_data="a2")
            a3 = types.InlineKeyboardButton(text="3️⃣", callback_data="n3")
            a4 = types.InlineKeyboardButton(text="4️⃣", callback_data="a4")

            keyboard.add(a1, a2, a3, a4)
            bot.send_photo(call.message.chat.id, foto)
            bot.send_message(call.message.chat.id,"""✅Правильный ответ! Вы заработали 1800 тенге
❓ Страна на 2400 тенге
1️⃣  Малайзия
2️⃣  Испания
3️⃣  Китай
4️⃣  Индия""", reply_markup=keyboard)

        if call.data[0] == "n":
            print("maladec")
            with open(str(idik) + ".txt", "w+") as f:
                f.write("6400")
            foto = open('dubai.jpg', 'rb')
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            a1 = types.InlineKeyboardButton(text="1️⃣", callback_data="a1")
            a2 = types.InlineKeyboardButton(text="2️⃣", callback_data="m2")
            a3 = types.InlineKeyboardButton(text="3️⃣", callback_data="a3")
            a4 = types.InlineKeyboardButton(text="4️⃣", callback_data="a4")

            keyboard.add(a1, a2, a3, a4)
            bot.send_photo(call.message.chat.id, foto)
            bot.send_message(call.message.chat.id,"""✅Правильный ответ! Вы заработали 2400 тенге
❓ Страна на 3600 тенге
1️⃣  Иран
2️⃣  ОЭА
3️⃣  Малайзия
4️⃣  Китай""", reply_markup=keyboard)

        if call.data[0] == "m":
            print("maladec")
            with open(str(idik) + ".txt", "w+") as f:
                f.write("10000")
            foto = open('malaysia.jpg', 'rb')
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            a1 = types.InlineKeyboardButton(text="1️⃣", callback_data="a1")
            a2 = types.InlineKeyboardButton(text="2️⃣", callback_data="z2")
            a3 = types.InlineKeyboardButton(text="3️⃣", callback_data="a3")
            a4 = types.InlineKeyboardButton(text="4️⃣", callback_data="a4")

            keyboard.add(a1, a2, a3, a4)
            bot.send_photo(call.message.chat.id, foto)
            bot.send_message(call.message.chat.id,"""✅Правильный ответ! Вы заработали 3600 тенге
❓ Страна на 7200 тенге
1️⃣  Египет
2️⃣  Малайзия
3️⃣  Испания
4️⃣  Турция""", reply_markup=keyboard)

        if call.data[0] == "z":
            print("maladec")
            with open(str(idik) + ".txt", "w+") as f:
                f.write("17200")
            foto = open('iran.jpg', 'rb')
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            a1 = types.InlineKeyboardButton(text="1️⃣", callback_data="a1")
            a2 = types.InlineKeyboardButton(text="2️⃣", callback_data="a2")
            a3 = types.InlineKeyboardButton(text="3️⃣", callback_data="a3")
            a4 = types.InlineKeyboardButton(text="4️⃣", callback_data="x4")

            keyboard.add(a1, a2, a3, a4)
            bot.send_photo(call.message.chat.id, foto)
            bot.send_message(call.message.chat.id,"""✅Правильный ответ! Вы заработали 7200 тенге
❓ Страна на 9800 тенге
1️⃣  Египет
2️⃣  Малайзия
3️⃣  ОЭА
4️⃣  Иран""", reply_markup=keyboard)

        if call.data == "check":
            bot.send_message(call.message.chat.id,"""✅Вы получили бонус 270 тенге""")

        if call.data[0] == "z":
            print("maladec")
            with open(str(idik) + ".txt", "w+") as f:
                f.write("27000")
            foto = open('egypt.jpg', 'rb')
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            a1 = types.InlineKeyboardButton(text="1️⃣", callback_data="a1")
            a2 = types.InlineKeyboardButton(text="2️⃣", callback_data="a2")
            a3 = types.InlineKeyboardButton(text="3️⃣", callback_data="q3")
            a4 = types.InlineKeyboardButton(text="4️⃣", callback_data="a4")

            keyboard.add(a1, a2, a3, a4)
            bot.send_photo(call.message.chat.id, foto)
            bot.send_message(call.message.chat.id,"""✅Правильный ответ! Вы заработали 9800 тенге
❓ Страна на 12000 тенге
1️⃣  Малайзия
2️⃣  Италия
3️⃣  Египет
4️⃣  США""", reply_markup=keyboard)

        if call.data[0] == "q":
            print("maladec")
            with open(str(idik) + ".txt", "w+") as f:
                f.write("39000")
            bot.send_message(call.message.chat.id,"""🎉 Поздравляю, 🗽𝔄𝔯𝔪𝔪𝔪𝔪! Ты - Победитель!
Ты заработал 12000 рублей. Жми «Вывод» и получи деньги прямо на свою карту!""")


        if call.data[0] == "a" and attempts != 0:
            attempts = attempts - 1
            bot.send_message(call.message.chat.id,"""ℹ
Осталось попыток пройти игру на сегодня: {}""".format(attempts))

        if call.data[0] == "a" and attempts == 0:

            bot.send_message(call.message.chat.id,"""❌Вы выбрали неправильный вариант ответа, но...
😈Игра на этом не закончилась.

Приглашай своих друзей в игру и зарабатывай на этом деньги.
1 Пользователь = 600 тенге
🔽Вот твоя пригласительная ссылка: {}""".format("https://t.me/guesscountrykz_bot?start=" + str(idik)))


        if call.data == "userlist":
            bot.send_message(call.message.chat.id, """⬇️Пользователи\n""")
            for i in userlist:
                bot.send_message(call.message.chat.id, """@{}\n""".format(i))


        if call.data == "sending":
            bot.send_message(call.message.chat.id, """Введите сообщение рассылки...\n""")


        if call.data == "stats":
            for i in userlist:
                sum = sum + 1

            bot.send_message(call.message.chat.id,"""Количество пользователей - {}""".format(sum))    


        if call.data == "withdraw":

            bot.send_message(call.message.chat.id,"""Введите карту(16 цифр без пробелов)...""")


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == "💸Заработать":
        if attempts == 0:
            bot.send_message(message.chat.id, """❓ℹ️
Вы исчерпали свои 3 попытки в день. Завтра попытки восстановятся снова.""")
        else:
            print("yes")
            foto = open('russia.jpg', 'rb')

            keyboard = types.InlineKeyboardMarkup(row_width=2)
            a1 = types.InlineKeyboardButton(text="1️⃣", callback_data="a1")
            a2 = types.InlineKeyboardButton(text="2️⃣", callback_data="ca2")
            a3 = types.InlineKeyboardButton(text="3️⃣", callback_data="a3")
            a4 = types.InlineKeyboardButton(text="4️⃣", callback_data="a4")

            keyboard.add(a1, a2, a3, a4)
            bot.send_photo(message.chat.id, foto)
            bot.send_message(message.chat.id, """❓ Страна на 600 тенге
1️⃣  Франция
2️⃣  Россия
3️⃣  Малайзия
4️⃣  ОЭА""", reply_markup=keyboard)

    if message.text == "💼Партнёрство":
        bot.send_message(message.chat.id, """💰 Зарабатывайте деньги за приглашенных пользователей)

➡️ Ваша пригласительная ссылка:
{}

✔️ 270 рублей за каждого приглашенного Вами пользователя.
✔️ 150 рублей за каждого пришлашенного вашим пользователем.

👥 Вы пригласили: {}
""".format("https://t.me/guesscountrykz_bot?start=" + str(idik), rand))


    if message.text == "🤑Больше денег":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        a1 = types.InlineKeyboardButton(text="💰Канал", url ="https://t.me/onrealevents")
        a2 = types.InlineKeyboardButton(text="✅Проверить", callback_data="check")

        keyboard.add(a1)

        keyboard.add(a1)
        bot.send_message(message.chat.id, """НУЖДАЕТЕСЬ В ДЕНЬГАХ? 100 РУБ ЗА ПОДПИСКУ!

🚀Предлагаем Вам подписаться на канал интернет-маркетолога, которые действительно показывает и обучают заработку в интернете.

Никакой воды: только сухие действия, обучения и результат. 90% учеников уже вышли на доход более 100.000 рублей в месяц и это не предел! Они продолжают развиваться, строят свое будущее и понимают, что работать можно мозгами! И все это бесплатно!

⚖️Единственное, о чем просит администратор - это отдавать 20% от заработанного.
Так же за подписку на канал мы начислим Вам 100 рублей!""")


    if message.text == "💰Вывод":
         with open(str(idik) + ".txt", "r+") as f:
            balance = f.read()

         if int(balance) >= 35000:
             keyboard = types.InlineKeyboardMarkup(row_width=1)
             a1 = types.InlineKeyboardButton(text="💳Вывести", callback_data="withdraw")

             keyboard.add(a1)
             bot.send_message(message.chat.id, """Баланс: {} тенге.
Минимальная сумма вывода: 35000 тенге """.format(str(balance)), reply_markup = keyboard)

         else:
             bot.send_message(message.chat.id, """Баланс: {} тенге.
Минимальная сумма вывода: 35000 тенге """.format(str(balance)))

    if len(message.text) == 16:
             bot.send_message(message.chat.id, """Спасибо, ваш платеж находится в обработке""")




bot.polling()
