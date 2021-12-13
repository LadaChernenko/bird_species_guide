import os
TOKEN = os.getenv('BOT_TOKEN')
# TOKEN = '1944875868:AAH3sciPPOs7gaQHdge4pkQAvLMhax8TC_A'
IMG_SIZE = [256, 256]

# webhook settings
WEBHOOK_HOST = 'https://bird-species-bot-app.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))


