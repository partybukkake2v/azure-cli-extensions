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


class ApplicationGatewayAutoscaleBounds(Model):
    """Application Gateway autoscale bounds on number of Application Gateway
    instance.

    All required parameters must be populated in order to send to Azure.

    :param min: Required. Lower bound on number of Application Gateway
     instances.
    :type min: int
    :param max: Required. Upper bound on number of Application Gateway
     instances.
    :type max: int
    """

    _validation = {
        'min': {'required': True},
        'max': {'required': True},
    }

    _attribute_map = {
        'min': {'key': 'min', 'type': 'int'},
        'max': {'key': 'max', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayAutoscaleBounds, self).__init__(**kwargs)
        self.min = kwargs.get('min', None)
        self.max = kwargs.get('max', None)
