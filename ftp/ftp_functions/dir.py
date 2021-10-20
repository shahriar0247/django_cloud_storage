import os

from ftp.ftp_functions.settings import FTP_HOME


def load_dir(dir_path):
    output = os.listdir(os.path.join(FTP_HOME, dir_path))
    return (output)