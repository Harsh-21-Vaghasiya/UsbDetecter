from asyncio import sleep
import json
import subprocess
from dataclasses import dataclass
from typing import Callable, List

# !Data Class function
# @dataclass
# class Drive:
#     letter: str
#     disk_name: str
#     drive_type: str


# @property
# def is_removable(self) -> bool:
#     return self.drive_type == 'Removable Disk'

# ! continuels run this program
# subprocess.Popen(["python", "new.py"], stdout=subprocess.PIPE)

# !  This is code for sencond method of run code continues
# def watch_drives(on_change: Callable[[List[Drive]], None], poll_interval: int = 1):
#     prev = None
#     while True:
#         drives = list_drives()#         if prev != drives:
#             on_change(drives)
#             prev = drives
#         sleep(poll_interval)


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

    # ? Powershell code to detect the all the usb devices
#  Get-pnpDevice -Class USB |  Where-Object { $_.InstanceId -match '^USB' } | Select-object FriendlyName  |ConvertTo-Json

    devices = json.loads(proc.stdout)

    return devices

# ? Return using dataclass
    # return [Drive(
    #     letter=d['deviceid'],
    #     disk_name=d['volumename'],
    #     drive_type=drive_types[d['drivetype']]
    # )for d in devices]


# Function to cheak new drives are inserted or not
def watch_drives():
    drive_types = {
        0: 'Unknown',
        1: 'No Root Directory',
        2: 'Removable Disk',
        3: 'Local Disk',
        4: 'Network Drive',
        5: 'Compact Disc',
        6: 'RAM Disk',
    }
    prev = None
    while True:
        drives = list_drives()

        if prev != drives:
            for d in drives:
                print("Drive_Letter :- {0} Drive_name :- {1} Drive_Type :- {2}".format(
                    d['deviceid'], d['volumename'], drive_types[d['drivetype']]), sep='\n')
            print('\n')    

        prev = drives


        # Main function
if __name__ == '__main__':
    # Calling the continues cheak function
    watch_drives()
