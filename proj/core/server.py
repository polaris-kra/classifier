from flask import Flask
from core.utils import read_config, load_model
from core.store import ImageStore


class ClassifierServer:
    def __init__(self, config_path="config.yml"):
        self.config = read_config(config_path)
        self.model = None
        self.image_store = None
        self.app = None

    def create(self):
        # create Flask app
        server_cfg = self.config["server"]
        name = server_cfg["name"]
        self.app = Flask(name)

        # create classification model
        model_name = server_cfg["model"]
        model_cfg = self.config["models"][model_name]
        self.model = load_model(model_name, model_cfg)

        # initialize image store
        self.image_store = ImageStore(self.config)

        return self.app

    def run(self):
        if self.app is None:
            raise Exception("ERROR: create server first")

        server_cfg = self.config["server"]
        host = server_cfg["host"]
        port = server_cfg["port"]
        debug = server_cfg["debug"]

        self.app.run(host=host, port=port, debug=debug)

    def classify(self, image):
        # put to store + log(ts, userid, image.size, project, uid, path)
        # classify + log(ts[=store.ts], project, uid, model_name, model_version, label)
        return self.model.predict(image)
