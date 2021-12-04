from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.webhook import *
import logging
import os
from config import TOKEN
from wiki_parser import get_wiki_info
from app import get_prediction



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

species = []
with open('labels.txt', 'r') as f:
    for bird in f:
        species.append(bird[:-1].lower())

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ бот рассказывающий про птиц!\nЯ могу угадать птицу по картинке. \n Пришли мне фотографию интересующей тебя птицы, и скажу что это за вид")

# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Пришли мне латинское название, и я расскажу об этой птичке!\nПришли мне фотографию птицы, и я пришлю её латинское название")


@dp.message_handler()
async def ans_message(msg: types.Message):
    query = msg.text
    if query.lower() not in species:
        await bot.send_message(chat_id=msg.from_user.id, text='Я не знаю такой птицы:(\nПопробуй другое название')
    else:
        title, answer, wiki_url = get_wiki_info(query)
        await bot.send_message(chat_id=msg.from_user.id, text=title+'\n\n'+ answer +'\n' + wiki_url + '\n')

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(msg):
    # download user img
    download_dir = './img/'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    img_name = 'img'+str(msg.from_user.id)+'.jpg'
    await msg.photo[-1].download('./img/' + img_name)
    # predict
    top_3_pred, top_3_prob = get_prediction('./img/' + img_name)
    # delate user img
    os.remove('./img/' + img_name)
    if top_3_prob[0] < .5:
        await bot.send_message(chat_id=msg.from_user.id, text='Увы, я не знаю такой птицы :( ')
    else:
        await bot.send_message(chat_id=msg.from_user.id, 
                                text='*{label} ({p:.2f}%)*'.format(label=top_3_pred[0], p=top_3_prob[0]*100)+'\n'+
                                    '{label} ({p:.2f}%)'.format(label=top_3_pred[1], p=top_3_prob[1]*100)+'\n'+
                                    '{label} ({p:.2f}%)'.format(label=top_3_pred[2], p=top_3_prob[2]*100),parse_mode='Markdown')
        title, wiki_url = get_wiki_info(top_3_pred[0])
        await bot.send_message(chat_id=msg.from_user.id, text=title+'\n' + wiki_url + '\n')

if __name__ == '__main__':
    # webhook_path = ''
    # if webhook_path:
    #     executor.start_webhook(dp, webhook_path)
    # else:
    executor.start_polling(dp)