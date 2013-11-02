import json


class Output(object):
    request_status = ''
    error_message = None
    server_state = None

    def __init__(self, request_status='', error_message='', server_state=''):
        self.request_status = request_status
        self.error_message = error_message
        self.server_state = server_state

    def __repr__(self):
        return json.dumps(
            {
                'RequestStatus': self.request_status,
                'ErrorMessage': self.error_message,
                'ServerState': self.server_state
            }
        )
