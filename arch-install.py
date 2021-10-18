import os

#from colorama.ansi import Fore
os.system('clear')
print("------------------------------------------------------------------------------------------│")
print("Instalando las herramientas necesarias para continuar con el proceso, porfavor espere.... │")
print("------------------------------------------------------------------------------------------│")
import os
os.system('sleep 1s')
# instalar dependencias
import os
os.system('pacman -Sy')

import os
os.system('sleep 3s')

#from colorama import init
#Bienvendia
def inicio():
    import os
    os.system('clear')
    print("│-------------------------│")
    print("  --==[ BIENVENIDO ]==-- ")
    print("│-------------------------│")
    import os
    os.system('sleep 1s')
    print("")
    print("Configurando teclado al español (es)...")
    import os
    os.system('loadkeys es')
    import os
    os.system('sleep 2s')
    print("-------------------------------------------------------------------------------------------")
    print("""A continuacion realice las 3 particiones principales de su disco duro:
   
    "IMPORTANTE: Disklabel type debe ser tipo GTP"

 /dev/sda1 "tamaño" tipo >>> EFI 
 /dev/sda2 "tamaño" tipo >>> Linux Swap 
 /dev/sda3 "tamaño" tipo >>> Linux Filesystem
 """)
    import os
    os.system('sleep 3s')    
    
    import os
    os.system('fdisk /dev/sda')

#### Formateo de particiones
    import os
    os.system('mkfs.fat -F 32 /dev/sda1')
    import os
    os.system('mkswap /dev/sda2')
    import os
    os.system('swapon')
    import os
    os.system('mkfs.ext4 /dev/sda3')
    import os
    os.system('sleep 2s')
## Montar sistema
    print("---------------------------------")
    print("Montando sistema, espere...")
    print("---------------------------------")
    import os
    os.system('sleep 2s')
    import os
    os.system('mount /dev/sda3 /mnt/')
    import os
    os.system('mkdir /mnt/boot')
    print("Directorio creado")
    import os
    os.system('sleep 3s')
    import os
    os.system('mount /dev/sda1 /mnt/boot')

    import os
    os.system('nano /etc/pacman.conf')
### Pacstrap
    print()
    import os
    os.system('pacstrap /mnt base base-devel nano dhcpcd netctl iwd net-tools wireless_tools networkmanager wpa_supplicant dialog grub efibootmgr os-prober openssh linux linux-firmware linux-headers mkinitcpio xterm lxdm i3 terminus-font')
    print("---------------------------------")
    print("Acabando descarga del kernel, espere...")
    print("---------------------------------")
### Genfstab
    import os
    os.system('sleep 1s')
    print("---------------------------------")
    print("Generando genfstab, espere...")
    print("---------------------------------")               
    import os
    os.system('genfstab -p /mnt')
    import os
    os.system('genfstab -p /mnt >> /mnt/etc/fstab')
    import os
    os.system('sleep 2s')
    print("---------------------------------")
    print("Configuracion de usuario, espere...")
    print("---------------------------------")
    
    import os
    os.system('mv arch-chroot.py /mnt/')
    import os
    os.system('cd /mnt/')
    

    import os
    os.system('python /mnt/arch-chroot.py')
    import os
    os.system('sleep 1s')


inicio()

