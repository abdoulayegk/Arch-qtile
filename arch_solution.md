## Fixing an Arch Linux system that is booting into emergency mode.

1. check your mount poing using the following command:
   `lsblk `
2. Check your fstab to see if everyting is okay (in my case there was /Backup that was there at the place of root)
   `cat /etc/fstab `
   if that's the case then chance it to / only.
   Sometimes you can see that the disk partition is not showing the right name use following command

`nvim /etc/fstab `
fix it and reboot.

**Note** you have to be careful with the fstab file.

This save my life because I had some very important documents on the computer
when I got this problem.
