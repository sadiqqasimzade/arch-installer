<!-- INFORMATION -->
<h1>About</h1>
<h3>Arch-linux install scripts and guide.IT CONFIGUREATES SYSTEM FOR MY PREFERENCES,DONT RUN IT!!!!</h3>


### Create partitions with cfdisk

- 200MB fat32 Boot
- 4GB Swap
- Rest ext4

### Format partitions

```bash
mkfs.fat -F32 /dev/sda1      #(boot)
mkfs.ext4 /dev/sda3      #(linux/main)
mkswap    /dev/sda2
```

### Mounting partitions

```bash
swapon /dev/sda2
mount /dev/sda3 /mnt
cd /mnt
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi
```

use lsblk to confirm mount points

### Installing Linux

```bash
pacstrap /mnt base linux linux-firmware sof-firmware micro vim base-devel grub iwd networkmanager efibootmgr git python
genfstab /mnt >> /mnt/etc/fstab
arch-chroot /mnt
```

### Configurating Arch
Clone this repo

Run configurateArch.py

Reboot system

```bash
exit 
umount -a
reboot
```

Login as user not as root

Run preInstall.py

Run installPackages.py

Run postInstallConfig.py




### inspired from [Zproger](https://github.com/Zproger/bspwm-dotfiles)