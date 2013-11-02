import json


class GameError(object):
    error_no = ''
    error_message = ''

    def __init__(self, error_no='', error_message=''):
        self.error_no = error_no
        self.error_message = error_message

    def __repr__(self):
        json.dumps(
            {
                'ErrorNo': self.error_no,
                'ErrorMessage': self.error_message
            }
        )
