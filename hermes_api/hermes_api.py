import base.request
import base.output
import base.change_request
import requests
import utils
import tier
import region


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

    def change_servers(self, my_tier, my_region, num_servers):
        # handle strings
        if not hasattr(my_tier, 'name'):
            if my_tier == 'WEB':
                my_tier = tier.WEB
            elif my_tier == 'JAVA':
                my_tier = tier.JAVA
            elif my_tier == 'DB':
                my_tier = tier.DB

        if not hasattr(my_region, 'code'):
            if my_region == 'eu':
                my_region = region.EUROPE
            elif my_region == 'na':
                my_region = region.NORTHAMERICA
            elif my_region == 'ap':
                my_region = region.ASIAPACIFIC

        change = base.change_request.ChangeRequest()
        change.servers = {
            my_tier.name: {
                "ServerRegions": {
                    my_region.code: {
                        'NodeCount': num_servers
                    }
                }
            }
        }

        return self.chng(change)
