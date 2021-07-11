import random, string, uuid, time, sys, subprocess, json
from purviewcli.demo.utils import http_get

class ControlPlane():
    def __init__(self):
        self.token = None
        self.tokenGraph = None

    # SUBSCRIPTIONS
    def subscriptionsList(self):
        result = subprocess.run(['az', 'account', 'list'], stdout=subprocess.PIPE)
        response = json.loads(result.stdout)
        return response

    # PROVIDERS
    def providersGet(self, subscriptionId, resourceProviderNamespace):
        method = 'GET'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}'
        params = {'api-version': '2021-04-01'}
        payload = None
        data = http_get(method, endpoint, params, payload, self.token)
        return data

    # RESOURCE GROUP
    def resourceGroupCheckExistence(self, subscriptionId, resourceGroupName):
        method = 'HEAD'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'
        params = {'api-version': '2021-04-01'}
        payload = None
        data = http_get(method, endpoint, params, payload, self.token)
        response = True if data['status_code'] == 204 else False
        return response

    def resourceGroupCreateUpdate(self, subscriptionId, resourceGroupName, location):
        method = 'PUT'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'
        params = { 'api-version': '2021-04-01' }
        payload = { 'location': location }
        data = http_get(method, endpoint, params, payload, self.token)      
        return data

    def resourceGroupGet(self, subscriptionId, resourceGroupName):
        method = 'GET'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'
        params = {'api-version': '2021-04-01'}
        payload = None
        data = http_get(method, endpoint, params, payload, self.token)
        return data

    def resourceGroupProvision(self, subscriptionId, resourceGroupName, location):
        # 1. Set resourceGroupName
        resourceGroupName = resourceGroupName or 'purview-rg-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # 2. Create resourceGroupName if does not exists
        isExists = self.resourceGroupCheckExistence(subscriptionId, resourceGroupName)
        if isExists:
            print(f' - Will use existing resource group: [{resourceGroupName}]')
        else:
            print(f' - Creating new resource group: [{resourceGroupName}]...')
            data = self.resourceGroupCreateUpdate(subscriptionId, resourceGroupName, location)
            if 'error' in data:
                print(data)
                sys.exit()

            provisioning = True
            while provisioning:
                if data['properties']['provisioningState'] == 'Succeeded':
                    provisioning = False
                else:
                    data = self.resourceGroupGet(subscriptionId, resourceGroupName)
            print(f' - Resource group [{resourceGroupName}] created successfully!')

        return resourceGroupName

    # AZURE PURVIEW ACCOUNT
    def purviewAccountCheckNameAvailability(self, subscriptionId, accountName):
        method = 'POST'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Purview/checkNameAvailability'
        params = {'api-version': '2020-12-01-preview'}
        payload = {'name': accountName, 'type': 'Microsoft.Purview/accounts'}
        data = http_get(method, endpoint, params, payload, self.token)
        return data

    def purviewAccountCreateUpdate(self, subscriptionId, resourceGroupName, accountName, location):
        method = 'PUT'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
        params = {'api-version': '2020-12-01-preview'}
        payload = {
            "identity": {
                "type": "SystemAssigned"
            },
            "location": location,
            "sku": {
                "name": "Standard",
                "capacity": 4
            }
        }
        data = http_get(method, endpoint, params, payload, self.token)
        return data

    def purviewAccountGet(self, subscriptionId, resourceGroupName, accountName):
        method = 'GET'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}'
        params = {'api-version': '2020-12-01-preview'}
        payload = None
        data = http_get(method, endpoint, params, payload, self.token)
        return data

    def purviewAccountProvision(self, subscriptionId, location, resourceGroupName, accountName):
        # 1. Set accountName
        accountName = accountName or 'purview-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # 2. Create account if accountName does not exist
        data = self.purviewAccountCheckNameAvailability(subscriptionId, accountName)
        if data['nameAvailable'] == False:
            print(f' - Azure Purview account name [{accountName}] is not available.')
            print(data)
            sys.exit()
        else:
            print(f' - Creating Azure Purview account [{accountName}].')
            data = self.purviewAccountCreateUpdate(subscriptionId, resourceGroupName, accountName, location)
            print(f' - Please wait while Azure Purview account [{accountName}] is being prepared, this will take a couple of minutes...')
        
        # 3. Periodically check provisioningState until Succeeded
        time.sleep(60)
        provisioning = True
        while provisioning:
            time.sleep(5)
            data = self.purviewAccountGet(subscriptionId, resourceGroupName, accountName)
            if data['properties']['provisioningState'] == 'Succeeded':
                provisioning = False

        print(f' - Purview account [{accountName}] created successfully!')
        print(f' - https://ms.web.purview.azure.com/resource/{accountName}')
        return data

    # STORAGE ACCOUNT
    def provisionStorageAccount(self, subscriptionId, location, resourceGroupName, token):
        accountName = 'adls' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        method = 'PUT'
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}'
        params = { 'api-version': '2018-02-01' }
        payload = {
            "sku": {
                "name": "Standard_LRS"
            },
            "properties": {
                "isHnsEnabled": True
            },
            "kind": "StorageV2",
            "location": location,
        }
        data = http_get(method, endpoint, params, payload, token)
        print(f'ADLS Gen2 Storage Account: {accountName}')
        return accountName

    # GRAPH
    # def getMe(self):
    #     method = 'GET'
    #     endpoint = 'https://graph.microsoft.com/v1.0/me'
    #     params = None
    #     payload = None
    #     data = http_get(method, endpoint, params, payload, self.tokenGraph)
    #     principalId = data['id']
    #     userPrincipalName = data['userPrincipalName']
    #     return principalId, userPrincipalName

    def getUser(self, objectId):
        method = 'GET'
        endpoint = f'https://graph.microsoft.com/v1.0/users/{objectId}'
        params = None
        payload = None
        data = http_get(method, endpoint, params, payload, self.tokenGraph)
        return data

    # AUTHORIZATION
    def roleAssignmentCreate(self, scope, roleDefinitionId, principalId):
        method = 'PUT'
        roleAssignmentName = uuid.uuid4()
        endpoint = f'{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}?api-version=2015-07-01'
        params = None
        payload = {
            "properties": {
                "roleDefinitionId": f"/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId}",
                "principalId": f'{principalId}'
            }
        }
        data = http_get(method, endpoint, params, payload, self.token)
        return data