conf = {
    "iasl": {
        "Darwin": "https://bitbucket.org/RehabMan/acpica/downloads/iasl.zip",
        "Windows": "https://acpica.org/sites/acpica/files/iasl-win-20180105.zip",
        "Linux": "http://amdosx.kellynet.nl/iasl.zip"
    },
    "clover_dict": dict(
        sn='SMBIOS>SerialNumber',
        mlb='SMBIOS>BoardSerialNumber',
        smuuid='SMBIOS>SmUUID',
        uiscale='BootGraphics>UIScale',
        bootarg='Boot>Arguments',
        timeout='Boot>Timeout',
        defaultvolume='Boot>DefaultVolume',
        layoutid='Devices>Properties>PciRoot(0x0)/Pci(0x1f,0x3)>layout-id',
        deviceproperties='Devices>Properties'
    ),
    "opencore_dict": dict(
        sn='PlatformInfo>Generic>SystemSerialNumber',
        mlb='PlatformInfo>Generic>MLB',
        smuuid='PlatformInfo>Generic>SystemUUID',
        uiscale='NVRAM>Add>4D1EDE05-38C7-4A6A-9CC6-4BCCA8B38C14>UIScale',
        bootarg='NVRAM>Add>7C436110-AB2A-4BBB-A880-FE41995C9F82>boot-args',
        timeout='Misc>Boot>Timeout',
        defaultvolume='NVRAM>Add>7C436110-AB2A-4BBB-A880-FE41995C9F82>SystemAudioVolume',
        layoutid='DeviceProperties>Add>PciRoot(0x0)/Pci(0x1f,0x3)>layout-id',
        deviceproperties='DeviceProperties>Add'
    )
}
 