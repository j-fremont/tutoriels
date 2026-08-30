# Caméra

Installer Picamera2 (https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf) et ffmpeg pour les films.

```
sudo apt update
sudo apt install -y python3-picamera2
sudo apt install -y ffmpeg
```

Pour tester la caméra.

```
libcamera-hello
```

Si la caméra n'est pas reconnue, changer /boot/config.txt et rebooter.

```
camera_auto_detect=0
```

