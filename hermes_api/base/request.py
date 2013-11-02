import simplejson as json


class Request(object):
    command = ''
    token = ''
    change_request = None

    def __init__(self, command='', token='', change_request=None):
        self.command = command
        self.token = token
        self.change_request = change_request

    def __repr__(self):
        representation = {
            'Command': self.command,
            'Token': self.token,
        }
        if self.change_request:
            representation['ChangeRequest'] = self.change_request.to_dict()

        return json.dumps(representation)
