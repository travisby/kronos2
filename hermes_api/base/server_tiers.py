import json
from server_tier import ServerTier


class ServerTiers(object):
    web = ServerTier()
    java = ServerTier()
    db = ServerTier()

    def __repr__(self):
        return json.dumps(
            {
                'WEB': self.web,
                'JAVA': self.java,
                'DB': self.db
            }
        )
