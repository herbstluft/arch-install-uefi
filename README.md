## arch-install
He desarrollado este script con la finalidad de ahorrar tiempo a la hora de instalacion y compilacion de Archlinux, espero y les sea de gran ayuda. (Se vienen mejoras)
##

### ISO Archlinux
Pueden descargar la ISO de ArchLinux desde la pagina oficial, les dejo el siguiente [enlace](https://archlinux.org/download/)
##

### Conexion manual a internet
Como primer paso sera estar conectado a una red de internet, e instalar git, a continuacion se explicara como conectarse a internet mediante networkmanager y wpa_supplicant.

Utilizamos wpa_passphrase para guardad la informacion de la red.
```shell
wpa_passphrase (Nombre_de_la_Red) password (Contraseña_de_la_red) > /etc/wifi
```
Habilitamos el servicio de dhcpcd
```shell
systemctl enable dhcpcd
```
```shell
systemctl start dhcpcd
``````
Habilitamos el servicio de networkmanager
```shell
systemctl enable NetworkManager
```
```shell
systemctl start NetworkManager
```
Ahora establecemos conexion con la red de internet, estableciendo las credenciales correctas

```shell
wpa_supplicant -i (tarjeta_de_red) -D wext -c /etc/wifi
```
Con eso lograremos establecer una conexion correctamente, podemos confirmar que tenemos conexion a internet ejecutando un ping
```shell
ping 8.8.8.8
```

Comos resultado deberia darnos esto:
```shell
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=29.6 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=29.4 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=116 time=29.4 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=116 time=29.4 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=116 time=29.3 ms
64 bytes from 8.8.8.8: icmp_seq=6 ttl=116 time=29.3 ms
```


##

### Instrucciones de uso
Este script se podra utilizar solo con conexion a internet, ya que solo asi 
podriamos clonarlo.
```shell
pacman -S git
```


Una vez que esten dentro del sistema live de la ISO de ArchLinux clonen el repositorio de la siguiente manera.

```shell
git clone https://github.com/herbstluft/arch-install-uefi
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

Asi seguiremos las instrucciones hasta que se pare y nos toque avanzar con el [arch-chroot.py](https://github.com/herbstluft/arch-install/blob/main/arch-chroot.py).


##
### Ventajas de estos script
* Es un script automatizado
* Sencillo de ejecutar
* Ahorra tiempo
* Da a elejir un entorno grafico

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
