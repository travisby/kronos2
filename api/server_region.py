import json


class ServerRegion(object):
    node_count = 0
    no_of_transactions_input = 0
    no_of_transactions_executed = 0
    no_of_transactions_succeeded = 0
    node_change_state = []

    def __init__(
        self,
        node_count=0,
        no_of_transactions_input=0,
        no_of_transactions_executed=0,
        no_of_transactions_succeeded=0,
        node_change_state=[]
    ):
        self.node_count = node_count,
        self.no_of_transactions_input = no_of_transactions_input
        self.no_of_transactions_executed = no_of_transactions_executed
        self.no_of_transactions_succeeded = no_of_transactions_succeeded
        self.node_change_state = node_change_state

    def __repr__(self):
        return json.dumps(
            {
                'NodeCount': self.node_count,
                'NoOfTransactionsInput': self.no_of_transactions_input,
                'NoOfTransactionsExecuted': self.no_of_transactions_executed,
                'NoOfTransactionsSucceeded': self.no_of_transactions_succeeded,
                'NodeChangeState': self.node_change_state
            }
        )
