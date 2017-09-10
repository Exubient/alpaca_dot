from .common import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'HOST': "dot-master.cy0xy47wyrc6.ap-northeast-2.rds.amazonaws.com",
        "PORT": "5432",
        "USER": "master",
        "PASSWORD": load_credential("DB_PASSWORD"),
        "NAME": "dot_production",
    }
}


## AWS S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = load_credential("AWS_ACCESS_KEY_ID")  # access key
AWS_SECRET_ACCESS_KEY = load_credential("AWS_SECRET_ACCESS_KEY")  # secret access key
AWS_REGION = 'ap-northeast-2' ## Seoul Region
AWS_STORAGE_BUCKET_NAME = 'alpaca-dot'  # AWS S3 버켓 이름
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_S3_SECURE_URLS = False ## https
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "http://%s/" % AWS_S3_CUSTOM_DOMAIN

