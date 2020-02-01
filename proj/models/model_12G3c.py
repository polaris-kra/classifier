import os
import torch
from torchvision.models import GoogLeNet

from models.model_base import ModelBase

VERSION = '0.1'


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

    def load(self, file_path):
        if not os.path.exists(file_path):
            raise Exception(f'ERROR: File "{file_path}" not exists')

        state = torch.load(file_path)
        version = state['version']

        if version != VERSION:
            raise Exception(f'ERROR: Current version is {VERSION} but loaded is {version}')

        model_state = state['model_state']
        model = GoogLeNet()
        model.load_state_dict(model_state)

        self.model = model

    def predict(self, x):
        self.model.eval()

        with torch.no_grad():
            prediction = self.model(x.to(self.device)).detach().cpu()
            prediction = list(torch.argmax(prediction, dim=1).numpy())

            return prediction
