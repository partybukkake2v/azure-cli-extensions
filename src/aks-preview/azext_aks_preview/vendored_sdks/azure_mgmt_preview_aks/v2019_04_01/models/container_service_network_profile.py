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


class ContainerServiceNetworkProfile(Model):
    """Profile of network configuration.

    :param network_plugin: Network plugin used for building Kubernetes
     network. Possible values include: 'azure', 'kubenet'. Default value:
     "kubenet" .
    :type network_plugin: str or
     ~azure.mgmt.containerservice.v2019_04_01.models.NetworkPlugin
    :param network_policy: Network policy used for building Kubernetes
     network. Possible values include: 'calico', 'azure'
    :type network_policy: str or
     ~azure.mgmt.containerservice.v2019_04_01.models.NetworkPolicy
    :param pod_cidr: A CIDR notation IP range from which to assign pod IPs
     when kubenet is used. Default value: "10.244.0.0/16" .
    :type pod_cidr: str
    :param service_cidr: A CIDR notation IP range from which to assign service
     cluster IPs. It must not overlap with any Subnet IP ranges. Default value:
     "10.0.0.0/16" .
    :type service_cidr: str
    :param dns_service_ip: An IP address assigned to the Kubernetes DNS
     service. It must be within the Kubernetes service address range specified
     in serviceCidr. Default value: "10.0.0.10" .
    :type dns_service_ip: str
    :param docker_bridge_cidr: A CIDR notation IP range assigned to the Docker
     bridge network. It must not overlap with any Subnet IP ranges or the
     Kubernetes service address range. Default value: "172.17.0.1/16" .
    :type docker_bridge_cidr: str
    """

    _validation = {
        'pod_cidr': {'pattern': r'^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$'},
        'service_cidr': {'pattern': r'^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$'},
        'dns_service_ip': {'pattern': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'},
        'docker_bridge_cidr': {'pattern': r'^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$'},
    }

    _attribute_map = {
        'network_plugin': {'key': 'networkPlugin', 'type': 'str'},
        'network_policy': {'key': 'networkPolicy', 'type': 'str'},
        'pod_cidr': {'key': 'podCidr', 'type': 'str'},
        'service_cidr': {'key': 'serviceCidr', 'type': 'str'},
        'dns_service_ip': {'key': 'dnsServiceIP', 'type': 'str'},
        'docker_bridge_cidr': {'key': 'dockerBridgeCidr', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerServiceNetworkProfile, self).__init__(**kwargs)
        self.network_plugin = kwargs.get('network_plugin', "kubenet")
        self.network_policy = kwargs.get('network_policy', None)
        self.pod_cidr = kwargs.get('pod_cidr', "10.244.0.0/16")
        self.service_cidr = kwargs.get('service_cidr', "10.0.0.0/16")
        self.dns_service_ip = kwargs.get('dns_service_ip', "10.0.0.10")
        self.docker_bridge_cidr = kwargs.get('docker_bridge_cidr', "172.17.0.1/16")
