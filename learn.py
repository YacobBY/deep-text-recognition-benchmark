import torch
import torchvision


if torch.cuda.is_available():
    x = torch.tensor([5,5]).cuda()
    y = torch.ones_like(x)  # directly create a tensor on GP                       # or just use strings ``.to("cuda")``
    z = x * y * y
    print(z)
    print("aaa")
    print(z.to("cpu", torch.double))       # ``.to`` can also change dtype together!

