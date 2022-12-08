import numpy as np
import torch
from torch.utils.data import Dataset

class PIP_Dataset(Dataset):
    def __init__(self, pip: torch.Tensor, E: torch.Tensor):
        super(PIP_Dataset, self).__init__()
        self.pip = pip.float()
        self.E = E.float()
        
    def __getitem__(self, i):
        return self.pip[i], self.E[i]

    def __len__(self):
        return self.pip.shape[0]
