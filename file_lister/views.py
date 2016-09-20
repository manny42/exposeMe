import os, zipfile, mimetypes

from django.http import HttpResponseServerError, StreamingHttpResponse
from django.shortcuts import render
from wsgiref.util import FileWrapper
from .apps import FileListerConfig


# Create your views here.

class ZipStreamingHttpResponse(StreamingHttpResponse):
    def __init__(self, file, path, *args, **kwargs):
        super(ZipStreamingHttpResponse, self).__init__(file, *args, **kwargs)
        self._zip_path = path

    def _delete_zip_file(self):
        if zipfile.is_zipfile(self._zip_path):
            os.remove(self._zip_path)

    def close(self):
        super(ZipStreamingHttpResponse, self).close()
        self._delete_zip_file()


class FileLister:
    @staticmethod
    def zip_dir(path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                absfn = os.path.join(root, file)
                zfn = absfn[len(path) + len(os.sep):]
                ziph.write(absfn, zfn)

    @staticmethod
    def _generate_file_response(stream, file, size):
        filename = os.path.basename(file)
        chunk_size = 8192
        response = StreamingHttpResponse(FileWrapper(stream, chunk_size),
                                         content_type=mimetypes.guess_type(file)[0])
        response['Content-Length'] = size
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response

    @staticmethod
    def zip_file_download(request):
        path = os.path.dirname(os.path.abspath(__file__))
        myfiles = os.path.join(path, FileListerConfig.file_root)
        os.chdir(myfiles)
        path = request.GET.get('path', '').replace('../', '')
        if path[0] != '.':
            HttpResponseServerError("Server Error")
        else:
            zip_filename = "{}.zip".format(os.path.basename(path))
            zip_path = os.path.join('/tmp', zip_filename)
            zf = zipfile.ZipFile(zip_path, "w")
            FileLister.zipdir(path, zf)
            zf.close()
            size = os.path.getsize(zip_path)
            chunk_size = 8192
            response = ZipStreamingHttpResponse(FileWrapper(open(zip_path, 'rb'), chunk_size),
                                                zip_path,
                                                content_type="application/zip")
            response['Content-Length'] = size
            response['Content-Disposition'] = "attachment; filename=%s" % zip_filename
            return response

    @staticmethod
    def file_download(request):
        path = os.path.dirname(os.path.abspath(__file__))
        myfiles = os.path.join(path, FileListerConfig.file_root)
        os.chdir(myfiles)
        path = request.GET.get('path', '').replace('../', '')
        if path[0] != '.':
            HttpResponseServerError("Server Error")
        else:
            size = os.path.getsize(path)
            return FileLister._generate_file_response(open(path, "rb"), path, size)

    @staticmethod
    def _recursive_directory_search(directory='.'):
        result_list = []
        for file in os.listdir(directory):
            print(os.path.join(directory, file))
            try:
                os.path.join(directory, file).encode('utf-8', 'strict')
                if os.path.isdir(os.path.join(directory, file)):
                    result_list.append({
                        "type": "D",
                        "name": file,
                        "path": os.path.join(directory, file),
                        "files": FileLister._recursive_directory_search(os.path.join(directory, file))
                    })
                else:
                    result_list.append({
                        "type": "F",
                        "path": os.path.join(directory, file),
                        "name": file
                    })
            except Exception as e:
                print(e)

        return result_list

    @staticmethod
    def file_listing(request):
        path = os.path.dirname(os.path.abspath(__file__))
        myfiles = os.path.join(path, FileListerConfig.file_root)
        os.chdir(myfiles)
        file_listing = FileLister._recursive_directory_search()
        context = {
            "files": file_listing
        }
        return render(request, 'file_lister/listing.html', context)
