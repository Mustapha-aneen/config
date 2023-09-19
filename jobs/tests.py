import django,os
from django.test import TestCase
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
from models import PostJob
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_django_project.settings')

django.setup()

# Create your tests here.
