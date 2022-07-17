Step to follow for bluetooth pairing:
1. install bluez bluez-utils blueman
2. run this command ```lsmod | grep btusb```
3. Edit this file sudo vim /etc/bluetooth/main.conf
change AutoEnable to True

4. Enable the services: ```sudo vim /etc/bluetooth/main.conf```
5. ```sudo systemctl enable bluetooth.service```
