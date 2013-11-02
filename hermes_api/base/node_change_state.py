import json


class NodeChangeState(object):
    node_count = 0
    effective_after_turns = 0

    def __init__(self, node_count=0, effective_after_turns=0):
        self.node_count = node_count
        self.effective_after_turns = effective_after_turns

    def __repr__(self):
        return json.dumps(
            {
                'NodeCount': self.node_count,
                'EffectiveAfterTurns': self.effective_after_turns
            }
        )

    def json_factory(input_json):
        result = NodeChangeState()

        result.node_count = input_json['NodeCount']
        result.effective_after_turns = input_json['EffectiveAfterTurns']

        return result
