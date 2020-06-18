import urllib.request
import zipfile
import platform
import shutil
import os
import pathlib


def download_file(url: str, target: str):
    """Download file from url and store to target file

    Args:
        url (str): Url of file that need to be downloaded
        target (str): save's path

    Returns:
        str: save's path
    """
    if os.path.exists(target):
        return target
    urllib.request.urlretrieve(url, target)
    return target


def download_file_extract_and_find(url: str, target: str = ".", file_name: str or bool = False, unzip: bool = True):
    """Download file then extract and return path of file name

    Args:
        url (str): url of file that need to be download`
        target (str, optional): save's path of file. Defaults to ".".
        file_name (str, optional): file name that need to be found and return its path. Defaults to False.
        unzip (bool, optional): uzip downloaded file. Defaults to False.

    Returns:
        str: path of file that downloaded or found in downloaded folder
    """
    downloaded = download_file(
        url, "{}/{}".format(pathlib.Path(target).parent, os.path.basename(url)))
    if unzip is True:
        unzip_file(downloaded, target)
        if file_name is not False:
            find = pathlib.Path(target).rglob("**/{}*".format(file_name))
            for path in find:
                return path
    return downloaded


def zip_file(path: str, target: str):
    """Zip and folder and output to target path

    Args:
        path (str): path of folder that need to be zipped
        target (str): target output file

    Returns:
        bool: return True
    """
    shutil.make_archive(target, 'zip', path)
    return True


def unzip_file(path_file: str, target: str):
    """Unzip an file to target path

    Args:
        path_file (str): path of file need to be unzipped
        target (str): target path output
    """
    with zipfile.ZipFile(path_file, "r") as zip_ref:
        zip_ref.extractall(target)
        pass


def perm_exec(path_file: str) -> bool:
    """Add exec permission to given path

    Args:
        path_file (str): file that need exec permission

    Returns:
        bool: return True
    """
    if platform.system() != "Windows":
        from os import system as sh
        sh("chmod a+x {}".format(path_file))
    return True


def convert_dsl_to_aml(iasl_path: str, target: str = "") -> str:
    """Convert dsl file to aml

    Args:
        iasl_path (str): iasl excec path
        target (str, optional): Path of dsl file need to be converted. Defaults to "".

    Returns:
        str: output aml path file
    """
    from os import system as sh
    sh("{} -oa {}".format(iasl_path, target))
    return str(target).replace(".dsl", ".aml")


def dsl_to_patch_list(dsl_path: str) -> []:
    """Get array of patch from dsl file, your dsl file need to declear patch inside of it
    \n Sample of an path in dsl file
    \n// Patch: Rename _WAK to ZWAK
    \n// Find: FDlfV0FLAQ==
    \n// Replace: FDlaV0FLAQ==

    Args:
        dsl_path (str): dsl path need to be extract

    Returns:
        (Comment:str, Find: str, Replace: str)[]:  Array of patch
    """
    patches = []
    with open(dsl_path, 'r') as f:
        while True:
            line = f.readline()
            if line.startswith('// Patch:'):
                patches.append({
                    'Comment': line[9:].strip(),
                    'Find': f.readline()[8:].strip(),
                    'Replace': f.readline()[11:].strip()
                })
            elif not line:
                break
    return patches
