install the following font for the title bar
paru -S ttf-dejavu ttf-meslo-nerd-font-powerlevel10k
sudo pacman -S brithnessctl
sudo pacman -S python-docutils
pip install psutil
pip install iwlib
sudo pacman -S alsa-utils
pip install dbus-next
sudo pacman -S alsmixer
sudo pacman -S kitty

# if you want to use qtile as default on start
1. Naviatate: ``bash cd /usr/share/xsessions
2. you will see a file qtile.desktop if it doesn't exit create it
3. copy and paste below content and save it.
``bash
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=qtile start
Type=Application
Keywords=wn,tiling
``
