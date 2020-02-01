from flask import Flask
from classifier.utils import read_config


class ClassifierServer:
    def __init__(self, config_path="../config.yml"):
        self.config = read_config(config_path)["common"]
        self.app = None

    def create(self):
        name = self.config["name"]
        template_dir = self.config["template_dir"]

        app = Flask(name, template_folder=template_dir)
        self.app = app

        return self.app

    def run(self):
        if self.app is None:
            raise Exception("ERROR: create server first")

        is_debug = self.config["mode"] == "debug"

        self.app.run(debug=is_debug)
