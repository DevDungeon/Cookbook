#!/bin/sh
# Requires executable bit
# Move to `/etc/grub.d/99_dano_grub_colors`
# and run `sudo update-grub`
echo "set menu_color_normal=light-cyan/dark-gray"
echo "set menu_color_highlight=dark-gray/light-cyan"
echo "set color_normal=white/black"
echo "set color_highlight=black/white"

# To change image, update `/etc/default/grub` with the image path
# GRUB_BACKGROUND=/usr/share/images/grub/Plasma-lamp.tga
# That image comes from the `grub2-splashimages` package.