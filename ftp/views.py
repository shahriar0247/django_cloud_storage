from django.shortcuts import render
from ftp.ftp_functions.dir import load_dir

def load_dir_req(request, path=''):
    all_files = load_dir(path)
    jinja_vars = {'all_files': all_files}
    return render(request, 'path/dir.html', jinja_vars)