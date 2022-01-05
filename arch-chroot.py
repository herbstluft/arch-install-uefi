import os
from types import CellType
style = ("----------------------------------------------------------│")
### configuracion de usuario
os.system('arch-chroot /mnt ')
os.system('echo es_MX.UTF-8 UTF-8 >> /etc/locale.gen')
print("[* Generando idioma Español..]")
os.system('sleep 2s')
os.system('locale-gen')
os.system('touch /etc/locale.conf')
os.system('echo "LANG=es_MX.UTF-8" >> /etc/locale.conf')
os.system('sleep 1s')
### Zona horaria
print(style)
print("           Generando Zona Horaria, espere...               ")
print(style)

os.system('sleep 2s')
os.system('ln -sf /usr/share/zoneinfo/America/Monterrey /etc/localtime')
print("")
print("")
print(" ---== Zona horaria configurada correctamente ==--")
os.system('sleep 2s')
os.system('clear')
print("----------------------------------------------------------------------------")
host = input("""A continuacion establecera un nombre a su PC.
Presione (y) para continuar:""")
confirm_host = ('y')
if host == confirm_host:
    print()
    nombre_host = input("Escriba el nombre se su PC :")
    add_hostname = "echo ".format(nombre_host)
    add_hostname2 = " >> /etc/hostname".format()
    os.system(add_hostname+nombre_host+add_hostname2)
    
    os.system('touch /etc/vconsole.conf')
    os.system('echo KEYMAP=es >> /etc/vconsole.conf')
    os.system('sleep 1s')
    os.system('clear')
    ### Usuarios y contraseñas
    print(style)
    print("             Generacion de usuario, espere...            ")
    print(style)
    print()

    id_usuario = input("Ingrese su nombre de usuario:")
    useradd = "sudo useradd -m -g users -s /bin/bash ".format(id_usuario)
    os.system(useradd+id_usuario)
    passwd = "sudo passwd ".format(id_usuario)
    os.system(passwd+id_usuario)
    print()
    print(" [*] Añadiendo usuario al sistema.. ")
    os.system('sleep 2s')
    ### Systemctl
    os.system('systemctl enable sshd')
    os.system('systemctl enable lxdm')
    os.system('systemctl enable dhcpcd')
    os.system('clear')
    ### sudoers
    print(style)
    print("               Agregando sudoers, espere...                ")
    print(style)

    echo = "echo ".format(id_usuario)

    comilla = "'".format()
    comilla2 = "'".format()

    res = " ALL=(ALL) ALL".format()
    direccion = " >> /etc/sudoers"
    os.system(echo+comilla+id_usuario+res+comilla2+direccion)
    
    print("[*] Elevacion de privilegios aplicada.")
    os.system('sleep 2s')
    os.system('clear')
    ### ENTORNO DE ESCRITORIO
    print("----------------------------------------------------------│")
    print("                  Entorno De Escritorio                    ")
    print("----------------------------------------------------------│")
    print("""
[1] Fluxbox
[2] i3
[3] Gnome
[4] KDE Plasma
[5] Xfce4
[6] Cutefish """)
    print()
    
    entorno = input("Elija su entorno de escritorio:")
    if entorno=='1':
        os.system('pacman -S fluxbox --noconfirm')
    elif entorno=='2':
        os.system('pacman -S i3 --noconfirm')
    elif entorno=='3':
        os.system('pacman -S gnome --noconfirm')
    elif entorno=='4':
        os.system('pacman -S plasma --noconfirm')
    elif entorno=='5':
        os.system('pacman -S xfce4 --noconfirm')
    elif entorno=='6':
        os.system('pacman -S cutefish --noconfirm')
    else:
        print("-----------------------------------------------")
        print("    --== No selecciono ninguna opcion ==--     ")
        print("-----------------------------------------------")
    os.system('clear')
    ###grub
    print("----------------------------------------------------------│")
    print("                Instalando grub, espere...                 ")
    print("----------------------------------------------------------│")
    import os
    os.system('sleep 1s')
    import os
    os.system('grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=Arch')
    import os
    os.system('grub-install --target=x86_64-efi --efi-directory=/boot --removable')
    import os
    os.system('grub-mkconfig -o /boot/grub/grub.cfg')
    import os
    os.system('mkinitcpio -P')
    print("----------------------------------------------------------│")
    print("       Instalacion terminada con exito >> REINICIE         ")
    print("----------------------------------------------------------│")
else:
    print(style)
    print(" Gracias por probar este script")
    print(style)