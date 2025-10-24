from torchvision import models, transforms
from PIL import Image
import torch

class DamageClassifier:
    def __init__(self):
        self.model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])
        self.classes = ["Minor Scratch", "Major Dent", "Total Loss"]

    def predict_damage(self, image_path):
        img = Image.open(image_path).convert("RGB")
        input_tensor = self.transform(img).unsqueeze(0)
        with torch.no_grad():
            _ = self.model(input_tensor)  # placeholder inference
        # mock prediction
        damage_type = self.classes[torch.randint(0, 3, (1,)).item()]
        severity = ["Low", "Medium", "High"][torch.randint(0, 3, (1,)).item()]
        return damage_type, severity
