import os
import torch
from torch import nn
import torchvision.transforms as T
import numpy as np
import PIL
from efficientnet_pytorch import EfficientNet
import random
from config import IMG_SIZE

labels = []
with open('labels.txt', 'r') as rf:
    for label in rf:
        labels.append(label[:-1])
       
label_dict = {i:labels[i] for i in range(0, len(labels))}

num_classes = len(label_dict)
model = EfficientNet.from_name('efficientnet-b0')
checkpoint = torch.load('./my_checkpoint2021-11-21.pth.tar', map_location=torch.device('cpu'))
in_features = model._fc.in_features
model._fc = nn.Linear(in_features, num_classes)
model.load_state_dict(checkpoint["state_dict"])
model.eval()



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