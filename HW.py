import telebot
from telebot import types
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import os
import time


bot = telebot.TeleBot('6974578088:AAE-qBT6FVPesqpH6WcDTa61TJaXwTyyO_o')
project_folder = "/Users/Fedor/PycharmProjects/2kurs"

global ind
ind = 0


def delete_jpg_files(folder_path):
    try:
        files = os.listdir(folder_path)

        jpg_files = [file for file in files if file.endswith(".jpg")]

        for jpg_file in jpg_files:
            file_path = os.path.join(folder_path, jpg_file)
            os.remove(file_path)
            print(f"Удален файл: {file_path}")

    except Exception as e:
        print(f"Произошла ошибка при удалении файлов: {e}")


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='/start')
    btn2 = types.KeyboardButton(text='/help')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, text='выберите функцию', reply_markup=keyboard)



@bot.message_handler(commands=['help'])
def help(message):
    k_b = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = types.KeyboardButton(text='/reverse_photo')
    btn4 = types.KeyboardButton(text='/blur_photo')
    btn5 = types.KeyboardButton(text='/negative_photo')
    k_b.add(btn3)
    k_b.add(btn4)
    k_b.add(btn5)
    bot.send_message(message.chat.id, text='Выберите обработку', reply_markup=k_b)


@bot.message_handler(commands=['reverse_photo'])
def reverse(message):
    msg = bot.send_message(message.chat.id, "Send photo")
    bot.register_next_step_handler(msg, r_photo)


def r_photo(message):
    global ind
    ind += 1
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)

    with open('saved_photo' + str(ind) + '.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)

    im = Image.open('saved_photo' + str(ind) + '.jpg')
    im = im.transpose(Image.FLIP_LEFT_RIGHT)

    bot.send_photo(message.chat.id, im)

    time.sleep(10)
    delete_jpg_files(project_folder)




@bot.message_handler(commands=['blur_photo'])
def blur(message):
    msg = bot.send_message(message.chat.id, "Send photo")
    bot.register_next_step_handler(msg, b_photo)


def b_photo(message):
    global ind
    ind += 1
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)

    with open('saved_photo' + str(ind) + '.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)

    im = Image.open('saved_photo' + str(ind) + '.jpg')

    for i in range(100):
        im = im.filter(ImageFilter.BLUR)

    bot.send_photo(message.chat.id, im)

    time.sleep(10)
    delete_jpg_files(project_folder)







@bot.message_handler(commands=['negative_photo'])
def negative(message):
    msg = bot.send_message(message.chat.id, "Send photo")
    bot.register_next_step_handler(msg, n_photo)


def n_photo(message):
    global ind
    ind += 1
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)

    with open('saved_photo' + str(ind) + '.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)

    im = Image.open('saved_photo' + str(ind) + '.jpg')

    im = ImageOps.invert(im)

    bot.send_photo(message.chat.id, im)

    time.sleep(10)
    delete_jpg_files(project_folder)


bot.polling(none_stop=True, interval=0)
