from flask import Flask
from utils import read_config, load_model
from classifier.store import ImageStore


class ClassifierServer:
    def __init__(self, config_path="../config.yml"):
        self.config = read_config(config_path)
        self.model = None
        self.image_store = None
        self.app = None

    def create(self):
        # create Flask app
        common_cfg = self.config["common"]
        name = common_cfg["name"]
        template_dir = common_cfg["template_dir"]
        app = Flask(name, template_folder=template_dir)
        self.app = app

        # create classification model
        model_name = common_cfg["model"]
        model_cfg = self.config["models"][model_name]
        # self.model = load_model(model_name, model_cfg)

        # initialize image store
        self.image_store = ImageStore(self.config)

        return self.app

    def run(self):
        if self.app is None:
            raise Exception("ERROR: create server first")

        common_cfg = self.config["common"]
        port = common_cfg["port"]
        is_debug = common_cfg["mode"] == "debug"

        self.app.run(port=port, debug=is_debug)

    def classify(self, image):
        # put to store + log(ts, userid, image.size, project, uid, path)
        # classify + log(ts[=store.ts], project, uid, model_name, model_version, label)
        return -1  # return label
