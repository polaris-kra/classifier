from flask import Flask
from utils import read_config, load_model
from classifier.store import ImageStore


class ClassifierServer:
    def __init__(self, config_path="../config.yml"):
        self.config = read_config(config_path)["common"]
        self.model = None
        self.image_store = None
        self.app = None

    def create(self):
        # create Flask app
        name = self.config["name"]
        template_dir = self.config["template_dir"]
        app = Flask(name, template_folder=template_dir)
        self.app = app

        # create classification model
        self.model = load_model(self.config)

        # initialize image store
        self.image_store = ImageStore(self.config)

        return self.app

    def run(self):
        if self.app is None:
            raise Exception("ERROR: create server first")

        is_debug = self.config["mode"] == "debug"

        self.app.run(debug=is_debug)

    def process(self, image, project, uid):
        # put to store + log(ts, image.size, project, uid, path)
        # classify + log(ts[=store.ts], project, uid, model_name, model_version, label)
        return -1  # return label
