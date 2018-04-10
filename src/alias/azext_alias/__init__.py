# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.decorators import Completer
from azure.cli.core.commands.events import EVENT_INVOKER_PRE_CMD_TBL_TRUNCATE, EVENT_INVOKER_ON_TAB_COMPLETION
from azure.cli.command_modules.interactive.events import (
    EVENT_INTERACTIVE_PRE_COMPLETER_TEXT_PARSING,
    EVENT_INTERACTIVE_POST_SUB_TREE_CREATE
)
from azext_alias import _help  # pylint: disable=unused-import
from azext_alias.hooks import (
    alias_event_handler,
    enable_aliases_autocomplete,
    transform_cur_commands_interactive,
    enable_aliases_autocomplete_interactive
)
from azext_alias.util import get_alias_table
from azext_alias._validators import process_alias_create_namespace


# We don't have access to load_cmd_tbl_func in custom.py (need the entire command table
# for alias and command validation when the user invokes alias create).
# This cache saves the entire command table globally so custom.py can have access to it.
# Alter this cache through cache_reserved_commands(load_cmd_tbl_func) in util.py
cached_reserved_commands = []


class AliasExtCommandLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_command_type = CliCommandType(operations_tmpl='azext_alias.custom#{}')
        super(AliasExtCommandLoader, self).__init__(cli_ctx=cli_ctx,
                                                    custom_command_type=custom_command_type)
        self.cli_ctx.register_event(EVENT_INVOKER_PRE_CMD_TBL_TRUNCATE, alias_event_handler)
        self.cli_ctx.register_event(EVENT_INVOKER_ON_TAB_COMPLETION, enable_aliases_autocomplete)
        self.cli_ctx.register_event(EVENT_INTERACTIVE_PRE_COMPLETER_TEXT_PARSING, transform_cur_commands_interactive)
        self.cli_ctx.register_event(EVENT_INTERACTIVE_POST_SUB_TREE_CREATE, enable_aliases_autocomplete_interactive)

    def load_command_table(self, _):
        with self.command_group('alias') as g:
            g.custom_command('create', 'create_alias', validator=process_alias_create_namespace)
            g.custom_command('list', 'list_alias')
            g.custom_command('remove', 'remove_alias')

        return self.command_table

    def load_arguments(self, _):
        with self.argument_context('alias create') as c:
            c.argument('alias_name', options_list=['--name', '-n'], help='The name of the alias.')
            c.argument('alias_command', options_list=['--command', '-c'], help='The command that the alias points to.')

        with self.argument_context('alias remove') as c:
            c.argument('alias_name', options_list=['--name', '-n'], help='The name of the alias.',
                       completer=get_alias_completer)


@Completer
def get_alias_completer(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    """
    An argument completer for alias name.
    """
    return get_alias_table().sections()


COMMAND_LOADER_CLS = AliasExtCommandLoader
