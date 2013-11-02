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

    def get_attempted_transactions(self):
        return {
            tier.WEB.name: {
                region.NORTHAMERICA.code: self.server_state.server_tiers.web.server_regions.na['NoOfTransactionsInput'],
                region.EUROPE.code: self.server_state.server_tiers.web.server_regions.eu['NoOfTransactionsInput'],
                region.ASIAPACIFIC.code: self.server_state.server_tiers.web.server_regions.ap['NoOfTransactionsInput'],
            },
            tier.JAVA.name: {
                region.NORTHAMERICA.code: self.server_state.server_tiers.java.server_regions.na['NoOfTransactionsInput'],
                region.EUROPE.code: self.server_state.server_tiers.java.server_regions.eu['NoOfTransactionsInput'],
                region.ASIAPACIFIC.code: self.server_state.server_tiers.java.server_regions.ap['NoOfTransactionsInput'],
            },
            tierDB.name: {
                region.NORTHAMERICA.code: self.server_state.server_tiers.db.server_regions.na['NoOfTransactionsInput'],
                region.EUROPE.code: self.server_state.server_tiers.db.server_regions.eu['NoOfTransactionsInput'],
                region.ASIAPACIFIC.code: self.server_state.server_tiers.db.server_regions.ap['NoOfTransactionsInput'],
            }
        }

    def get_executed_transactions(self):
        #  f.server_state.server_tiers.web.server_regions.ap['NoOfTransactionsExecuted']
        return {
            tier.WEB.name: {
                region.NORTHAMERICA.code: self.server_state.server_tiers.web.server_regions.na['NoOfTransactionsExecuted'],
                region.EUROPE.code: self.server_state.server_tiers.web.server_regions.eu['NoOfTransactionsExecuted'],
                region.ASIAPACIFIC.code: self.server_state.server_tiers.web.server_regions.ap['NoOfTransactionsExecuted'],
            },
            tier.JAVA.name: {
                region.NORTHAMERICA.code: self.server_state.server_tiers.java.server_regions.na['NoOfTransactionsExecuted'],
                region.EUROPE.code: self.server_state.server_tiers.java.server_regions.eu['NoOfTransactionsExecuted'],
                region.ASIAPACIFIC.code: self.server_state.server_tiers.java.server_regions.ap['NoOfTransactionsExecuted'],
            },
            tier.DB.name: {
                region.NORTHAMERICA.code: self.server_state.server_tiers.db.server_regions.na['NoOfTransactionsExecuted'],
                region.EUROPE.code: self.server_state.server_tiers.db.server_regions.eu['NoOfTransactionsExecuted'],
                region.ASIAPACIFIC.code: self.server_state.server_tiers.db.server_regions.ap['NoOfTransactionsExecuted'],
            }
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
