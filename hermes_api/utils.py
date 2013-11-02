import os


class APITokenDoesNotExist(KeyError):
    pass

try:
    API_TOKEN = os.environ['HERMES_API_TOKEN']
except KeyError:
    raise APITokenDoesNotExist()


HERMES_API_URL = 'hermes.wha.la/api/hermes'
