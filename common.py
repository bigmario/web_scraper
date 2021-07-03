import yaml

___config = None


def config():
    global ___config
    if not ___config:
        with open('./config.yaml', mode='r') as f:
            ___config = yaml.load(f, Loader=yaml.FullLoader)

    return ___config


