import os

style = ("----------------------------------------------------------│")
os.system('clear')
print()
print("Autor: Juan Angel Castañeda Chavez")
print(style)
print("Actualizando sistema, porfavor espere....		  │")
print(style)
# Actualizar sistema
os.system('sudo pacman -Sy')
#from colorama import init
#Bienvendia
os.system('clear')
print("│-------------------------│")
print("  --==[ BIENVENIDO ]==-- ")
print("│-------------------------│")
os.system('sleep 2s')
print("")
print("Configurando teclado al español (es)...")
os.system('loadkeys es')
os.system('sleep 1s')
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
continuar=input("¿Desea continuar? (y/n) ")
    
if continuar == respuesta:
    ##################################################################################################    
    os.system('clear')

    ## Particiones ##    
    os.system('fdisk /dev/sda')
    os.system('clear')
    
#### Formateo de particiones

    print(style)
    print("                 Formateando Particiones                   ")
    print(style)
    print("")

    os.system('mkfs.fat -F 32 /dev/sda1 > /dev/null')
    os.system('mkswap /dev/sda2 > /dev/null')
    os.system('swapon')
    os.system('mkfs.ext4 /dev/sda3 > /dev/null')
    print(style)
    print("        Acabando formateo de particiones espere...         ")
    print(style)
    os.system('sleep 2s')
    os.system('clear')

    ## Montar sistema
    print(style)
    print("              Montando sistema, espere...                  ")
    print(style)
    os.system('sleep 2s')
    os.system('mount /dev/sda3 /mnt/')
    os.system('mkdir /mnt/boot')
    print("Directorio creado >> /mnt/boot")
    os.system('sleep 3s')
    os.system('mount /dev/sda1 /mnt/boot')
    os.system('clear')

    ### Pacstrap
    print(style)
    print("             Descargando kernel y paquetes                 ")
    print(style)
    print()
    print("[*] Esto tardara un poco, Espere....")
    os.system('pacstrap /mnt base base-devel nano dhcpcd netctl iwd net-tools wireless_tools networkmanager wpa_supplicant dialog grub efibootmgr os-prober openssh linux linux-firmware linux-headers mkinitcpio xterm lxdm terminus-font go > /dev/null')
    print("""
             INSTALANDO
-------------------------------------
* base              * wireless_tools
* base-devel        * networkmanager
* nano              * wpa_supplicant
* dhcpcd            * dialog
* netctl            * grub
* iwd               * efibootmgr
* net-tools         * os-prober
* openssh           * linux
* linux-firmware    * linux-headers
* mkinitcpio        * xterm
* lxdm              * terminus-font
* go         
-------------------------------------
        """)
    print(style)
    print("         Acabando descarga del kernel, espere...           ")
    print(style)
    os.system('sleep 2s')
    ### Genfstab

    os.system('clear')
    print(style)
    print("              Generando genfstab, espere...                ")
    print(style)            
    os.system('genfstab -p /mnt')
    os.system('genfstab -p /mnt >> /mnt/etc/fstab')
    os.system('clear')

    print(style)
    print("           Configuracion de usuario, espere...             ")
    print(style)
        
    os.system('cp arch-chroot.py /mnt/')
    os.system('cd /mnt/')
    print("""   
------------------------------------------------------------------------------- 
                            ---===> ATENCION <===---
-------------------------------------------------------------------------------        
Esta a punto de terminar el primer script de instalacion, al acabarlo podra 
iniciar la configuracion del usuario solo ejecutando:
    ____________________________
   |   python arch-chroot.py    |
    ----------------------------   
    """)
    print()
    respuesta2= 'y'
    continuar2 =input("Presione (y) para continuar:")

        
        
else:
    print("-----------------------------------")
    print("Gracias por probar este script")
    print("----------------------------------")
    
os.system('python /mnt/arch-chroot.py')
    