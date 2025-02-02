# pv scan runScan
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > runScan

## Description
Run a scan.

## Syntax
```
pv scan runScan --dataSourceName=<val> --scanName=<val> [--scanLevel=<val>]
```

## Required Arguments
`--dataSourceName` (string)  
The data source name.

`--scanName` (string)  
The scan name.

## Optional Arguments
`--scanLevel` (string)  
The scan level type (Full or Incremental).

## API Mapping
Scanning Data Plane > Scan Result > [Run Scan](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/scan-result/run-scan)
```
PUT https://{accountName}.purview.azure.com/scan/datasources/{dataSourceName}/scans/{scanName}/run
```

## Examples
Run a scan by data source name and scan name.
```powershell
pv scan runScan --dataSourceName "AzureDataLakeStorage-EqK" --scanName "Scan-p1E"
```