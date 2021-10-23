## arch-install
He desarrollado este script con la finalidad de ahorar tiempo en la hora de instalacion y compilacion de Archlinux, espero y les sea de gran ayuda. (Se vienen mejoras)
##

### ISO Archlinux
Pueden descargar la ISO de ArchLinux desde la pagina oficial, les dejo el siguiente [enlace](https://archlinux.org/download/)
##

### Instrucciones de uso

Como primer paso sera instalar git, este script se podra utilizar solo con conexion a internet, ya que solo asi podriamos clonarlo, o otra opcion seria descargar
los script pero antes de grabar la memoria con el sistema live.

Una vez que esten dentro del sistema live de la ISO de ArchLinux clonen el repositorio de la siguiente manera.

```shell
git clone https://github.com/herbstluft/arch-install
```
A continuacion, introducirse a la carpeta clonada, en este caso "arch-install"
```
cd arch-install
```
Al introducirnos en la carpeta nos apareceran dos archivos, [arch-install.py](https://github.com/herbstluft/arch-install/blob/main/arch-install.py) y [arch-chroot.py](https://github.com/herbstluft/arch-install/blob/main/arch-chroot.py).

Lo que haremos sera ejecutar el [arch-install.py](https://github.com/herbstluft/arch-install/blob/main/arch-install.py)

```shell
python arch-install.py
```

Asi seguiremos las instrucciones hasta que se pare y nos pregunte si queremos avanzar con el [arch-chroot.py](https://github.com/herbstluft/arch-install/blob/main/arch-chroot.py).





##
### Contribuyendo
Estoy un poco lejos de ser todo un experto, se que faltan cosas por aprender y sospecho que hay muchas formas de mejorar: si tiene ideas sobre cómo 
hacer que la configuración sea más fácil de mantener (y más rápida), ¡no dude en bifurcar y enviar solicitudes de extracción!

##
### Colaborador
Soy un estudiante universitario con hambre de aprender, la meta a largo o corto plazo sera contribuir un sistema ligero, rapido, 
amigable y facil de manejar para el usuario.
##

### Contacto
Red Social: [Facebook](https://www.facebook.com/juanangel.castaneda.71)

Correo: herbstluftwm.28@gmai.com
