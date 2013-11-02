import json
from server_performance import ServerPerformance
from server_regions import ServerRegions


class ServerTier(object):
    server_shutdown_turn_time = 0
    server_performance = None
    server_regions = []
    server_start_turn_time = 0

    def __init__(
        self,
        server_shutdown_turn_time=0,
        server_performance=None,
        server_regions=[],
        server_start_turn_time=0
    ):

        self.server_shutdown_turn_time = server_shutdown_turn_time
        self.server_performance = server_performance
        self.server_regions = server_regions
        self.server_start_turn_time = server_start_turn_time

    def __repr__(self):
        return json.dumps(
            {
                'ServerShutdownTurnTime': self.server_shutdown_turn_time,
                'ServerPerformance': self.server_performance,
                'ServerRegions': self.server_regions,
                'ServerStartTurnTime': self.server_start_turn_time
            }
        )

    @staticmethod
    def json_factory(input_json):
        result = ServerTier()

        result.server_shutdown_turn_time = input_json['ServerShutdownTurnTime']
        result.server_performance = ServerPerformance.json_factory(
            input_json['ServerPerformance']
        )
        result.server_regions = ServerRegions.json_factory(
            input_json['ServerRegions']
        )
        result.start_turn_time = input_json['ServerStartTurnTime']

        return result
