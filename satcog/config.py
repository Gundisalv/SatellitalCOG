from configparser import ConfigParser

def load_config():
    Config = ConfigParser()
    try:
        Config.read('conf/config.cfg')
    except:
        raise
    return Config

Config = load_config()
