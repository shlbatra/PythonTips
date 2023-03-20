import torch


#model to train 
class LinearNet(torch.nn.Module):
    def __init__(self):
        super(LinearNet, self).__init__()

        self.flatten = torch.nn.Flatten()
        self.linear1 = torch.nn.Linear(in_features=28 * 28, out_features=32)
        self.relu = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(in_features=32, out_features=10)
        self.softmax = torch.nn.Softmax(dim=1)
    #issue - same variable to store diff things
    #not use variables and store intermediate results in them 
    #for sequence use function composition - ex. Sequential in torch 
    def forward(self, x: torch.Tensor):
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        x = self.softmax(x)
        return x
