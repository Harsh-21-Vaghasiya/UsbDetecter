from asyncio import sleep
import json
import subprocess
from dataclasses import dataclass
from typing import Callable, List

# ! continuels run this program
# subprocess.Popen(["python", "new.py"], stdout=subprocess.PIPE)


def list_drives():
    proc = subprocess.run(
        args=[
            'powershell',
            '-noprofile',
            '-command',
            'Get-WmiObject -Class Win32_LogicalDisk | Select-Object deviceid,volumename,drivetype | ConvertTo-Json'
        ],
        text=True,
        stdout=subprocess.PIPE
    )
#  Get-pnpDevice -Class USB |  Where-Object { $_.InstanceId -match '^USB' } | Select-object FriendlyName  |ConvertTo-Json



    drive_types = {
        0: 'Unknown',
        1: 'No Root Directory',
        2: 'Removable Disk',
        3: 'Local Disk',
        4: 'Network Drive',
        5: 'Compact Disc',
        6: 'RAM Disk',
    }

    devices = json.loads(proc.stdout)
    for d in devices:
        print("Drive_Letter :- {0} Drive_name :- {1} Drive_Type :- {2}".format(
            d['deviceid'], d['volumename'], drive_types[d['drivetype']]), sep='\n')


if __name__ == '__main__':
    list_drives()
