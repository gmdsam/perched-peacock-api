import json
import os
import re


def update_config_from_env_vars(config):
    for k, v in config.items():
        if isinstance(v, dict):
            update_config_from_env_vars(v)
        if isinstance(v, str):
            for match in re.findall('@([A-Za-z0-9_-]+)@', v):
                try:
                    v = v.replace('@{}@'.format(match), os.environ[match])
                except KeyError:
                    raise Exception('this env variable is not set yet: {}'.format(match))
            config[k] = v


def load_config_from_json(flask_app=None):
    env = os.envrion['PP_ENV'] if 'PP_ENV' in os.environ else 'DEV'
    here = os.path.abspath(os.path.dirname(__file__))
    json_config_file = os.path.join(here, '{}.json'.format(env))
    if os.path.exists(json_config_file):
        if flask_app is not None:
            flask_app.config.from_json(json_config_file)
            update_config_from_env_vars(flask_app.config)
            return flask_app
        else:
            with open(json_config_file, 'r') as fp:
                config = json.load(fp)
            update_config_from_env_vars(config)
            return config
    else:
        raise Exception('Invalid Perched Peacock configuration: {}'.format(env))
