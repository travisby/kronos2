import json


class Request(object):
    command = ''
    token = ''
    change_request = None

    def __init__(self, command='', token='', change_request=None):
        self.command = command
        self.token = token
        self.change_request = change_request

    def __repr__(self):
        return json.dumps(
            {
                'Command': self.command,
                'Token': self.token,
                'ChangeRequest': self.change_request
            }
        )
