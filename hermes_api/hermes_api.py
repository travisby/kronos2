import base.request
import requests
import utils


class HermesApi(object):

    def __init__(self, api_token=utils.API_TOKEN):
        pass

    def _makeRequest(self, command, change_request=None):
        request = base.request.Request
        request.command = command
        request.change_request = change_request

        result = requests.post(utils.HERMES_API_URL, data=repr(request))

        if 'ErrorMessage' in result.json():
            raise Exception(result.json()['ErrorMessage'])

        return result

    def init(self):
        self._makeRequest(utils.INIT)

    def play(self):
        self._makeRequest(utils.PLAY)

    def chng(self, change_request):
        self._makeRequest(utils.CHANGE, change_request)
