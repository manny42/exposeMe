from django.conf.urls import url

from .views import FileLister

app_name = 'file_lister'
urlpatterns = [
    url(r'^zip_file?', FileLister.zip_file_download, name='File Downloading'),
    url(r'^get_file?', FileLister.file_download, name='File Downloading'),
    url(r'^$', FileLister.file_listing, name='File listing'),
]