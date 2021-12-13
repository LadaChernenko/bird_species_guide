# bird_species_guide
classification bird species

## Dataset preparation 
Для обучения нейросети был собран датасет с птицами европейской части России. Всего в обучении участовало 350 классов.
Не менее 100 изображений на класс.
[Bird dataset](https://drive.google.com/file/d/1cUw8hBoF0PEYHbLMfWB2x-k2lV1YMPb5/view?usp=sharing)

- латинские названия птиц были взяты [тут](https://www.ebirds.ru/russia/index.html)
- с помощью библиотек selenium; urllib; user_agent; logging были собраны изображения из google images по латинским названиям
- вручную очищен датасет 



___
## Image classification

[image_classification](https://github.com/LadaChernenko/bird_species_guide/tree/main/bird_classification)

В задаче классификации участвовали фотографии 350 классов. Это распростинённые в европейской части России виды птиц.
(фотографии были собраны из google images по латинским названиям.


В качестве модели использовалась предобученная [EfficientNet](https://arxiv.org/pdf/1905.11946.pdf)

![img_classification](https://github.com/LadaChernenko/bird_species_guide/blob/main/img/classification_pred.png?raw=true)___
