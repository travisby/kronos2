import json


class ResearchUpgradeLevel(object):
    name = ''
    upgrade_cost = 0
    no_of_turns_required = 0
    cost_per_server_benefit = 0
    transaction_benefit = 0
    fail_over_benefit = 0
    db_replication_benefit = 0

    def __init__(
        self,
        name='',
        upgrade_cost=0,
        no_of_turns_required=0,
        cost_per_server_benefit=0,
        transaction_benefit=0,
        fail_over_benefit=0,
        db_replication_benefit=0
    ):
        self.name = name
        self.upgrade_cost = upgrade_cost
        self.no_of_turns_required = no_of_turns_required
        self.cost_per_server_benefit = cost_per_server_benefit
        self.transaction_benefit = transaction_benefit
        self.fail_over_benefit = fail_over_benefit
        self.db_replication_benefit = db_replication_benefit

    def __repr__(self):
        return json.dumps(
            {
                'Name': self.name,
                'UpgradeCost': self.upgrade_cost,
                'No.OfTurnsRequired': self.no_of_turns_required,
                'CostPerServerBenefit': self.cost_per_server_benefit,
                'TransactionBenefit': self.transaction_benefit,
                'FailOverBenefit': self.fail_over_benefit,
                'DBReplicationBenefit': self.db_replication_benefit
            }
        )
