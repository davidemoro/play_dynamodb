#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_dynamodb` package."""

import pytest


@pytest.fixture(scope='session')
def variables():
    return {'skins': {'skin1': {'base_url': 'http://', 'credentials': {}}}}


@pytest.mark.parametrize(
    'command',
    [
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'get_item',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'TableName': 'Music',
      'parameters': {
          'Key': {
              'Artist': {
                  'S': 'Acme Band',
                  },
              'SongTitle': {
                  'S': 'Happy Day',
                  },
              },
          }
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'delete_item',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'TableName': 'Music',
      'parameters': {
          'Key': {
              'Artist': {
                  'S': 'No One You Know',
                  },
              'SongTitle': {
                  'S': 'Scared of My Shadow',
                  },
              },
          },
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'put_item',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'TableName': 'Music',
      'parameters': {
          'Item': {
              'AlbumTitle': {
                  'S': 'Somewhat Famous',
              },
              'Artist': {
                  'S': 'No One You Know',
              },
              'SongTitle': {
                  'S': 'Call Me Today',
              },
          },
          'ReturnConsumedCapacity': 'TOTAL',
          },
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'query',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'TableName': 'Music',
      'parameters': {
          'ExpressionAttributeValues': {
              ':v1': {
                  'S': 'No One You Know',
              },
          },
          'KeyConditionExpression': 'Artist = :v1',
          'ProjectionExpression': 'SongTitle',
          }
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'scan',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'TableName': 'Music',
      'parameters': {
          'ExpressionAttributeNames': {
              'AT': 'AlbumTitle',
              'ST': 'SongTitle',
          },
          'ExpressionAttributeValues': {
              ':a': {
                  'S': 'No One You Know',
              },
          },
          'FilterExpression': 'Artist = :a',
          'ProjectionExpression': '#ST, #AT',
          }
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'update_item',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'TableName': 'Music',
      'parameters': {
          'ExpressionAttributeNames': {
              '#AT': 'AlbumTitle',
              '#Y': 'Year',
          },
          'ExpressionAttributeValues': {
              ':t': {
                  'S': 'Louder Than Ever',
              },
              ':y': {
                  'N': '2015',
              },
          },
          'Key': {
              'Artist': {
                  'S': 'Acme Band',
              },
              'SongTitle': {
                  'S': 'Happy Day',
              },
          },
          'ReturnValues': 'ALL_NEW',
          'UpdateExpression': 'SET #Y = :y, #AT = :t',
          }
      },
    ])
def test_provider(play, command):
    import mock
    from play_dynamodb import providers
    provider = providers.DynamoDBProvider(play)
    assert provider.engine is play

    with mock.patch('play_dynamodb.providers.boto3') as boto3:
        provider.command_dynamodb(command)
        assert boto3 \
            .resource \
            .assert_called_with(
                'dynamodb',
                **command['connection']) is None
        assert boto3 \
            .resource \
            .return_value \
            .Table \
            .assert_called_once_with(command['TableName']) is None
        assert getattr(
                boto3.resource.return_value.Table.return_value,
                command['method']) \
            .assert_called_with(
                **command['parameters']) is None


@pytest.mark.parametrize(
    'command',
    [
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'delete_table',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'parameters': {
          }
      },
    ])
def test_provider_not_allowed(play, command):
    import mock
    from play_dynamodb import providers
    provider = providers.DynamoDBProvider(play)
    assert provider.engine is play

    with mock.patch('play_dynamodb.providers.boto3') as boto3:
        with pytest.raises(ValueError):
            provider.command_dynamodb(command)
        assert boto3 \
            .resource \
            .called is False
        assert getattr(
                boto3.resource.return_value,
                command['method']) \



@pytest.mark.parametrize(
    'command',
    [
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'get_item',
      'variable': 'item',
      'variable_expression': 'results["Item"]',
      'assertion': 'variables["item"]["AlbumTitle"]["S"] '
                   '== "Songs About Life"',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'TableName': 'Music',
      'parameters': {
          'Key': {
              'Artist': {
                  'S': 'Acme Band',
                  },
              'SongTitle': {
                  'S': 'Happy Day',
                  },
              },
          }
      },
    ])
def test_provider_variable_assertion(play, command):
    import mock
    from play_dynamodb import providers
    provider = providers.DynamoDBProvider(play)
    assert provider.engine is play

    with mock.patch('play_dynamodb.providers.boto3') as boto3:
        getattr(
                boto3.resource.return_value.Table.return_value,
                command['method']) \
            .return_value = {
                'Item': {
                    'AlbumTitle': {
                        'S': 'Songs About Life'
                        }
                    }
                }
        provider.command_dynamodb(command)
        assert boto3 \
            .resource \
            .assert_called_with(
                'dynamodb',
                **command['connection']) is None
        assert boto3 \
            .resource \
            .return_value \
            .Table \
            .assert_called_once_with(command['TableName']) is None
        assert getattr(
                boto3.resource.return_value.Table.return_value,
                command['method']) \
            .assert_called_with(
                **command['parameters']) is None
        assert 'item' in play.variables
        assert play.variables['item']


@pytest.mark.parametrize(
    'command',
    [
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'get_item',
      'variable': 'item',
      'variable_expression': 'results["Item"]',
      'assertion': 'variables["item"]["AlbumTitle"]["S"] '
                   '== "SonGs About Life"',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'TableName': 'Music',
      'parameters': {
          'Key': {
              'Artist': {
                  'S': 'Acme Band',
                  },
              'SongTitle': {
                  'S': 'Happy Day',
                  },
              },
          }
      },
    ])
def test_provider_variable_assertion_ko(play, command):
    import mock
    from play_dynamodb import providers
    provider = providers.DynamoDBProvider(play)
    assert provider.engine is play

    with mock.patch('play_dynamodb.providers.boto3') as boto3:
        getattr(
                boto3.resource.return_value.Table.return_value,
                command['method']) \
            .return_value = {
                'Item': {
                    'AlbumTitle': {
                        'S': 'Songs About Life'
                        }
                    }
                }
        with pytest.raises(AssertionError):
            provider.command_dynamodb(command)
        assert boto3 \
            .resource \
            .assert_called_with(
                'dynamodb',
                **command['connection']) is None
        assert boto3 \
            .resource \
            .return_value \
            .Table \
            .assert_called_once_with(command['TableName']) is None
        assert getattr(
                boto3.resource.return_value.Table.return_value,
                command['method']) \
            .assert_called_with(
                **command['parameters']) is None
        assert 'item' in play.variables
        assert play.variables['item']
