import torch
from torchvision.models import GoogLeNet

from models.model_base import ModelBase


class Model12G3c(ModelBase):
    """
    Model trained on 12G Kaggle dataset:
    https://www.kaggle.com/minhhuy2810/rice-diseases-image-dataset
    3 classes taken (no Hispa).

    """
    def __init__(self, device, **kwargs):
        super().__init__(device, **kwargs)

        self.classes = {
            0: 'brown_spot',
            1: 'healthy',
            2: 'leaf_blast'
        }

    @staticmethod
    def version():
        return '0.1'

    def init(self, model_state):
        model = GoogLeNet()
        model.load_state_dict(model_state)

        self.model = model

    def predict(self, x):
        self.model.eval()

        with torch.no_grad():
            prediction = self.model(x.to(self.device)).detach().cpu()
            prediction = list(torch.argmax(prediction, dim=1).numpy())

            return prediction
