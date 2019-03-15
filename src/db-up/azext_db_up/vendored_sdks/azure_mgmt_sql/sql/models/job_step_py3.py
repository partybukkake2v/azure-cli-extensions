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

from .proxy_resource_py3 import ProxyResource


class JobStep(ProxyResource):
    """A job step.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param step_id: The job step's index within the job. If not specified when
     creating the job step, it will be created as the last step. If not
     specified when updating the job step, the step id is not modified.
    :type step_id: int
    :param target_group: Required. The resource ID of the target group that
     the job step will be executed on.
    :type target_group: str
    :param credential: Required. The resource ID of the job credential that
     will be used to connect to the targets.
    :type credential: str
    :param action: Required. The action payload of the job step.
    :type action: ~azure.mgmt.sql.models.JobStepAction
    :param output: Output destination properties of the job step.
    :type output: ~azure.mgmt.sql.models.JobStepOutput
    :param execution_options: Execution options for the job step.
    :type execution_options: ~azure.mgmt.sql.models.JobStepExecutionOptions
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'target_group': {'required': True},
        'credential': {'required': True},
        'action': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'step_id': {'key': 'properties.stepId', 'type': 'int'},
        'target_group': {'key': 'properties.targetGroup', 'type': 'str'},
        'credential': {'key': 'properties.credential', 'type': 'str'},
        'action': {'key': 'properties.action', 'type': 'JobStepAction'},
        'output': {'key': 'properties.output', 'type': 'JobStepOutput'},
        'execution_options': {'key': 'properties.executionOptions', 'type': 'JobStepExecutionOptions'},
    }

    def __init__(self, *, target_group: str, credential: str, action, step_id: int=None, output=None, execution_options=None, **kwargs) -> None:
        super(JobStep, self).__init__(**kwargs)
        self.step_id = step_id
        self.target_group = target_group
        self.credential = credential
        self.action = action
        self.output = output
        self.execution_options = execution_options
