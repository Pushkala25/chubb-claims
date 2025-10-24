from PIL import Image
import imagehash

class FraudDetector:
    def __init__(self):
        self.hashes = set()

    def check_fraud(self, image_path):
        img = Image.open(image_path)
        h = str(imagehash.average_hash(img))
        if h in self.hashes:
            return True, "⚠️ Duplicate image detected"
        self.hashes.add(h)
        return False, "✅ No fraud detected"
