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
      'parameters': {
          'Key': {
              'Artist': {
                  'S': 'Acme Band',
                  },
              'SongTitle': {
                  'S': 'Happy Day',
                  },
              },
          'TableName': 'Music',
          }
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'batch_get_item',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'parameters': {
          'RequestItems': {
              'Music': {
                  'Keys': [
                      {
                          'Artist': {
                              'S': 'No One You Know',
                          },
                          'SongTitle': {
                              'S': 'Call Me Today',
                          },
                      },
                      {
                          'Artist': {
                              'S': 'Acme Band',
                          },
                          'SongTitle': {
                              'S': 'Happy Day',
                          },
                      },
                      {
                          'Artist': {
                              'S': 'No One You Know',
                          },
                          'SongTitle': {
                              'S': 'Scared of My Shadow',
                          },
                      }],
                  'ProjectionExpression': 'AlbumTitle',
                  },
              }
          }
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'batch_write_item',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'parameters': {
          'RequestItems': {
              'Music': [
                  {
                      'PutRequest': {
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
                      },
                  },
                  {
                      'PutRequest': {
                          'Item': {
                              'AlbumTitle': {
                                  'S': 'Songs About Life',
                              },
                              'Artist': {
                                  'S': 'Acme Band',
                              },
                              'SongTitle': {
                                  'S': 'Happy Day',
                              },
                          },
                      },
                  },
                  {
                      'PutRequest': {
                          'Item': {
                              'AlbumTitle': {
                                  'S': 'Blue Sky Blues',
                              },
                              'Artist': {
                                  'S': 'No One You Know',
                              },
                              'SongTitle': {
                                  'S': 'Scared of My Shadow',
                              },
                          },
                      },
                  }],
              },
          },
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'delete_item',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'parameters': {
          'Key': {
              'Artist': {
                  'S': 'No One You Know',
                  },
              'SongTitle': {
                  'S': 'Scared of My Shadow',
                  },
              },
          'TableName': 'Music',
          },
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'describe_limits',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'parameters': {
          },
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'describe_table',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'parameters': {
              'TableName': 'Music'
          },
      },
     {
      'provider': 'play_dynamodb',
      'type': 'dynamodb',
      'method': 'list_tables',
      'connection': {
          'region_name': 'us-west-2',
          'endpoint_url': 'http://localhost:8000',
          },
      'parameters': {
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
          'TableName': 'Music',
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
      'parameters': {
          'ExpressionAttributeValues': {
              ':v1': {
                  'S': 'No One You Know',
              },
          },
          'KeyConditionExpression': 'Artist = :v1',
          'ProjectionExpression': 'SongTitle',
          'TableName': 'Music',
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
          'TableName': 'Music',
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
          'TableName': 'Music',
          'UpdateExpression': 'SET #Y = :y, #AT = :t',
          }
      },
    ])
def test_provider(play_json, command):
    import mock
    from play_dynamodb import providers
    provider = providers.DynamoDBProvider(play_json)
    assert provider.engine is play_json

    with mock.patch('play_dynamodb.providers.boto3') as boto3:
        provider.command_dynamodb(command)
        assert boto3 \
            .resource \
            .assert_called_with(
                'dynamodb',
                **command['connection']) is None
        assert getattr(
                boto3.resource.return_value,
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
          'TableName': 'Music',
          }
      },
    ])
def test_provider_not_allowed(play_json, command):
    import mock
    from play_dynamodb import providers
    provider = providers.DynamoDBProvider(play_json)
    assert provider.engine is play_json

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
      'parameters': {
          'Key': {
              'Artist': {
                  'S': 'Acme Band',
                  },
              'SongTitle': {
                  'S': 'Happy Day',
                  },
              },
          'TableName': 'Music',
          }
      },
    ])
def test_provider_variable_assertion(play_json, command):
    import mock
    from play_dynamodb import providers
    provider = providers.DynamoDBProvider(play_json)
    assert provider.engine is play_json

    with mock.patch('play_dynamodb.providers.boto3') as boto3:
        getattr(
                boto3.resource.return_value,
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
        assert getattr(
                boto3.resource.return_value,
                command['method']) \
            .assert_called_with(
                **command['parameters']) is None
        assert 'item' in play_json.variables
        assert play_json.variables['item']
