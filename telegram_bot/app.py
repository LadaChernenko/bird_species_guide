import torch
from torch import nn
import torchvision.transforms as T
import PIL
from efficientnet_pytorch import EfficientNet
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



def transform(image, img_size):

    mean=[0.485, 0.456, 0.406]
    std=[0.229, 0.224, 0.225]
    new_image = image
            
    base_transform = T.Compose([T.ToTensor(), 
                                T.Resize(img_size), 
                                T.Normalize(mean=mean, std=std)])
    new_image = base_transform(new_image)  

    return new_image

def get_prediction(input_img_path):
    input_img = PIL.Image.open(input_img_path)
    tensor = transform(input_img, IMG_SIZE)
    outputs = model(torch.unsqueeze(tensor, dim=0))
    # predictions
    labels = []
    probs = []
    for idx in torch.topk(outputs, k=3).indices.squeeze(0).tolist():
        prob = torch.softmax(outputs, dim=1)[0, idx].item()
        labels.append(' '.join(label_dict[idx].split('_')))
        probs.append(prob)
        
    return labels, probs