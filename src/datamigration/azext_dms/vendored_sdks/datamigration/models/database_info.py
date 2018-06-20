# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DatabaseInfo(Model):
    """Project Database Details.

    :param source_database_name: Name of the database
    :type source_database_name: str
    """

    _validation = {
        'source_database_name': {'required': True},
    }

    _attribute_map = {
        'source_database_name': {'key': 'sourceDatabaseName', 'type': 'str'},
    }

    def __init__(self, source_database_name):
        super(DatabaseInfo, self).__init__()
        self.source_database_name = source_database_name
