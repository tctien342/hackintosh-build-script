import os
import tools
import config
import platform
import pathlib
import shutil
import log
import acpi
import plist

# Init project
tmp_folder = './.tmp'
conf_folder = './config'
patches = []
exec_file = {
    "iasl": ""
}


def init_project():
    # Int tmp folder
    log.title("Checking project...")
    if os.path.exists(tmp_folder) is False:
        log.sub("New project, create tmp folder...")
        os.mkdir(tmp_folder)
        os.mkdir("{}/acpi".format(tmp_folder))
        os.mkdir("{}/kexts".format(tmp_folder))
        os.mkdir("{}/oc".format(tmp_folder))
        os.mkdir("{}/clover".format(tmp_folder))
        shutil.copy("{}/opencore/config.plist".format(conf_folder),
                    "{}/oc/config.plist".format(tmp_folder))
        shutil.copy("{}/clover/config.plist".format(conf_folder),
                    "{}/clover/config.plist".format(tmp_folder))
    else:
        log.sub("Found project, bypass init project")


def update_acpi():
    log.title("Updating acpi folder...")
    # IASL for DSL files process
    exec_file['iasl'] = acpi.download_iasl("{}/iasl".format(tmp_folder))
    tools.perm_exec(exec_file['iasl'])
    # Convert all dsl to aml
    patches = acpi.convert_and_get_patches(
        exec_file["iasl"], conf_folder, tmp_folder)


if __name__ == "__main__":
    init_project()
    update_acpi()
    print(plist.Plist('./.tmp/oc/config.plist').get_key_value("layoutid"))
    pass
