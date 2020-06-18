// Disable discrete GPU
// Patch: Rename _WAK to ZWAK
// Find: FDlfV0FLAQ==
// Replace: FDlaV0FLAQ==
// Patch: Rename _PTS to ZPTS
// Find: FEkEX1BUUwE=
// Replace: FEkEWlBUUwE=
// Reference:
// [1] https://github.com/RehabMan/OS-X-Clover-Laptop-Config/blob/master/hotpatch/SSDT-DDGPU.dsl
// [2] https://github.com/RehabMan/OS-X-Clover-Laptop-Config/blob/master/hotpatch/SSDT-PTSWAK.dsl
DefinitionBlock ("", "SSDT", 2, "hack", "DGPU", 0x00000000)
{
    External (_SB_.PCI0.PEG0.PEGP._OFF, MethodObj)    // 0 Arguments (from opcode)
    External (_SB_.PCI0.PEG0.PEGP._ON_, MethodObj)
    External (_SB_.PCI0.PEG0.PG00._OFF, MethodObj)    // 0 Arguments (from opcode)
    External (_SB_.PCI0.PGOF, MethodObj)
    External (EXT4, MethodObj)    // 1 Arguments (from opcode)
    External (ZWAK, MethodObj)    // 1 Arguments (from opcode)
    External (ZPTS, MethodObj)     // 1 Arguments (from opcode)

    Method (DGPU, 0, NotSerialized)
    {
        If (CondRefOf (\_SB.PCI0.PEG0.PEGP._OFF))
        {
            \_SB.PCI0.PEG0.PEGP._OFF ()
        }
        If (CondRefOf (\_SB.PCI0.PEG0.PG00._OFF))
        {
            \_SB.PCI0.PEG0.PG00._OFF ()
        }
        If (CondRefOf (\_SB_.PCI0.PGOF))
        {
            \_SB.PCI0.PGOF ()
        }
    }

    Device (RMD1)
    {
        Name (_HID, "RMD10000")  // _HID: Hardware ID
        Method (_INI, 0, NotSerialized)  // _INI: Initialize
        {
            If (_OSI ("Darwin"))
            {
                DGPU ()
            }
        }

        Method (_STA, 0, NotSerialized)  // _STA: Status
        {
            If (_OSI ("Darwin"))
            {
                Return (0x0F)
            }

            Return (Zero)
        }
    }

    Method (_WAK, 1, NotSerialized)  // _WAK: Wake
    {
        Store (ZWAK (Arg0), Local0)
        If (_OSI ("Darwin"))
        {
            If (CondRefOf (EXT4))
            {
                EXT4 (Arg0)
            }

            DGPU ()
        }

        Return (Local0)
    }

    Method (_PTS, 1, NotSerialized) // _PTS: Sleep
    {
        If (_OSI ("Darwin"))
        {
            \_SB.PCI0.PEG0.PEGP._ON ()
        }
        ZPTS(Arg0)
    }
}

