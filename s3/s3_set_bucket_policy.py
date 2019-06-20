#!/usr/bin/python
'''
description: sample code to set S3 bucket policy for a specify user
author: lok.bruce@gmail.com
'''
import os
from minio import Minio
from minio.error import ResponseError
import json

your_tenant = 'myTenant'
your_username = 'bruce'
bucket_name = 'test101'

client = Minio('your-s3-endpoint.com',
               access_key='xxxxxxxxxxxxxx',
               secret_key='xxxxxxxxxxxxxx',
               secure=True)

# the policy only allows user of tenant to list and get objects from bucket
policy_data = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ReadBucket",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{0}:user/{1}".format(your_tenant, your_username)
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::{0}/*".format(bucket_name),
                "arn:aws:s3:::{0}".format(bucket_name)
            ]
        }
    ]
}

try:
    print('### applying policy to bucket '%s' ###' %bucket_name)
    client.set_bucket_policy(bucket_name, json.dumps(policy_data))
except ResponseError as err:
    print(err)
    sys.exit(1)
