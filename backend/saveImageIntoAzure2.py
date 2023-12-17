from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, generate_blob_sas, BlobSasPermissions, ContentSettings
from azure.storage.blob._shared.base_client import create_configuration
import requests
from datetime import datetime, timedelta
#from azure.storage.common import SharedAccessSignature, CloudStorageAccount


def uploadFileToStorage(file_stream, file_name, storage_config):
    # Create a BlobServiceClient
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_config['AccountName']};AccountKey={storage_config['AccountKey']};EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Create a ContainerClient
    container_client = blob_service_client.get_container_client(storage_config['ImageContainer'])

    # 画像のContent-Typeを指定します
    image_content_setting = ContentSettings(content_type='image/png')

    # Upload the file
    blob_name = file_name
    blob_client = container_client.get_blob_client(blob_name)
    # blob_client.upload_blob(file_stream)
    # 画像ファイルをアップロードします
    blob_client.upload_blob(file_stream, overwrite=True, content_settings=image_content_setting, timeout = 600)

    return True

def get_authorization_header(account_name, container_name, account_key, now, request, blob_name = None):
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
    # Implement the logic for generating Azure Storage authorization header
    # You may need to use the Azure SDK or other libraries to handle this.

    # Example: Using Azure SDK for Python (azure-storage-blob)
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)


    sas_token = generate_blob_sas(
        blob_client.account_name,
        container_name,
        blob_name,
        account_key=blob_service_client.credential.account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=1),
    )

    authorization_header = {'Authorization': f'Bearer {sas_token}'}
    return authorization_header

def saveImageIntoAzure2(imageName):
    # Example usage
    storage_config = {
        "AccountName": "myblobstorage434606520",
        "AccountKey": "GXRpqI3JZThlyqzb9KqlACDukO/lL4DssvR67PIqVM8soWIP/qKOzGc2U6F+XH5lvTaJBtCIMHwk+AStiirkJg==",
        "ImageContainer": "thumbnails",
        "BlobName": "Ikeojidrinkingbeer.png"
    }

    file_stream = open("./createdImage/"+imageName, "rb")
    now = datetime.utcnow()
    # Assuming httpRequestMessage is a requests.Request object
    http_request_message = requests.Request('GET', 'https://'+storage_config['AccountName']+'.blob.core.windows.net/'+storage_config['ImageContainer']+'/'+storage_config['BlobName'])
    headers = get_authorization_header(storage_config['AccountName'], storage_config['ImageContainer'], storage_config['AccountKey'], now, http_request_message, storage_config['BlobName'])

    # Add the generated Authorization header to the request
    http_request_message.headers.update(headers)

    # Now, you can use the updated request for making a request to Azure Storage
    response = requests.Session().send(http_request_message.prepare())
    
    uploadFileToStorage(file_stream, imageName, storage_config)

    url="https://"+storage_config['AccountName']+".blob.core.windows.net/"+storage_config['ImageContainer']+"/"+imageName
    return(url)
