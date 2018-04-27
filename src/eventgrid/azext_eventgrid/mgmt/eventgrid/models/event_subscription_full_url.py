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


class EventSubscriptionFullUrl(Model):
    """Full endpoint url of an event subscription.

    :param endpoint_url: The URL that represents the endpoint of the
     destination of an event subscription.
    :type endpoint_url: str
    """

    _attribute_map = {
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
    }

    def __init__(self, endpoint_url=None):
        super(EventSubscriptionFullUrl, self).__init__()
        self.endpoint_url = endpoint_url
