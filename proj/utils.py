import os
import yaml
from models.model_12G3c import Model12G3c


def read_config(config_path="../config.yml"):
    if not os.path.exists(config_path):
        raise Exception(f"ERROR: config file {config_path} not found")

    with open(config_path, "r") as file:
        return yaml.load(file, yaml.FullLoader)


def load_model(config):
    common_cfg = config["common"]
    if common_cfg is None:
        raise Exception("ERROR: no common section in config")

    model_name = config["model"]
    if model_name is None:
        raise Exception('ERROR: no model_name entry in common config section')

    models_cfg = config["models"]
    if models_cfg is None:
        raise Exception("ERROR: no models section in config")

    model_cfg = models_cfg["model_name"]
    if model_cfg:
        raise Exception(f"ERROR: config section for model '{model_name}' not found")

    device = model_cfg["device"]
    file_path = model_cfg["file_path"]

    if model_name == "model_12G3c":
        model = Model12G3c(device=device)
        model.load(file_path)
        return model

    raise Exception(f"ERROR: unknown model '{model_name}'")
