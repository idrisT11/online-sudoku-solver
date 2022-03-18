

import torch as tc
import torch.nn as nn
import torch.nn.functional as F

class NumberNetwork(nn.Module):

    def __init__(self):
        super(NumberNetwork, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=1, out_channels=20, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=20, out_channels=15, kernel_size=3)

        self.dense1 = nn.Linear(in_features=5*5*15, out_features=140)
        self.dense2 = nn.Linear(in_features=140, out_features=100)
        self.dense3 = nn.Linear(in_features=100, out_features=54)
        self.out = nn.Linear(in_features=54, out_features=9)

        """
        nn.init.xavier_uniform(self.dense1.weight)
        nn.init.xavier_uniform(self.dense2.weight)
        nn.init.xavier_uniform(self.dense3.weight)
        nn.init.xavier_uniform(self.out.weight)
        """

    def forward(self, t):
    
        
        #conv 1 
        t = self.conv1(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size= 2, stride = 2)

        t = F.dropout2d(t, p=0.2)

        #conv 2
        t = self.conv2(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size= 2, stride = 2)

        t = F.dropout2d(t, p=0.2)
        
        #fc 1
        t = t.reshape(-1, 5*5*15)

        t = self.dense1(t)
        t = F.relu(t)
        #t = F.dropout(t, p=0.3)


        #fc 2
        t = self.dense2(t)
        t = F.relu(t)  
        #t = F.dropout(t, p=0.2)

        #fc 3
        t = self.dense3(t)
        t = F.relu(t)  
        #t = F.dropout(t, p=0.2)

        #output
        t = self.out(t)
        t = F.softmax(t, dim=1)

        return t

        
