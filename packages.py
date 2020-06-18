from urllib.request import urlopen, Request, urlretrieve
import tools
import os


def map_github_assets(asset):
    return dict(
        name = asset['name'],
    )


def call_github_api(author: str, repo: str, ver: str = 'latest', headers={}):
    if ver != 'latest':
        ver = 'tags/' + ver
    req = Request('https://api.github.com/repos/{}/{}/releases/{}'.format(author, repo, ver),
                  headers=headers)
    info = json.loads(urlopen(req).read())
    return dict(
        about=info['body'],
        assets=map(map_github_assets, info['assets']),
    )


def call_bitbucket_api(author: str, repo: str, ver: str = 'latest'):
    return "https://api.bitbucket.org/2.0/repositories/{}/{}/downloads".format(author, repo)


class Package:
    def __init__(self, path: str, url: str, name: str, about: str, ver: str, prefix: str = "*RELEASE", tmp_path: str = './.tmp'):
        self.info = {
            "path": path,
            "url": url,
            "name": name,
            "about": about,
            "ver": ver,
            "prefix": prefix
        }
        self.tmp = tmp_path

    def check_new_version(self):
        if os.path.exists("{}/{}")

    def get_package_info(self):

    def download_and_check(tmp_path: str = "./.tmp"):
