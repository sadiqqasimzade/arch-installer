import os


ARCHIVE=['unrar','zip','unzip','p7zip','gzip']
EDITORS=['nano']
VIDEO=['ffmpeg','ffmpegthumbnailer','tumbler']
SOUND=['alsa-plugins','alsa-tools','alsa-utils','pulseaudio','pulseaudio-alsa','pulseaudio-bluetooth','pamixer','pavucontrol']
DESKTOP_ENV=['xfce4-power-manager','xfce4-settings','thunar','xorg','xorg-xinit','xterm','gedit','htop','btop']
WM=['bspwm','sxhkd','rofi','rofi-calc','rofi-emoji','picom','polybar','dunst']
SHELL_UTILS=['bat','calc','lsd','fakeroot','neofetch','tree','dpkg','make','automake','alacritty','fish']
NETWORK=['networkmanager-openvpn','openvpn','blueman','bluez','bluez-utils','netctl','openssh','sshfs','firefox']
OFFICE=['libreoffice','zathura','zathura-djvu','zathura-pdf-mupdf',]
FONTS=['ttf-jetbrains-mono','ttf-jetbrains-mono-nerd','ttf-fira-code','ttf-iosevka-nerd']
DRIVERS=['mesa', 'xf86-video-nouveau', 'xf86-video-intel', 'vulkan-intel','intel-ucode','xf86-video-amdgpu','usbutils',]


def main():
    os.system(f"mkdir -p ~/Documents ~/Downloads ~/Media ~/Desktop ~/.config")
    # print(' '.join(ARCHIVE+EDITORS+VIDEO+SOUND+DESKTOP_ENV+WM+SHELL_UTILS+NETWORK+OFFICE+FONTS+DRIVERS))
    os.system(f"sudo pacman -S --noconfirm {' '.join(ARCHIVE+EDITORS+VIDEO+SOUND+DESKTOP_ENV+WM+SHELL_UTILS+NETWORK+OFFICE+FONTS+DRIVERS)}")



if __name__ == "__main__":
    main()
