# Dolphin-UltraCopier 0.1

**Release**: 28 Aug 2024  
**Author**: [ernzo](https://github.com/ernzo)  
**Repository**: [Dolphin-UltraCopier](https://github.com/ernzo/Dolphin-UltraCopier)

This script is an Action for [Dolphin](https://github.com/KDE/dolphin) that uses [CopyQ](https://hluk.github.io/CopyQ/) to Paste the clipboard content with [Ultracopier](https://github.com/alphaonex86/Ultracopier).

It works perfecly in Debian (trixie) Plasma/Wayland + latest stock CopyQ & Ultracopier.


1. **Copy the Script:**
   - Copy `dolphin.ultracopier.py` to `/home/USER/scripts/`

2. **Copy the Desktop Entry:**
   - Copy `ultrapaste.desktop` to `/home/USER/.local/share/kservices5/ServiceMenus/`
   - Alternatively, copy it to `/usr/share/kservices5/ServiceMenus/` for a system-wide application.

3. **Set Permissions:**
   ```bash
	chmod +x /home/USER/scripts/dolphin_ultracopier.py

	chmod 644 /home/USER/.local/share/kservices5/ServiceMenus/ultrapaste.desktop   
	sudo chmod 644 /usr/share/kservices5/ServiceMenus/ultrapaste.desktop
   
	chown USER:USER /home/USER/.local/share/kservices5/ServiceMenus/ultrapaste.desktop
	sudo chown root:root /usr/share/kservices5/ServiceMenus/ultrapaste.desktop

4. **Restart Dolphin:**
   - Restart Dolphin file manager, the "Paste with Ultracopier" option should appear on the Right Click Context/Dropdown Menu.
 
Voila?
 
 
PS: If anyone manages to Bind it to a Keyboard Shortcut,
be it via Dolphin Shortcuts, or KWin Global Shortcuts.. be my guest.
 
 
 
Change log
-----------
0.1 - First release
