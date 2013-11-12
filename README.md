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

You'll also need to provide an uploader/static/ subdirectory (css/ and js/) with the FineUploader code.
(I'm not sure I can redistribute it here - though under the GPL maybe yes?)

Here's the contents of my static/ subdir:

```
(uploader.env)ciaron@tangerine:~/djangofine/uploader$ ls -lR static
total 0
drwxr-xr-x  7 ciaron  staff  238 Nov 12 22:56 css
drwxr-xr-x  5 ciaron  staff  170 Nov 12 22:56 js

static/css:
total 32
-rw-r--r--  1 ciaron  staff   145 Nov 12 22:48 edit.gif
-rw-r--r--  1 ciaron  staff  3796 Nov 12 22:48 fineuploader-4.0.3.min.css
-rw-r--r--  1 ciaron  staff  1688 Nov 12 22:48 loading.gif
-rw-r--r--  1 ciaron  staff  3209 Nov 12 22:48 processing.gif
-rw-r--r--  1 ciaron  staff     0 Nov 12 22:50 style.css

static/js:
total 424
-rw-r--r--  1 ciaron  staff     144 Nov 12 22:48 iframe.xss.response-4.0.3.js
-rw-r--r--  1 ciaron  staff   96936 Nov 12 22:48 jquery.fineuploader-4.0.3.min.js
-rw-r--r--  1 ciaron  staff  113317 Nov 12 22:48 s3.jquery.fineuploader-4.0.3.min.js
```
