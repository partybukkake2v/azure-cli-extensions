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


class TopicUpdateParameters(Model):
    """Properties of the Topic update.

    :param tags: Tags of the resource.
    :type tags: dict[str, str]
    :param allow_traffic_from_all_ips: This determines if IP filtering rules
     ought to be evaluated or not. By default it will not evaluate and will
     allow traffic from all IPs.
    :type allow_traffic_from_all_ips: bool
    :param inbound_ip_rules: This determines the IP filtering rules that ought
     be applied when events are received on this domain.
    :type inbound_ip_rules: list[~azext_eventgrid.models.InboundIpRule]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'allow_traffic_from_all_ips': {'key': 'allowTrafficFromAllIPs', 'type': 'bool'},
        'inbound_ip_rules': {'key': 'inboundIpRules', 'type': '[InboundIpRule]'},
    }

    def __init__(self, **kwargs):
        super(TopicUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.allow_traffic_from_all_ips = kwargs.get('allow_traffic_from_all_ips', None)
        self.inbound_ip_rules = kwargs.get('inbound_ip_rules', None)
