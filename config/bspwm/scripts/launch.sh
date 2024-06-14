#!/bin/bash

# Random Wallpaper Script
sh ~/bin/random_wallpaper

# launch notification daemon
dunst -config $HOME/.config/bspwm/dunstrc &

# launch battery tracker and redshift
pkill battery-alert; ~/bin/battery-alert &
pgrep -x redshift > /dev/null || redshift &

~/.config/polybar/launch.sh
