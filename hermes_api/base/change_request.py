import json


class ChangeRequest(object):
    """
    servers = {
        'WEB': {
            'ServerRegions': {
                'EU': {
                    'NodeCount': 0
                },
                'NA': {
                    'NodeCount': 0
                },
                'AP': {
                    'NodeCount': 0
                }
            }
        },
        'JAVA': {
            'ServerRegions': {
                'EU': {
                    'NodeCount': 0
                },
                'NA': {
                    'NodeCount': 0
                },
                'AP': {
                    'NodeCount': 0
                }
            }
        },
        'DB': {
            'ServerRegions': {
                'EU': {
                    'NodeCount': 0
                },
                'NA': {
                    'NodeCount': 0
                },
                'AP': {
                    'NodeCount': 0
                }
            }
        }
    }
    """
    servers = {}
    upgrade_infrastructure = False
    upgrade_to_research = ''

    def __init__(
        self,
        servers={},
        upgrade_infrastructure=False,
        upgrade_to_research=''
    ):
        self.servers = servers
        self.upgrade_infrastructure = upgrade_infrastructure
        self.upgrade_to_research = upgrade_to_research

    def __repr__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        representation = {
            'Servers': self.servers,
            'UpgradeInfraStructure': self.upgrade_infrastructure,
        }
        if self.upgrade_to_research:
            representation['UpgradeToResearch'] = self.upgrade_to_research

        return representation



    # This is made client side, so no need for json_factory
