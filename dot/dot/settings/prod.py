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
