import os


def main():
    os.system("sudo systemctl enable bluetooth.service")
    os.system("chsh -s /usr/bin/fish")
    os.system("sudo chmod -R 700 ~/.config/*")


if __name__ == "__main__":
    main()
