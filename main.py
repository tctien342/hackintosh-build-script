import os
import tools
import config
import platform
import pathlib
import shutil

# Init project
tmp_folder = './.tmp'
conf_folder = './config'
exec_file = {
    "iasl": ""
}
if os.path.exists(tmp_folder) is False:
    os.mkdir(tmp_folder)
    os.mkdir("{}/acpi".format(tmp_folder))
    os.mkdir("{}/kexts".format(tmp_folder))

# IASL for DSL files process
exec_file['iasl'] = tools.download_file_extract_and_find(
    config.conf["iasl"][platform.system()], "{}/iasl".format(tmp_folder), "iasl", True)
tools.perm_exec(exec_file['iasl'])

# Convert all dsl to aml
if os.path.exists("{}/acpi".format(conf_folder)):
    for dsl in pathlib.Path("{}/acpi".format(conf_folder)).rglob("*.dsl"):
        tools.convert_dsl_to_aml(exec_file["iasl"], dsl)
    for aml in pathlib.Path("{}/acpi".format(conf_folder)).rglob("*.aml"):
        shutil.move(aml, "{}/acpi/{}".format(tmp_folder, os.path.basename(aml)))
