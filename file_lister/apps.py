from __future__ import unicode_literals

from django.apps import AppConfig

class FileListerConfig(AppConfig):
    name = 'file_lister'

    file_root = '/var/www/files'
