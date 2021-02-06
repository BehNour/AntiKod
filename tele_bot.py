import telebot

token = "1600823712:AAHxfoGTg43X4KBYUK69pzOG32x92S7_iGs"
bot = telebot.TeleBot(token, parse_mode=None)
bot.set_webhook("https://shrouded-meadow-23659.herokuapp.com/" + token)
dict_kod = {"مولا":"محسن دهنوی"}
@bot.message_handler(commands=['help', 'start'])
    def send_welcome(message):
        bot.reply_to(message, "hello :)")

@bot.message_handler(func=lambda message:True)
    def AKod (message):
        for item in dict_kod.keys():
            if message.text == item:
                str_ = "عبارت \"" + item + "\" می تواند اشاره به \"" + dict_kod[item] + "\" داشته باشد."
                bot.reply_to(message, str_)



# offset = None
# print(bot.get_me(),'\n')
# upd_list = bot.get_updates(offset)
# print(len(upd_list))
# upd_last = upd_list[len(upd_list)-2]
# print(upd_last)
# offset = upd_last.update_id
#
# print(upd_list)
# print(upd_last.message)
# if (upd_last.message.content_type == 'new_chat_members'):
#     first_name = upd_last.message.new_chat_members[0].first_name
#     if first_name == None:
#         first_name = ""
#     last_name = upd_last.message.new_chat_members[0].last_name
#     if last_name == None:
#         last_name = ""
#     print(first_name,last_name , "\n خوش اومدی")





