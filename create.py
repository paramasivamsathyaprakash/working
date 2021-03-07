import random
import json
import string
from typing import List, Optional


class Ranges:
    max_storage: int
    min_memory: int
    max_memory: int
    min_cores: int
    max_cores: int

    def __init__(self, max_storage: int, min_memory: int, max_memory: int, min_cores: int, max_cores: int) -> None:
        self.max_storage = max_storage
        self.min_memory = min_memory
        self.max_memory = max_memory
        self.min_cores = min_cores
        self.max_cores = max_cores


class Config:
    ranges: Ranges

    def __init__(self, ranges: Ranges) -> None:
        self.ranges = ranges


class Site:
    id: None
    default: bool

    def __init__(self, id: None, default: bool) -> None:
        self.id = id
        self.default = default


class ResourcePermissions:
    all_clouds: bool
    sites: List[Site]

    def __init__(self, all_clouds: bool, sites: List[Site]) -> None:
        self.all_clouds = all_clouds
        self.sites = sites


class TenantPermissions:
    accounts: List[int]

    def __init__(self, accounts: List[int]) -> None:
        self.accounts = accounts


class Permissions:
    resource_permissions: ResourcePermissions
    tenant_permissions: TenantPermissions

    def __init__(self, resource_permissions: ResourcePermissions, tenant_permissions: TenantPermissions) -> None:
        self.resource_permissions = resource_permissions
        self.tenant_permissions = tenant_permissions


class ProvisionType:
    id: Optional[int]

    def __init__(self, id: Optional[int]) -> None:
        self.id = id


class ServicePlan:
	length = 5
    rand_str = ''.join(random.choices(string.ascii_letters+string.digits,k=length))
    name: str
    code: rand_str
    description: None
    provision_type: ProvisionType
    custom_cores: bool
    config: Config
    max_storage: int
    max_memory: int
    price_sets: List[ProvisionType]
    visibility: str
    permissions: Permissions

    def __init__(self, name: str, code: str, description: None, provision_type: ProvisionType, custom_cores: bool, config: Config, max_storage: int, max_memory: int, price_sets: List[ProvisionType], visibility: str, permissions: Permissions) -> None:
        self.name = name
        self.code = code
        self.description = description
        self.provision_type = provision_type
        self.custom_cores = custom_cores
        self.config = config
        self.max_storage = max_storage
        self.max_memory = max_memory
        self.price_sets = price_sets
        self.visibility = visibility
        self.permissions = permissions


class Welcome7:
    service_plan: ServicePlan

    def __init__(self, service_plan: ServicePlan) -> None:
        self.service_plan = service_plan
