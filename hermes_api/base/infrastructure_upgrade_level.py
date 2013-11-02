import json


class InfrastructureUpgradeLevel(object):
    name = ''
    upgrade_cost = 0
    no_of_turns_required = 0
    transaction_benefit = 0

    def __init__(
        self,
        name='',
        upgrade_cost=0,
        no_of_turns_required=0,
        transaction_benefit=0
    ):
        self.name = name
        self.upgrade_cost = upgrade_cost
        self.no_of_turns_required = no_of_turns_required
        self.transaction_benefit = transaction_benefit

    def __repr__(self):
        return json.dumps(
            {
                'Name': self.name,
                'UpgradeCost': self.upgrade_cost,
                'No.OfTurnsRequired': self.nu_of_turns_required,
                'TransactionBenefit': self.transaction_benefit
            }
        )

    def json_factory(input_json):
        result = InfrastructureUpgradeLevel()

        result.name = input_json['Name']
        result.upgrade_cost = input_json['UpgradeCost']
        result.no_of_turns_required = input_json['No.OfTurnsRequired']
        result.transaction_benefit = input_json['TransactionBenefit']

        return result
