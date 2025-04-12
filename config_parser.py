import configparser

def read_config(filename="config.ini"):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

if __name__ == "__main__":
    config = read_config()
    print(dict(config["DEFAULT"]))
