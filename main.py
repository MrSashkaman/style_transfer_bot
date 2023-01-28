import telebot
from telegram import Update as update
import os
from model import transfer_model
import os.path
import gc

with open("bot_token.txt") as f:
    TOKEN = f.read()

bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Этот бот берет две фотографии и применяет стиль одной к другой. \
        Чтобы получить результат отправьте сначала фотографию, которую хотите изменить,\
             а затем фотографию, стиль которой хотите применить к первой")

@bot.message_handler(content_types=['text'])
def send_instruction(message):
    bot.reply_to(message, "Отправьте по очереди сначала фотографию, которую хотите изменить,\
                        а затем фотографию, стиль которой вы хотите применить к первой")


@bot.message_handler(content_types=['photo'])
def load_img_and_run(message):
    
    os.makedirs('images/created', exist_ok=True)
    os.makedirs('images/original', exist_ok=True)
    os.makedirs('images/style', exist_ok=True)

    print(os.getcwd()) 
    
    path_img = 'images/original/img.png'
    path_style = 'images/style/style.png'
    path_pics = 'images/created'
    
    if os.path.exists(path_img) == False:

    
        file_info_img = bot.get_file(message.photo[-1].file_id)
        downloaded_file_img = bot.download_file(file_info_img.file_path)
       
        
        with open(path_img, 'wb') as new_file:
            new_file.write(downloaded_file_img)

        bot.reply_to(message, "Добавлено фото для редактирования")

               
    elif os.path.exists(path_img) and os.path.exists(path_style) == False:
    
        
        file_info_style = bot.get_file(message.photo[-1].file_id)
        downloaded_file_style = bot.download_file(file_info_style.file_path)
        src_style = path_style
        
        with open(path_style, 'wb') as new_file:
            new_file.write(downloaded_file_style)

        bot.reply_to(message, "Добавлено фото стиля")
             
        print('OK0')
        
        tf_model = transfer_model(num_steps=200,
                    style_weight=100000,
                    learning_rate=1,
                   step_checkpoint=10)
        tf_model.run_style_transfer()
        
        del tf_model
        gc.collect()
        
        print('OK1')
        img = open('images/created/result_final.jpg', 'rb')
        print('OK2')
        bot.send_photo(message.chat.id, img)


        #os.remove('images/created/result_final.jpg')
        os.remove('images/style/style.png')
        os.remove('images/original/img.png')

bot.infinity_polling()