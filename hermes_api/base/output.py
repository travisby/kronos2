from game_error import GameError
from game_server_farm_state import GameServerFarmState
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

    def json_factory(input_json):
        result = Output()
        result.request_status = input_json['RequestStatus']
        result.error_message = GameError.json_factory(
            input_json['ErrorMessage']
        )
        result.server_state = GameServerFarmState.json_factory(
            input_json['ServerState']
        )

        return result
