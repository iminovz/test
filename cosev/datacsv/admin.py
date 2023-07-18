from django.contrib import admin

from datacsv.models import CsvFile
from .models import Profile

admin.site.register(CsvFile)

admin.site.register(Profile)
