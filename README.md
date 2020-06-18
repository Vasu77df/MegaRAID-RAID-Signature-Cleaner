# MegaRAID-RAID-Signature-Cleaner
Script to clear RAID Signature using MegaCli Bash Tool

## RAID Signature Clearer Setup

This is a guide to create and a setup a server to erase RAID Signature of old drives using the MegaRAID controller's MegaCli Command Line tool or using the script developed for easier operation. 

### Installing Centos 6

IBM System X3550 M2 are installed with ServeRAID 1015 RAID Controllers this Hardware RAID Controller is only detected and supported in Centos 6 and Centos 7. They are not supported in Centos 8 and above. 

#### Flashing USB Drive with Centos 6 

First Centos 6 ISO has to bee flashed on an USB for us to install it onto or RAID Clearer Server. 

*_Rufus_* is an utility that helps format and create bootable USB flash drives. This can be installed [here](https://rufus.ie/)

*_Centos 6_* can be downloaded from [here](https://wiki.centos.org/Download)

Now create a bootable drive using *_Rufus_*. 