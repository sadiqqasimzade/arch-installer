import os


def main():
    os.system("sudo systemctl enable bluetooth.service")
    os.system("chsh -s /usr/bin/fish")
    os.system("sudo chmod -R 700 ~/.config/*")

    os.system("cp -r config/* ~/.config/")
    os.system("cp Xresources ~/.Xresources")
    os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
    os.system("cp xinitrc ~/.xinitrc")
    os.system("cp -r bin/ ~/")
    os.system("cp -r Media/ ~/")
    
if __name__ == "__main__":
    main()
