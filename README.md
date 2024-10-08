# Dolphin-UltraCopier 0.5

**Release**: 28 Aug 2024  
**Author**: [ernzo](https://github.com/ernzo)  
**Repository**: [Dolphin-UltraCopier](https://github.com/ernzo/Dolphin-UltraCopier)

Action script for [Dolphin](https://github.com/KDE/dolphin) that uses [CopyQ](https://hluk.github.io/CopyQ/) to Paste the clipboard content via [Ultracopier](https://github.com/alphaonex86/Ultracopier).

Works perfecly in Debian (trixie) Plasma/Wayland + latest stock CopyQ & Ultracopier.

1. **Copy the Script:**
   - Copy `dolphin_ultracopier.py` to `/home/USER/scripts/`

2. **Copy Desktop Entry:**
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

<p align="center">
  <img src="https://i.imgur.com/feZQtFD.png" alt="Dolphin Ultracopier">
</p>

Voila?

PS: If anyone manages to Bind it to a Keyboard Shortcut,
be it via Dolphin Shortcuts, or KWin Global Shortcuts.. be my guest.
 
 
 
Change log
-----------
	0.1 - First release
	0.2 - Fixed USER path in `ultrapaste.desktop`; Updated `README.MD`
	0.3 - Updated `ultrapaste.desktop` to run from any user path; Updated README.MD
 	0.5 - Updated script to better handle special paths.
