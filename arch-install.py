import os

#from colorama.ansi import Fore
os.system('clear')
print("-----------------------------------------------------------│")
print("Actualizando sistema, porfavor espere....		  │")
print("-----------------------------------------------------------│")
# Actualizar sistema
import os
os.system('pacman -Sy')

import os
os.system('sleep 2s')

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

    import os
    os.system('clear')

    print("-------------------------------------------------------------------------------------------")
    print("""A continuacion realice las 3 particiones principales de su disco duro:
   
    "IMPORTANTE: Disklabel type debe ser tipo GTP"

 /dev/sda1 "tamaño" tipo >>> EFI 
 /dev/sda2 "tamaño" tipo >>> Linux Swap 
 /dev/sda3 "tamaño" tipo >>> Linux Filesystem
 """)

################################# Confirmacion para continuar #######################################
    
    respuesta=('y')
    continuar=input("Presione "y" para continuar. ")    
##################################################################################################    
    import os
    os.system('clear')

## Particiones ##    
    import os
    os.system('fdisk /dev/sda')
    import os
    os.system('clear')
    
#### Formateo de particiones

    print("########## Formateando particiones ##########")
    print("")

    import os
    os.system('mkfs.fat -F 32 /dev/sda1 > /dev/null')
    import os
    os.system('mkswap /dev/sda2 > /dev/null')
    import os
    os.system('swapon')
    import os
    os.system('mkfs.ext4 /dev/sda3 > /dev/null')
    print("---------------------------------")
    print("Acabando formateo de particiones espere...")
    import os
    os.system('sleep 3s')

   import os
   os.system('clear')
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
    os.system('echo ParallelDownloads = 15 >> /etc/pacman.conf')
### Pacstrap
    print("---------------------------------")
    print("Descargando kernel y paquetes")
    print("---------------------------------")
    import os
    os.system('pacstrap /mnt base base-devel nano dhcpcd netctl iwd net-tools wireless_tools networkmanager wpa_supplicant dialog grub efibootmgr os-prober openssh linux linux-firmware linux-headers mkinitcpio xterm lxdm i3 terminus-font')
    priknt("--------------------------------------")
    print("Acabando descarga del kernel, espere...")
    print("---------------------------------------")
### Genfstab
    import os
    os.system('sleep 1s')

    import os
    os.system('clear')
    print("---------------------------------")
    print("Generando genfstab, espere...    ")
    print("---------------------------------")               
    import os
    os.system('genfstab -p /mnt')
    import os
    os.system('genfstab -p /mnt >> /mnt/etc/fstab')
    import os
    os.system('sleep 2s')

    import os
    os.system('clear')

    print("---------------------------------")
    print("Configuracion de usuario, espere...")
    print("---------------------------------")
    
    import os
    os.system('cp arch-chroot.py /mnt/')
    import os
    os.system('cd /mnt/')
    

    import os
    os.system('python /mnt/arch-chroot.py')
    import os
    os.system('sleep 1s')


inicio()

