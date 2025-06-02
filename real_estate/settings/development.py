from .base import *
import environ
from pathlib import Path

# Initialize environment variables
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()  # Load .env file

# Development settings for the Real Estate project
DATABASES = {
    'default': {
        'ENGINE':env('POSTGRES_ENGINE') ,
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),   
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}