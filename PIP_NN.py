from torch import nn

class PIP_NN(nn.Module):
    def __init__(self, m):
        super(PIP_NN, self).__init__()
        self.layer_stack = nn.Sequential(
            nn.Linear(m, 10),
            nn.Tanh(),
            nn.Linear(10, 50),
            nn.Tanh(),
            nn.Linear(50, 1)
        )

    def forward(self, pip):
        E = self.layer_stack(pip)
        return E
        