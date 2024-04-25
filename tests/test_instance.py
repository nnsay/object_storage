from object_storage.object_storage import ObjectStorage


def test_s3():
  client = ObjectStorage('S3', {})
  assert client.client is not None


def test_minio():
  client = ObjectStorage(
    'MINO',
    {
      'access_key_id': 'ak',
      'access_key_secret': 'sk',
      'endpoint': 'http://localhost:9100',
    },
  )
  assert client.client is not None


def test_oss():
  client = ObjectStorage(
    'OSS',
    {'access_key_id': 'ak', 'access_key_secret': 'sk', 'region': 'oss-cn-hangzhou'},
  )
  assert client.client is not None
