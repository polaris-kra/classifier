from models.model_12G3c import Model12G3c


class ModelFactory:
    @staticmethod
    def load_model(config):
        common_cfg = config['common']
        if common_cfg is None:
            raise Exception('ERROR: no common section in config')

        model_name = common_cfg['model']
        if model_name is None:
            raise Exception('ERROR: no model_name entry in common config section')

        model_cfg = config['model_name']
        if model_cfg:
            raise Exception(f'ERROR: config section for model "{model_name}" not found')

        if model_name == 'model_12G3c':
            return Model12G3c(**model_cfg)

        raise Exception(f'ERROR: unknown model "{model_name}"')