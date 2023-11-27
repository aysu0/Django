from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = "c1008080dcbs"
    account_key = "BHkERBQmEw6JVhrymI8BxPF+udlvext7Y+dcMggE5dxq2kbagd02ihNeO12pyKiKzfV3bpXk9Uwi+ASt9sS1eA=="
    azure_container = "media"
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = "c1008080dcbs"
    account_key = "BHkERBQmEw6JVhrymI8BxPF+udlvext7Y+dcMggE5dxq2kbagd02ihNeO12pyKiKzfV3bpXk9Uwi+ASt9sS1eA=="
    azure_container = "static"
    expiration_secs = None