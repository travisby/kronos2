# TODO get rid of this class.
# Who's to say it will look like this at other levels?

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
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            'EU': self.eu,
            'NA': self.na,
            'AP': self.ap
        }

    @staticmethod
    def json_factory(input_json):
        result = ServerRegions()

        result.eu = input_json['EU']
        result.na = input_json['NA']
        result.ap = input_json['AP']

        return result
