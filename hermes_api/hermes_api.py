import base.request
import base.output
import requests
import utils


class HermesApi(object):
    api_token = ''

    def __init__(self, api_token=utils.API_TOKEN):
        self.api_token = api_token

    def _makeRequest(self, command, change_request=None):
        request = base.request.Request()
        request.command = command
        request.change_request = change_request
        request.token = self.api_token

        result = requests.post(
            utils.HERMES_API_URL,
            data=repr(request),
            headers={'content-type': 'application/json'}
        ).json()

        if result['Error']:
            print '----------- What we sent! --------'
            print repr(request)
            print '----------- What we got! --------'
            print result
            raise Exception(result['Error']['ErrorMessage'])

        return base.output.Output.json_factory(result)

    def init(self):
        return self._makeRequest(utils.INIT)

    def play(self):
        return self._makeRequest(utils.PLAY)

    def chng(self, change_request):
        return self._makeRequest(utils.CHANGE, change_request)
