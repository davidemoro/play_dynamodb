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
      }
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
