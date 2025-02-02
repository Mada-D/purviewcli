# pv search suggest
[Command Reference](../../../README.md#command-reference) > [search](./main.md) > suggest

## Description
Get search suggestions by query criteria.

## Syntax
```
pv search suggest [--keywords=<val> --limit=<val> --filter-file=<val>]
```

## Required Arguments
*None*

## Optional Arguments
`--keywords` (string)  
The keywords applied to all fields that support suggest operation. It must be at least 1 character, and no more than 100 characters.

`--limit` (integer)  
The number of suggestions we hope to return. The default value is 5. The value must be a number between 1 and 100.

`--filter-file` (string)  
The filter for the search.

## API Mapping
Catalog Data Plane > Discovery > [Suggest](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/discovery/suggest)
```
POST https://{accountName}.purview.azure.com/catalog/api/search/suggest
```

## Examples
Search suggestions by keywords.
```powershell
pv search suggest --keywords "Sta"
```