import json


class FailOver(object):
    region_to = ''
    region_from = ''
    success_percentage = 0

    def __init__(self, region_to='', region_from='', success_percentage=''):
        self.region_to = region_to
        self.region_from = region_from
        self.success_percentage = success_percentage

    def __repr__(self):
        return json.dumps(
            {
                'RegionTo': self.region_to,
                'RegionFrom': self.region_from,
                'SuccessPercentage': self.success_percentage
            }
        )

    def json_factory(input_json):
        result = FailOver()

        result.region_to = input_json['RegionTo']
        result.region_from = input_json['RegionFrom']
        result.success_percentage = input_json['SuccessPercentage']

        return result
