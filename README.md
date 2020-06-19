# MegaRAID-RAID-Signature-Cleaner

Script to clear RAID Signature using MegaCli Bash Tool

## RAID Signature Clearer Setup

This is a guide to create and a setup a server to erase RAID Signature of old drives using the MegaRAID controller's MegaCli Command Line tool or using the script developed for easier operation.

### Installing Centos 6

---------------------------------
IBM System X3550 M2 are installed with ServeRAID 1015 RAID Controllers this Hardware RAID Controller is only detected and supported in Centos 6 and Centos 7. They are not supported in Centos 8 and above.

#### Flashing USB Drive with Centos 6

----------------------------------- 
First Centos 6 ISO has to bee flashed on an USB for us to install it onto or RAID Clearer Server. Use your workstation to complete this process.

- **Rufus** is an utility that helps format and create bootable USB flash drives. This can be downloaded from [here](https://rufus.ie/)

- **Centos 6** can be downloaded from [here](https://wiki.centos.org/Download)

Now create a bootable drive using **Rufus**.

![rufus setup](https://github.com/Vasu77df/MegaRAID-RAID-Signature-Cleaner/blob/master/images/rufus.png)

#### Installation and Setting up the Centos Environment for running the utility

----------------------------------------------

- Plug in the usb Drive to the server and enter the BIOS to choose the USB drive as boot drive.

- Run through the installer as directed and setup your login credentials

- The username after intial installation is _root_ and the password is the credentials you have setup during installation

##### Downloading prerequistes and packages

For our utility to run certain prerequistes have to be installed and configured.

The **MegaCli** command line tool has to be downloaded and installed. This can be downloaded [here](https://www.broadcom.com/support/download-search?dk=megacli)

- Use your workstation to download this package and copy the _zip_ file to a USB Drive

![megacli download page](https://github.com/Vasu77df/MegaRAID-RAID-Signature-Cleaner/blob/master/images/mega_cli_download_page.png)

- Insert the USB drive to the server and copy the _zip_ file using the following command to the */root/Downloads* directory.

'''console
cp /media/usb_drive_name/8-07-14_MegaCLI /root/Downloads
'''
