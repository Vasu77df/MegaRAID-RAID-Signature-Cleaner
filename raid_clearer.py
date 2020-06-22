#!/usr/bin/python3
from time import sleep
import subprocess as sb

def clearing(slot_number):
    ''' This function cleares the RAID Signature of Disk and changing 
    the disk into a JBOD by accepting the slot number as an argument
    Arg: slot_number (integer)'''
    
    print("Clearing the RAID Signature of Disk in Slot:{}".format(slot_number))
    sleep(1)
    print("Clearing Foreign Configuration.......")
    foreign_clear = './MegaCli64 -CfgForeign -Clear -aALL'
    sb.run(foreign_clear, shell=True, stdout=sb.PIPE, stderr=sb.STDOUT, cwd='/opt/MegaRAID/MegaCli/')
    sleep(1)
    print("Converting the Disk into JBOD mode......")
    change_JBOD = './MegaCli64 -PDMakeJBOD -PhysDrv[64:$slot_number] -aALL'
    sb.run(change_JBOD, shell=True, stdout=sb.PIPE, stderr=sb.STDOUT, cwd='/opt/MegaRAID/MegaCli/')
    sleep(1)
    print("----------------Done Clearing RAID Configuration---------------")
    sleep(1)

def get_confirmation( slot_number):
    dec = input("Are you sure you want to clear RAID Signature in slot: {} ? [y/n]:".format(slot_number))
    if dec in('y', 'yes', 'Y', 'Yes'):
        clearing
    elif dec in('n', 'N', 'No', 'no'):
        break
    else:
        input("Please enter 'y' or 'n: " )


if __name__=='__main__':
    print("---------------------Welcome to RAID Cleaner-------------------")
    
    print("List of all the available Disk attached to the controller:")
    list_disks = './MegaCli64 -PDList -aALL | grep -i "enclosure device id\|slot number\|Drive's Position\|Device id\|Firmware state\|foreign state"'
    l_disks = sb.run(list_disks, shell=True, stdout=sb.PIPE, stderr=sb.STDOUT, cwd='/opt/MegaRAID/MegaCli/')
    print(l_disks)
    
    nu_disks = int(input("How many disks would you like to clear?: "))

    if nu_disks 
