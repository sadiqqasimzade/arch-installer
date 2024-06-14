import os


ARCHIVE=['unrar','zip','unzip','p7zip','gzip']
EDITORS=['nano']
MEDIA= [
    'ffmpeg','ffmpegthumbnailer','tumbler',
    'feh' #image viewer/background setter 
    ]
SOUND=['alsa-plugins','alsa-tools','alsa-utils','pulseaudio','pulseaudio-alsa','pulseaudio-bluetooth','pamixer','pavucontrol']
DESKTOP_ENV=['xfce4-power-manager','xfce4-settings','xorg','xorg-xinit','xterm', 
             'gedit', #text editor
             'htop','btop', #task manager
             'gpick', #color picker
             'flameshot', #screenshot tool
             'thunar', #file manager
            ]
WM=[
    'bspwm', #window manager
    'sxhkd', #keybindings
    'rofi', #application launcher,
    'rofi-calc',
    'rofi-emoji',
    'picom', #compositor
    'polybar', #status bar
    'dunst' #notification daemon
    ]

SHELL_UTILS=[
    'bat', #cat replacement
    'calc',
    'lsd',
    'fakeroot',
    'neofetch', #system info
    'tree', #directory tree
    'dpkg','make','automake', #build tools
    'alacritty','fish', #terminal
    'ranger', #file manager
    'entr' #run command on file modification  
    ]
NETWORK=['networkmanager-openvpn','openvpn','blueman','bluez','bluez-utils','netctl','openssh','sshfs','firefox']
OFFICE=['libreoffice','zathura','zathura-djvu','zathura-pdf-mupdf',]
FONTS=['ttf-jetbrains-mono','ttf-jetbrains-mono-nerd','ttf-fira-code','ttf-iosevka-nerd']
DRIVERS=[
    'mesa', 'xf86-video-nouveau', 'xf86-video-intel', 'vulkan-intel','intel-ucode','xf86-video-amdgpu','usbutils',
    'xclip', #clipboard
    'ufw' #Firewall
    ]


def main():
    os.system(f"mkdir -p ~/Documents ~/Downloads ~/Desktop ~/.config")
    #print(' '.join(ARCHIVE+EDITORS+MEDIA+SOUND+DESKTOP_ENV+WM+SHELL_UTILS+NETWORK+OFFICE+FONTS+DRIVERS))
    os.system(f"sudo pacman -S --noconfirm {' '.join(ARCHIVE+EDITORS+MEDIA+SOUND+DESKTOP_ENV+WM+SHELL_UTILS+NETWORK+OFFICE+FONTS+DRIVERS)}")



if __name__ == "__main__":
    main()
