=============
play dynamodb
=============


.. image:: https://img.shields.io/pypi/v/play_dynamodb.svg
        :target: https://pypi.python.org/pypi/play_dynamodb

.. image:: https://travis-ci.org/davidemoro/play_dynamodb.svg?branch=develop
       :target: https://travis-ci.org/davidemoro/play_dynamodb

.. image:: https://readthedocs.org/projects/play-dynamodb/badge/?version=latest
        :target: https://play-dynamodb.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/davidemoro/play_dynamodb/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/davidemoro/play_dynamodb


pytest-play support for AWS DynamoDB queries and assertions

More info and examples on:

* pytest-play_, documentation
* cookiecutter-qa_, see ``pytest-play`` in action with a working example if you want to start hacking


Features
--------

This project defines new pytest-play_ commands for AWS DynamoDB:

::

    {"type": "dynamodb",
     "provider": "play_dynamodb",
     "method": "get_item",
     "connection": {
         "region_name": "us-west-2",
         "endpoint_url": "http://localhost:8000"
         },
     "variable": "item",
     "variable_expression": "response",
     "assertion": "item['Item']['AlbumTitle']['S'] == 'Songs About Life'",
     "TableName": "Music",
     "parameters": {
         "Key": {
             "Artist": {
                 "S": "Acme Band"
                 },
             "SongTitle": {
                 "S": "Happy Day"
                 }
             }
         }
    }

Supported methods:

* batch_get_item
* batch_write_item
* delete_item
* get_item
* put_item
* query
* scan
* update_item


Twitter
-------

``pytest-play`` tweets happens here:

* `@davidemoro`_

Credits
-------

This package was created with Cookiecutter_ and the cookiecutter-play-plugin_ (based on `audreyr/cookiecutter-pypackage`_ project template).

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`cookiecutter-play-plugin`: https://github.com/davidemoro/cookiecutter-play-plugin
.. _pytest-play: https://github.com/davidemoro/pytest-play
.. _cookiecutter-qa: https://github.com/davidemoro/cookiecutter-qa
.. _`@davidemoro`: https://twitter.com/davidemoro
