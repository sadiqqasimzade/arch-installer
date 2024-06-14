import os


def main():
    os.system("sudo systemctl enable bluetooth.service")
    
    #ssh
    os.system("sudo systemctl enable ufw.service")
    os.system("sudo ufw allow 22/tcp")
    
    
    os.system("chsh -s /usr/bin/fish")

    os.system("cp -r config/* ~/.config/")
    os.system("cp Xresources ~/.Xresources")
    os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
    os.system("cp xinitrc ~/.xinitrc")
    os.system("cp -r local ~/.local")
    os.system("cp -r themes ~/.themes")
    os.system("cp -r bin/ ~/")
    os.system("cp -r Media/ ~/")
    
    os.system("sudo chmod -R 700 ~/.config/*")
    
    
if __name__ == "__main__":
    main()
