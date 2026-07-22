from configparser import ConfigParser
import os

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Configuration", "config.ini")

config = ConfigParser()
config.read(config_path)

class ReadConfig:

    @staticmethod
    def get_baseurl():
        return config.get('login details', 'baseurl')

    @staticmethod
    def get_browser():
        return config.get('login details', 'browser') 
