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


class MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInput(Model):
    """Database specific information for PostgreSQL to Azure Database for
    PostgreSQL migration task inputs.

    :param name: Name of the database
    :type name: str
    :param target_database_name: Name of target database. Note: Target
     database will be truncated before starting migration.
    :type target_database_name: str
    :param make_source_db_read_only: Whether to set database read only before
     migration
    :type make_source_db_read_only: bool
    :param table_map: Mapping of source to target tables
    :type table_map: dict[str, str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'target_database_name': {'key': 'targetDatabaseName', 'type': 'str'},
        'make_source_db_read_only': {'key': 'makeSourceDbReadOnly', 'type': 'bool'},
        'table_map': {'key': 'tableMap', 'type': '{str}'},
    }

    def __init__(self, name=None, target_database_name=None, make_source_db_read_only=None, table_map=None):
        super(MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInput, self).__init__()
        self.name = name
        self.target_database_name = target_database_name
        self.make_source_db_read_only = make_source_db_read_only
        self.table_map = table_map
