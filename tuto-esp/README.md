## Tutoriels ESP

+ wifi : Connecter au Wifi
+ ntp : Connecter à un serveur NTP
+ mqtt : Connecter à un serveur MQTT
+ dht11_in_mqtt : Envoyer les mesures DHT11 à un serveur MQTT
+ bmp280_in_mqtt : Envoyer les mesures BMP280 à un serveur MQTT
+ inside : Capteurs utilisés pour l'intérieur
+ outside : Capteurs utilisés pour l'extérieur

## Utilisation de l'IDE Arduino pour les ESP8266

Pour ajouter l'ESP8266 à l'IDE Arduino.

+ Sur https://github.com/esp8266/Arduino/blob/master/README.md.
+ Dans les Préférences de l'IDE Arduino, ajouter l'URL https://arduino.esp8266.com/stable/package_esp8266com_index.json.
+ Dans Outils, Gestionnaire de cartes, Installer ESP8266.

Voir https://www.fais-le-toi-meme.fr/fr/electronique/tutoriel/programmes-arduino-executes-sur-esp8266-arduino-ide.

## ESP8266-12

![Pictures/ESP8266_12X.jpg](https://github.com/j-fremont/tuto-esp/blob/main/Pictures/ESP8266_12X.jpg)

![Pictures/ESP8266_12X_I2C.png](https://github.com/j-fremont/tuto-esp/blob/main/Pictures/ESP8266_12X_I2C.png)

Pour flasher un sketch sur l'ESP8266-12, voir https://www.instructables.com/id/ESP-12F-ESP8266-Module-Minimal-Breadboard-for-Flas/.

![Pictures/ESP8266_flash.png](https://github.com/j-fremont/tuto-esp/blob/main/Pictures/ESP8266_flash.png)

Utiliser le montage et téléverser.

1. Avant la fin de la compilation, rester appuyer sur le bouton Flash.
2. Puis pendant "Connecting........_____....._____....._____....._____....._", appui bref sur le bouton Reset.
3. A la fin de "Wrote XXXXXX bytes...", relacher le bouton Flash.

Pour mettre les ESP8266 en mode deep sleep, voir https://projetsdiy.fr/esp8266-test-mode-deep-sleep-reveil-wakeup-detecteur-mouvement-pir/.

## ESP8266-01

![Pictures/ESP-01-Pin-Out.png](https://github.com/j-fremont/tuto-esp/blob/main/Pictures/ESP-01-Pin-Out.png)

Pour programmer l'ESP8266-01, utiliser un adaptateur USB to ESP-01.

![Pictures/usb-esp01-adapter.jpg](https://github.com/j-fremont/tuto-esp/blob/main/Pictures/usb-esp01-adapter.jpg)

La connexion Wifi fonctionne les premiers temps mais plus ensuite. On finit par avoir une adresse en 169.254 qui est l'adresse attribuée quand le serveur DHCP ne répond pas.

La solution est d'attribuer une IP fixe. Voir ici https://arduino.stackexchange.com/questions/78604/esp8266-wifi-not-connecting-to-internet-without-static-ip.

## Autres liens.

+ https://www.instructables.com/id/Minitaure-Weather-Station-ESP8266/
+ https://tttapa.github.io/ESP8266/Chap01%20-%20ESP8266.html
+ https://www.circuito.io/blog/programming-esp8266-12e/

