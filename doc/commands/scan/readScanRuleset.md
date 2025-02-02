# pv scan readScanRuleset
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readScanRuleset

## Description
Get a scan ruleset

## Syntax
```
pv scan readScanRuleset --scanRulesetName=<val>
```

## Required Arguments
`--scanRulesetName` (string)  
The scan ruleset name.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Scan Rulesets > [Get](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-rulesets/get)
```
GET https://{accountName}.purview.azure.com/scan/scanrulesets/{scanRulesetName}
```

## Examples
Get a custom scan ruleset.
```powershell
pv scan readScanRuleset --scanRulesetName "twitter_scan_rule_set"
```