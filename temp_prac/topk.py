import torch
### but why topk return 2 tensors?
x = torch.arange(1.,6)
print(x)
print(torch.topk(x,1))
print(torch.topk(x,2))
print(torch.topk(x,3))
print(torch.topk(x,4))
## dim option
print(x.topk(1,dim=1))

