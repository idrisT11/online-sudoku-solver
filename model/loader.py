import os
import cv2
import pandas as pd
import torch as tc

from torch.utils.data import Dataset



default_path = './data/printed_digits/assets/'

class PrintedDigitDataset(Dataset):
    def __init__(self, img_dir, transform=None, target_transform=None):
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

        self.image_tensor = tc.empty(1, 28, 28, dtype=tc.float)
        self.label_tensor = tc.empty(1, dtype=tc.long)

        self.load_data()



    def __len__(self):
        return self.label_tensor.shape[0]

    def __getitem__(self, idx):
        image = self.image_tensor[idx]
        label = self.label_tensor[idx]

        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)

        return image, label

    def load_data(self):
        print("Loading the dataSet")

        for i in range(9):
            digit = i + 1
            for file_name in os.listdir( self.img_dir + str(digit)):
                file_path = self.img_dir + str(digit) + '/' + file_name
                img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

                tensor_img = tc.tensor(img, dtype=tc.float).unsqueeze(dim=0)
                tensor_lbl = tc.tensor([digit], dtype=tc.long)

                self.image_tensor = tc.cat((self.image_tensor, tensor_img ))
                self.label_tensor = tc.cat((self.label_tensor, tensor_lbl))
        
        #Here we remove the first "empty tensor" added in __init__
        self.label_tensor = self.label_tensor[1:,]
        self.image_tensor = self.image_tensor[1:,]



