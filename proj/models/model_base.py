import torch


class ModelBase:
    def __init__(self, device, **kwargs):
        self.model = None

        if device.lower() == 'gpu':
            avail = torch.cuda.is_available()
            if not avail:
                raise Exception('ERROR: unable to run model on GPU')
            device = torch.cuda.current_device()

        self.device = device

    def train(self):
        pass

    def predict(self, x):
        raise Exception('ERROR: predictions not implemented')
