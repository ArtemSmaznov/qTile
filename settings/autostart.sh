#!/bin/bash
paplay '/usr/share/mint-artwork-cinnamon/sounds/login.oga' &
/opt/piavpn/bin/pia-client --quiet &
picom -b --experimental-backends --dbus &
# nitrogen --restore &
~/.local/bin/dmscripts/dmwallpaper faded &
redshift-gtk &
solaar -w hide &
nm-applet &
xscreensaver -no-splash &

alacritty &
brave &
/usr/bin/steam-runtime %U &
