from game_error import GameError
from game_server_farm_state import GameServerFarmState
import json


class Output(object):
    request_status = ''
    error = None
    server_state = None

    def __init__(self, request_status='', error='', server_state=''):
        self.request_status = request_status
        self.error = error
        self.server_state = server_state

    def __repr__(self):
        return json.dumps(
            {
                'RequestStatus': self.request_status,
                'Error': self.error,
                'ServerState': self.server_state
            }
        )

    @staticmethod
    def json_factory(input_json):
        result = Output()
        result.request_status = input_json['Status']
        result.error = GameError.json_factory(
            input_json['Error']
        )
        result.server_state = GameServerFarmState.json_factory(
            input_json['ServerState']
        )

        return result
