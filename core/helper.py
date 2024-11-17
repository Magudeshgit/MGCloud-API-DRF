import boto3
from botocore.client import Config
import hashlib

# VITE_CLOUD_API_ENDPOINT = https://208d0f24df52505b5e34ad8d4adaf567.r2.cloudflarestorage.com
# VITE_ACCESS_KEY_ID = 04404223c42f65e58706deeae5df73f4
# VITE_SECRET_KEY = 19df6177a769498f2517f257a2367529001f6d4e6333f245f9e0641d5cbfdc12
# sk = hashlib.sha256("19df6177a769498f2517f257a2367529001f6d4e6333f245f9e0641d5cbfdc12".encode()).hexdigest()
sk="19df6177a769498f2517f257a2367529001f6d4e6333f245f9e0641d5cbfdc12"

s3_client = boto3.client(
    's3',
   endpoint_url=f'https://{"208d0f24df52505b5e34ad8d4adaf567"}.r2.cloudflarestorage.com',
   aws_access_key_id="04404223c42f65e58706deeae5df73f4",
   aws_secret_access_key=sk,
   config=Config(signature_version='v4', region_name='auto'),
)

def UploadPresignedUrl(filename):
    url=s3_client.generate_presigned_url('put_object', 
                                       Params=
                                       {
                                           "Bucket":"mgcloud", 
                                           "Key": filename,
                                        }, 
                                       ExpiresIn=3600)
    return url

def getFileURLForPreview(filename):
    url = s3_client.generate_presigned_url('get_object',
                                           Params=
                                           {
                                               "Bucket": "mgcloud",
                                               "Key": filename,
                                           },
                                           ExpiresIn=3600
                                           )
    return url


def getFileURLForDownload(filename):
    url = s3_client.generate_presigned_url('get_object',
                                           Params=
                                           {
                                               "Bucket": "mgcloud",
                                               "Key": filename,
                                               "ResponseContentDisposition": f'attachment; filename="{filename}"'
                                           },
                                           )
    return url