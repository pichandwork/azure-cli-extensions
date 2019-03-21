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


class ManagedInstanceFamilyCapability(Model):
    """The managed server family capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Family name.
    :vartype name: str
    :ivar sku: SKU name.
    :vartype sku: str
    :ivar supported_license_types: List of supported license types.
    :vartype supported_license_types:
     list[~azure.mgmt.sql.models.LicenseTypeCapability]
    :ivar supported_vcores_values: List of supported virtual cores values.
    :vartype supported_vcores_values:
     list[~azure.mgmt.sql.models.ManagedInstanceVcoresCapability]
    :ivar included_max_size: Included size.
    :vartype included_max_size: ~azure.mgmt.sql.models.MaxSizeCapability
    :ivar supported_storage_sizes: Storage size ranges.
    :vartype supported_storage_sizes:
     list[~azure.mgmt.sql.models.MaxSizeRangeCapability]
    :ivar status: The status of the capability. Possible values include:
     'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :param reason: The reason for the capability not being available.
    :type reason: str
    """

    _validation = {
        'name': {'readonly': True},
        'sku': {'readonly': True},
        'supported_license_types': {'readonly': True},
        'supported_vcores_values': {'readonly': True},
        'included_max_size': {'readonly': True},
        'supported_storage_sizes': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
        'supported_license_types': {'key': 'supportedLicenseTypes', 'type': '[LicenseTypeCapability]'},
        'supported_vcores_values': {'key': 'supportedVcoresValues', 'type': '[ManagedInstanceVcoresCapability]'},
        'included_max_size': {'key': 'includedMaxSize', 'type': 'MaxSizeCapability'},
        'supported_storage_sizes': {'key': 'supportedStorageSizes', 'type': '[MaxSizeRangeCapability]'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ManagedInstanceFamilyCapability, self).__init__(**kwargs)
        self.name = None
        self.sku = None
        self.supported_license_types = None
        self.supported_vcores_values = None
        self.included_max_size = None
        self.supported_storage_sizes = None
        self.status = None
        self.reason = kwargs.get('reason', None)
