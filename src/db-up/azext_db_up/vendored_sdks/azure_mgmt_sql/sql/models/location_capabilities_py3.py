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


class LocationCapabilities(Model):
    """The location capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The location name.
    :vartype name: str
    :ivar supported_server_versions: The list of supported server versions.
    :vartype supported_server_versions:
     list[~azure.mgmt.sql.models.ServerVersionCapability]
    :ivar supported_managed_instance_versions: The list of supported managed
     instance versions.
    :vartype supported_managed_instance_versions:
     list[~azure.mgmt.sql.models.ManagedInstanceVersionCapability]
    :ivar status: The status of the capability. Possible values include:
     'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :param reason: The reason for the capability not being available.
    :type reason: str
    """

    _validation = {
        'name': {'readonly': True},
        'supported_server_versions': {'readonly': True},
        'supported_managed_instance_versions': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'supported_server_versions': {'key': 'supportedServerVersions', 'type': '[ServerVersionCapability]'},
        'supported_managed_instance_versions': {'key': 'supportedManagedInstanceVersions', 'type': '[ManagedInstanceVersionCapability]'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(self, *, reason: str=None, **kwargs) -> None:
        super(LocationCapabilities, self).__init__(**kwargs)
        self.name = None
        self.supported_server_versions = None
        self.supported_managed_instance_versions = None
        self.status = None
        self.reason = reason
