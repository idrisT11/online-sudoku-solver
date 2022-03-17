from matplotlib import pyplot as plt
import numpy as np
from sklearn.utils import shuffle
from sympy import true
import torch as tc
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision 
import torchvision.transforms as transforms

from model import *
from loader import PrintedDigitDataset 


def get_num_correct(pred, labels):
    return pred.argmax(dim=1).eq(labels).sum().item()

train_set_mnist = torchvision.datasets.MNIST(
    root='./data/MNIST',
    train=True,
    download=True,
    transform=transforms.Compose([
        transforms.ToTensor()
    ])
)


train_set = PrintedDigitDataset('./data/printed_digits/assets/')

train_loader = tc.utils.data.DataLoader(
    train_set,
    shuffle=True,
    batch_size=5
)


nt = NumberNetwork()
optimazer = optim.Adam(nt.parameters(), lr=0.00005)

print("Der Anfang des Lernens, (Het Begin van het leren)")

for epoch in range(80):

    total_loss = 0
    total_correct = 0

    for batch in train_loader:
        images, labels = batch

        train_filter = np.where(labels != 0)
        images = images[train_filter]
        labels = labels[train_filter]
        labels = labels - 1

        preds = nt(images.reshape(-1, 1, 28, 28))
        loss = F.cross_entropy(preds, labels)

        optimazer.zero_grad()
        loss.backward()
        optimazer.step()

        total_loss += loss.item()
        total_correct += get_num_correct(preds, labels)

    print("Epoch : ", epoch,", total_correct : ",total_correct,", loss: ", total_loss)
    print("Ratio : ", total_correct/len(train_set)*100, "%")


print("Das Ende des Lernens, (Het einde van het leren)")

tc.save(nt.state_dict(), './model.nt')
