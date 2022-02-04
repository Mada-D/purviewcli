# pv types readClassificationDef
[Command Reference](../../../README.md#command-reference) > [types](./main.md) > readClassificationDef

## Description
Get the classification definition for the given GUID or by its name (unique).

## Syntax
```
pv types readClassificationDef (--guid=<val> | --name=<val>)
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the classification.

`--name` (string)  
The name of the classification.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Types > [Get Classification Def By Guid](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-classification-def-by-guid)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/classificationdef/guid/{guid}
```

Catalog Data Plane > Types > [Get Classification Def By Name](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/types/get-classification-def-by-name)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/types/classificationdef/name/{name}
```

## Examples
Get classification definition by name.
```powershell
pv types readClassificationDef --name "MICROSOFT.GOVERNMENT.CANADA.DRIVERS_LICENSE_NUMBER"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "attributeDefs": [],
    "category": "RELATIONSHIP",
    "createTime": 1615887114341,
    "createdBy": "admin",
    "description": "bigquery_dataset_tables",
    "endDef1": {
        "cardinality": "SET",
        "isContainer": true,
        "isLegacyAttribute": false,
        "name": "tables",
        "type": "bigquery_dataset"
    },
    "endDef2": {
        "cardinality": "SINGLE",
        "isContainer": false,
        "isLegacyAttribute": false,
        "name": "dataset",
        "type": "bigquery_table"
    },
    "guid": "94dced37-45a9-7660-f63d-fd2ab949da82",
    "lastModifiedTS": "1",
    "name": "bigquery_dataset_tables",
    "propagateTags": "NONE",
    "relationshipCategory": "COMPOSITION",
    "serviceType": "Google BigQuery",
    "typeVersion": "1.0",
    "updateTime": 1615887114341,
    "updatedBy": "admin",
    "version": 1
}
</p>
</details>

Get classification definition by guid.
```powershell
pv types readClassificationDef --guid "324fd07d-327a-3c0a-5f74-ee9310936782"
```