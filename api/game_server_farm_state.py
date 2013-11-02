import json


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
