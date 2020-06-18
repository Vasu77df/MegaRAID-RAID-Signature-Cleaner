#!/bin/bash

cd /opt/MegaRAID/MegaCli/

function clearing {
	if [ "$opt" = "y" ]||[ "$opt" = "Y" ]; then
	echo "Clearing RAID configuration of Disk in Slot: $slot_number"
        sleep 1 
	echo "Clearing Foreign Configuration......"
        ./MegaCli64 -CfgForeign -Clear -aALL
        sleep 1
	echo "Converting the Disk into JBOD mode....."
	echo $slot_number
        ./MegaCli64 -PDMakeJBOD -PhysDrv[64:$slot_number] -aALL
        sleep 1
        echo "----------------Done Clearing RAID Configuration---------------"
        sleep 1
	fi
}

echo "---------------------Welcome to RAID Cleaner-------------------"

echo "List of all available drives attached to the controller:"

./MegaCli64 -PDList -aALL | grep -i "enclosure device id\|slot number\|Drive's Position\|Device id\|Firmware state\|foreign state"

read -p "How many disks would you like to clear?: " -r nu_disks

for (( c=1; c<=$nu_disks; c++))
do
    read -p "You can clean the Foreign RAID configuration of the Disk by specifing the slot number(please enter the slot of disk one by one): " -r slot_number

    read -p "Are you sure you want to clear RAiD configuration in slot: $slot_number ?[y/n]: " -r opt

    clearing 

    if [ $c -lt $nu_disks ]; then
         echo "---------------------------Next Disk---------------------------"
    fi

done

"--------------------- Current Configuration--------------------"
./MegaCli64 -PDList -aALL | grep -i "enclosure device id\|slot number\|Drive's Position\|Device id\|Firmware state\|foreign state"

cd ~

echo "----------------------------Exiting----------------------------"
sleep 1
