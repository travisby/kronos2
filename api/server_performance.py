import json


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
            {
                'CapacityLevels': self.capacity_levels,
                'FailOverLevels': self.fail_over_levels,
                'DBReplicationLevels': self.db_replication_levels
            }
        )
