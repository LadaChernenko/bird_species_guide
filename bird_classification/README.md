# classification bird species

## Image classification


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

![object center prediction](https://github.com/LadaChernenko/bird_species_guide/blob/main/img/localisation_pred.png?raw=true)
___
