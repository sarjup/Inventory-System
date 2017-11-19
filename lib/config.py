from ConfigParser import ConfigParser
from os import path

config = ConfigParser()
config.read(path.abspath('configuration/config.conf'))

postgres = 'postgresql://{}:{}@{}:{}/{}'.format(
    config.get('postgres','user'),
    config.get('postgres','pw'),
    config.get('postgres','host'), 
    config.get('postgres','port'),
    config.get('postgres','db'))




