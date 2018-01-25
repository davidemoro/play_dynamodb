import boto3
from pytest_play.providers import BaseProvider


class DynamoDBProvider(BaseProvider):
    """ DynamoDB provider """

    ALLOWED_METHODS = [
        'get_item',
        'batch_get_item',
        'batch_write_item',
        'delete_item',
        'describe_limits',
        'describe_table',
        'list_tables',
        'put_item',
        'query',
        'scan',
        'update_item',
    ]

    def command_dynamodb(self, command, **kwargs):
        method = command['method']
        if method in self.ALLOWED_METHODS:
            dynamodb = boto3.resource(
                'dynamodb',
                **command['connection'])
            method = getattr(dynamodb, method)
            method(**command['parameters'])
        else:
            raise ValueError("method not allowed", method)
