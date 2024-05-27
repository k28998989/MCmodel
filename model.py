import torch.nn as nn
import torch

import os
import torch.nn.functional as F
from collections import OrderedDict
from torchvision.models.swin_transformer import swin_b, Swin_B_Weights


model_urls = {
    'cnn': 'https://github.com/k28998989/MCmodel/releases/download/v1/dir_model.pt'
}
class CNN(nn.Module):
  def __init__(self, num_classes: int):
    super(CNN, self).__init__()
    self.num_classes = num_classes

    # in[N, 3, 32, 32] => out[N, 16, 16, 16]
    self.conv1 = nn.Sequential(
        nn.Conv2d(
            in_channels=3,
            out_channels=16,
            kernel_size=5,
            stride=1,
            padding=2
        ),
        nn.ReLU(True),
        nn.MaxPool2d(kernel_size=2)
    )
    # in[N, 16, 16, 16] => out[N, 32, 8, 8]
    self.conv2 = nn.Sequential(
        nn.Conv2d(16, 32, 5, 1, 2),
        nn.ReLU(True),
        nn.MaxPool2d(2)

    )
    # in[N, 32 * 8 * 8] => out[N, 128]
    self.fc1 = nn.Sequential(
        nn.Linear(32 * 8 * 8 * 4, 256),
        nn.ReLU(True)
    )
    # in[N, 128] => out[N, 64]
    self.fc2 = nn.Sequential(
        nn.Linear(256, 128),
        nn.ReLU(True)
    )
    self.fc3 = nn.Sequential(
        nn.Linear(128, 64),
        nn.ReLU(True)
    )
    # in[N, 64] => out[N, 10]
    self.out = nn.Linear(65, self.num_classes)

  def forward(self, x, w, h):
    x = self.conv1(x)
    x = self.conv2(x)
    x = x.view(x.size(0), -1) # [N, 32 * 8 * 8]
    x = self.fc1(x)
    x = self.fc2(x)
    x = self.fc3(x)
    handw = h/w
    #print(handw)
    handw = torch.unsqueeze(torch.tensor(handw),1)
    #print(x.shape, w.shape, h.shape)
    x = torch.cat((x,handw),dim=1)
    #print(x.shape)
    output = self.out(x)
    return output
 
def cnn():
    model = CNN(8)
    model.load_state_dict(torch.hub.load_state_dict_from_url(model_urls['cnn']))
    #model = torch.load("./models/cnn_model_93_1_65.pt")
    #torch.save(model.state_dict(), "./models/dir_model.pt")

    

    return model



