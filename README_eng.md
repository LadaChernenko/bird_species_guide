# Bird species bot (Телеграм бот для классификации птиц по фотографии)



## Dataset preparation 
[Код для сбора датасета](https://github.com/LadaChernenko/bird_species_guide/tree/main/collecting_dataset)

Для обучения нейросети был собран датасет с птицами европейской части России. 
Всего в обучении участовало 350 классов.

At least 100 images per class. 

[Bird dataset from Google Drive](https://drive.google.com/file/d/1cUw8hBoF0PEYHbLMfWB2x-k2lV1YMPb5/view?usp=sharing)

- the latin names of the birds were taken from [here](https://www.ebirds.ru/russia/index.html)
- images were collected from google images by latin names using libraries  selenium; urllib; user_agent; logging 
- dataset was manually cleared  



___
## Image classification

[image_classification](https://github.com/LadaChernenko/bird_species_guide/tree/main/bird_classification)



### Architecture

For model used pretrained [EfficientNet-b0](https://arxiv.org/pdf/1905.11946.pdf)
350 classes on the last layer 

![Architecture](https://github.com/LadaChernenko/bird_species_guide/blob/main/img/Architecture-of-EfficientNet-B0-with-MBConv-as-Basic-building-blocks.png)
*EfficientNet-b0*

### Results
![img_classification](https://github.com/LadaChernenko/bird_species_guide/blob/main/img/classification_pred.png?raw=true)

Loss function **CrossEntropyLoss**
- train loss: 0.665
- validation loss: 0.693

- Train accuracy: 82.559685%
- Validation accuracy: 81.350510%
___
## Telegram bot
@bird_species_bot  [link](https://t.me/bird_species_bot)


[Telegram bot code](https://github.com/LadaChernenko/bird_species_guide/tree/main/telegram_bot)
### Libraries:
- aiogram==2.17.1
- torch==1.10.0+cpu
- torchvision==0.11.1+cpu
- efficientnet-pytorch==0.7.1
- wikipedia==1.4.0

[requirements.txt](https://github.com/LadaChernenko/bird_species_guide/blob/main/telegram_bot/requirements.txt)
### How it works:
- 1 Telegram bot **bot.py** get the image 
- 2 Saves to folder 
- 3 **app.py** get img
  - 3.1 Transform
  - 3.2 Pretrained efficientnet-b0 predict labels and probability
- 4 Bot give to the user  top-3 predicted classes and probability
- 5 Delete the image
- 6 **wiki_parser.py** search wikipedia page for latin name of species and give it to user


