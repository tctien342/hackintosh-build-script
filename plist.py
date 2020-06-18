import plistlib
import config
import pathlib
from base64 import b64decode
import log


class Plist:
    """Handle Hackintosh's config plist file, support Opencore and Clover
    """

    def __init__(self, file: str):
        self.file = pathlib.Path(file).absolute()
        with open(file, 'rb') as f:
            self.plist = plistlib.load(f)
        if 'Boot' in self.plist:  # clover
            self.type = 'clover'
            self.keywords = config.conf["clover_dict"]
        else:
            self.type = 'oc'
            self.keywords = config.conf["opencore_dict"]
        log.title("Init {} plist file".format(self.type))

    def save(self):
        """Save current config to config file
        """
        with open(self.file, 'wb') as f:
            plistlib.dump(self.plist, f)

    def get_keyword_path(self, key: str):
        """Get config path by keyword of current config file

        Args:
            key (str): Keyword of path

        Returns:
            str: config path of current config plist
        """
        return self.keywords.get(key, key)

    @staticmethod
    def data(b64str: str):
        """Convert string to data string

        Args:
            b64str (str): string of config need to be convert

        Returns:
            str: data string to be placed in plist
        """
        return b64decode(b64str)

    def get_key_value(self, key: str, value=False):
        """Get value by given keyword

        Args:
            key (str): keyword of config that need to take data
            value (bool, optional): Out put item and value. Defaults to False.

        Returns:
            str or (item, key): out put value of current config plist file
        """
        key_paths = self.get_keyword_path(key).split(">")
        item = self.plist
        for key_path in key_paths[:-1]:
            item = item[key_path]
        return item[key_paths[-1]] if value else (item, key_paths[-1])

    def set_key_value(self, key: str, value: str):
        """Set keyword's value in config plist 

        Args:
            key (str): keyword of config
            value (str): value to be stored
        """
        item, key = self.get_key_value(key)
        if type(item[key]) is bytes:
            if type(value) is not bytes:
                value = Plist.data(value)
            else:
                value = type(item[key])(value)
        item[key] = value

    def copy(self, another):
        """Copy config from an another config plist file

        Args:
            another (Plist): An Plist file

        Returns:
            Plist: return current config file
        """
        if self.type == another.type:
            log.title('Replace everything from',
                      another.file, '\nExcept:')
            for key in self.keywords.values():
                value = self.get_key_value(key, True)
                another.set(key, value)
                print('{}={}'.format(key, value))
            self.plist = another.plist
        else:
            log.title('Replace following fields from', another.file)
            for k in self.keywords.keys():
                i1, k1 = self.get_key_value(self.keywords[k])
                value = another.get(another.keywords[k])
                print('Set {} to {}'.format(k1, value))
                i1[k1] = value
        return self
