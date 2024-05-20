#Import required module dependencies
import asyncio
import systemlink.clients.nitestmonitor as nitestmonitor

# Go to this web site for the Test Monitor object model and query syntax
# https://github.com/ni/systemlink-OpenAPI-documents/wiki/Dynamic-Linq-Query-Language#test-monitor


class UploadTestRecords(object):
    def __init__(self, host_api, TestmonitorApiClient):
        self.host_api = host_api
        self.connect_api = TestmonitorApiClient
        self.products_api = nitestmonitor.ProductsApi(TestmonitorApiClient)
        self.results_api = nitestmonitor.ResultsApi(TestmonitorApiClient)
        self.steps_api = nitestmonitor.StepsApi(TestmonitorApiClient)
    
def testmonitor_api_connect_client(host_api):
    TestmonitorApiClient = nitestmonitor.ApiClient()
    upload_test_records = UploadTestRecords(host_api, TestmonitorApiClient)
    return upload_test_records

def testmonitor_api_connect_usr_pwd(host_api, username, password):
    configuration_object = nitestmonitor.Configuration(host=host_api, username=username, password=password)
    configuration_object.verify_ssl = False
    TestmonitorApiClient = nitestmonitor.ApiClient(configuration_object)
    upload_test_records = UploadTestRecords(host_api, TestmonitorApiClient)
    return upload_test_records

def testmonitor_api_connect_api_key(host_api, api_key): # open SystemLink Server connection using existing ApiKey
    headers = {'x-ni-api-key': api_key}
    configuration_object = nitestmonitor.Configuration(host=host_api, api_key=headers)
    configuration_object.verify_ssl = False
    TestmonitorApiClient = nitestmonitor.ApiClient(configuration_object)
    upload_test_records = UploadTestRecords(host_api, TestmonitorApiClient)
    return upload_test_records

async def main_async():
    host_url = "https://bradt2-lt/"
    #host_url = "https://demo.systemlink.io/"
    #host_url = "https://test.systemlink.io/"
    #host_url = "https://localhost/"
    host_api = host_url + "nitestmonitor" # "https://bradt2-lt/nitag"

    #username = "lvadmin"
    #password = "LabVIEW==="
    username = "admin"
    password = "mypassword"
    api_key = "8oSPBkB2XiRuZP4XeTVybBTaGXzH5gzlBt3bLut3YT"

    #upload_test_records = testmonitor_api_connect_client(host_api)                      # open SystemLink Server connection
    upload_test_records = testmonitor_api_connect_usr_pwd(host_api, username, password) # open SystemLink Server connection
    #upload_test_records = testmonitor_api_connect_api_key(host_api, api_key)            # open SystemLink Server connection

    product = nitestmonitor.ProductRequestObject(part_number="AB-123", name="Hello", family="World")
    create_product_request = nitestmonitor.CreateProductsRequest(products=[product])
    response = await upload_test_records.products_api.create_products_v2(create_product_request)
    await upload_test_records.connect_api.close()
    print(str(response))

if __name__ == "__main__":
    asyncio.run(main_async()) # start asynchronous loop (implicit in jupyter notebook)
    print("done")