import logging
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

    def __init__(self, engine):
        super(DynamoDBProvider, self).__init__(engine)
        self.logger = logging.getLogger()

    def command_dynamodb(self, command, **kwargs):
        method = command['method']
        if method in self.ALLOWED_METHODS:
            dynamodb = boto3.resource(
                'dynamodb',
                **command['connection'])
            method = getattr(dynamodb, method)
            results = method(**command['parameters'])
            try:
                self._make_variable(command, results=results)
                self._make_assertion(command, results=results)
            except Exception as e:
                self.logger.exception(
                    'Exception for command %r',
                    command,
                    e)
                raise e
        else:
            raise ValueError("method not allowed", method)

    def _make_assertion(self, command, **kwargs):
        """ Make an assertion based on python
            expression against kwargs
        """
        assertion = command.get('assertion', None)
        if assertion:
            self.engine.execute_command(
                {'provider': 'python',
                 'type': 'assert',
                 'expression': assertion
                 },
                **kwargs,
            )

    def _make_variable(self, command, **kwargs):
        """ Make a variable based on python
            expression against kwargs
        """
        expression = command.get('variable_expression', None)
        if expression:
            self.engine.execute_command(
                {'provider': 'python',
                 'type': 'store_variable',
                 'name': command['variable'],
                 'expression': expression
                 },
                **kwargs,
            )
