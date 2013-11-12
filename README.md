djangofine
==========

fine-upload example using Django (1.6)

There are two apps: uploader (at 127.0.0.1:8000) and s3uploader (at 127.0.0.1:8000/s3)

The S3 version expects to find the following environment variables:

```
  AWS_SERVER_PUBLIC_KEY (your Access Key ID)
  AWS_SERVER_SECRET_KEY (Your secret key)
  AWS_CLIENT_SECRET_KEY (Your secret key again)
```
