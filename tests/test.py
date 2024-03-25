import os

from object_storage.object_storage import ObjectStorage

bucket = 'nnsay-cn'
provider = os.environ.get('OBJECT_STORAGE_PROVIDER', 'S3')
config = {
  'access_key_id': os.environ.get('OBJECT_STORAGE_AK'),
  'access_key_secret': os.environ.get('OBJECT_STORAGE_SK'),
  'region': os.environ.get('OBJECT_STORAGE_REGION'),
  'endpoint': os.environ.get('OBJECT_STORAGE_ENDPOINT'),
}
object_storage = ObjectStorage(provider, config)

# 上传操作

etag = object_storage.put_object(bucket, 'hello.log', 'hello world')
print(f'etag: {etag}')

# 下载操作
object_storage.download_file('download-hello-minio.log', bucket, 'hello.log')

# 获取对象
bytes = object_storage.get_object(bucket, 'hello.log')
data = bytes.decode('utf-8')
print(f'get data: {data}')

# 获取下载地址
url = object_storage.get_object_signed_url(bucket, 'hello.log')
print(f'download signed url: {url}')
