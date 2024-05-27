import torch
from PIL import Image
from torchvision import transforms

net = torch.hub.load('b06b01073/veri776-pretrain', 'resnet101_ibn_a') 
# net = torch.hub.load('b06b01073/veri776-pretrain', 'resnext101_ibn_a') 
# net = torch.hub.load('b06b01073/veri776-pretrain', 'densenet169_ibn_a') 
# net = torch.hub.load('b06b01073/veri776-pretrain', 'se_resnet101_ibn_a') 

net = net.to('cpu')
net.eval()



# see Transform.py
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]
IMAGE_SIZE = 224
img = Image.open('demo.jpg')

img = transforms.Compose([
    transforms.ToTensor(),          
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE), antialias=True),  # Resize the image to IMAGE_SIZE*IMAGE_SIZE
    transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
])(img)


eu_feat, cos_feat, _ = net(img.unsqueeze(dim=0))


# some useful functions
# torch.cdist: calculate Euclidean distance between eu_feat embeddings
# pairwise_cosine_similarity (from torchmetrics package): calculate cosine distance between cos_feat embeddings


