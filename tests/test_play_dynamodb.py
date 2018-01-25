#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_dynamodb` package."""


def test_provider():
    from play_dynamodb import providers
    provider = providers.DynamoDBProvider(None)
    assert provider.engine is None
    provider.command_dynamodb(
        {'provider': 'play_dynamodb',
         'type': 'dynamodb'})
