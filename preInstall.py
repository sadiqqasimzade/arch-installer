import os


class Prepare:
    @staticmethod
    def all():
        Prepare.prepare_pacman()
        Prepare.prepare_aur()

    def prepare_pacman():
        os.system(r"sudo sed -i '/^[^#]*[multilib]/ s/^#//' /etc/pacman.conf")
        os.system("sudo pacman-key --init")
        os.system("sudo pacman-key --populate")
        os.system("sudo pacman -Sl multilib")
        os.system("sudo pacman -Syu")

    def prepare_aur():
        os.system("git -C /tmp clone https://aur.archlinux.org/yay.git")
        os.system("cd /tmp/yay && makepkg -si")

def main():
    Prepare.all()


if __name__ == "__main__":
    main()
