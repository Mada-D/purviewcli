# pv account regenerateAccessKeys
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > regenerateAccessKeys

## Description
Regenerate the authorization keys associated with this data catalog.

## Syntax
```
pv account regenerateAccessKeys --keyType=<val>
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Accounts > [Regenerate Access Key](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/accounts/regenerate-access-key)
```
POST https://{accountName}.purview.azure.com/account/regeneratekeys
```

## Examples
Regenerate the primary Atlas Kafka authorization key.
```powershell
pv account regenerateAccessKeys --keyType "PrimaryAtlasKafkaKey"
```

Regenerate the secondary Atlas Kafka authorization key.
```powershell
pv account regenerateAccessKeys --keyType "SecondaryAtlasKafkaKey"
```
