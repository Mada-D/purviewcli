# pv account getResourceSetRules
[Command Reference](../../../README.md#command-reference) > [account](./main.md) > getResourceSetRules

## Description
List all resource sets.

## Syntax
```
pv account getResourceSetRules
```

## Required Arguments
*None*

## Optional Arguments
*None*

## API Mapping
Account Data Plane > Resource Set Rules > [List Resource Set Rules](https://docs.microsoft.com/en-us/rest/api/purview/accountdataplane/resource-set-rules/list-resource-set-rules)
```
GET https://{accountName}.purview.azure.com/account/resourceSetRuleConfigs
```

## Examples
List all resource sets.
```powershell
pv account getResourceSetRules
```