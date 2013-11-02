import json


class ChangeRequest(object):
    servers = {}
    upgrade_infastructure = False
    upgrade_to_research = ''

    def __init__(
        self,
        servers={},
        upgrade_infastructure=False,
        upgrade_to_research=''
    ):
        self.servers = servers
        self.upgrade_infastructure = upgrade_infastructure
        self.upgrade_to_research = upgrade_to_research

    def __repr__(self):
        return json.dumps(
            {
                'Servers': self.servers,
                'UpgradeInfraStructure': self.upgrade_infrastructure,
                'UpgradeToResearch': self.upgrade_to_research
            }
        )
