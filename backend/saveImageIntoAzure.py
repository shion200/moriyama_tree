from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from PIL import Image
import io
import os
import base64

def saveImageIntoAzure(img, imageName):
    os.environ["AZURE_STORAGE_CONNECTION_STRING"] = "DefaultEndpointsProtocol=https;AccountName=myblobstorage434606520;AccountKey=YOUR_ACCOUNT_KEY;EndpointSuffix=core.windows.net"
    # Azure Storageアカウントの接続文字列
    connection_string = base64.b64encode(os.environ.get("AZURE_STORAGE_CONNECTION_STRING")).decode()
    print(connection_string)
    # Blobコンテナ名
    container_name = "myblobstorage434606520"

    # Blob Storageのクライアントを作成
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    # 画像ファイルのBlobに対する名前を取得（ファイル名をそのまま使用する例）
    blob_name = imageName

    # 画像をバイナリデータに変換
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")  # 保存するフォーマットに応じて変更
    # バイナリデータを取得
    image_binary = buffer.getvalue()


    # Blobに画像をアップロード
    container_client.upload_blob(name=blob_name, data=image_binary)

    print(f"Image uploaded to Blob Storage. Blob URL: {container_client.url}/{blob_name}")
