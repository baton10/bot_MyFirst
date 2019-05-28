from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # 0 при работе ользователей с ботом присылает уведомление. позволяет реагировать админу и отвечать самостоятельно
# 7 импортируем CommandHandler
# 17 import MessageHandler и Filters - для обработки сообщений пользователей
import logging # 13 логировани.импортируем

import settings #PROXY см settings # 5 настройки прокси. Консанты приято писать капсом 'PROXY'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # 14.1 формат нашего лога: %(asctime)s - дата и время; %(name)s - имя нашего файла в котором, что-то произошло; %(levelname)s - уровень важности события; %(message)s - сообщение, что произошло
                    level=logging.INFO, # 14.2 INFO - будем получать сообщения всех уровней. включает в себя уровень error, warning
                    filename='bot.log' # 14.3 название файла с логами
                    ) # 14 конфигурируем логирование. Появилась файл "bot.log"

def talk_to_me(bot, update): # 6 (!!!!!!СТРАННО ПЕРЕСМОТРЕТЬ. 19 )обращаемся к updater что бы он использовал
    #user_text = update.message.text
    user_text = "Привет {}! Ты написал {}".format(update.message.chat.first_name, update.message.text) # 21 достаем и возвращаем данные из update.message пользователю
    #print(user_text)
    #print(update.message)  # 20 подробная информация о сообщении и пользователе: номер чата, время, имя....в консоле
    logging.info("User: %s, Chat id: %s, Message %s",
                 update.message.chat.username, update.message.chat.id, update.message.text) # 22 заносим информацию с update.message в log. %s - информация из update.massage
    update.message.reply_text(user_text)
def greet_user(bot, update): # 10 создаем функцию greet_user. Обязательно два параметра - (bot, update)
    text = 'Вызван /start'
    print(text) # 11 При запросе в боте /start в консоле будет отображаться Вызван /start
    logging.info(text)  # 16 Можем текст заносить в log
    update.message.reply_text(text) # 12 выводтекста пользователю

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY) # 1 Переменная для взаимодействия с ботом. Тут так же храниться ключ

    logging.info('Бот запускается') # 15 создаем информационное сообщение при запуске бота. В файл "bot.log"

    dp = mybot.dispatcher # 9 положим mybot.dispatcher в переменную dp, что бы сократить код
    dp.add_handler(CommandHandler("start", greet_user)) # 8 специальный обект .dispatcher, который принимает соощение от пользователя и отправляет его. При start вызывается функция greet_user
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) # 18 Filters.text - реагирует только на текстовые сообщения; talk_to_me -  название функции, которая будет вызвана, когда сработает add.handler
    mybot.start_polling() # 2 команда начинающая работу боту: "ходи в телеграм и проверяй наличие сообщений"
    mybot.idle() # 3 будет работать пока мы не остановим (работать бесконечно).

main() # 4 вызов функции. № 0 - 3 минимальое тело бота