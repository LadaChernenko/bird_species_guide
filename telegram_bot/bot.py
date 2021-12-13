from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.webhook import *
import logging
import os
from config import TOKEN, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
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
    await message.reply("Привет!\nЯ могу угадать птицу по картинке. \n Пришли мне фотографию, и скажу что это за вид. \n\n К сожалению, я пока знаю не всех птиц, \n а только тех что живут в Европейской части России.")

# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Пришли мне латинское название, и я расскажу об этой птичке!\nПришли мне фотографию птицы, и я пришлю её латинское название")



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
    if top_3_prob[0] < .3:
        await bot.send_message(chat_id=msg.from_user.id, text='Увы, я не знаю такой птицы :( ')
    else:
        await bot.send_message(chat_id=msg.from_user.id, 
                                text='*{label} ({p:.2f}%)*'.format(label=top_3_pred[0], p=top_3_prob[0]*100)+'\n'+
                                    '{label} ({p:.2f}%)'.format(label=top_3_pred[1], p=top_3_prob[1]*100)+'\n'+
                                    '{label} ({p:.2f}%)'.format(label=top_3_pred[2], p=top_3_prob[2]*100),parse_mode='Markdown')
        title, wiki_url = get_wiki_info(top_3_pred[0])
        await bot.send_message(chat_id=msg.from_user.id, text=title+'\n' + wiki_url + '\n')


async def on_startup(dp):
    logging.warning('Starting connection. ')
    await bot.set_webhook(WEBHOOK_URL,drop_pending_updates=True)


async def on_shutdown(dp):
    logging.warning('Bye! Shutting down webhook connection')


if __name__ == '__main__':
    # executor.start_webhook(
    #     dispatcher=dp,
    #     webhook_path=WEBHOOK_PATH,
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    #     host=WEBAPP_HOST,
    #     port=WEBAPP_PORT,
    # )
    executor.start_polling(dp)