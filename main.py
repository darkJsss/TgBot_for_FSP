import requests
import telebot as tg
from telebot import types

from config import TOKEN

bot = tg.TeleBot(TOKEN)
users = {}
Admin_list = requests.get(f'https://12447695.pythonanywhere.com/api/schools').json()
Admin_list_ids = list(str(i["id"]) for i in Admin_list)
Admin_list_passwords = list(str(i["password"]) for i in Admin_list)
Admin_list_names = list(str(i["name"]) for i in Admin_list)

@bot.message_handler(commands=['start'])
def start(message):
    global users
    user_id = message.from_user.id
    users[user_id] = {}
    bot.send_message(message.from_user.id, "Здравствуйте", reply_markup=types.ReplyKeyboardRemove(),
                     parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)