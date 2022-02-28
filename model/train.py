
import torch as tc
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision 
import torchvision.transforms as transforms

from model import *


def get_num_correct(pred, labels):
    return pred.argmax(dim=1).eq(labels).sum().item()

train_set = torchvision.datasets.MNIST(
    root='./data/MNIST',
    train=True,
    download=True,
    transform=transforms.Compose([
        transforms.ToTensor()
    ])
)

train_loader = tc.utils.data.DataLoader(
    train_set,
    batch_size=20
)


nt = NumberNetwork()
optimazer = optim.Adam(nt.parameters(), lr=0.001)

print("Der Anfang des Lernens, (Het Begin van het leren)")

for epoch in range(10):

    total_loss = 0
    total_correct = 0

    for batch in train_loader:

        images, labels = batch

        preds = nt(images)
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
