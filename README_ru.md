# Bird species bot (Телеграм бот для классификации птиц по фотографии)



## Dataset preparation 
[Код для сбора датасета](https://github.com/LadaChernenko/bird_species_guide/tree/main/collecting_dataset)

Для обучения нейросети был собран датасет с птицами европейской части России. 
Всего в обучении участовало 350 классов.

Не менее 100 изображений на класс.

[Bird dataset from Google Drive](https://drive.google.com/file/d/1cUw8hBoF0PEYHbLMfWB2x-k2lV1YMPb5/view?usp=sharing)

- латинские названия птиц были взяты [тут](https://www.ebirds.ru/russia/index.html)
- с помощью библиотек selenium; urllib; user_agent; logging были собраны изображения из google images по латинским названиям
- вручную очищен датасет 



___
## Image classification

[image_classification](https://github.com/LadaChernenko/bird_species_guide/tree/main/bird_classification)

В задаче классификации участвовали фотографии 350 классов. Это распростинённые в европейской части России виды птиц.
(фотографии были собраны из google images по латинским названиям.


В качестве модели использовалась предобученная [EfficientNet](https://arxiv.org/pdf/1905.11946.pdf)
### Architecture
![Architecture](https://github.com/LadaChernenko/bird_species_guide/blob/main/img/Architecture-of-EfficientNet-B0-with-MBConv-as-Basic-building-blocks.png)

### Result
![img_classification](https://github.com/LadaChernenko/bird_species_guide/blob/main/img/classification_pred.png?raw=true)

**CrossEntropyLoss**
- train loss: 0.665
- validation loss: 0.693

- Train accuracy: 82.559685%
- Validation accuracy: 81.350510%
___
## Telegram bot
@bird_species_bot по [ссылке](https://t.me/bird_species_bot)


[Код telegram bot](https://github.com/LadaChernenko/bird_species_guide/tree/main/telegram_bot)
### Библиотеки:
- aiogram==2.17.1
- torch==1.10.0+cpu
- torchvision==0.11.1+cpu
- efficientnet-pytorch==0.7.1
- wikipedia==1.4.0

[requirements.txt](https://github.com/LadaChernenko/bird_species_guide/blob/main/telegram_bot/requirements.txt)
### Принцип работы бота:
- 1 Телеграм бот **bot.py** получает на вход картинку 
- 2 Сохраняет в папку
- 3 Передаёт на вход **app.py**
  - 3.1 Трансформирование изображения
  - 3.2 Предсказание класса и вероятности предобученной моделью efficientnet-b0
- 4 Бот передёт пользователю топ-3 предсказанных класса и вероятности.
- 5 Удаляет картинку
- 6 По латинскому названию класса с максимальной вероятностью выдаётся страница с википедии **wiki_parser.py**


