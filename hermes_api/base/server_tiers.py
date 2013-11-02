import json
from server_tier import ServerTier


class ServerTiers(object):
    web = ServerTier()
    java = ServerTier()
    db = ServerTier()

    def __repr__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            'WEB': self.web.to_dict(),
            'JAVA': self.java.to_dict(),
            'DB': self.db.to_dict()
        }

    @staticmethod
    def json_factory(input_json):
        result = ServerTiers()

        result.web = ServerTier.json_factory(input_json['WEB'])
        result.java = ServerTier.json_factory(input_json['JAVA'])
        result.db = ServerTier.json_factory(input_json['DB'])

        return result
