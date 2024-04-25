from io import StringIO

import boto3
from botocore.response import StreamingBody
from botocore.stub import Stubber

from object_storage.object_storage import ObjectStorage

client = boto3.client('s3')
stubber = Stubber(client)


def test_get_object():
  string_data = 'helle world'
  bucket = 'nnsay-cn-ut'
  stubber.add_response(
    'get_object',
    {'Body': StreamingBody(StringIO(str(string_data)), len(str(string_data)))},
    {'Bucket': bucket, 'Key': 'hello.log'},
  )
  stubber.activate()
  object_storage = ObjectStorage(
    'MINIO',
    {
      'access_key_id': 'x01paW1tNk9pbim9VH2D',
      'access_key_secret': 'D76Xc3aJ1yVrTcYPVkm6pOnAclBcCXo7YgRIcFlK',
      'endpoint': 'http://localhost:9000',
    },
  )
  object_storage.client = client
  result = object_storage.get_object(bucket, 'hello.log')
  assert str(result) == string_data


def test_put_object():
  string_data = 'helle world'
  bucket = 'nnsay-cn-ut'
  stubber.add_response(
    'put_object',
    {'ETag': 'aabbccdd'},
    {'Bucket': bucket, 'Key': 'hello.log', 'Body': string_data},
  )
  stubber.activate()
  object_storage = ObjectStorage(
    'MINIO',
    {
      'access_key_id': 'x01paW1tNk9pbim9VH2D',
      'access_key_secret': 'D76Xc3aJ1yVrTcYPVkm6pOnAclBcCXo7YgRIcFlK',
      'endpoint': 'http://localhost:9000',
    },
  )
  object_storage.client = client
  result = object_storage.put_object(bucket, 'hello.log', string_data)
  assert str(result) == 'aabbccdd'
