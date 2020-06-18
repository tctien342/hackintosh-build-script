import urllib.request
import zipfile
import platform
import shutil
import os
import pathlib


def download_file(url, target):
    if os.path.exists(target):
        return target
    urllib.request.urlretrieve(url, target)
    return target


def download_file_extract_and_find(url, target=".", file_name=False, unzip=False):
    downloaded = download_file(
        url, "{}/{}".format(pathlib.Path(target).parent, os.path.basename(url)))
    if unzip is True:
        unzip_file(downloaded, target)
        if file_name is not False:
            find = pathlib.Path(target).rglob("**/{}*".format(file_name))
            for path in find:
                return path
    return downloaded


def zip_file(path, target):
    shutil.make_archive(target, 'zip', path)
    return True


def unzip_file(path_file, target):
    with zipfile.ZipFile(path_file, "r") as zip_ref:
        zip_ref.extractall(target)
        pass


def perm_exec(path_file):
    if platform.system() != "Windows":
        from os import system as sh
        sh("chmod a+x {}".format(path_file))
    return True


def convert_dsl_to_aml(iasl_path, target=""):
    from os import system as sh
    sh("{} -oa {}".format(iasl_path, target))
    return str(target).replace(".dsl", ".aml")
