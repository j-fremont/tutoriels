# Tutoriels Raspberry

+ tuto-1 : Faire clignoter une LED
+ tuto-2 : Allumer une LDE sur mouvement
+ tuto-3 : Utiliser une Caméra
+ tuto-4 : Déclenchement d'une caméra sur mouvement

https://www.raspberrypi.com/documentation/computers/raspberry-pi.html

# GPIO

## Raspberry 5

![Pictures/GPIO-Pinout-Diagram-2.png](https://github.com/j-fremont/tuto-raspberry/blob/main/Pictures/GPIO-Pinout-Diagram-2.png)

# Librairie Python

+ Rpi.GPIO
+ gpiozero (https://gpiozero.readthedocs.io/en/stable/index.html)

## gpiozero

Installer gpiozero (https://gpiozero.readthedocs.io/en/stable/installing.html).

# Librairie C

Librairies C à installer sur Raspberry pour utiliser le GPIO en C.

## BCM2835

http://www.airspayce.com/mikem/bcm2835/

Installer la librairie C BCM2835.

```
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.XX.tar.gz
tar zxvf bcm2835-1.XX.tar.gz
cd bcm2835-1.XX
./configure
make
sudo make check
sudo make install
```

## WiringPi

https://github.com/WiringPi/WiringPi

```
git clone https://github.com/WiringPi/WiringPi.git
cd WiringPi
./build
```

Sur http://wiringpi.com/.

```
$ gpio -v
...
$ gpio readall
 +-----+-----+---------+------+---+-Model B1-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |  OUT | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |  OUT | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |  OUT | 1 |  7 || 8  | 1 | ALT0 | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | ALT0 | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Model B1-+---+------+---------+-----+-----+
```

*The operating voltage of the GPIO pins is 3.3v with a maximum current draw of 16mA. This means that we can safely power one or two LEDs (Light Emitting Diodes) from a single GPIO pin, via a resistor.*

