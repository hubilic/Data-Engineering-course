import json

class ConfigError(Exception):
    pass

def parse_config(path):
    try:
        with open(path) as file:
            data = file.read()
            return json.loads(data)
    except FileNotFoundError as e:
        raise ConfigError("could not load config file") from e
    except json.JSONDecodeError as e:
        raise ConfigError("could not load config file") from e