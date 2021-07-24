# bird_species_guide
detection and classification bird species

## Bird detection

[object_detection](https://github.com/LadaChernenko/bird_species_guide/tree/main/bird_detection)
### Libraries:
* torch
* torchvision
* numpy
* matplotlib
* json
* PIL
* pathlib
* albumentations

Для детекции были взяты фотографии птиц из [Систематической галлереи птиц россии](http://www.rbcu.ru/birdclass/) и, с помощью парсера из Google images, 
для 3 самомым распространённым видам птиц.
Разметка производилась с помощью Label Studio. Для каждого изображения были найдены bounding boxы.

В качестве модели была выбрана предобученая сеть `ResNet-18`.

Изменения 24.07.2021:
- [x] Датасет расширен до 20 классов
- [x] Вместо `ResNet-18` использовалась `YOLOv3`
- [x] Использовались фотографии с более чем одним объектом/классом

Дальнейшие шаги:
- [ ] Использовать предобученую Darknet-53
- [ ] Переписать ф-цию отображения картинок для предсказаний
- [ ] Переписать расчёт MAP на валидационной выборке

![detection_gt](https://github.com/LadaChernenko/bird_species_guide/blob/main/img/detection_gt.png?raw=true)
___
## Image classification

[image_classification](https://github.com/LadaChernenko/bird_species_guide/tree/main/bird_classification)

### Libraries:
* torch
* torchvision
* numpy
* matplotlib
* PIL
* pathlib
* efficientnet_pytorch

В задаче классификации участвовали фотографии 20 классов 
(фотографии были собраны из google images по английским названиям.
`black_kite`,
`chaffinch`,
`common_magpie`,
`crested_tit`,
`common_raven`,
`eurasian_jay`,
`eurasian_pygmy-owl`,
`eurasian_tree_sparrow`,
`european_turtle-dove`,
`great_spotted_woodpecker`,
`hazel_grouse`,
`northern_harrier`,
`ruddy_shelduck`,
`rock_pigeon`,
`snowy_owl`,
`snow_goose`,
`waxwing`,
`white_stork`,
`white_wagtail`,
`willow_grouse`

В качестве модели использовалась предобученная [EfficientNet](https://arxiv.org/pdf/1905.11946.pdf)

![img_classification](https://github.com/LadaChernenko/bird_species_guide/blob/main/img/classification_pred.png?raw=true)___
