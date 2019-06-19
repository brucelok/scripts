#!/usr/bin/python
'''
description: basic CRUD operation of S3 storage
author: lok.bruce@gmail.com
'''
import os
from minio import Minio
from minio.error import ResponseError

bucket_name = 'test101'

client = Minio('your-s3-endpoint.com',
               access_key='xxxxxxxxxxxxxx',
               secret_key='xxxxxxxxxxxxxx',
               secure=True)

print("\n=== check if bucket '%s' exists ===" %bucket_name)
try:
    print(client.bucket_exists(bucket_name))
    print('\n=== check bucket info ===')
    print(client.get_bucket_policy(bucket_name))
except ResponseError as err:
    raise
    print(err)
    sys.exit(1)

print("\n=== list all buckets '%s' ===" %bucket_name)
buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

print("\n=== put object to buckets '%s' ===" %bucket_name)
try:
    client.fput_object(bucket_name,
                       'test1.csv',
                       'test1.csv',
                       content_type='application/csv')
except ResponseError as err:
    print(err)

print("\n=== list objects ===")
objects = client.list_objects_v2(bucket_name, recursive=True)
for obj in objects:
	print(obj.object_name, obj.size)
