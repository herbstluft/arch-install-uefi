def chroot():

### configuracion de usuario
    
    import os
    os.system('arch-chroot /mnt ')
    import os
    os.system('echo LANG=es_MX.UTF-8 UTF-8 >> /etc/locale.gen')
    import os
    os.system('locale-gen')
    import os
    os.system('touch /etc/locale.conf')
    import os
    os.system('echo "LANG=es_MX.UTF-8" >> /etc/locale.conf')
#Zona horaria
    import os
    os.system('sleep 1s')
    print("---------------------------------")
    print("Generando Zona Horaria, espere...")
    print("---------------------------------")
    import os
    os.system('sleep 2s')
    import os
    os.system('ln -sf /usr/share/zoneinfo/America/Monterret /etc/localtime')
    print("")
    print("")
    print(" ---== Zona horaria configurada correctamente ==--")
    import os
    os.system('nano /etc/hostname')
    import os
    os.system('touch /etc/vconsole.conf')
    import os
    os.system('echo KEYMAP=es >> /etc/vconsole.conf')
### PASSWORDS
    import os
    os.system('sleep 2s')
    print("---------------------------------")
    print("Generacion de passwords, espere...")
    print("---------------------------------")
    import os
    os.system('passwd')
    import os
    os.system('sleep 2s')
    import os
    os.system('useradd -m -g users -s /bin/bash hack')
    import os
    os.system('sleep 2s')
    import os
    os.system('passwd hack')
    
################ Systemctl
    import os
    os.system('systemctl enable sshd')
    import os
    os.system('systemctl enable lxdm')
    import os
    os.system('systemctl enable dhcpcd')
    
#### sudoers
    print("---------------------------------")
    print("Agregando sudoers, espere...")
    print("---------------------------------")
    import os
    os.system('echo hack ALL=(ALL) ALL >> /etc/sudoers')
    import os
    os.system('sleep 2s')
#grub
    print("---------------------------------")
    print("Instalando grub, espere...")
    print("---------------------------------")
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
    import os
    os.system('exit')
    print("---------------------------------")
    print(" Instalacion terminada con exito ")
    print("---------------------------------")

chroot()
