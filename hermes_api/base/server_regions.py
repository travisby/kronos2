import json


class ServerRegions(object):
    eu = None
    na = None
    ap = None

    def __init__(self, eu=None, na=None, ap=None):
        self.eu = eu
        self.na = na
        self.ap = ap

    def __repr__(self):
        return json.dumps(
            {
                'EU': self.eu,
                'NA': self.na,
                'AP': self.ap
            }
        )
