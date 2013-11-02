import json


class Capacity(object):
    upper_limit = 0
    lower_limit = 0
    success_percentage = 0
    is_at_overload = False

    def __init__(
        self,
        upper_limit=0,
        lower_limit=0,
        success_percentage=0,
        is_at_overload=0
    ):
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.success_percentage = success_percentage
        self.is_at_overload = is_at_overload

    def __repr__(self):
        return json.dumps(
            {
                'UpperLimit': self.upper_limit,
                'LowerLimit': self.lower_limit,
                'SuccessPercentage': self.success_percentage,
                'IsAtOverLoad': self.is_at_overload
            }
        )

    def json_factory(input_json):
        result = Capacity()
        result.upper_limit = input_json['UpperLimit']
        result.lower_limit = input_json['LowerLimit']
        result.success_percentage = input_json['SuccessPercentage']
        result.is_at_overload = input_json['IsAtOverLoad']

        return result
