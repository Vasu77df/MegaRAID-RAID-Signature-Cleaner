# MegaRAID RAID-Signature-Cleaner

This is a guide to setup or run the Raid-Signature Cleaner Application on Either Windows or CentOS 6 Linux

## Running the application on existing machines with setup already completed

### On Windows Server

- Login to the machine as administrator

- Password: *Americaneagle#2020*

- Run the mega_raid_clearer.ps1 by right clicking the script and running with PowerShell

- Open PowerShell

- Navigate to Desktop Directory where the application resides using the command

```powershell
PS C:\Users> Set-Location C:\Users\Adminstrator\Desktop
```

- Run the application using the following command

```powershell
PS C:\Users> .\mega_raid_clearer.ps1
```

Please Check the **Foreign State** of the Disk before Clearing if the state is *Foreign* it has an old RAID Signature if state is *None* then there is no old RAID Configuration.