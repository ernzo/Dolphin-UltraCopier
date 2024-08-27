
Dolphin-UltraCopier 0.1
---------------------
Release: 28 Aug 2024

Author: [ernzo] (https://github.com/ernzo)
(https://github.com/ernzo/Dolphin-UltraCopier)

This script is an Action for Dolphin that uses CopyQ to Paste the clipboard content with Ultracopier.

It works perfecly in Debian (trixie) Plasma/Wayland + latest stock CopyQ & Ultracopier.


Installation:
=============
1.- Copy "ultrapaste.desktop" to /home/USER/.local/share/kservices5/ServiceMenus/
and /usr/share/kservices5/ServiceMenus/ for a system-wide application.

2.- Copy "dolphin.ultracopier.py" to /home/USER/scripts/

3.- Grant Permissions:
sudo chmod 644 /usr/share/kservices5/ServiceMenus/ultrapaste.desktop
chmod 644 /home/USER/.local/share/kservices5/ServiceMenus/ultrapaste.desktop

sudo chown root:root /usr/share/kservices5/ServiceMenus/ultrapaste.desktop
chown USER:USER /home/USER/.local/share/kservices5/ServiceMenus/ultrapaste.desktop

chmod +x /home/USER/scripts/dolphin.ultracopier.py

4.- Reset Dolphin file manager,
the "Paste with UltraCopier" option should appear on the Right Click Context/Dropdown Menu.

Voila?


PS: If anyone manages to Bind it to a Keyboard Shortcut,
be it via Dolphin Shortcuts, or KWin Global Shortcuts.. be my guest.



Change log
-----------
0.1 - First release
