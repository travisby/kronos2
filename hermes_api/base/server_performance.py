import json
from capacity_level import CapacityLevel
from fail_over_level import FailOverLevel


class ServerPerformance(object):
    capacity_levels = []
    fail_over_levels = []
    db_replication_levels = []

    def __init__(
        self,
        capacity_levels=[],
        fail_over_levels=[],
        db_replication_levels=[]
    ):
        self.capacity_levels = capacity_levels
        self.fail_over_levels = fail_over_levels
        self.db_replication_levels = db_replication_levels

    def __repr__(self):
        return json.dumps(
            self.to_dict()
        )

    def to_dict(self):
        return {
            'CapacityLevels': [x.to_dict() for x in self.capacity_levels],
            'FailOverLevels': [x.to_dict() for x in self.fail_over_levels],
            'DBReplicationLevels': [
                x.to_dict()
                for x in
                self.db_replication_levels
            ]
        }

    @staticmethod
    def json_factory(input_json):
        result = ServerPerformance()

        result.capacity_levels = (
            [
                CapacityLevel.json_factory(x)
                for x in
                # spelling mistake is for realz
                input_json['CapactityLevels']
            ]
        )

        result.fail_over_levels = (
            [
                FailOverLevel.json_factory(x)
                for x in
                input_json['FailOverLevels']
            ]
        )

        if input_json['DBReplicationLevels']:
            result.db_replication_levels = (
                [
                    FailOverLevel.json_factory(x)
                    for x in
                    input_json['DBReplicationLevels']
                ]
            )
        else:
            result.db_replication_levels = []

        return result
