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


class SlackChannelProperties(Model):
    """The parameters to provide for the Slack channel.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param client_id: The Slack client id
    :type client_id: str
    :param client_secret: The Slack client secret. Value only returned through
     POST to the action Channel List API, otherwise empty.
    :type client_secret: str
    :param verification_token: The Slack verification token. Value only
     returned through POST to the action Channel List API, otherwise empty.
    :type verification_token: str
    :param landing_page_url: The Slack landing page Url
    :type landing_page_url: str
    :ivar redirect_action: The Slack redirect action
    :vartype redirect_action: str
    :ivar last_submission_id: The Sms auth token
    :vartype last_submission_id: str
    :ivar register_before_oauth_flow: Whether to register the settings before
     OAuth validation is performed. Recommended to True.
    :vartype register_before_oauth_flow: bool
    :ivar is_validated: Whether this channel is validated for the bot
    :vartype is_validated: bool
    :param is_enabled: Whether this channel is enabled for the bot
    :type is_enabled: bool
    """

    _validation = {
        'client_id': {'required': True},
        'client_secret': {'required': True},
        'verification_token': {'required': True},
        'redirect_action': {'readonly': True},
        'last_submission_id': {'readonly': True},
        'register_before_oauth_flow': {'readonly': True},
        'is_validated': {'readonly': True},
        'is_enabled': {'required': True},
    }

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'client_secret': {'key': 'clientSecret', 'type': 'str'},
        'verification_token': {'key': 'verificationToken', 'type': 'str'},
        'landing_page_url': {'key': 'landingPageUrl', 'type': 'str'},
        'redirect_action': {'key': 'redirectAction', 'type': 'str'},
        'last_submission_id': {'key': 'lastSubmissionId', 'type': 'str'},
        'register_before_oauth_flow': {'key': 'registerBeforeOAuthFlow', 'type': 'bool'},
        'is_validated': {'key': 'isValidated', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
    }

    def __init__(self, client_id, client_secret, verification_token, is_enabled, landing_page_url=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.verification_token = verification_token
        self.landing_page_url = landing_page_url
        self.redirect_action = None
        self.last_submission_id = None
        self.register_before_oauth_flow = None
        self.is_validated = None
        self.is_enabled = is_enabled
