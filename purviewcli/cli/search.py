"""
usage: 
    pv search query [--keywords=<val> --limit=<val> --offset=<val> --filter-file=<val> --facets-file=<val>]
    pv search autoComplete [--keywords=<val> --limit=<val> --filter-file=<val>]
    pv search suggest [--keywords=<val> --limit=<val> --filter-file=<val>]
    pv search browse  (--entityType=<val> | --path=<val>) [--limit=<val> --offset=<val>]

options:
  --purviewName=<val>     [string]  Azure Purview account name.
  --keywords=<val>        [string]  The keywords applied to all searchable fields.
  --entityType=<val>      [string]  The entity type to browse as the root level entry point.
  --path=<val>            [string]  The path to browse the next level child entities.
  --limit=<val>           [integer] By default there is no paging [default: 25].
  --offset=<val>          [integer] Offset for pagination purpose [default: 0].
  --filter-file=<val>     [string]  File path to a filter json file.
  --facets-file=<val>     [string]  File path to a facets json file.

mapping:
https://{account_name}.catalog.purview.azure.com
+---------+--------+-------------------+
| Command | Method | Path              |
+---------+--------+-------------------+
| query   | POST   | /api/search/query |
+---------+--------+-------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
