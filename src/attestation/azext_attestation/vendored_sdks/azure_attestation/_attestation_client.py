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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AttestationClientConfiguration
from .operations import PolicyOperations
from .operations import PolicyCertificatesOperations
from .operations import SigningCertificatesOperations
from .operations import MetadataConfigurationOperations
from . import models


class AttestationClient(SDKClient):
    """Describes the interface for the per-tenant enclave service.

    :ivar config: Configuration for client.
    :vartype config: AttestationClientConfiguration

    :ivar policy: Policy operations
    :vartype policy: azure.attestation.operations.PolicyOperations
    :ivar policy_certificates: PolicyCertificates operations
    :vartype policy_certificates: azure.attestation.operations.PolicyCertificatesOperations
    :ivar signing_certificates: SigningCertificates operations
    :vartype signing_certificates: azure.attestation.operations.SigningCertificatesOperations
    :ivar metadata_configuration: MetadataConfiguration operations
    :vartype metadata_configuration: azure.attestation.operations.MetadataConfigurationOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    """

    def __init__(
            self, credentials):

        self.config = AttestationClientConfiguration(credentials)
        super(AttestationClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-09-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.policy = PolicyOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policy_certificates = PolicyCertificatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.signing_certificates = SigningCertificatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.metadata_configuration = MetadataConfigurationOperations(
            self._client, self.config, self._serialize, self._deserialize)
