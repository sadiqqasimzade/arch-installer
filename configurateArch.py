import os

class ConfigurateArch:
    @staticmethod
    def configurate_all():
        ConfigurateArch.configurate_timezone()
        ConfigurateArch.configurate_lang()
        ConfigurateArch.configurate_host()
        ConfigurateArch.enable_services()
        ConfigurateArch.setup_grub()
        
    @staticmethod
    def configurate_timezone():
        os.system('ln -sf /usr/share/zoneinfo/Asia/Baku /etc/localtime')
        os.system('hwclock --systohc')
        os.system('date')
        print("If date is correct timezone configurated")
    
    def configurate_lang():
        os.system('echo -e "en_US.UTF-8 UTF-8 \n ru_RU.UTF-8 UTF-8" >> /etc/locale.gen')
        os.system('locale-gen')
        os.system('echo LANG=en_US.UTF-8 >> /etc/locale.conf')
        print("Language configurated")

    def configurate_host():
        hostname=input('hostname:')
        username=input('username:')
        os.system(f'echo {hostname} >> /etc/hostname')
        os.system(f'useradd -m -G wheel -s /bin/bash {username}')
        print(f'added user "{username}".Dont forget to set password')
    
    def enable_services():
        os.system('systemctl enable NetworkManager')
        os.system('systemctl enable iwd.service')

    def setup_grub():
        os.system(f'grub-install /dev/{input('disk (sda/sdb ...):')}')
        os.system('grub-mkconfig -o /boot/grub/grub.cfg')

def main():
    ConfigurateArch.start()
    print("Basic arch configurated")


if __name__ == "__main__":
    main()
