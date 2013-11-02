import os


class APITokenDoesNotExist(KeyError):
    pass

try:
    API_TOKEN = os.environ['HERMES_API_TOKEN']
except KeyError:
    raise APITokenDoesNotExist()


HERMES_API_URL = 'http://hermes.wha.la/api/hermes'

INIT = 'INIT'
PLAY = 'PLAY'
CHANGE = 'CHNG'
