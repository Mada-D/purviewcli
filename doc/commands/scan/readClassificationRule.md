# pv scan readClassificationRule
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readClassificationRule

## Description
Get a classification rule

## Syntax
```
pv scan readClassificationRule --classificationRuleName=<val>
```

## Required Arguments
`--classificationRuleName` (string)  
The name of the classification rule.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Classification Rules > [Get](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/classification-rules/get)
```
GET https://{accountName}.purview.azure.com/scan/classificationrules/{classificationRuleName}
```

## Examples
Get a classification rule by name.
```powershell
pv scan readClassificationRule --classificationRuleName "twitter_handle"
```