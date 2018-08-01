# how to use

USB Wifi modules  
aircrack

## install

```
$ sudo apt-get install aircrack-ng
```

## edit cron

```
$ crontab -e

* * * * * cd login; python inlog.py & sleep 10; python inlog.py & sleep 10; pyt$
```

## run cron

```
$ sudo /etc/init.d/cron stop
$ sudo /etc/init.d/cron start
```

## run aircrack

```
$ sudo airodump-ng mon0 --bssid XX:XX:XX:XX:XX:XX[AP MAC Address] -w log
$ sudo airmon-ng start wlan0
```
