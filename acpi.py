import config
import platform
import tools
import os
import pathlib
import shutil
import log


def download_iasl(target: str) -> str:
    return tools.download_file_extract_and_find(
        config.conf["iasl"][platform.system()], target, "iasl", True)


def convert_and_get_patches(iasl_path: str, conf_folder: str, target_folder: str) -> []:
    patches = []
    if os.path.exists("{}/acpi".format(conf_folder)):
        for dsl in pathlib.Path("{}/acpi".format(conf_folder)).rglob("*.dsl"):
            tools.convert_dsl_to_aml(iasl_path, dsl)
            patches = patches + tools.dsl_to_patch_list(dsl)
        for aml in pathlib.Path("{}/acpi".format(conf_folder)).rglob("*.aml"):
            shutil.move(
                aml, "{}/acpi/{}".format(target_folder, os.path.basename(aml)))
        log.title("Convert DSL to AML done.")
        log.title("Found {} patches.".format(len(patches)))
        for patch in patches:
            log.sub(patch["Comment"])
    return patches
