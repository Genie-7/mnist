import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)
print("cuDNN version:", torch.backends.cudnn.version())

# Test CUDA functionality
if torch.cuda.is_available():
    x = torch.rand(5, 3).cuda()
    y = torch.rand(5, 3).cuda()
    print("CUDA is working! Here is a random tensor addition result:")
    print(x + y)
else:
    print("CUDA is not available. Please check your installation.")