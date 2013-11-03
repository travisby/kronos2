from game_error import GameError
from game_server_farm_state import GameServerFarmState
import region
import tier
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
        return json.dumps(self.to_dict())

    def to_dict(self):
        result = {}
        result['RequestStatus'] = self.request_status
        result['Error'] = self.error
        result['ServerState'] = None

        if self.server_state:
            result['ServerState'] = self.server_state.to_dict()

        return result

    def get_date(self):
        return self.server_state.transaction_time

    def get_servers_for_load(self, load):
        # prevent / 0
        if load == 0:
            load = 1

        loads = {}
        loads['WEB'] = load / min([x.upper_limit for x in self.server_state.server_tiers.web.server_performance.capacity_levels])
        loads['JAVA'] = load / min([x.upper_limit for x in self.server_state.server_tiers.java.server_performance.capacity_levels])
        loads['DB'] = load / min([x.upper_limit for x in self.server_state.server_tiers.db.server_performance.capacity_levels])

        return loads

    def get_max_startup_time(self):
        return max(
            [
                self.server_state.server_tiers.web.start_turn_time,
                self.server_state.server_tiers.java.start_turn_time,
                self.server_state.server_tiers.db.server_start_turn_time
            ]
        )

    def get_attempted_transactions(self):
        return {
            'na': max(
                [
                    self.server_state.server_tiers.web.server_regions.na['NoOfTransactionsInput'],
                    self.server_state.server_tiers.java.server_regions.na['NoOfTransactionsInput'],
                    self.server_state.server_tiers.db.server_regions.na['NoOfTransactionsInput'],
                ]
            ),
            'eu': max(
                [
                    self.server_state.server_tiers.web.server_regions.eu['NoOfTransactionsInput'],
                    self.server_state.server_tiers.java.server_regions.eu['NoOfTransactionsInput'],
                    self.server_state.server_tiers.db.server_regions.eu['NoOfTransactionsInput'],
                ]
            ),
            'ap': max(
                [
                    self.server_state.server_tiers.web.server_regions.ap['NoOfTransactionsInput'],
                    self.server_state.server_tiers.java.server_regions.ap['NoOfTransactionsInput'],
                    self.server_state.server_tiers.db.server_regions.ap['NoOfTransactionsInput'],
                ]
            )
        }

    def get_executed_transactions(self):
        #  f.server_state.server_tiers.web.server_regions.ap['NoOfTransactionsExecuted']
        return {
            'na': max(
                [
                    self.server_state.server_tiers.web.server_regions.na['NoOfTransactionsExecuted'],
                    self.server_state.server_tiers.java.server_regions.na['NoOfTransactionsExecuted'],
                    self.server_state.server_tiers.db.server_regions.na['NoOfTransactionsExecuted'],
                ]
            ),
            'eu': max(
                [
                    self.server_state.server_tiers.web.server_regions.eu['NoOfTransactionsExecuted'],
                    self.server_state.server_tiers.java.server_regions.eu['NoOfTransactionsExecuted'],
                    self.server_state.server_tiers.db.server_regions.eu['NoOfTransactionsExecuted'],
                ]
            ),
            'ap': max(
                [
                    self.server_state.server_tiers.web.server_regions.ap['NoOfTransactionsExecuted'],
                    self.server_state.server_tiers.java.server_regions.ap['NoOfTransactionsExecuted'],
                    self.server_state.server_tiers.db.server_regions.ap['NoOfTransactionsExecuted'],
                ]
            )
        }

    @staticmethod
    def json_factory(input_json):
        result = Output()
        result.request_status = input_json['Status']
        result.error = GameError.json_factory(
            input_json['Error']
        )

        # this is blank on change
        if input_json['ServerState']:
            result.server_state = GameServerFarmState.json_factory(
                input_json['ServerState']
            )
        else:
            result.server_state = None

        return result
