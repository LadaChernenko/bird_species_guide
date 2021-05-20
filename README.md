# bird_species_guide
detection and classification bird species

## Bird detection

[object_detecrtion](https://github.com/LadaChernenko/bird_species_guide/tree/main/object_detecrtion)
### Libraries:
* torch
* torchvision
* numpy
* matplotlib
* json
* PIL
* pathlib
* albumentations

Для детекции были взяты фотографии птиц из [Систематической галлереи птиц россии](http://www.rbcu.ru/birdclass/) и с помощью парсера из Google images для 21 самому распространённому виду птиц.
Разметка производилась с помощью Label Studio. Для каждого изображения были найдены bounding boxы.

В качестве модели была выбрана предобученая сеть `ResNet-18`.
![object center prediction](https://github.com/LadaChernenko/bird_species_guide/blob/main/img/localisation_pred.png?raw=true)
___
