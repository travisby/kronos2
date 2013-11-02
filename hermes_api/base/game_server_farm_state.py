import json
import datetime
from infrastructure_upgrade_level import InfrastructureUpgradeLevel
from research_upgrade_level import ResearchUpgradeLevel


class GameServerFarmState(object):
    transaction_time = None
    turn_no = 0
    cost_per_server = 0
    profit_constant = 0
    profit_accumulated = 0
    profit_earned = 0
    server_tiers = []
    infrastructure_upgrade_levels = []
    research_upgrade_levels = []
    infrastructure_upgrade_state = []
    research_upgrade_state = []

    def __init__(
        self,
        transaction_time=None,
        turn_no=0,
        cost_per_server=0,
        profit_constant=0,
        profit_accumulated=0,
        profit_earned=0,
        server_tiers=[],
        infrastructure_upgrade_levels=[],
        research_upgrade_levels=[],
        infrastructure_upgrade_state=[],
        research_upgrade_state=[]
    ):
        self.transaction_time = transaction_time
        self.turn_no = turn_no
        self.cost_per_server = cost_per_server
        self.profit_constant = profit_constant
        self.profit_accumulated = profit_accumulated
        self.profit_earned = profit_earned
        self.server_tiers = server_tiers
        self.infrastructure_upgrade_levels = infrastructure_upgrade_levels
        self.research_upgrade_levels = research_upgrade_levels
        self.infrastructure_upgrade_state = infrastructure_upgrade_state
        self.research_upgrade_state = research_upgrade_state

    def __repr__(self):
        return json.dumps(
            {
                'TransactionTime': self.transaction_time,
                'TurnNo': self.turn_no,
                'CostPerServer': self.cost_per_server,
                'ProfitConstant': self.profit_constant,
                'ProfitAccumulated': self.profit_accumulated,
                'ProfitEarned': self.profit_earned,
                'ServerTiers': self.server_tiers,
                'InfraStructureUpgradeLevels': (
                    self.infrastructure_upgrade_levels
                ),
                'ResearchUpgradeLevels': self.research_upgrade_levels,
                'InfraStructureUpgradeState': (
                    self.infrastructure_upgrade_state
                ),
                'ResearchUpgradeState': self.research_upgrade_state,
            }
        )

    def json_factory(input_json):
        result = GameServerFarmState()

        result.transaction_time = datetime.strptime(
            input_json['TransactionTime']
        )
        result.turn_no = input_json['TurnNo']
        result.cost_per_server = input_json['CostPerServer']
        result.profit_constant = input_json['ProfitConstant']
        result.profit_accumulated = input_json['ProfitAccumulated']
        result.profit_earned = input_json['ProfitEarned']

        # TODO figure out what this translates to
        result.server_tiers = input_json['ServerTiers']
        result.infrastructure_upgrade_levels = (
            InfrastructureUpgradeLevel.json_factory(
                input_json['InfraStructureUpgradeLevels']
            )
        )
        result.research_upgrade_levels = ResearchUpgradeLevel.json_factory(
            input_json['ResearchUpgradeLevel']
        )

        # TODO figure out what this translates to
        result.infrastructure_upgrade_state = (
            input_json['InfraStructureUpgradeState'])

        # TODO figure out what this translates to
        result.research_upgrade_state = input_json['ResearchUpgradeState']

        return result
