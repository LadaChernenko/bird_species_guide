import os
import torch
from torch import nn
import torchvision.transforms as T
import numpy as np
import PIL
from efficientnet_pytorch import EfficientNet
import random
from config import IMG_SIZE

num_classes = 20
model = EfficientNet.from_name('efficientnet-b0')
checkpoint = torch.load('./my_checkpoint2021-09-04.pth.tar', map_location=torch.device('cpu'))
in_features = model._fc.in_features
model._fc = nn.Linear(in_features, num_classes)
model.load_state_dict(checkpoint["state_dict"])
model.eval()

label_dict = {0: 'black_kite',
1: 'chaffinch',
2: 'common_magpie',
3: 'common_raven',
4: 'crested_tit',
5: 'eurasian_jay',
6: 'eurasian_pygmy-owl',
7: 'eurasian_tree_sparrow',
8: 'european_turtle-dove',
9: 'great_spotted_woodpecker',
10: 'hazel_grouse',
11: 'northern_harrier',
12: 'rock_pigeon',
13: 'ruddy_shelduck',
14: 'snow_goose',
15: 'snowy_owl',
16: 'waxwing',
17: 'white_stork',
18: 'white_wagtail',
19: 'willow_grouse'}

def transform(image, img_size, split):
    # different transformations for 'train' or 'test' splits
    assert split in {'TRAIN', 'TEST'}

    mean=[0.485, 0.456, 0.406]
    std=[0.229, 0.224, 0.225]
    new_image = image

    if split == 'TRAIN':
        img_blurrer = T.GaussianBlur(kernel_size=(5, 9), sigma=(0.1, 5))
        img_autocontrast = T.RandomAutocontrast(p=0.5)
        rotate = T.RandomRotation(degrees=(0, 90))
        sharpness_adjuster = T.RandomAdjustSharpness(sharpness_factor=2)
        hflip = T.RandomHorizontalFlip(p=0.5)

        new_image = hflip(new_image)

        if random.random() < 0.4:
            new_image = img_blurrer(new_image)
            new_image = img_autocontrast(new_image)
        if random.random() < 0.3:
            new_image = sharpness_adjuster(new_image)
            new_image = rotate(new_image)
            
    base_transform = T.Compose([T.ToTensor(), 
                                T.Resize(img_size), 
                                T.Normalize(mean=mean, std=std)])
    new_image = base_transform(new_image)  

    return new_image

def get_prediction(input_img_path):
    input_img = PIL.Image.open(input_img_path)
    tensor = transform(input_img, IMG_SIZE, 'TEST')
    outputs = model(torch.unsqueeze(tensor, dim=0))
    # predictions
    labels = []
    probs = []
    for idx in torch.topk(outputs, k=3).indices.squeeze(0).tolist():
        prob = torch.softmax(outputs, dim=1)[0, idx].item()
        labels.append(' '.join(label_dict[idx].split('_')))
        probs.append(prob)
        
    return labels, probs